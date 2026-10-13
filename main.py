
from src.imobiliaria.crew import criar_crew


def ler_texto(mensagem, padrao=None):
    valor = input(mensagem).strip()

    if not valor and padrao is not None:
        return padrao

    return valor


def ler_preco_maximo():
    while True:
        valor = input(
            "Preço máximo em reais (Enter para não informar): "
        ).strip()

        if not valor:
            return None

        valor = valor.replace("R$", "").replace(" ", "")

        if "," in valor and "." in valor:
            if valor.rfind(",") > valor.rfind("."):
                valor = valor.replace(".", "").replace(",", ".")
            else:
                valor = valor.replace(",", "")
        elif "," in valor:
            valor = valor.replace(",", ".")

        try:
            preco = float(valor)

            if preco <= 0:
                print("Informe um valor maior que zero.")
                continue

            return preco

        except ValueError:
            print("Valor inválido. Exemplo: 350000 ou 350000,00.")


def main():
    print("\n===== CONSULTORIA IMOBILIÁRIA =====\n")
    print("Informe os critérios desejados para a busca.\n")

    cidade = ler_texto("Cidade: ", "São Paulo")
    tipo_imovel = ler_texto(
        "Tipo de imóvel (apartamento, casa etc.): ",
        "apartamento"
    )
    finalidade = ler_texto(
        "Finalidade (compra ou aluguel): ",
        "compra"
    )
    preco_maximo = ler_preco_maximo()
    quartos = ler_texto(
        "Número de quartos (Enter para não informar): "
    )
    area_minima = ler_texto(
        "Área mínima em m² (Enter para não informar): "
    )
    bairros = ler_texto(
        "Bairros de interesse (Enter para não informar): "
    )

    # Valores vazios são mantidos como strings vazias para que
    # as variáveis usadas nas descrições das tarefas sejam preenchidas.
    inputs = {
        "cidade": cidade,
        "tipo_imovel": tipo_imovel,
        "finalidade": finalidade,
        "preco_maximo": (
            f"R$ {preco_maximo:,.2f}".replace(",", "X")
            .replace(".", ",").replace("X", ".")
            if preco_maximo is not None
            else "Não informado"
        ),
        "quartos": quartos or "Não informado",
        "area_minima": area_minima or "Não informada",
        "bairros": bairros or "Não informados",
    }

    print("\n===== CRITÉRIOS DA BUSCA =====")
    for criterio, valor in inputs.items():
        print(f"{criterio}: {valor}")

    try:
        crew = criar_crew()

        resultado = crew.kickoff(inputs=inputs)

        print("\n===== RESULTADO FINAL =====\n")
        print(resultado)

    except Exception as erro:
        print("\n===== ERRO NA EXECUÇÃO =====")
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()