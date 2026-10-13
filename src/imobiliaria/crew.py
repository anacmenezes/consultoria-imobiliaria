from crewai import Crew, Process

from .config import OPENAI_API_KEY, SERPER_API_KEY

from .agents.financeiro import criar_financeiro
from .agents.mercado import criar_mercado
from .agents.corretor import criar_corretor
from .agents.noticias import criar_noticias
from .agents.redator import criar_redator

from .tasks.analisar_financeiro import criar_analisar_financeiro
from .tasks.analisar_mercado import criar_analisar_mercado
from .tasks.buscar_imoveis import criar_buscar_imoveis
from .tasks.buscar_noticias import criar_buscar_noticias
from .tasks.redigir_resposta import criar_redigir_resposta

def criar_crew():

    corretor = criar_corretor()
    financeiro = criar_financeiro()
    mercado = criar_mercado()
    noticias = criar_noticias()
    redator = criar_redator()

    buscar_imoveis = criar_buscar_imoveis(corretor)

    analisar_mercado = criar_analisar_mercado(
        mercado,
        buscar_imoveis
    )

    analisar_financeiro = criar_analisar_financeiro(
        financeiro, 
        buscar_imoveis)

    buscar_noticias = criar_buscar_noticias(noticias)

    redigir_resposta = criar_redigir_resposta(
        redator,
        analisar_mercado,
    )

    return Crew(
        agents=[
            corretor,
            financeiro,
            mercado,
            noticias,
            redator
        ],

        tasks=[
            buscar_imoveis,
            analisar_mercado,
            analisar_financeiro,
            buscar_noticias,
            redigir_resposta
        ],

        process=Process.sequential,

        verbose=True
    )