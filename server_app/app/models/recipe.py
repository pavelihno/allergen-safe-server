from database import db
from models._base import BaseModel
from models.cuisine import Cuisine

class Recipe(BaseModel):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.Text)
    description = db.Column(db.Text)

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisines.id'), nullable=False)

    def to_dict(self):
        cuisine = Cuisine.get_by_id(self.cuisine_id)
        return {
            'id': self.id,
            'ingredients': self.ingredients,
            'description': self.description,
            'profile_id': self.profile_id,
            'cuisine': cuisine.name
        }

    @classmethod
    def get_by_profile_id(cls, _profile_id):
        return cls.query.filter_by(profile_id=_profile_id).all()