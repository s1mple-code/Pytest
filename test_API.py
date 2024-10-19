import requests

endpoint = "https://todo.pixegami.io/"

#python -m pytest
#-m pytest -v -s
#pip install requests

def test_can_call_endpoint():
    response = requests.get(endpoint)
    assert response.status_code == 200

def test_can_create_task():
    payload = {
        "content": "my teste content",
        "user_id": "tst_user",
        "is_done": False
    }
    create_response = requests.put(endpoint + "/create-task",json = payload)
    assert create_response.status_code == 200

    data = create_response.json()
    print(data)

    # pega um componente de task
    task_id = data["task"]["task_id"]

    get_task_response = requests.get(endpoint + f"/get-task/{task_id}/")
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)

    # comparando a resposta da consulta com o q foi criado
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert  create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my teste content",
        "is_done": True
    }
    update_task_resp = requests.put(endpoint + "/update-task", json=new_payload)
    assert update_task_resp.status_code == 200

    get_task_data_resp = get_task(task_id)
    print(get_task_data_resp)
    assert  get_task_data_resp.status_code == 200

    get_task_data = get_task_data_resp.json()
    print(get_task_data)
    # comparando a resposta da consulta com o q foi atualizado
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]




def create_task(payload):
    return requests.put(endpoint + "/create-task",json=payload)

def get_task(task_id):
    return requests.get(endpoint + f"/get-task/{task_id}")

def new_task_payload():
    return{
        "content": "my teste content",
        "user_id": "tst_user",
        "is_done": False
    }