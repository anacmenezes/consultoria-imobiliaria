
from crewai import Task


def criar_buscar_imoveis(corretor):
    return Task(
        description=(
            "Pesquise imóveis para o cliente utilizando a ferramenta "
            "buscar_imoveis disponível no agente corretor.\n\n"

            "CRITÉRIOS INFORMADOS PELO CLIENTE:\n"
            "- Cidade: {cidade}\n"
            "- Tipo de imóvel: {tipo_imovel}\n"
            "- Finalidade: {finalidade}\n"
            "- Preço máximo: {preco_maximo}\n"
            "- Número de quartos: {quartos}\n"
            "- Área mínima: {area_minima}\n"
            "- Bairros de interesse: {bairros}\n\n"

            "REGRAS DE BUSCA:\n"
            "1. Utilize a ferramenta buscar_imoveis para consultar anúncios reais.\n"
            "2. Construa a consulta com os critérios efetivamente informados.\n"
            "3. Considere preço, quartos, área e bairros como opcionais quando "
            "não forem informados pelo cliente.\n"
            "4. Não interprete valores ausentes, vazios ou nulos como zero.\n"
            "5. Se a primeira busca não retornar resultados, tente uma consulta "
            "alternativa mais ampla, sem descartar os critérios essenciais.\n"
            "6. Não invente anúncios, preços, links, características ou "
            "disponibilidade.\n"
            "7. Preserve os links e as descrições retornadas pela ferramenta.\n"
            "8. Diferencie anúncios individuais de páginas de resultados.\n"
            "9. Não declare que o mercado não possui imóveis apenas porque "
            "uma consulta não retornou resultados.\n"
            "10. Registre quando a busca falhar, retornar vazia ou apresentar "
            "informações insuficientes.\n\n"

            "ANÁLISE DOS RESULTADOS:\n"
            "Para cada imóvel encontrado, informe apenas os dados disponíveis "
            "na fonte: título, link, preço, localização, área e quartos.\n"
            "Identifique quais informações foram confirmadas e quais "
            "precisam de verificação.\n"
            "Não transforme resultados de busca em anúncios confirmados."
        ),
        expected_output=(
            "Relatório da busca contendo:\n"
            "- Critérios utilizados;\n"
            "- Consultas realizadas;\n"
            "- Título e link de cada resultado;\n"
            "- Preço, localização, área e quartos, quando disponíveis;\n"
            "- Tipo de página: anúncio individual ou página de resultados;\n"
            "- Informações ausentes ou não verificadas;\n"
            "- Quantidade de resultados retornados pela ferramenta;\n"
            "- Tentativas alternativas realizadas, se necessárias;\n"
            "- Limitações e possíveis causas de ausência de resultados.\n\n"
            "Se nenhum resultado for encontrado, informe isso explicitamente. "
            "Não invente dados para preencher campos ausentes."
        ),
        agent=corretor
    )