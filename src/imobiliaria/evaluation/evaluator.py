def avaliar_task(task_output, criterios):
    texto = task_output.raw

    resultados = {}

    for criterio, palavras in criterios.items():
        resultados[criterio] = any(
            palavra.lower() in texto.lower()
            for palavra in palavras
        )

    total = len(resultados)
    pontos = sum(resultados.values())

    score = (pontos / total) * 10 if total > 0 else 0

    return {
        "criterios": resultados,
        "score": round(score, 1)
    }


def avaliar_qualidade(task_output):
    texto = task_output.raw.lower()

    criterios = {
        "possui_fontes": (
            "fontes internas" in texto
            and "fontes externas" in texto
        ),

        "possui_dados": any(
            palavra in texto
            for palavra in [
                "dados",
                "estatísticas",
                "estatisticas",
                "%",
                "milhões",
                "milhoes",
                "bilhões",
                "bilhoes"
            ]
        ),

        "possui_tendencias": (
            "tendências" in texto
            or "tendencias" in texto
        ),

        "possui_oportunidades": (
            "oportunidades" in texto
        ),

        "possui_desafios": (
            "desafios" in texto
        ),

        "possui_conclusao": (
            "conclusão" in texto
            or "conclusões" in texto
            or "conclusao" in texto
            or "conclusoes" in texto
            or "considerações finais" in texto
        ),

        "possui_estrutura": (
            ("introdução" in texto or "introducao" in texto)
            and (
                "conclusão" in texto
                or "conclusões" in texto
                or "conclusao" in texto
                or "conclusoes" in texto
                or "considerações finais" in texto
            )
        )
    }

    pontos = sum(criterios.values())
    total = len(criterios)

    score = (pontos / total) * 10

    return {
        "criterios": criterios,
        "score": round(score, 1)
    }