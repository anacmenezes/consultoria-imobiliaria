from crewai import Agent
from ..config import MODEL_NAME
from ..tools.imoveis_tool import imoveis_tool

def criar_corretor():
    return Agent(
        role="Corretor Imobiliário",
        goal="Buscar e organizar imóveis em {cidade} conforme os critérios informados pelo cliente.",
        backstory="""
            Você é um profissional especializado no mercado
            imobiliário de {cidade}.

            Sua função é buscar e organizar imóveis compatíveis
            com os critérios do cliente, apresentando informações
            claras e estruturadas.

            Não invente anúncios, preços ou características.
            Quando os dados forem insuficientes, informe
            as limitações encontradas.
        """,
        llm=MODEL_NAME,
        tools=[imoveis_tool],
        allow_delegation=False,
        verbose=True
    )