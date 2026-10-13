from crewai import Task


def criar_analisar_mercado(mercado, contexto):

    return Task(

        description=(
        "Analise os dados imobiliários coletados para a região solicitada. "
        "Identifique padrões de preços, características dos imóveis, diferenças regionais e tendências observáveis. "
        "Considere o período, a origem e a representatividade dos dados. "
        "Não invente estatísticas nem trate preços anunciados como valores de transações concluídas."
    ),
    expected_output=(
        "Um relatório de mercado contendo a região analisada, "
        "a quantidade e o perfil dos imóveis da amostra, "
        "as faixas de preços observadas, os padrões identificados, "
        "as fontes disponíveis e as limitações dos dados."
        ),

        agent=mercado,

        context=[contexto]
    )