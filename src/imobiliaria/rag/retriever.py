import chromadb
from chromadb.utils import embedding_functions


CHROMA_PATH = "data/chroma"


def get_collection():

    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    return client.get_or_create_collection(
        name="imobiliaria",
        embedding_function=embedding_function
    )


def search(query: str, n_results: int = 3):

    collection = get_collection()

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    return [
        {
            "content": document,
            "metadata": metadata
        }
        for document, metadata in zip(
            documents,
            metadatas
        )
    ]