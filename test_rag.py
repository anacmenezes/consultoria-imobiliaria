from src.imobiliaria.rag.retriever import search


query = "Quais são as principais tendências de inteligência artificial?"

results = search(query)

print("\nRESULTADOS DO RAG:")
print("=" * 50)

for i, result in enumerate(results, start=1):
    print(f"\nDOCUMENTO {i}")
    print("-" * 50)
    print(result)