from database import db


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredients = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey('cuisines.id'), nullable=False)