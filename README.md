# 📌 Projeto Teste Técnico – Consumo de API JSONPlaceholder

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white">
<img src="https://img.shields.io/badge/Requests-005C84?style=for-the-badge&logo=python&logoColor=white">

---

## 📖 Descrição
Este projeto foi desenvolvido como parte de um **teste técnico**.  
Ele consome a API pública **JSONPlaceholder** para:

- ✅ Obter a lista de usuários.
- ✅ Obter a lista de tarefas (todos).
- ✅ Processar os dados e gerar um relatório de tarefas concluídas e pendentes por usuário.
- ✅ Enviar o relatório processado para a API (endpoint de posts).

---

## ⚙️ Funcionalidades

- 🔗 Integração com API via `requests`.
- 📊 Processamento de dados relacionando usuários e suas tarefas.
- 📝 Geração de relatório com total de tarefas concluídas e pendentes.
- 📤 Envio do relatório para a API no formato JSON.
- 🛑 Tratamento de erros em todas as chamadas à API.

---

## 🔗 Links Úteis

[![JSONPlaceholder](https://img.shields.io/badge/JSONPlaceholder-FF6F61?style=for-the-badge&logo=postman&logoColor=white)](https://jsonplaceholder.typicode.com/)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

[![Requests](https://img.shields.io/badge/Requests-005C84?style=for-the-badge&logo=python&logoColor=white)](https://docs.python-requests.org/en/latest/)

---

## 📂 Estrutura do Projeto

```text
.
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
└── venv/                # Ambiente virtual (ignorado pelo git)


🚀 Tecnologias Utilizadas
Python 3.13
Requests – consumo de APIs HTTP
JSON – manipulação e envio de dados
VS Code – desenvolvimento

📦 Instalação e Execução
Clone o repositório
git clone https://github.com/BarbaraGuimaraes21/teste_tecnico.git
cd teste_tecnico

Crie e ative um ambiente virtual
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate

Instale as dependências
pip install -r requirements.txt

Execute o projeto
python main.py


📊 Exemplo de Saída
Dados de usuários e tarefas obtidos com sucesso!
Relatório de tarefas criado com sucesso!
Relatório enviado com sucesso!
Resposta da API: [{'user_id': 1, 'title': 'Leanne Graham tasks', 'body': 'completed_tasks: 11, pending_...}]
