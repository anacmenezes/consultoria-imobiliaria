from imobiliaria.tools.imoveis_tool import ImoveisTool


def main():
    tool = ImoveisTool()

    resultado = tool._run("Rio de Janeiro")

    print(resultado)

if __name__ == "__main__":
    main()