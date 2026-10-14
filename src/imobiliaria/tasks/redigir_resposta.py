from crewai import Task

from src.imobiliaria.models.relatorio import RelatorioImobiliario

def criar_redigir_resposta(redator, contexto):

    return Task(

       description=(
        "Consolide os resultados das tasks anteriores que sejam relevantes para a solicitação do cliente. "
        "Produza uma resposta organizada, clara e fundamentada nos dados recebidos. "
        "Diferencie fatos, estimativas e interpretações. "
        "Preserve as fontes, os indicadores e as limitações identificadas. "
        "Não invente informações para preencher lacunas."
    ),
    expected_output=(
        "Um relatório final de consultoria imobiliária com título, "
        "resumo executivo, "
        "análise pertinente à solicitação, "
        "indicadores relevantes, "
        "evidências e fontes disponíveis, "
        "riscos, "
        "limitações e conclusão fundamentada. "
        "Omita seções que não sejam pertinentes ao tipo de consulta."
        ),

        agent=redator,

        context=[contexto],
        output_pydantic=RelatorioImobiliario
    )