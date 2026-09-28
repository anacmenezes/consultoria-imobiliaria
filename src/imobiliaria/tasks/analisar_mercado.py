from crewai import Task


def criar_task_analisar_mercado(analista, task_buscar_imoveis):

    return Task(
        description=(
            "Analise os imóveis encontrados pelo corretor "
            "para a cidade de {cidade}. "
            "Avalie os preços, tipos de imóveis, quantidade "
            "de quartos, áreas e demais características. "
            "Identifique padrões e apresente uma análise "
            "objetiva do conjunto de imóveis."
        ),
        expected_output=(
            "Uma análise objetiva do mercado imobiliário "
            "com base nos imóveis encontrados, destacando "
            "faixas de preço, características predominantes "
            "e observações relevantes para o cliente."
        ),
        agent=analista,
        context=[task_buscar_imoveis]
    )