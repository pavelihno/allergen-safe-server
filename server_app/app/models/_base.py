from app.database import db

class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def create(cls, **data):
        model = cls()
        for key, value in data.items():
            setattr(model, key, value)
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def update(cls, _id, **data):
        model = cls.get_by_id(_id)
        if model:
            for key, value in data.items():
                if value:
                    setattr(model, key, value)
            db.session.commit()
            return model
        return None

    @classmethod
    def delete(cls, _id):
        model = cls.get_by_id(_id)
        if model:
            db.session.delete(model)
            db.session.commit()
            return model
        return None