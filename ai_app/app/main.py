from fastapi import FastAPI

from app.controllers.allergen_controller import identify_potential_allergens
from app.controllers.recipe_controller import generate_recipe

app = FastAPI()


app.post('/allergens/identify', response_model=list)(identify_potential_allergens)
app.post('/recipes/generate', response_model=dict)(generate_recipe)