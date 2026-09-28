from crewai import Agent
from langchain_openai import ChatOpenAI

from imobiliaria.config import MODEL_NAME


def criar_analista_mercado() -> Agent:

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
    )

    analista = Agent(
        role="Analista de mercado imobiliário",
        goal=(
            "Analisar as condições do mercado imobiliário "
            "e identificar informações relevantes para "
            "a tomada de decisão do cliente."
        ),
        backstory=(
            "Você é um analista especializado no mercado "
            "imobiliário. Sua função é interpretar dados de "
            "preços, localização e características dos imóveis "
            "e apresentar uma análise objetiva."
        ),
        llm=llm,
        verbose=True
    )

    return analista