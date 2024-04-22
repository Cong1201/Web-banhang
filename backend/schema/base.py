from pydantic import BaseModel
from typing import Any
from peewee import ModelSelect

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True

class PeeweeGetterDict:
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res
