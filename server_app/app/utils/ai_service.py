import os, requests

def get_ai_response(endpoint, json):
    response = requests.post(f'{os.environ.get('SERVER_AI_URL')}/{endpoint}', json=json)

    response.raise_for_status()

    return response.json()