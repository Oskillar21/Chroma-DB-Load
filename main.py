from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from api.routes import router

app = FastAPI()
app.include_router(router)