from pydantic import Field
from .inspectable import Inspectable
from .interactable import Interactable


class NPC(Inspectable, Interactable):
    description: str = Field(default="A little guy")

    def inspect(self):
        return self.description

    def interact(self, player):
        print("You poke it.")
