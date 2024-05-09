from database import db

class Reaction(db.Model):
    __tablename__ = 'reactions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    dish_name = db.Column(db.String(50), nullable=False)
    dish_description = db.Column(db.Text)
    reaction_strength = db.Column(db.Integer, nullable=False)

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    reaction_type_id = db.Column(db.Integer, db.ForeignKey('reaction_types.id'), nullable=False)