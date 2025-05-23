import chromadb
from fastapi import HTTPException

# Usar PersistentClient (almacenamiento local)
client = chromadb.PersistentClient(path="./chroma_db")

# Obtén o crea colección
collection = client.get_or_create_collection(name="document_embeddings")

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

def query_embedding(embedding: list[float], top_k: int = 3):
    try:
        results = collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=["documents", "metadatas"]  #  CORREGIDO
        )

        combined = []
        documents = results.get("documents")
        metadatas = results.get("metadatas")
        if documents and documents[0] is not None and metadatas and metadatas[0] is not None:
            for i in range(len(documents[0])):
                combined.append({
                    "document": documents[0][i],
                    "metadata": metadatas[0][i]
                })

        return combined

    except Exception as e:
        print(" ERROR al consultar ChromaDB:", str(e))
        raise HTTPException(status_code=500, detail=f"Error al consultar ChromaDB: {str(e)}")
