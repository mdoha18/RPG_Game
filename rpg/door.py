from typing import TYPE_CHECKING, Union
from pydantic import Field
from .inspectable import Inspectable
from .interactable import Interactable
from .jsonserializable import JsonSerializable

if TYPE_CHECKING:
    from .room import Room


class Door(Inspectable, Interactable, JsonSerializable):
    description: str = Field(default="A pink door")
    connected_room: Union['Room', None] = Field(default=None)

    def inspect(self):
        pass

    def interact(self, player):
        if self.connected_room:
            player.current_room = self.connected_room
        else:
            print("Cannot proceed! There is no connected room.")
