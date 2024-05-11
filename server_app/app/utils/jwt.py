import os, jwt
from datetime import datetime, timedelta

SECRET_KEY = os.environ.get('SERVER_SECRET_KEY')

def signJWT(email, expiration_date=datetime.now() + timedelta(weeks=4)):
    token_data = {'email': email, 'exp': expiration_date}
    return jwt.encode(token_data, SECRET_KEY, algorithm='HS256')

def verifyJWT(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])