from fastapi import APIRouter, HTTPException
from models.embedding import Embedding
from services.chroma_service import store_embedding as save_embedding

router = APIRouter()

@router.post("/store_embedding")
def store_embedding_api(payload: Embedding):
    try:
        save_embedding(payload.id, payload.embedding, payload.metadata)
        return {"message": "Embedding almacenado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
