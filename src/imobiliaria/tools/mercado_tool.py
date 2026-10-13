from crewai.tools import BaseTool
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field


class MercadoInput(BaseModel):
    cidade: str = Field(
        ...,
        description="Cidade ou região a ser analisada."
    )
    tema: str = Field(
        default="preços de imóveis e aluguel",
        description="Indicador ou assunto do mercado imobiliário."
    )


class MercadoTool(BaseTool):
    name: str = "consultar_mercado_imobiliario"
    description: str = (
        "Pesquisa indicadores, estudos e tendências do mercado "
        "imobiliário de uma cidade ou região."
    )
    args_schema: type[BaseModel] = MercadoInput

    def _run(
        self,
        cidade: str,
        tema: str = "preços de imóveis e aluguel"
    ) -> str:
        consulta = (
            f"mercado imobiliário em {cidade} "
            f"{tema} indicadores estudos dados"
        )

        ferramenta = SerperDevTool()
        resultados = ferramenta.run(search_query=consulta)

        return (
            f"Região: {cidade}\n"
            f"Tema pesquisado: {tema}\n"
            "Verifique as datas, as fontes e a metodologia dos dados. "
            "Preços anunciados não representam necessariamente preços "
            "de transações efetivamente realizadas.\n"
            f"Resultados encontrados:\n{resultados}"
        )


mercado_tool = MercadoTool()