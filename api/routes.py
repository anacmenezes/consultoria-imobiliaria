
import json

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .database import get_db
from .models import Analise
from .schemas import AnaliseCreate, AnaliseResponse, AnaliseUpdate
from .services import gerar_analise, atualizar_analise, deletar_analise

router = APIRouter()


def preparar_resposta(analise: Analise) -> dict:
    """Converte o relatório armazenado em uma resposta compatível com a API."""
    relatorio = analise.relatorio

    if isinstance(relatorio, str):
        try:
            relatorio = json.loads(relatorio)
        except json.JSONDecodeError as exc:
            raise HTTPException(
                status_code=500,
                detail="O relatório armazenado não contém um JSON válido."
            ) from exc

    return {
        "id": analise.id,
        "cidade": analise.cidade,
        "relatorio": relatorio,
    }


@router.post("/analises", response_model=AnaliseResponse, status_code=201)
def criar_analise(
    request: AnaliseCreate,
    db: Session = Depends(get_db),
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


@router.get("/analises", response_model=list[AnaliseResponse])
def listar_analises(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    analises = (
        db.query(Analise)
        .order_by(Analise.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return [preparar_resposta(a) for a in analises]


@router.get("/analises/{analise_id}", response_model=AnaliseResponse)
def buscar_analise(
    analise_id: int,
    db: Session = Depends(get_db),
):
    analise = (
        db.query(Analise)
        .filter(Analise.id == analise_id)
        .first()
    )

    if analise is None:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada."
        )

    return preparar_resposta(analise)


@router.put("/analises/{analise_id}", response_model=AnaliseResponse)
def atualizar(
    analise_id: int,
    request: AnaliseUpdate,
    db: Session = Depends(get_db),
):
    analise = atualizar_analise(
        analise_id=analise_id,
        cidade=request.cidade,
        db=db,
    )

    if analise is None:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada."
        )

    return preparar_resposta(analise)


@router.delete("/analises/{analise_id}")
def deletar(
    analise_id: int,
    db: Session = Depends(get_db),
):
    sucesso = deletar_analise(analise_id, db)

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada."
        )

    return {"message": "Análise excluída com sucesso."}