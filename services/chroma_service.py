import chromadb
from fastapi import HTTPException
from sentence_transformers import SentenceTransformer

# Usar PersistentClient (almacenamiento local)
client = chromadb.PersistentClient(path="./chroma_db")

# Obtén o crea colección
collection = client.get_or_create_collection(name="document_embeddings")

# Cargar el modelo de embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def store_embedding(document_id: str, embedding: list[float], metadata: dict):
    collection.add(
        embeddings=[embedding],
        ids=[document_id],
        metadatas=[metadata]
    )

def get_all_embeddings():
    data = collection.get()
    return {
        "ids": data["ids"],
        "embeddings": data["embeddings"],
        "metadatas": data["metadatas"]
    }

def generate_embedding(text: str) -> list[float]:
    return model.encode(text).tolist()

def query_similar_documents(message: str) -> str:
    # Generar el embedding del mensaje
    embedding = generate_embedding(message)

    # Consultar los documentos más similares
    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    # Extraer los metadatos de los resultados
    metadatas = results.get("metadatas", [[]])[0]

    if not metadatas:
        return "No se encontraron resultados relevantes."

    # Construir una respuesta basada en los metadatos
    response = "He encontrado la siguiente información relacionada:\n"
    for idx, metadata in enumerate(metadatas, start=1):
        response += f"\n{idx}. {metadata}"
        
    return response
