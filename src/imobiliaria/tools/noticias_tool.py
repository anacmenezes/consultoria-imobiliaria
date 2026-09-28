from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from ddgs import DDGS


class NoticiasInput(BaseModel):
    cidade: str = Field(
        ...,
        description="Cidade cujo mercado imobiliário deve ser pesquisado."
    )


class NoticiasTool(BaseTool):

    name: str = "buscar_noticias_imobiliarias"

    description: str = (
        "Pesquisa notícias recentes relacionadas ao mercado "
        "imobiliário de uma determinada cidade."
    )

    args_schema: type[BaseModel] = NoticiasInput

    def _run(self, cidade: str) -> str:

        consulta = f"mercado imobiliário {cidade}"

        resultados = []

        with DDGS() as ddgs:

            noticias = ddgs.news(
                consulta,
                max_results=5
            )

            for noticia in noticias:

                resultados.append({
                    "titulo": noticia.get("title"),
                    "descricao": noticia.get("body"),
                    "url": noticia.get("url"),
                    "data": noticia.get("date")
                })

        if not resultados:
            return f"Nenhuma notícia encontrada para {cidade}."

        return str(resultados)