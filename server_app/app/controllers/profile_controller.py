from flask import request, jsonify

from app.models.profile import Profile
from app.models.user import User
from app.middlewares.auth_middleware import login_required

@login_required
def create_profile(current_user):
    body = request.json
    if body.get('user_id') == current_user.id:
        new_profile = Profile.create(**body)
        if new_profile:
            return jsonify(new_profile.to_dict()), 201
    return jsonify({'message': 'Failed to create profile'}), 400

@login_required
def get_profiles(current_user):
    profiles = Profile.get_by_user_id(current_user.id)
    return jsonify([profile.to_dict() for profile in profiles])

@login_required
def get_profile(current_user, profile_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        return jsonify(profile.to_dict())
    return jsonify({'message': 'Profile not found'}), 404

@login_required
def update_profile(current_user, profile_id):
    body = request.json
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        updated_profile = Profile.update(profile_id, **body)
        if updated_profile:
            return jsonify(updated_profile.to_dict())
    return jsonify({'message': 'Profile not found'}), 404

@login_required
def delete_profile(current_user, profile_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        deleted_profile = Profile.delete(profile_id)
        if deleted_profile:
            return jsonify(deleted_profile.to_dict())
    return jsonify({'message': 'Profile not found'}), 404