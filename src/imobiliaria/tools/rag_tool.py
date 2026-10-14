
from crewai.tools import tool

from src.imobiliaria.rag.retriever import search


@tool("Buscar conhecimento imobiliário")
def buscar_conhecimento_imobiliario(query: str) -> str:
    """
    Busca informações na base de conhecimento imobiliário local.
    Use para consultar documentos sobre financiamento, amortização,
    custos de aquisição, avaliação e análise de imóveis.
    """

    try:
        results = search(query, n_results=3)

        if not results:
            return "Nenhum documento relevante foi encontrado na base local."

        resposta = []

        for i, result in enumerate(results, start=1):
            conteudo = result.get("content", "")
            metadata = result.get("metadata") or {}
            fonte = metadata.get("source", "Fonte não identificada")

            resposta.append(
                f"Documento {i} | Fonte: {fonte}\n{conteudo}"
            )

        return "\n\n".join(resposta)

    except Exception as e:
        return f"Erro ao consultar a base de conhecimento: {e}"