from crewai import Crew, Process

from imobiliaria.agents.corretor import criar_corretor
from imobiliaria.agents.mercado import criar_analista_mercado
from imobiliaria.agents.noticias import criar_analista_noticias

from imobiliaria.tasks.buscar_imoveis import (
    criar_task_buscar_imoveis
)

from imobiliaria.tasks.analisar_mercado import (
    criar_task_analisar_mercado
)

from imobiliaria.tasks.buscar_noticias import (
    criar_task_buscar_noticias
)


def criar_crew():

    # =========================
    # AGENTS
    # =========================

    corretor = criar_corretor()

    analista_mercado = criar_analista_mercado()

    analista_noticias = criar_analista_noticias()

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

    # =========================
    # CREW
    # =========================

    crew = Crew(
        agents=[
            corretor,
            analista_mercado,
            analista_noticias
        ],
        tasks=[
            buscar_imoveis,
            analisar_mercado,
            buscar_noticias
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew