from google.oauth2 import id_token
from google.auth.transport import requests

from flask import current_app

def get_google_user_data(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), current_app.config['GOOGLE_CLIENT_ID'])
        return {
            'email': idinfo['email'],
            'name': idinfo['given_name'],
        }
    except ValueError:
        return {}