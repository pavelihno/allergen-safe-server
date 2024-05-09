from database import db

class Allergen(db.Model):
    __tablename__ = 'allergens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nFASS = db.Column(db.Float, nullable=False)
    probability = db.Column(db.Float, nullable=False)

    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    allergen_type_id = db.Column(db.Integer, db.ForeignKey('allergen_types.id'), nullable=False)