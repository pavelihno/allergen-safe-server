import requests

from flask import current_app

def get_ai_response(endpoint, json):
    response = requests.post(f'{current_app.config['AI_URL']}/{endpoint}', json=json)

    response.raise_for_status()

    return response.json()