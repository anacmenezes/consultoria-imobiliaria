from pathlib import Path

import pandas as pd
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class ImoveisInput(BaseModel):
    cidade: str = Field(
        ...,
        description="Nome da cidade onde o usuário deseja encontrar imóveis."
    )


class ImoveisTool(BaseTool):
    name: str = "buscar_imoveis"

    description: str = (
        "Busca imóveis disponíveis no banco de dados "
        "a partir da cidade informada."
    )

    args_schema: type[BaseModel] = ImoveisInput

    def _run(self, cidade: str) -> str:

        base_dir = Path(__file__).resolve().parents[3]
        csv_path = base_dir / "data" / "imoveis.csv"

        df = pd.read_csv(csv_path)

        resultado = df[
            df["cidade"].str.lower() == cidade.lower()
        ]

        if resultado.empty:
            return f"Nenhum imóvel encontrado em {cidade}."

        return resultado.to_json(
            orient="records",
            force_ascii=False
        )