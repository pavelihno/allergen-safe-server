from database import db

class AllergenType(db.Model):
    __tablename__ = 'allergen_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    image = db.Column(db.LargeBinary)