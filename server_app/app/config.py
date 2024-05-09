import os

class Config:
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    SECRET_KEY = os.environ.get('SERVER_SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('SERVER_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AI_URL = os.environ.get('SERVER_AI_URL')

    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')

    CSRF_ENABLED = True
