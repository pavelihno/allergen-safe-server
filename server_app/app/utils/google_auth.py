import os

from google.oauth2 import id_token
from google.auth.transport import requests

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')

def get_google_user_data(token):
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        return {
            'email': id_info['email'],
            'name': id_info['given_name'],
        }
    except ValueError:
        return {}