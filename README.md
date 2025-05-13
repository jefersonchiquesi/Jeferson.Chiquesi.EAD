📄 README.md – Projeto E-Shop Brasil
🧑 Autor: Jeferson Aparecido Chiquesi junior
📁 Diretório: /workspaces/Jeferson.Chiquesi.EAD/e-shop-brasil
🧾 Descrição do Projeto
O E-Shop Brasil é uma aplicação de exemplo construída com foco em Backend Web, utilizando Python, MongoDB, Docker e Streamlit. O objetivo é praticar operações CRUD, simular um ambiente de ecommerce e consolidar habilidades com banco de dados, containers e APIs em Python.

✅ Funcionalidades Implementadas
Conexão com o MongoDB local via Docker

Inserção em massa de dados fake com a biblioteca Faker

Estrutura de diretórios organizada

Criação de ambiente virtual Python

Instalação de bibliotecas com requirements.txt

Testes de importação e execução de scripts como db.py, insert_data.py, etc.

🛠️ Tecnologias e Bibliotecas Usadas
Ferramenta	Versão / Observação
Python	3.12
MongoDB	Via Docker (localhost:27017)
Docker + Compose	Containers isolados
Faker	Para gerar dados falsos
Streamlit	Interface simples para testes
PyMongo	Conexão Python ↔ MongoDB
BSON	Suporte a serialização Mongo

📦 Arquivo requirements.txt
txt
Copiar
Editar
pymongo
streamlit
faker
bson
⚙️ Etapas Realizadas
✅ Criado diretório e-shop-brasil no projeto

✅ Configurado ambiente virtual com venv e ativado corretamente

✅ Instaladas bibliotecas necessárias

✅ Corrigido erro de ModuleNotFoundError com pymongo, faker, bson e streamlit

✅ Criado e preenchido o requirements.txt

✅ Testado acesso ao MongoDB local via Docker

✅ Tentativa de execução de insert_data.py com containers

✅ Corrigido erro de ambiente .conda inexistente

✅ Planejamento e metas definidos para organização e automação do projeto

🚧 Problemas Corrigidos
❌ Erros de "No such file or directory" ao chamar Python de ambientes inexistentes

❌ Ambiente .conda incorreto foi substituído por venv

❌ requirements.txt não existente — foi criado corretamente

❌ Falha de conexão com MongoDB — Docker ajustado para uso local

❌ Imports quebrados — resolvidos com pip install

📂 Estrutura de Diretórios
Copiar
Editar
e-shop-brasil/
│
├── db.py
├── insert_data.py
├── pythonteste.py
├── requirements.txt
└── README.md
📌 Próximos Passos
 Adicionar suporte a Streamlit para visualização dos dados

 Automatizar container MongoDB com docker-compose.yml

 Criar rotas REST com Flask ou FastAPI (se desejado)

 Adicionar testes unitários para as funções CRUD

 Publicar documentação no GitHub