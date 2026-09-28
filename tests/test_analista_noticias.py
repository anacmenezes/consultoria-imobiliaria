from crewai import Crew, Process

from imobiliaria.agents.noticias import criar_analista_noticias
from imobiliaria.tasks.buscar_noticias import criar_task_buscar_noticias


def main():

    analista = criar_analista_noticias()

    task = criar_task_buscar_noticias(analista)

    crew = Crew(
        agents=[analista],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    resultado = crew.kickoff(
        inputs={
            "cidade": "Rio de Janeiro"
        }
    )

    print("\n===== RESULTADO =====\n")
    print(resultado)


if __name__ == "__main__":
    main()