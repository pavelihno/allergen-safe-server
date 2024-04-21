from flask import request, jsonify

from models.user import User
from utils.jwt import signJWT
from utils.google_auth import get_google_user_data
from middlewares.auth_middleware import login_required

def register():
    body = request.json

    new_user = User.create(**{
        'email': body.get('email', ''),
        'password': body.get('password', ''),
        'role': 'standard',
        'is_active': True
    })
    if new_user:
        return jsonify(new_user.to_dict()), 201
    return jsonify({'message': 'Invalid email or password'}), 400

def login():
    body = request.json
    email = body.get('email', '')
    password = body.get('password', '')

    user = User.login(email, password)
    if user:
        token = signJWT(email)
        return jsonify(token), 200
    return jsonify({'message': 'Invalid email or password'}), 401

def login_google():
    body = request.json
    token = body.get('token', '')
    email = body.get('email', '')

    user_data = get_google_user_data(token)
    if not user_data:
        return jsonify({'message': 'Invalid Google credentials'}), 401

    user = User.get_by_email(email)
    if user:
        token = signJWT(email)
        return jsonify(token), 200
    else:
        new_user = User.create(**{
            'email': email,
            'role': 'standard',
            'is_active': True
        })
        if new_user:
            token = signJWT(email)
            return jsonify(token), 200
        return jsonify({'message': 'Failed to create user'}), 500


@login_required
def auth(current_user):
    return jsonify(current_user.to_dict()), 200