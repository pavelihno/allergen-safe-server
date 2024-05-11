from typing import List

from ._base import Base

class PotentialAllergen(Base):
    id: int
    name: str
    weight: float

class ExistingAllergen(Base):
    id: int
    allergen_name: str
    allergen_weight: float
    nFASS: float
    probability: float

class Reaction(Base):
    dish_name: str
    dish_description: str
    reaction: str
    reaction_weight: float
    reaction_strength: int

class NewAllergen(Base):
    nFASS: float
    probability: float
    allergen_type_id: int

class UpdatedAllergen(Base):
    id: int
    nFASS: float = None
    probability: float = None

class AllergenRequestBody(Base):
    potential_allergens: List[PotentialAllergen]
    identified_allergens: List[ExistingAllergen]
    reactions: List[Reaction]

class AllergenResponseBody(Base):
    identified_allergens: List[NewAllergen]
    updated_allergens: List[UpdatedAllergen]