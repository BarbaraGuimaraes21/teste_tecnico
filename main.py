import requests
import json

def obter_dados_usuarios():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar usuários: {e}")
        return None
    pass

def obter_dados_todos():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar tarefas: {e}")
        return None
    pass

def processar_dados(users,todos):
    if not users or not todos:
        return None

    user_tasks = {}
    for user in users:
        user_tasks[user['id']] = {'completed': 0, 'pending': 0}

    for todo in todos:
        user_id = todo['userId']
        if user_id in user_tasks:
            if todo['completed']:
                user_tasks[user_id]['completed'] += 1
            else:
                user_tasks[user_id]['pending'] += 1

    report = []
    for user in users:
        tasks = user_tasks.get(user['id'],{'completed': 0, 'pending': 0})
        report.append({
            "user_id": user['id'],
            "title": f"{user['name']} tasks",
            "body": f"completed_tasks: {tasks['completed']}, pending_tasks:{tasks['pending']}"
        })
    return report

def enviar_relatorio(report):
    if not report:
        print("Relatório vazio, não será enviado.")
        return
    
    payload = json.dumps(report)
    headers = {'Content-type': 'application/json'}

    try:
        response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        data=payload,
        headers=headers
        )
        response.raise_for_status()
        print("Relatório enviado com sucesso!")
        print("Resposta da API:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar o relatório: {e}")

if __name__ == "__main__":
    users = obter_dados_usuarios()
    todos = obter_dados_todos()

    if users and todos:
        print("Dados de usuários e tarefas obtidos com sucesso!")
        final_report = processar_dados(users, todos)
        if final_report:
            print("Relatório de tarefas criado com sucesso!")
            enviar_relatorio(final_report)
    else:
        print("Falha ao obter dados.")