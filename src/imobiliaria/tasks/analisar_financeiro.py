from crewai import Task


def criar_analisar_financeiro(financeiro, contexto):

    return Task(

        description=(
        "Analise a viabilidade financeira dos imóveis com base nos dados fornecidos."
        "Considere preço de aquisição, aluguel estimado, despesas, rentabilidade e riscos financeiros. "
        "Identifique informações ausentes e diferencie dados confirmados de estimativas. "
        "Não invente valores nem realize recomendações sem evidências suficientes."
    ),
    expected_output=(
        "Uma análise financeira estruturada contendo os imóveis avaliados, "
        "os dados financeiros disponíveis, as estimativas de receitas e despesas, "
        "os indicadores de rentabilidade fornecidos ou calculados pelo sistema, "
        "os principais riscos e as limitações da análise."
        ),

        agent=financeiro,

        context=[contexto]
    )