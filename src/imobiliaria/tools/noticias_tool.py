from crewai.tools import BaseTool
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

class NoticiasInput(BaseModel):
    tema: str = Field(
        default="mercado imobiliário",
        description="Tema das notícias a pesquisar."
    )
    cidade: str = Field(
        default="Brasil",
        description="Cidade ou região relacionada às notícias."
    )


class NoticiasTool(BaseTool):
    name: str = "buscar_noticias_imobiliarias"
    description: str = (
        "Pesquisa notícias sobre o mercado imobiliário, "
        "economia, juros e acontecimentos relevantes para o setor."
    )
    args_schema: type[BaseModel] = NoticiasInput

    def _run(
        self,
        tema: str = "mercado imobiliário",
        cidade: str = "Brasil"
    ) -> str:
        consulta = (
            f"notícias sobre {tema} em {cidade} "
            "recentes economia imóveis"
        )

        ferramenta = SerperDevTool()
        resultados = ferramenta.run(search_query=consulta)

        return (
            f"Tema: {tema}\n"
            f"Região: {cidade}\n"
            "Confira a data de publicação, a fonte e os links. "
            "A pesquisa não garante que todas as notícias sejam "
            "recentes ou que os fatos estejam verificados.\n"
            f"Resultados encontrados:\n{resultados}"
        )


noticias_tool = NoticiasTool()