# Chroma-DB-Load

API desarrollada con FastAPI para generar embeddings a partir de documentos y almacenarlos en una base de datos vectorial usando ChromaDB. Esta herramienta es ideal para preparar datos que luego se consultan desde otras aplicaciones.

## Características

- Procesamiento de documentos y generación de embeddings
- Almacenamiento en ChromaDB
- Listo para integrarse con sistemas externos

## Instalación y uso

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
uvicorn main:app --reload --port 8002
