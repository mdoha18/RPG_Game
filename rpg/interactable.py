from pydantic import BaseModel
from abc import ABC, abstractmethod


class Interactable(ABC, BaseModel):
    """Abstract base for player interation"""

    @abstractmethod
    def interact(self, player):
        pass
