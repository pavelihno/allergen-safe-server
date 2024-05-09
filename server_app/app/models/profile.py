from database import db
from models.allergen import Allergen
from models.reaction import Reaction
from models.recipe import Recipe


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    allergens = db.relationship('Allergen', backref=db.backref('profiles', lazy='select'))
    reactions = db.relationship('Reaction', backref=db.backref('profiles', lazy='select'))
    recipes = db.relationship('Recipe', backref=db.backref('profiles', lazy='select'))