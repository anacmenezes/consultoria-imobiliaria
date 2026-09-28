from imobiliaria.crew import criar_crew


def main():

    crew = criar_crew()

    resultado = crew.kickoff(
        inputs={
            "cidade": "Rio de Janeiro"
        }
    )

    print("\n===== RESULTADO =====\n")
    print(resultado)


if __name__ == "__main__":
    main()