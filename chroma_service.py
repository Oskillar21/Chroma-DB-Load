import chromadb
from chromadb.config import Settings

#inicializa el cliente de chroma
client= chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_storage"
))

# si no existe la coleccion la crea
collection = client.create_collection(name="embeddings")

def save_embedding(id: str, embedding: list[float], metadata: dict):
  
    # guarda el embedding en la coleccion
    collection.add(
        ids=[id],
        embeddings=[embedding],
        metadatas=[metadata]
    )
