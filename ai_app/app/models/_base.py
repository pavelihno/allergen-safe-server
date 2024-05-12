from typing import List, get_args, get_origin
from pydantic import BaseModel

class JsonEncoder:
    def default(self, obj):
        if isinstance(obj, List):
            if obj and isinstance(obj[0], BaseModel):
                return [self.default(item) for item in obj]
            else:
                return obj
        else:
            return obj

class JsonEncoderCallable:
    def __init__(self):
        self.encoder = JsonEncoder()

    def __call__(self, obj):
        return self.encoder.default(obj)

class Base(BaseModel):
    class Config:
        json_encoders = {BaseModel: JsonEncoderCallable()}

    @classmethod
    def get_annotations(cls):
        annotations = {}
        for name, type_ in cls.__annotations__.items():
            if get_origin(type_) is None:
                # Not a generic type (e.g., str, int, float)
                annotations[name] = type_.__name__
            else:
                # A generic type (e.g., List[T])
                origin = get_origin(type_)
                args = get_args(type_)
                if origin == list:
                    # Handle List[T]
                    nested_type = args[0]
                    if issubclass(nested_type, BaseModel):
                        # Nested Pydantic model
                        annotations[name] = [nested_type.get_annotations()]
                    else:
                        # Not a nested Pydantic model (e.g., List[str])
                        annotations[name] = [nested_type.__name__]
                else:
                    # Other generic types (e.g., Dict[str, int])
                    annotations[name] = str(type_)
        return annotations