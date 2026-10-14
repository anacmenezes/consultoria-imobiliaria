from crewai.tools import tool

from src.imobiliaria.rag.retriever import search

@tool("Busca na base de conhecimento")
def search_market_knowledge(query: str) -> str:
    """
    Busca informações relevantes na base de conhecimento
    utilizando RAG e retorna os documentos encontrados.
    """

    results = search(query)

    if not results:
        return "Nenhuma informação relevante encontrada."

    return "\n\n".join(results)