import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

collection = client.get_or_create_collection(name="document_embeddings")

def store_embedding(document_id: str, embedding: list[float], metadata: dict):
    collection.add(
        embeddings=[embedding],
        ids=[document_id],
        metadatas=[metadata]
    )
