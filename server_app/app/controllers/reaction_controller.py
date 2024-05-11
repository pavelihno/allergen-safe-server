from flask import request, jsonify

from app.models.profile import Profile
from app.models.reaction import Reaction
from app.models.allergen_type import AllergenType
from app.middlewares.auth_middleware import login_required
from app.celery_app import identify_potential_allergens_task

def __create_identify_potential_allergens_task(current_user, profile):
    return identify_potential_allergens_task.delay(
        current_user.email, 
        profile.id, 
        {
            'potential_allergens': [allergen_type.to_dict() for allergen_type in AllergenType.get_all()],
            'identified_allergens': [allergen.to_dict(for_ai=True) for allergen in profile.allergens],
            'reactions': [reaction.to_dict(for_ai=True) for reaction in profile.reactions]
        }
    )

@login_required
def create_reaction(current_user, profile_id):
    body = request.json
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        new_reaction = Reaction.create(**body)
        if new_reaction:
            __create_identify_potential_allergens_task(current_user, profile)
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
            __create_identify_potential_allergens_task(current_user, profile)
            return jsonify(updated_reaction.to_dict())
    return jsonify({'message': 'Reaction not found'}), 404

@login_required
def delete_reaction(current_user, profile_id, reaction_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        deleted_reaction = Reaction.delete(reaction_id)
        if deleted_reaction:
            __create_identify_potential_allergens_task(current_user, profile)
            return jsonify(deleted_reaction.to_dict())
    return jsonify({'message': 'Reaction not found'}), 404