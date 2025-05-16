import chromadb

# Crea cliente con persistencia directamente
client = chromadb.PersistentClient(path="./chroma_data")

# Obtén o crea colección
collection = client.get_or_create_collection(name="document_embeddings")

def store_embedding(document_id: str, embedding: list[float], metadata: dict):
    collection.add(
        embeddings=[embedding],
        ids=[document_id],
        metadatas=[metadata]
    )
    # No hace falta llamar a persist, se guarda automáticamente

def get_all_embeddings():
    collection = client.get_or_create_collection(name="document_embeddings")
    data = collection.get()
    return {
        "ids": data["ids"],
        "embeddings": data["embeddings"],
        "metadatas": data["metadatas"]
    }

