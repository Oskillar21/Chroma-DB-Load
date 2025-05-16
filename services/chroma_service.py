import chromadb

# Usar PersistentClient (almacenamiento local)
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="document_embeddings")

def store_embedding(document_id: str, embedding: list[float], metadata: dict):
    collection.add(
        embeddings=[embedding],
        ids=[document_id],
        metadatas=[metadata]
    )
