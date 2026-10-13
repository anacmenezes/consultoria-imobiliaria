from crewai import Task


def criar_buscar_imoveis(corretor):

    return Task(
        description=(
            "Pesquise imóveis para o cliente utilizando a ferramenta buscar_imoveis disponível no agente corretor.\n\n"

            "CRITÉRIOS INFORMADOS PELO CLIENTE:\n"
            "- Cidade: {cidade}\n"
            "- Tipo de imóvel: {tipo_imovel}\n"
            "- Finalidade: {finalidade}\n"
            "- Preço máximo: {preco_maximo}\n"
            "- Número de quartos: {quartos}\n"
            "- Área mínima: {area_minima}\n"
            "- Bairros de interesse: {bairros}\n\n"

            "INSTRUÇÕES:\n"
            "1. Utilize os critérios fornecidos para realizar a busca.\n"
            "2. Não invente critérios que o cliente não informou.\n"
            "3. Quando um critério opcional não for informado, não o trate como obrigatório.\n"
            "4. Utilize a ferramenta de busca para pesquisar anúncios.\n"
            "5. Preserve os links e as descrições retornadas pela fonte.\n"
            "6. Diferencie anúncios individuais de páginas que agrupam vários imóveis.\n"
            "7. Não considere preços ou disponibilidade como confirmados sem verificar a fonte original.\n"
            "8. Se não houver resultados suficientes, informe claramente essa limitação."
    ),
        expected_output=(
            "Relatório estruturado da busca contendo:\n"
            "- Critérios utilizados;\n"
            "- Título e link de cada resultado;\n"
            "- Preço anunciado, quando identificado;\n"
            "- Localização, área e quartos, quando disponíveis;\n"
            "- Identificação de páginas de busca versus anúncios individuais;\n"
            "- Informações ausentes ou que precisam de confirmação;\n"
            "- Limitações encontradas durante a pesquisa.\n\n"
            "Não invente informações para preencher campos ausentes."
        ),

        agent=corretor
    )