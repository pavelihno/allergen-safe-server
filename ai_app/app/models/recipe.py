from typing import List

from ._base import Base
from ..models.allergen import ExistingAllergen

class RecipeRequestBody(Base):
    cuisine: str
    description: str
    allergens: List[ExistingAllergen]

class RecipeResponseBody(Base):
    name: str
    ingredients: str
    description: str