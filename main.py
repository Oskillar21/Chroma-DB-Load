from fastapi import FastAPI, HTTPException
from pydantic  import BaseModel
from chroma_service import save_embedding

app = FastAPI()

# esquema del embeding
class Embedding(BaseModel):
    id: str
    embedding: list[float]
    metadata: dict


@app.post("/store_embedding")
def store_embedding_api(embedding: Embedding):
    try:
        save_embedding(embedding.id, embedding.embedding, embedding.metadata)
        return {"message": "Embedding almacenado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    