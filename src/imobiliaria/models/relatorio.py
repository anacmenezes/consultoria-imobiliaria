
from typing import List
from pydantic import BaseModel, Field


class RelatorioImobiliario(BaseModel):
    contexto: str = Field(
        description="Resumo do cenário imobiliário da cidade ou região analisada."
    )

    imoveis: List[str] = Field(
        description="Lista de imóveis encontrados, com características, preços e localização disponíveis."
    )

    analise_financeira: List[str] = Field(
        description="Informações sobre financiamento, capacidade de pagamento, custos e condições financeiras."
    )

    tendencias_mercado: List[str] = Field(
        description="Tendências identificadas no mercado imobiliário da região."
    )

    estatisticas: List[str] = Field(
        description="Dados quantitativos encontrados, com período e contexto quando disponíveis."
    )

    oportunidades: List[str] = Field(
        description="Oportunidades imobiliárias identificadas com base nos dados coletados."
    )

    desafios: List[str] = Field(
        description="Riscos, limitações e dificuldades identificados na análise."
    )

    noticias_relevantes: List[str] = Field(
        description="Notícias relevantes para o mercado imobiliário analisado."
    )

    fontes_internas: List[str] = Field(
        default_factory=list,
        description=(
            "Somente documentos locais efetivamente consultados pelo RAG. "
            "Não incluir sites ou plataformas externas."
        )
    )

    fontes_externas: List[str] = Field(
        default_factory=list,
        description=(
            "URLs ou referências de páginas externas efetivamente consultadas. "
            "Não inventar links nem incluir fontes apenas mencionadas."
        )
    )

    estatisticas: List[str] = Field(
        default_factory=list,
        description=(
            "Indicadores calculados a partir dos dados disponíveis. "
            "Informar a base utilizada e as limitações. "
            "Não apresentar estimativas como fatos verificados."
        )
    )