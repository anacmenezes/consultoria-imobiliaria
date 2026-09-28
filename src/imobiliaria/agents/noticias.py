from crewai import Agent
from langchain_openai import ChatOpenAI

from imobiliaria.config import MODEL_NAME
from imobiliaria.tools.noticias_tool import NoticiasTool


def criar_analista_noticias() -> Agent:

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
    )

    analista = Agent(
        role="Analista de notícias do mercado imobiliário",
        goal=(
            "Pesquisar e analisar notícias relevantes sobre o "
            "mercado imobiliário da cidade solicitada pelo cliente."
        ),
        backstory=(
            "Você é um analista especializado em acompanhar "
            "notícias econômicas e imobiliárias. Sua função é "
            "identificar informações recentes que possam "
            "influenciar preços, financiamento, oferta ou "
            "demanda de imóveis."
        ),
        tools=[NoticiasTool()],
        llm=llm,
        verbose=True
    )

    return analista