import requests

def obter_dados_usuarios():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar usuários: {e}")
        return None

def obter_dados_todos():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar tarefas: {e}")
        return None

if __name__ == "__main__":
    users = obter_dados_usuarios()
    todos = obter_dados_todos()

    if users and todos:
        print("Dados de usuários e tarefas obtidos com sucesso!")
    else:
        print("Falha ao obter dados.")