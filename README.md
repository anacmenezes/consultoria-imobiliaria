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

## 🛠️ Tecnologias
- Python
- CrewAI
- CrewAI Tools
- Pandas
- DDGS
- OpenAI API
- python-dotenv
- CSV

---

## 🔄 Fluxo de Execução

              1. Cliente informa a cidade
                          ↓
              2. Corretor consulta os imóveis
                          ↓
              3. Analista de Mercado analisa os imóveis
                          ↓
              4. Analista de Notícias pesquisa informações
                          ↓
              5. Analista Financeiro realiza a análise
                          ↓
              6. Redator recebe os resultados
                          ↓
              7. Sistema gera a resposta final

---

## ⚙️ Instalação

Clone o repositório:

git clone https://github.com/anacmenezes/consultoria-imobiliaria.git

Entre na pasta:

cd consultoria-imobiliaria

Crie o ambiente virtual:

python -m venv .venv

Ative o ambiente:

.\.venv\Scripts\Activate.ps1

Instale as dependências:

pip install -r requirements.txt

---

## 🔐 Configuração

Crie um arquivo .env na raiz do projeto:

OPENAI_API_KEY=sua_chave_aqui

O arquivo .env não deve ser enviado para o GitHub.

Utilize o .env.example como referência.

---

## ▶️ Executando o Projeto

Com o ambiente virtual ativado:

python -m imobiliaria.main

O sistema executará o fluxo completo dos agentes.

---

## 🧪 Testes
Testar a Tool de imóveis
python tests/test_imoveis_tool.py
Testar a Tool de notícias
python tests/test_noticias_tool.py
Testar o Analista de Notícias
python tests/test_analista_noticias.py
Testar o Analista Financeiro
python tests/test_analista_financeiro.py
Testar o Redator
python tests/test_redator.py
Testar a Crew completa
python -m imobiliaria.main

---

## 📊 Exemplo

Entrada:

Rio de Janeiro

O sistema consulta os imóveis disponíveis e pode encontrar resultados como:

Apartamento
2 quartos
4 banheiros
90 m²
R$ 675.138

e:

Cobertura
1 quarto
4 banheiros
59 m²
R$ 1.927.052

Esses dados são posteriormente analisados pelos agentes e consolidados pelo Redator.

---

## 🧠 Próximas Evoluções

O projeto foi estruturado pensando em futuras evoluções de Engenharia de IA.

🔹 RAG

Adicionar uma base de conhecimento própria contendo:

PDFs
Documentos
Regulamentos
Informações de financiamento
Dados históricos
Informações imobiliárias

🔹 Memória

Adicionar mecanismos para manter informações relevantes durante as interações com o cliente.

🔹 Validação

Implementar mecanismos para:

Validar respostas
Reduzir alucinações
Verificar consistência dos dados
Validar informações antes da resposta final

🔹 Testes Automatizados

Expandir a cobertura de testes para garantir maior confiabilidade e estabilidade do sistema.

---

## 🎯 Objetivo

Este projeto faz parte da construção de um portfólio voltado para Engenharia de IA, demonstrando conhecimentos práticos em:

Sistemas Multiagentes
CrewAI
Python
LLMs
Tool Calling
Orquestração de agentes
Contexto entre Tasks
Engenharia de Prompt
Integração com APIs
Arquitetura modular
Testes

👩‍💻 Ana Carulina Menezes

Desenvolvedora em formação com foco em Engenharia de IA, sistemas multiagentes e aplicações com LLMs.
