import json
import requests


def getMetaplayer(): # get totalpages from searching players
    response_API = requests.get('https://www.balldontlie.io/api/v1/players?per_page=100&page=1')
    python_data = json.loads(response_API.text)
    all_data = python_data['meta']
    total_pages = all_data.get('total_pages')
    return total_pages

def responseTeam(): #get from api all teams data
    response_API = requests.get('https://www.balldontlie.io/api/v1/teams')
    python_data = json.loads(response_API.text)
    all_data = python_data['data']
    return all_data

def responsePlayer(name): # get data from api from current searching player
    for page in range(1, getMetaplayer()):
        response_API = requests.get(
            'https://www.balldontlie.io/api/v1/players?per_page=100&page={}'.format(page) + '&search={}'.format(name))
        python_data = json.loads(response_API.text)
        all_data = python_data['data']
        return all_data
