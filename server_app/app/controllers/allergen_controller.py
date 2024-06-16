from flask import jsonify, request

from app.models.profile import Profile
from app.models.allergen import Allergen
from app.middlewares.auth_middleware import login_required

@login_required
def create_allergens(current_user, profile_id):
    body = request.json
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        allergens = body.get('allergens')
        if allergens:
            new_allergens = []
            for allergen in allergens:
                new_allergen = Allergen.create(**allergen, profile_id=profile_id)
                if new_allergen:
                    new_allergens.append(new_allergen)
            return jsonify([allergen.to_dict() for allergen in new_allergens])
    return jsonify({'message': 'Failed to create allergens'}), 400

@login_required
def update_allergens(current_user, profile_id):
    body = request.json
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        allergens = body.get('allergens')
        if allergens:
            updated_allergens = []
            for allergen in allergens:
                updated_allergen = Allergen.update(allergen.get('id'), **allergen)
                if updated_allergen:
                    updated_allergens.append(updated_allergen)
            return jsonify([allergen.to_dict() for allergen in updated_allergens])
    return jsonify({'message': 'Failed to update allergens'}), 400

@login_required
def get_allergens(current_user, profile_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        allergens = profile.allergens
        return jsonify([allergen.to_dict() for allergen in allergens])
    return jsonify({'message': 'Failed to get allergens'}), 400

@login_required
def get_allergen(current_user, profile_id, allergen_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        allergen = Allergen.get_by_id(allergen_id)
        if allergen:
            return jsonify(allergen.to_dict())
    return jsonify({'message': 'Allergen not found'}), 404

@login_required
def delete_allergen(current_user, profile_id, allergen_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        deleted_allergen = Allergen.delete(allergen_id)
        if deleted_allergen:
            return jsonify(deleted_allergen.to_dict())
    return jsonify({'message': 'Allergen not found'}), 404