from fastapi import APIRouter, HTTPException
from models.embedding import Embedding
from services.chroma_service import get_all_embeddings, store_embedding as save_embedding
from services.chroma_service import store_embedding as save_embedding
from services.chroma_service import get_all_embeddings, store_embedding as save_embedding

router = APIRouter()

@router.post("/store_embedding")
def store_embedding_api(payload: Embedding):
    try:
        save_embedding(payload.id, payload.embedding, payload.metadata)
        return {"message": "Embedding almacenado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_embeddings")
def get_embeddings_api():
    try:
        data = get_all_embeddings()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))