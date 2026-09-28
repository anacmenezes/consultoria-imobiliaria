import random
from pathlib import Path

import pandas as pd


def gerar_imoveis(quantidade: int = 20):

    cidades = [
        "Rio de Janeiro",
        "São Paulo",
        "Belo Horizonte",
        "Niterói",
        "Campos dos Goytacazes",
    ]

    tipos = [
        "Apartamento",
        "Casa",
        "Cobertura",
    ]

    imoveis = []

    for i in range(1, quantidade + 1):
        imovel = {
            "id": i,
            "cidade": random.choice(cidades),
            "tipo": random.choice(tipos),
            "quartos": random.randint(1, 5),
            "banheiros": random.randint(1, 4),
            "area_m2": random.randint(40, 250),
            "preco": random.randint(200000, 2000000),
        }

        imoveis.append(imovel)

    return pd.DataFrame(imoveis)


def salvar_imoveis():

    df = gerar_imoveis()

    base_dir = Path(__file__).resolve().parents[2]
    data_dir = base_dir / "data"

    data_dir.mkdir(exist_ok=True)

    csv_path = data_dir / "imoveis.csv"

    df.to_csv(
        csv_path,
        index=False,
        encoding="utf-8"
    )

    print(f"Arquivo criado em: {csv_path}")


if __name__ == "__main__":
    salvar_imoveis()