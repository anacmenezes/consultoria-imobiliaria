from crewai import Task


def criar_task_analisar_financeiro(
    financeiro,
    task_buscar_imoveis
):

    return Task(
        description=(
            "Analise financeiramente os imóveis encontrados "
            "para a cidade de {cidade}. "
            "Utilize os dados fornecidos pelo corretor para "
            "comparar preços e identificar diferenças relevantes "
            "entre os imóveis. "
            "Quando não houver informações suficientes para "
            "calcular financiamento, deixe isso explícito e "
            "não invente taxas ou condições."
        ),
        expected_output=(
            "Uma análise financeira objetiva dos imóveis, "
            "comparando preços e destacando aspectos financeiros "
            "relevantes para o cliente."
        ),
        agent=financeiro,
        context=[task_buscar_imoveis]
    )