from database import db

class ReactionType(db.Model):
    __tablename__ = 'reaction_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    image = db.Column(db.LargeBinary)