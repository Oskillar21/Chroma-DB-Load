from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.embedding import Embedding
from fastapi.responses import JSONResponse
from services.chroma_service import (
    store_embedding as save_embedding,
    get_all_embeddings,
    query_similar_documents,
)

router = APIRouter()

# Modelo para la consulta de similitud
class QueryRequest(BaseModel):
    embedding: list[float]
    top_k: int

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

class MessageInput(BaseModel):
    message: str

@router.post("/embeddings")
def chroma_response(input: MessageInput):
    try:
        response = query_similar_documents(input.message)
        return {"response": response}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"},
        )