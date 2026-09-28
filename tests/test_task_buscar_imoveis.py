from imobiliaria.agents.corretor import criar_corretor
from imobiliaria.tasks.buscar_imoveis import criar_task_buscar_imoveis


def main():

    corretor = criar_corretor()

    task = criar_task_buscar_imoveis(corretor)

    print("Task criada com sucesso!")
    print(f"Descrição: {task.description}")
    print(f"Agente: {task.agent.role}")


if __name__ == "__main__":
    main()