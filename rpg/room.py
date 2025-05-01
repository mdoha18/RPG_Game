from .jsonserializable import JsonSerializable
from .inspectable import Inspectable
from pydantic import Field
from .door import Door
from .enemy import Enemy
from .shopkeeper import Shopkeeper


class Room(Inspectable, JsonSerializable):
    description: str = Field(default="A dark room")
    room_level: int = Field(default=0)
    doors: list[Door] = Field(default=[])
    NPCs: list[Enemy | Shopkeeper] = Field(default=[])

    def inspect(self):
        door_text = "door" if len(self.doors) == 1 else "doors"
        print(
            f"You see: {self.description}. "
            f"The room has {len(self.doors)} {door_text}. "
            f"A sign in the room reads that this is floor {self.room_level}."
        )

    def add_door(self) -> Door:
        new_door = Door()
        self.doors.append(new_door)
        return new_door
