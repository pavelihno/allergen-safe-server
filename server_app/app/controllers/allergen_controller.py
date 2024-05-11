from flask import jsonify

from app.models.profile import Profile
from app.models.allergen import Allergen
from app.models.reaction import Reaction
from app.models.allergen_type import AllergenType
from app.middlewares.auth_middleware import login_required
from app.utils.ai_service import get_ai_response

def identify_potential_allergens(profile_id, reaction_id):
    profile = Profile.get_by_id(profile_id)
    reaction = Reaction.get_by_id(reaction_id)

    ai_response = get_ai_response(
        'allergens/identify',
        json={
            'potential_allergens': [allergen_type.to_dict() for allergen_type in AllergenType.get_all()],
            'identified_allergens': [allergen.to_dict(for_ai=True) for allergen in profile.allergens],
            'reactions': [reaction.to_dict(for_ai=True) for reaction in profile.reactions]
        }
    )

    identified_allergens = ai_response.get('identified_allergens', [])
    updated_allergens = ai_response.get('updated_allergens', [])

    for identified_allergen in identified_allergens:
        new_allergen = Allergen.create(**identified_allergen, profile_id=profile.id)

    for updated_allergen in updated_allergens:
        allergen = Allergen.update(updated_allergen.get('id'), **updated_allergen)

    return True

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