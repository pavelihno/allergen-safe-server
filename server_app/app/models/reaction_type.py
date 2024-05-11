from app.database import db
from app.models._base import BaseModel

class ReactionType(BaseModel):
    __tablename__ = 'reaction_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    image = db.Column(db.LargeBinary)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'weight': self.weight
        }