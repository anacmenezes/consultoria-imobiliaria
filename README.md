# 🏠 Consultoria Imobiliária Multiagente

Sistema de consultoria imobiliária desenvolvido em Python utilizando **CrewAI**, com uma arquitetura multiagente formada por especialistas responsáveis por busca de imóveis, análise de mercado, análise de notícias, análise financeira e geração do relatório final.

O projeto foi estruturado de forma modular, separando **Agents, Tasks, Tools, dados e orquestração**, permitindo evolução futura para RAG, memória, validação e observabilidade.

---

## 🚀 Sobre o Projeto

A aplicação simula uma equipe de especialistas em mercado imobiliário.

O usuário informa uma cidade e o sistema executa um fluxo multiagente para:

- 🔎 Buscar imóveis disponíveis
- 📊 Analisar características e preços
- 📰 Pesquisar notícias relacionadas ao mercado imobiliário
- 💰 Realizar análise financeira
- 📝 Consolidar as informações em uma resposta final

O objetivo é demonstrar na prática conceitos de **Engenharia de IA, sistemas multiagentes, ferramentas, orquestração e passagem de contexto entre agentes**.

---

## 🤖 Arquitetura Multiagente

```text
                         👤 CLIENTE
                             │
                             ▼
                         🧠 CREW
                             │
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                 ▼
       🏠 CORRETOR       📊 MERCADO        📰 NOTÍCIAS
           │                 │                 │
           ▼                 ▼                 ▼
      ImoveisTool          Análise         NoticiasTool
           │                 │                 │
           └─────────────────┼─────────────────┘
                             ▼
                       💰 FINANCEIRO
                             │
                             ▼
                         📝 REDATOR
                             │
                             ▼
                      📋 RESPOSTA FINAL
