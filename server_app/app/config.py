import os

class Config:

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get('SERVER_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CSRF_ENABLED = True
