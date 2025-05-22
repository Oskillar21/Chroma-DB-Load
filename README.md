# Chroma-DB-Load


API encargada de la generacion de Embeddings para su debido guardado.

Cuando descarguen los cambios de la rama ejecutar el siguiente comando para que le instale todas las dependencias necesarias del proyecto.

python -m venv venv ///hace un entorno virtual necesario para que corran las APIs
venv\Scripts\activate /// activa el entorno virtual
pip install -r requirements.txt /// instala dependencias
deactivate /// para desactivar el venv

uvicorn main:app --reload --port 8002 /// levantar la API (Con el venv activado)

http://127.0.0.1:8002/docs#/ /// direccion para que abra swagger
http://127.0.0.1:8002/process-documents /// Solicitud POST en postman
PD: Poner localhost si gustan xd, asi lo tiro chat jjj

Estructura JSON a utilizar
{
"id": "pruebaaaa2222",
"embedding": [
0.1, 0.2, 0.3
],
"metadata": {
"source": "testsegundo"
}
}
=======
API encargada de la generacion de Embeddings para su debido guardado. 


Nueva edicion para veficacion de commits
