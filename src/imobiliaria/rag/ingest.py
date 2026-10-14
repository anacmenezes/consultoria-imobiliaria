from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions

from .splitter import split_text


DOCUMENTS_PATH = Path("data/documents")
CHROMA_PATH = "data/chroma"

def create_vector_store():

    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="imobiliaria",
        embedding_function=embedding_function
    )
    
    collection.delete(
    where={"source": "mercado_imobiliario.txt"}
    )

    documents = []
    metadatas = []
    ids = []

    for file in DOCUMENTS_PATH.glob("*.txt"):

        content = file.read_text(
            encoding="utf-8-sig"
        )

        chunks = split_text(content)

        for index, chunk in enumerate(chunks):

            documents.append(chunk)

            metadatas.append({
                "source": file.name,
                "chunk_id": index
            })

            ids.append(
                f"{file.stem}_chunk_{index}"
            )

    if documents:

        collection.upsert(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    return collection


if __name__ == "__main__":

    collection = create_vector_store()

    print(
        f"Documentos/chunks indexados: {collection.count()}"
    )