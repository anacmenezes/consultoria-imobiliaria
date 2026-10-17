<h1>Consultoria Imobiliária - Multiagente</h1>

<p align="center">
  <a href="#sobre-o-projeto">Sobre o projeto</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#practices-adopted">Práticas adotadas</a> •
  <a href="#pre-requisites">Requisitos</a> •
  <a href="#how-to-Installing">Instalando o projeto</a> •
  <a href="#deploy">Deploy</a>
</p>

<p align="center">
  <a href="https://github.com/anacmenezes/analise-mercado">
    <img src="https://img.shields.io/badge/GitHub-Projeto-black?logo=github" alt="GitHub">
  </a>
  <a href="https://analise-mercado-api.ashysky-801299e3.brazilsouth.azurecontainerapps.io/docs">
    <img src="https://img.shields.io/badge/API-Swagger-85EA2D?logo=swagger&logoColor=black" alt="Swagger">
  </a>
  <a href="https://c63274731f07410fb46542e75ca3018e.prod.enter.pro">
    <img src="https://img.shields.io/badge/Frontend-Live-4CAF50" alt="Frontend">
  </a>
</p>

<h2 id="sobre-o-projeto">📌 Sobre o projeto</h2>

<p>
Essa aplicação foi desenvolvida utilizando Python e CrewAI para criação de um sistema de consultoria imobiliária baseado em arquitetura multiagente. O sistema utiliza agentes especializados para buscar imóveis, analisar o mercado imobiliário, pesquisar notícias, realizar análises financeiras e gerar uma resposta consolidada para o cliente.

O projeto possui uma arquitetura completa envolvendo:
</p>

<ul>
  <li>Frontend web</li>
  <li>API REST</li>
  <li>Sistema multiagente</li>
  <li>RAG</li>
  <li>LLMs</li>
  <li>Busca de informações externas</li>
  <li>Banco de dados PostgreSQL</li>
  <li>Avaliação de agentes</li>
  <li>Observabilidade</li>
  <li>Docker</li>
  <li>Cloud computing</li>
  <li>Deploy em Azure</li>
</ul>

<h2 id="tecnologias">🔌 Tecnologias</h2>

<h3>Inteligência Artificial</h3>

<ul>
  <li><a href="https://www.python.org/">Python</a></li>
  <li><a href="https://www.crewai.com/">CrewAI</a></li>
  <li><a href="https://platform.openai.com/">OpenAI API</a></li>
  <li><a href="https://www.trychroma.com/">ChromaDB</a></li>
  <li>RAG (Retrieval-Augmented Generation)</li>
  <li>Engenharia de prompts</li>
  <li>Arquitetura multiagente</li>
</ul>

<h3>Backend</h3>

<ul>
  <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
  <li>Pydantic</li>
  <li>SQLAlchemy</li>
  <li>PostgreSQL</li>
  <li>REST API</li>
</ul>

<h3>Busca e dados</h3>

<ul>
  <li><a href="https://serper.dev/">Serper API</a></li>
  <li>ChromaDB</li>
  <li>Embeddings</li>
  <li>Base de conhecimento interna</li>
  <li>PostgreSQL</li>
</ul>

<h3>Infraestrutura</h3>

<ul>
  <li>Docker</li>
  <li>Azure Container Registry</li>
  <li>Azure Container Apps</li>
  <li>Azure Database for PostgreSQL</li>
  <li>Azure Managed Identity</li>
  <li>Azure CLI</li>
</ul>

<h3>Frontend</h3>

<ul>
  <li>React</li>
  <li>Lovable</li>
  <li>Integração via REST API</li>
</ul>

<h2 id="practices-adopted">📖 Práticas adotadas</h2>

<ul>
  <li>Arquitetura Multiagente</li>
  <li>Separação de responsabilidades</li>
  <li>Orquestração de agentes com CrewAI</li>
  <li>Engenharia de Prompt</li>
  <li>Desenvolvimento modular</li>
  <li>Execução sequencial de tarefas</li>
  <li>Utilização de LLMs</li>
  <li>Variáveis de ambiente para configuração</li>
  <li>RAG para consulta de conhecimento interno</li>
  <li>Busca de informações externas</li>
  <li>Avaliação da qualidade dos relatórios</li>
  <li>Observabilidade da execução</li>
  <li>Tratamento de erros</li>
  <li>Persistência de dados com PostgreSQL</li>
  <li>Containerização com Docker</li>
  <li>Deploy em cloud</li>
  <li>Configuração de CORS</li>
  <li>Uso de Managed Identity para acesso ao Azure Container Registry</li>
</ul>

<h2 id="pre-requisites">💻 Requisitos</h2>

<p>
Para executar esse projeto localmente é necessário possuir o Python instalado
na máquina.
</p>

<ul>
  <li>Python 3.10+</li>
  <li>OpenAI API Key</li>
  <li>Serper API Key</li>
  <li>PostgreSQL</li>
  <li>Docker (opcional)</li>
</ul>

<h2 id="how-to-Installing">🚀 Instalando o projeto</h2>

<p>
Primeiro, clone o repositório:
</p>

<pre>
<code>git clone https://github.com/anacmenezes/consultoria-imobiliaria.git</code>
</pre>

<p>
Acesse o projeto:
</p>

<pre>
<code>cd consultoria-imobiliaria</code>
</pre>

<p>
Crie o ambiente virtual:
</p>

<pre>
<code>python -m venv .venv</code>
</pre>

<p>
Ative o ambiente virtual no PowerShell:
</p>

<pre>
<code>.\.venv\Scripts\Activate.ps1</code>
</pre>

<p>
Instale as dependências:
</p>

<pre>
<code>pip install -r requirements.txt</code>
</pre>

<h2 id="database">🗄️ Persistência de dados</h2>

<p>
As análises geradas são persistidas utilizando
<strong>PostgreSQL</strong>.
</p>

<p>
A camada de persistência utiliza:
</p>

<ul>
  <li>PostgreSQL</li>
  <li>SQLAlchemy</li>
  <li>Pydantic</li>
  <li>Variáveis de ambiente</li>
</ul>

<p>
A separação entre a camada de IA, API e persistência permite manter uma
arquitetura modular e facilita futuras evoluções do sistema.
</p>

<h2 id="observability">🔎 Observabilidade</h2>

<p>
O projeto também possui mecanismos de observabilidade para acompanhar
a execução do fluxo multiagente.
</p>

<p>
São acompanhadas informações como:
</p>

<ul>
  <li>Execução das tarefas</li>
  <li>Resultado produzido por cada agente</li>
  <li>Status das avaliações</li>
  <li>Qualidade do relatório final</li>
  <li>Erros durante a execução</li>
</ul>

<h2 id="docker">🐳 Docker</h2>

<p>
A aplicação possui suporte a Docker para padronizar o ambiente de execução
e facilitar o processo de deploy.
</p>

<p>
Para construir a imagem:
</p>

<pre>
<code>docker build -t consultoria-imobiliaria .</code>
</pre>

<p>
Para executar localmente:
</p>

<pre>
<code>docker run -p 8000:8000 consultoria-imobiliaria</code>
</pre>

<h2 id="deploy">☁️ Deploy</h2>

<p>
O backend foi disponibilizado em produção utilizando serviços da
<strong>Microsoft Azure</strong>.
</p>

<h3>Serviços utilizados</h3>

<ul>
  <li><strong>Azure Container Apps:</strong> execução da aplicação containerizada</li>
  <li><strong>Azure Container Registry:</strong> armazenamento da imagem Docker</li>
  <li><strong>Azure Database for PostgreSQL:</strong> persistência dos dados</li>
  <li><strong>Azure Managed Identity:</strong> autenticação do Container App no Registry</li>
  <li><strong>Azure CLI:</strong> gerenciamento dos recursos</li>
</ul>

<p>
O backend possui uma URL pública e pode ser acessado por meio da documentação
interativa do FastAPI.
</p>

<p>
<strong>API:</strong><br>
<a href="https://consultoria-imobiliaria-api.ashysky-801299e3.brazilsouth.azurecontainerapps.io/docs">
https://consultoria-imobiliaria-api.ashysky-801299e3.brazilsouth.azurecontainerapps.io/docs
</a>
</p>

<p>
<strong>Swagger:</strong><br>
<a href="https://consultoria-imobiliaria-api.ashysky-801299e3.brazilsouth.azurecontainerapps.io/docs">
Documentação da API
</a>
</p>

<p>
A API permite requisições provenientes da origem do frontend publicado,
mantendo o controle sobre quais origens podem acessar os endpoints.
</p>

<h2 id="frontend">🖥️ Frontend</h2>

<p>
O projeto possui uma interface web para interação com a API.
</p>

<p>
O frontend permite:
</p>

<ul>
  <li>Informar o setor que deseja analisar</li>
  <li>Enviar a solicitação para a API</li>
  <li>Acompanhar o processamento</li>
  <li>Receber o relatório gerado</li>
  <li>Visualizar o relatório formatado em Markdown</li>
</ul>

<p>
A comunicação entre frontend e backend é realizada utilizando
<strong>HTTP/JSON</strong>.
</p>

<h2 id="security">🔐 Segurança</h2>

<p>
Informações sensíveis não são armazenadas diretamente no código-fonte.
</p>

<p>
As credenciais utilizadas pela aplicação são configuradas por meio de
variáveis de ambiente e secrets.
</p>

<ul>
  <li>OpenAI API Key</li>
  <li>Serper API Key</li>
  <li>Database URL</li>
</ul>

<p>
Em produção, os secrets são configurados no Azure Container Apps.
</p>

<p>
O acesso do Container App ao Azure Container Registry utiliza
<strong>Managed Identity</strong>, evitando a necessidade de armazenar
credenciais administrativas do Registry na aplicação.
</p>

<h2 id="author">👩‍💻 Ana Carulina Menezes</h2>

<p>
Projeto desenvolvido como parte da construção de portfólio em
<strong>Engenharia de IA</strong>, com foco em:
</p>

<ul>
  <li>Sistemas multiagentes</li>
  <li>LLMs</li>
  <li>RAG</li>
  <li>APIs</li>
  <li>Cloud</li>
  <li>Docker</li>
  <li>Python</li>
  <li>Automação</li>
  <li>Arquitetura de software</li>
</ul>