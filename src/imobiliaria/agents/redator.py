from crewai import Agent
from langchain_openai import ChatOpenAI

from imobiliaria.config import MODEL_NAME


def criar_redator() -> Agent:

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0
    )

    redator = Agent(
        role="Consultor imobiliário e redator final",
        goal=(
            "Consolidar as informações produzidas pelos "
            "especialistas e apresentar uma resposta clara, "
            "objetiva e útil para o cliente."
        ),
        backstory=(
            "Você é responsável por transformar análises "
            "imobiliárias, financeiras e de mercado em uma "
            "resposta final compreensível. "
            "Utilize somente as informações fornecidas pelas "
            "outras etapas. Não invente dados. "
            "Diferencie claramente fatos de hipóteses."
        ),
        llm=llm,
        verbose=True
    )

    return redator