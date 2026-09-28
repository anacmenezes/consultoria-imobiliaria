from crewai import Crew, Process, Task

from imobiliaria.agents.redator import criar_redator


def main():

    redator = criar_redator()

    task_imoveis = Task(
        description=(
            "Forneça os seguintes imóveis encontrados no Rio de Janeiro: "
            "Apartamento, 2 quartos, 90 m², R$ 675.138; "
            "Cobertura, 1 quarto, 59 m², R$ 1.927.052."
        ),
        expected_output="Lista dos imóveis encontrados.",
        agent=redator
    )

    task_mercado = Task(
        description=(
            "Informe que foram encontrados dois imóveis com "
            "preços e características diferentes."
        ),
        expected_output="Resumo da análise de mercado.",
        agent=redator
    )

    task_noticias = Task(
        description=(
            "Informe que existem notícias recentes indicando "
            "movimentação no mercado imobiliário do Rio de Janeiro."
        ),
        expected_output="Resumo das notícias.",
        agent=redator
    )

    task_financeiro = Task(
        description=(
            "Compare os preços dos dois imóveis e informe que "
            "o segundo possui preço significativamente maior."
        ),
        expected_output="Resumo financeiro.",
        agent=redator
    )

    task_final = Task(
        description=(
            "Produza uma resposta final para um cliente interessado "
            "em imóveis no Rio de Janeiro. Consolide todas as "
            "informações recebidas das tarefas anteriores. "
            "Não invente informações."
        ),
        expected_output=(
            "Resposta final clara e organizada para o cliente."
        ),
        agent=redator,
        context=[
            task_imoveis,
            task_mercado,
            task_noticias,
            task_financeiro
        ]
    )

    crew = Crew(
        agents=[redator],
        tasks=[
            task_imoveis,
            task_mercado,
            task_noticias,
            task_financeiro,
            task_final
        ],
        process=Process.sequential,
        verbose=True
    )

    resultado = crew.kickoff()

    print("\n===== RESULTADO FINAL =====\n")
    print(resultado)


if __name__ == "__main__":
    main()