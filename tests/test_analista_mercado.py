from imobiliaria.agents.mercado import criar_analista_mercado


def main():

    analista = criar_analista_mercado()

    print("Agente criado com sucesso!")
    print(f"Role: {analista.role}")
    print(f"Goal: {analista.goal}")


if __name__ == "__main__":
    main()