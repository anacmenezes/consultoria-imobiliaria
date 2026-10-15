
from sqlalchemy.orm import Session

from src.imobiliaria.crew import criar_crew
from .models import Analise

import json


def gerar_analise(
    cidade: str,
    tipo_imovel: str,
    finalidade: str,
    preco_maximo: float | None,
    quartos: int | None,
    area_minima: float | None,
    bairros: str | None,
    db: Session,
):
    try:
        crew = criar_crew()

        resultado = crew.kickoff(
            inputs={
                "cidade": cidade,
                "tipo_imovel": tipo_imovel,
                "finalidade": finalidade,
                "preco_maximo": preco_maximo,
                "quartos": quartos,
                "area_minima": area_minima,
                "bairros": bairros or "",
            }
        )

        relatorio = resultado.raw

        if isinstance(relatorio, str):
            try:
                relatorio = json.loads(relatorio)
            except json.JSONDecodeError:
                raise ValueError("O relatório gerado não contém um JSON válido.")

        analise = Analise(
            cidade=cidade,
            relatorio=json.dumps(relatorio, ensure_ascii=False)
        )

        db.add(analise)
        db.commit()
        db.refresh(analise)

        return analise

    except Exception as e:
        db.rollback()
        print(f"ERRO REAL AO GERAR ANÁLISE: {e!r}")
        raise RuntimeError(
            "Não foi possível gerar a análise. "
            "Confira o erro real no terminal."
        ) from e


def atualizar_analise(
    analise_id: int,
    cidade: str,
    db: Session,
):
    analise = (
        db.query(Analise)
        .filter(Analise.id == analise_id)
        .first()
    )

    if not analise:
        return None

    analise.cidade = cidade
    db.commit()
    db.refresh(analise)

    return analise


def deletar_analise(analise_id: int, db: Session):
    analise = (
        db.query(Analise)
        .filter(Analise.id == analise_id)
        .first()
    )

    if not analise:
        return False

    db.delete(analise)
    db.commit()

    return True