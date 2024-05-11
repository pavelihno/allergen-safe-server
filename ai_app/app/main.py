from fastapi import FastAPI

from .controllers.allergen_controller import *
from .controllers.recipe_controller import *

app = FastAPI()


app.post('/allergens/identify', response_model=list)(identify_potential_allergens)
app.post('/recipes/generate', response_model=dict)(generate_recipe)