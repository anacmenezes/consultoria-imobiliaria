from api.routes import router
from api.database import Base, engine
from api import models

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Imobiliária - Multiagente",
    description="API de imobiliária padrão utilizando CrewAI, RAG e LLMs.",
    version="1.0.0"
)

app.include_router(router)

@app.exception_handler(Exception)
async def tratar_erro_global(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Erro interno do servidor."
        }
    )