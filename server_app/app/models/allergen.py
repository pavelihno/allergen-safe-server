from database import db
from models._base import BaseModel
from models.allergen_type import AllergenType

class Allergen(BaseModel):
    __tablename__ = 'allergens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nFASS = db.Column(db.Float, nullable=False)
    probability = db.Column(db.Float, nullable=False)

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    allergen_type_id = db.Column(db.Integer, db.ForeignKey('allergen_types.id'), nullable=False)

    def to_dict(self, for_ai=False):
        allergen_type = AllergenType.query.get(self.allergen_type_id)
        if for_ai:
            return {
                'id': self.id,
                'allergen_name': allergen_type.name,
                'allergen_weight': allergen_type.weight,
                'nFASS': self.nFASS,
                'probability': self.probability
            }
        return {
            'id': self.id,
            'nFASS': self.nFASS,
            'probability': self.probability,
            'profile_id': self.profile_id,
            'allergen_type': allergen_type.to_dict()
        }

    @classmethod
    def get_by_profile_id(cls, _profile_id):
        return cls.query.filter_by(profile_id=_profile_id).all()