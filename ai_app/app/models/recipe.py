from typing import List

from app.models._base import Base

class Allergen(Base):
    allergen_name: str
    allergen_weight: float
    nFASS: float
    probability: float

class RecipeRequestBody(Base):
    cuisine: str
    description: str
    allergens: List[Allergen]

class RecipeResponseBody(Base):
    name: str
    ingredients: str
    description: str