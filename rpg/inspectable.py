from abc import ABC, abstractmethod
from pydantic import BaseModel, Field


class Inspectable(ABC, BaseModel):
    description: str = Field(default="")

    @abstractmethod
    def inspect(self):
        pass
