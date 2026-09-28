from crewai import Crew, Process

from imobiliaria.agents.corretor import criar_corretor
from imobiliaria.agents.mercado import criar_analista_mercado
from imobiliaria.agents.noticias import criar_analista_noticias
from imobiliaria.agents.financeiro import criar_analista_financeiro
from imobiliaria.agents.redator import criar_redator

from imobiliaria.tasks.buscar_imoveis import criar_task_buscar_imoveis
from imobiliaria.tasks.analisar_mercado import criar_task_analisar_mercado
from imobiliaria.tasks.buscar_noticias import criar_task_buscar_noticias
from imobiliaria.tasks.analisar_financeiro import criar_task_analisar_financeiro
from imobiliaria.tasks.redigir_resposta import criar_task_redigir_resposta


def criar_crew():

    # =========================
    # AGENTS
    # =========================

    corretor = criar_corretor()

    analista_mercado = criar_analista_mercado()

    analista_noticias = criar_analista_noticias()

    analista_financeiro = criar_analista_financeiro()

    redator = criar_redator()

    # =========================
    # TASKS
    # =========================

    buscar_imoveis = criar_task_buscar_imoveis(
        corretor
    )

    analisar_mercado = criar_task_analisar_mercado(
        analista_mercado,
        buscar_imoveis
    )

    buscar_noticias = criar_task_buscar_noticias(
        analista_noticias
    )

    analisar_financeiro = criar_task_analisar_financeiro(
        analista_financeiro,
        buscar_imoveis
    )

    redigir_resposta = criar_task_redigir_resposta(
        redator,
        buscar_imoveis,
        analisar_mercado,
        buscar_noticias,
        analisar_financeiro
    )

    # =========================
    # CREW
    # =========================

    crew = Crew(
        agents=[
            corretor,
            analista_mercado,
            analista_noticias,
            analista_financeiro,
            redator
        ],
        tasks=[
            buscar_imoveis,
            analisar_mercado,
            buscar_noticias,
            analisar_financeiro,
            redigir_resposta
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew