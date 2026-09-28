from crewai import Agent
from langchain_openai import ChatOpenAI

from imobiliaria.config import MODEL_NAME
from imobiliaria.tools.imoveis_tool import ImoveisTool


def criar_corretor() -> Agent:

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
    )

    corretor = Agent(
        role="Corretor de imóveis",
        goal=(
            "Encontrar imóveis que atendam aos critérios "
            "informados pelo cliente."
        ),
        backstory=(
            "Você é um corretor de imóveis especializado "
            "em analisar imóveis disponíveis e identificar "
            "opções adequadas às necessidades dos clientes."
        ),
        tools=[ImoveisTool()],
        llm=llm,
        verbose=True
    )

    return corretor