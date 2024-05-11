import os
import importlib
from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.database import db

from app.controllers.auth_controller import register, login, login_google, auth
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user, activate_user, deactivate_user, change_password
from app.controllers.profile_controller import create_profile, get_profiles, get_profile, update_profile, delete_profile
from app.controllers.reaction_controller import create_reaction, get_reactions, get_reaction, update_reaction, delete_reaction
from app.controllers.recipe_controller import generate_recipe, get_recipes, get_recipe, delete_recipe
from app.controllers.allergen_controller import get_allergens, get_allergen, delete_allergen

def __import_models():
   app_dir = 'app'
   models_dir = 'models'
   for dir_path, dir_names, file_names in os.walk('/'.join([app_dir, models_dir])):
      for file_name in [f for f in file_names if f.endswith('.py') and f != '__init__.py']:
         file_path_wo_ext, _ = os.path.splitext(os.path.join(dir_path, file_name))
         module_name = file_path_wo_ext.replace(os.sep, '.')
         importlib.import_module(module_name, package=None)

   return True

def __create_app(_config_class, _db):
   app = Flask(__name__)
   app.config.from_object(_config_class)

   # Required for tracking migrations
   __import_models()

   _db.init_app(app)

   return app

app = __create_app(Config, db)
migrate = Migrate(app, db)

# auth
app.route('/register', methods=['POST'])(register)
app.route('/login', methods=['POST'])(login)
app.route('/login-google', methods=['POST'])(login_google)
app.route('/auth', methods=['GET'])(auth)

# users
app.route('/users', methods=['GET'])(get_users)
app.route('/users', methods=['POST'])(create_user)
app.route('/users/<int:user_id>', methods=['GET'])(get_user)
app.route('/users/<int:user_id>', methods=['PUT'])(update_user)
app.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
app.route('/users/<int:user_id>/activate', methods=['PUT'])(activate_user)
app.route('/users/<int:user_id>/deactivate', methods=['PUT'])(deactivate_user)
app.route('/users/change-password', methods=['PUT'])(change_password)

# profiles
app.route('/profiles', methods=['GET'])(get_profiles)
app.route('/profiles', methods=['POST'])(create_profile)
app.route('/profiles/<int:profile_id>', methods=['GET'])(get_profile)
app.route('/profiles/<int:profile_id>', methods=['PUT'])(update_profile)
app.route('/profiles/<int:profile_id>', methods=['DELETE'])(delete_profile)

# reactions
app.route('/reactions/<int:profile_id>', methods=['POST'])(create_reaction)
app.route('/reactions/<int:profile_id>', methods=['GET'])(get_reactions)
app.route('/reactions/<int:profile_id>/<int:reaction_id>', methods=['GET'])(get_reaction)
app.route('/reactions/<int:profile_id>/<int:reaction_id>', methods=['PUT'])(update_reaction)
app.route('/reactions/<int:profile_id>/<int:reaction_id>', methods=['DELETE'])(delete_reaction)

# recipes
app.route('/recipes/<int:profile_id>', methods=['POST'])(generate_recipe)
app.route('/recipes/<int:profile_id>', methods=['GET'])(get_recipes)
app.route('/recipes/<int:profile_id>/<int:recipe_id>', methods=['GET'])(get_recipe)
app.route('/recipes/<int:profile_id>/<int:recipe_id>', methods=['DELETE'])(delete_recipe)

# allergens
app.route('/allergens/<int:profile_id>', methods=['GET'])(get_allergens)
app.route('/allergens/<int:profile_id>/<int:allergen_id>', methods=['GET'])(get_allergen)
app.route('/allergens/<int:profile_id>/<int:allergen_id>', methods=['DELETE'])(delete_allergen)