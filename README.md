<h1>Consultoria Imobiliária - Multiagente</h1>

<p align="center">
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#practices-adopted">Práticas adotadas</a> •
  <a href="#pre-requisites">Requisitos</a> •
  <a href="#how-to-Installing">Instalando o projeto</a> •
  <a href="#how-to-use">Como executar</a> •
  <a href="#future">Próximos passos</a>
</p>

Essa aplicação foi desenvolvida utilizando Python e CrewAI para criação de um sistema de consultoria imobiliária baseado em arquitetura multiagente.
O sistema utiliza agentes especializados para buscar imóveis, analisar o mercado imobiliário, pesquisar notícias, realizar análises financeiras e gerar uma resposta consolidada para o cliente.

<h2 id="tecnologias">🔌 Tecnologias </h2>

- [Python](https://www.python.org/)
- [CrewAI](https://www.crewai.com/)
- [Pandas](https://pandas.pydata.org/)
- [DDGS](https://pypi.org/project/ddgs/)
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

<h2 id="practices-adopted">📖 Práticas adotadas </h2>

- Arquitetura Multiagente
- Separação entre Agents, Tasks e Tools
- Orquestração de agentes com CrewAI
- Desenvolvimento modular
- Testes individuais dos componentes
- Integração de ferramentas externas

<h2 id="pre-requisites">💻 Requisitos</h2>

Para rodar esse projeto você precisa ter o Python instalado na sua máquina. Também é necessário possuir uma chave de API da OpenAI.

- Python 3.10+
- OpenAI API Key

<h2 id="how-to-Installing"> 🚀 Instalando o projeto</h2>

Primeiro você deve clonar o repositório:

```bash
# Clone o repositório
git clone https://github.com/anacmenezes/consultoria-imobiliaria.git
```
```bash
# Acesse o projeto
cd consultoria-imobiliaria
```
```bash
# Crie o ambiente virtual
python -m venv .venv
```
```
# Ative o ambiente virtual
.\.venv\Scripts\Activate.ps1
```
```
# Instale as dependências
pip install -r requirements.txt
```

<h2 id="how-to-use">💡 Como Executar</h2>

Com o ambiente virtual ativado, execute:
```
python -m imobiliaria.main
```

Para testar o fluxo completo:
```
python -m imobiliaria.main
```

<h2 id="future">🚀 Próximos passos</h2>

O projeto foi estruturado para receber novas funcionalidades de Engenharia de IA, como:

Implementação de RAG
Base de conhecimento própria
Memória para os agentes
Validação das respostas
Redução de alucinações
Observabilidade
Monitoramento de custos e tokens
Testes automatizados
Integração com bancos de dados
Melhorias na arquitetura multiagente

<h2 id="author">👩‍💻 Ana Carulina Menezes</h2>

Projeto desenvolvido como parte da construção de portfólio em Engenharia de IA, com foco em sistemas multiagentes, LLMs, automação e aplicações utilizando Python e CrewAI.
