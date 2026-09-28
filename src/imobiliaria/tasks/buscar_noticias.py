from crewai import Task


def criar_task_buscar_noticias(analista):

    return Task(
        description=(
            "Pesquise e analise notícias recentes relacionadas "
            "ao mercado imobiliário de {cidade}. "
            "Identifique informações relevantes sobre preços, "
            "financiamento, juros, oferta, demanda ou mudanças "
            "que possam afetar o mercado local."
        ),
        expected_output=(
            "Um resumo objetivo das notícias relevantes encontradas, "
            "incluindo a informação principal e sua possível relação "
            "com o mercado imobiliário da cidade."
        ),
        agent=analista
    )