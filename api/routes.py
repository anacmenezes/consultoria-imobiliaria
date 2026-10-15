from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import Analise
from .schemas import (
    AnaliseCreate,
    AnaliseResponse,
    AnaliseUpdate
)
from .services import (
    gerar_analise,
    atualizar_analise,
    deletar_analise
)

import json

router = APIRouter()

def preparar_resposta(analise):
    try:
        if isinstance(analise.relatorio, str):
            analise.relatorio = json.loads(analise.relatorio)
        return analise
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500,
            detail="O relatório armazenado não contém um JSON válido."
        ) from e

@router.post("/analises", response_model=AnaliseResponse)
def criar_analise(
    request: AnaliseCreate,
    db: Session = Depends(get_db)
):
    analise = gerar_analise(
        cidade=request.cidade,
        tipo_imovel=request.tipo_imovel,
        finalidade=request.finalidade,
        preco_maximo=request.preco_maximo,
        quartos=request.quartos,
        area_minima=request.area_minima,
        bairros=request.bairros,
        db=db,
        )
    
    return preparar_resposta(analise)

@router.get("/analises/{analise_id}", response_model=AnaliseResponse)
def buscar_analise(
    analise_id: int,
    db: Session = Depends(get_db)
):

    analise = (
        db.query(Analise)
        .filter(Analise.id == analise_id)
        .first()
    )

    if isinstance(analise.relatorio, str):
        try:
            analise.relatorio = json.loads(analise.relatorio)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=500,
                detail="O relatório armazenado não contém um JSON válido."
            )

    return preparar_resposta(analise)


@router.put("/analises/{analise_id}", response_model=AnaliseResponse)
def atualizar(
    analise_id: int,
    request: AnaliseUpdate,
    db: Session = Depends(get_db)
):
    analise = atualizar_analise(
        analise_id=analise_id,
        cidade=request.cidade,
        db=db
    )

    if not analise:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada"
        )

    return analise

@router.delete("/analises/{analise_id}")
def deletar(
    analise_id: int,
    db: Session = Depends(get_db)
):
    sucesso = deletar_analise(analise_id, db)

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada"
        )

    return {
        "message": "Análise excluída com sucesso"
    }