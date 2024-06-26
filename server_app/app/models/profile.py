from app.database import db
from app.models._base import BaseModel
from app.models.allergen import Allergen
from app.models.reaction import Reaction
from app.models.recipe import Recipe


class Profile(BaseModel):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    allergens = db.relationship('Allergen', backref=db.backref('profiles', lazy='select'))
    reactions = db.relationship('Reaction', backref=db.backref('profiles', lazy='select'))
    recipes = db.relationship('Recipe', backref=db.backref('profiles', lazy='select'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }

    @classmethod
    def get_by_user_id(cls, _user_id):
        return cls.query.filter_by(user_id=_user_id).all()