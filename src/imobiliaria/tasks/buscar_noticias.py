from crewai import Task


def criar_buscar_noticias(noticias):

    return Task(

        description=(
        "Pesquise notícias relevantes para o mercado imobiliário "
        "da região ou do tema solicitado. Priorize fontes "
        "identificáveis e informações recentes quando a atualidade "
        "for relevante. Examine a data de publicação e a relação "
        "da notícia com o mercado. Não invente notícias, fontes "
        "ou datas."
    ),
    expected_output=(
        "Uma lista estruturada de notícias relevantes contendo "
        "título, fonte, data de publicação, resumo, URL quando "
        "disponível e possível impacto no mercado imobiliário. "
        "Sinalize quando não houver notícias suficientes ou "
        "quando a atualidade das informações não puder ser verificada."
        ),

        agent=noticias
    )