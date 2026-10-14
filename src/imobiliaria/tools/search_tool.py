from crewai_tools import SerperDevTool
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

from ..rag.retriever import search


search_tool = SerperDevTool()


class RAGSearchInput(BaseModel):
    query: str = Field(
        ...,
        description="Pergunta ou consulta para buscar na base de conhecimento."
    )


class RAGSearchTool(BaseTool):
    name: str = "Busca na base de conhecimento"

    description: str = (
        "Busca informações relevantes na base de conhecimento "
        "utilizando RAG."
    )

    args_schema: type[BaseModel] = RAGSearchInput

    def _run(self, query: str) -> str:

        results = search(query)

        if not results:
            return "Nenhuma informação relevante encontrada na base de conhecimento."

        formatted_results = []

        for result in results:

            content = result["content"]
            metadata = result["metadata"]

            formatted_results.append(
                f"Fonte: {metadata['source']}\n"
                f"Conteúdo:\n{content}"
            )

        return "\n\n---\n\n".join(formatted_results)