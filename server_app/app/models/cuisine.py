from database import db

class Cuisine(db.Model):
    __tablename__ = 'cuisines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)