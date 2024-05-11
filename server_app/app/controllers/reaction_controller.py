from flask import request, jsonify

from models.reaction import Reaction
from models.profile import Profile
from middlewares.auth_middleware import login_required
from controllers.allergen_controller import identify_potential_allergens

@login_required
def create_reaction(current_user, profile_id):
    body = request.json
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        new_reaction = Reaction.create(**body)
        if new_reaction:
            identify_potential_allergens(profile, new_reaction)
            return jsonify(new_reaction.to_dict()), 201
    return jsonify({'message': 'Failed to create reaction'}), 400

@login_required
def get_reactions(current_user, profile_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        reactions = Reaction.get_by_profile_id(profile_id)
        return jsonify([reaction.to_dict() for reaction in reactions])
    return jsonify({'message': 'Failed to get reactions'}), 400

@login_required
def get_reaction(current_user, profile_id, reaction_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        reaction = Reaction.get_by_id(reaction_id)
        if reaction:
            return jsonify(reaction.to_dict())
    return jsonify({'message': 'Reaction not found'}), 404

@login_required
def update_reaction(current_user, profile_id, reaction_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        body = request.json
        updated_reaction = Reaction.update(reaction_id, **body)
        if updated_reaction:
            identify_potential_allergens(profile, updated_reaction)
            return jsonify(updated_reaction.to_dict())
    return jsonify({'message': 'Reaction not found'}), 404

@login_required
def delete_reaction(current_user, profile_id, reaction_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        deleted_reaction = Reaction.delete(reaction_id)
        if deleted_reaction:
            identify_potential_allergens(profile, deleted_reaction)
            return jsonify(deleted_reaction.to_dict())
    return jsonify({'message': 'Reaction not found'}), 404