from app.database import db
from app.models._base import BaseModel
from app.models.reaction_type import ReactionType

class Reaction(BaseModel):
    __tablename__ = 'reactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    dish_name = db.Column(db.String(50), nullable=False)
    dish_description = db.Column(db.Text)
    reaction_strength = db.Column(db.Integer, nullable=False)

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    reaction_type_id = db.Column(db.Integer, db.ForeignKey('reaction_types.id'), nullable=False)

    def to_dict(self, for_ai=False):
        reaction_type = ReactionType.query.get(self.reaction_type_id)
        if for_ai:
            return {
                'dish_name': self.dish_name,
                'dish_description': self.dish_description,
                'reaction': reaction_type.name,
                'reaction_weight': reaction_type.weight,
                'reaction_strength': self.reaction_strength
            }
        return {
            'id': self.id,
            'date': self.date,
            'dish_name': self.dish_name,
            'dish_description': self.dish_description,
            'reaction_strength': self.reaction_strength,
            'profile_id': self.profile_id,
            'reaction_type': reaction_type.to_dict()
        }

    @classmethod
    def get_by_profile_id(cls, _profile_id):
        return cls.query.filter_by(profile_id=_profile_id).all()