from imobiliaria.agents.corretor import criar_corretor


def main():

    corretor = criar_corretor()

    print("Agente criado com sucesso!")
    print(f"Role: {corretor.role}")
    print(f"Goal: {corretor.goal}")


if __name__ == "__main__":
    main()