from crewai import Crew, Process

from imobiliaria.agents.corretor import criar_corretor
from imobiliaria.agents.mercado import criar_analista_mercado

from imobiliaria.tasks.buscar_imoveis import (
    criar_task_buscar_imoveis
)

from imobiliaria.tasks.analisar_mercado import (
    criar_task_analisar_mercado
)


def criar_crew():

    # =========================
    # AGENTS
    # =========================

    corretor = criar_corretor()

    analista = criar_analista_mercado()

    # =========================
    # TASKS
    # =========================

    buscar_imoveis = criar_task_buscar_imoveis(
        corretor
    )

    analisar_mercado = criar_task_analisar_mercado(
        analista,
        buscar_imoveis
    )

    # =========================
    # CREW
    # =========================

    crew = Crew(
        agents=[
            corretor,
            analista
        ],
        tasks=[
            buscar_imoveis,
            analisar_mercado
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew