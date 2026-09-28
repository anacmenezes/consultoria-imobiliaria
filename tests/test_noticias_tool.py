from imobiliaria.tools.noticias_tool import NoticiasTool


def main():

    tool = NoticiasTool()

    resultado = tool._run("Rio de Janeiro")

    print("\n===== NOTÍCIAS =====\n")
    print(resultado)


if __name__ == "__main__":
    main()