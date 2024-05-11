from flask import request, jsonify

from app.models.profile import Profile
from app.models.cuisine import Cuisine
from app.models.recipe import Recipe
from app.middlewares.auth_middleware import login_required
from app.utils.ai_service import get_ai_response

@login_required
def generate_recipe(current_user, profile_id):
    body = request.json
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        cuisine_id = body.get('cuisine_id')
        cuisine = Cuisine.get_by_id(cuisine_id)
        if cuisine:
            ai_response = get_ai_response(
                'recipes/generate',
                json={
                    'cuisine': cuisine.name,
                    'description': body.get('description', ''),
                    'allergens': [allergen.to_dict(for_ai=True) for allergen in profile.allergens]
                }
            )
            new_recipe = Recipe.create(
                name=ai_response['name'],
                ingredients=ai_response['ingredients'],
                description=ai_response['description'],
                cuisine_id=cuisine_id,
                profile_id=profile_id
            )
            if new_recipe:
                return jsonify(new_recipe.to_dict()), 201
    return jsonify({'message': 'Failed to generate recipe'}), 400

@login_required
def get_recipes(current_user, profile_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        recipes = profile.recipes
        return jsonify([recipe.to_dict() for recipe in recipes])
    return jsonify({'message': 'Failed to get recipes'}), 400

@login_required
def get_recipe(current_user, profile_id, recipe_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        recipe = Recipe.get_by_id(recipe_id)
        if recipe:
            return jsonify(recipe.to_dict())
    return jsonify({'message': 'Recipe not found'}), 404

@login_required
def delete_recipe(current_user, profile_id, recipe_id):
    profile = Profile.get_by_id(profile_id)
    if profile and profile.user_id == current_user.id:
        deleted_recipe = Recipe.delete(recipe_id)
        if deleted_recipe:
            return jsonify(deleted_recipe.to_dict())
    return jsonify({'message': 'Recipe not found'}), 404