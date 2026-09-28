from crewai import Task

from imobiliaria.agents.corretor import criar_corretor


def criar_task_buscar_imoveis(corretor):

    return Task(
        description=(
            "Analise os critérios fornecidos pelo cliente e encontre "
            "imóveis disponíveis que atendam às suas necessidades. "
            "Utilize a ferramenta de busca de imóveis para consultar "
            "os dados disponíveis."
        ),
        expected_output=(
            "Uma lista organizada dos imóveis encontrados, contendo "
            "cidade, tipo, quantidade de quartos, quantidade de "
            "banheiros, área em metros quadrados e preço."
        ),
        agent=corretor
    )