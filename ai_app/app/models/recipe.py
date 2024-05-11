from typing import List

from app.models._base import Base
from app.models.allergen import ExistingAllergen

class RecipeRequestBody(Base):
    cuisine: str
    description: str
    allergens: List[ExistingAllergen]

class RecipeResponseBody(Base):
    name: str
    ingredients: str
    description: str