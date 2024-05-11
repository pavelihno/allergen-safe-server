from pydantic import BaseModel

class Base(BaseModel):
    @classmethod
    def get_annotations(cls):
        annotations = {}
        for name, type_ in cls.__annotations__.items():
            annotations[name] = type_.__name__
        return annotations