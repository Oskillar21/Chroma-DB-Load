from pydantic import BaseModel

# esquema del embedding
class Embedding(BaseModel):
    id: str
    embedding: list[float]
    metadata: dict
