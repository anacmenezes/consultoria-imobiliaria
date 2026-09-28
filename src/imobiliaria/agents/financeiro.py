from crewai import Agent
from langchain_openai import ChatOpenAI

from imobiliaria.config import MODEL_NAME


def criar_analista_financeiro() -> Agent:

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
    )

    analista = Agent(
        role="Analista financeiro imobiliário",
        goal=(
            "Analisar os aspectos financeiros relacionados aos "
            "imóveis encontrados e fornecer informações úteis "
            "para a tomada de decisão do cliente."
        ),
        backstory=(
            "Você é um analista financeiro especializado no "
            "mercado imobiliário. Sua função é analisar preços "
            "de imóveis, comparar valores e, quando houver dados "
            "suficientes, avaliar cenários de financiamento. "
            "Nunca invente taxas, juros, renda ou condições "
            "financeiras que não tenham sido fornecidas."
        ),
        llm=llm,
        verbose=True
    )

    return analista