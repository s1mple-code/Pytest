import requests

url_base = 'https://api.github.com'


def consult_all_datas(user):

    consult_data = requests.get(url_base + "/users/" + user)
    return consult_data.json()

def consult_repo(user):

    params = {
    "type": "owner",  # 'all', 'owner', 'member'
    "page": 1,      # Página que deseja consultar
    "per_page": 1, # Quantidade de resultados por página
    "sort": "created"  # 'created', 'updated', 'pushed', 'full_name'
}

    consult_repo = requests.get(url_base + f"/repos/{user}/boysenberry-repo-1")
    return consult_repo.json()


def specific_datas():

    datas = consult_all_datas('octocat')
    repo = consult_repo('octocat')

    #print(repo)

    name = datas['name']
    name_repo = repo['name']
    number_repo = datas['public_repos']
    followers = datas['followers']
    following = datas['following']

    print('Nome do usuário: ' + name)
    print('Nome do usuário: ' + name_repo)
    print(f'Número de repositório: {number_repo}')
    print(f'Número de seguidores: {followers}')
    print(f'Seguindo: {following}')

    



specific_datas()

