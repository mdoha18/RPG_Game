from pydantic import BaseModel
from .custom_encoder import DictEncoder
import json


class JsonSerializable(BaseModel):
    def toJSON(self) -> str:
        try:
            return self.model_dump()
        except TypeError:
            return json.dumps(self.model_dump(), cls=DictEncoder)

    @classmethod
    def fromJSON(cls, data: str) -> 'JsonSerializable':
        return cls.model_validate(data)
