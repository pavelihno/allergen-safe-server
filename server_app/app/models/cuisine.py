from app.database import db
from app.models._base import BaseModel

class Cuisine(BaseModel):
    __tablename__ = 'cuisines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }