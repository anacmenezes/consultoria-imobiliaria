from imobiliaria.agents.financeiro import criar_analista_financeiro


def main():

    financeiro = criar_analista_financeiro()

    print("Agente criado com sucesso!")
    print(f"Role: {financeiro.role}")
    print(f"Goal: {financeiro.goal}")


if __name__ == "__main__":
    main()