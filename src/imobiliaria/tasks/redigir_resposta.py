from crewai import Task


def criar_task_redigir_resposta(
    redator,
    task_buscar_imoveis,
    task_analisar_mercado,
    task_buscar_noticias,
    task_analisar_financeiro
):

    return Task(
        description=(
            "Elabore a resposta final para o cliente interessado "
            "no mercado imobiliário de {cidade}. "
            "Consolide os resultados produzidos pelo corretor, "
            "analista de mercado, analista de notícias e analista "
            "financeiro. "
            "Apresente os imóveis encontrados, a análise de mercado, "
            "as informações relevantes das notícias e os aspectos "
            "financeiros. "
            "Não invente informações. Diferencie dados observados "
            "de hipóteses ou interpretações."
        ),
        expected_output=(
            "Uma resposta final clara, organizada e objetiva, "
            "com uma síntese dos imóveis encontrados, análise "
            "de mercado, contexto das notícias e análise "
            "financeira."
        ),
        agent=redator,
        context=[
            task_buscar_imoveis,
            task_analisar_mercado,
            task_buscar_noticias,
            task_analisar_financeiro
        ]
    )