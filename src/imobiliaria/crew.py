from crewai import Crew, Process

from imobiliaria.agents.corretor import criar_corretor
from imobiliaria.tasks.buscar_imoveis import criar_task_buscar_imoveis


def criar_crew():

    corretor = criar_corretor()

    buscar_imoveis = criar_task_buscar_imoveis(
        corretor
    )

    crew = Crew(
        agents=[corretor],
        tasks=[buscar_imoveis],
        process=Process.sequential,
        verbose=True
    )

    return crew