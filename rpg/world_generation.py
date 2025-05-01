from .room import Room
from .enemy import Enemy
from .shopkeeper import Shopkeeper
from random import randint


class Generation:
    def generate_shop(self, lvl=0) -> Room:
        """Creates a shop room with a NPC that sells items."""
        shopkeep = Shopkeeper(description="A nice looking fella")
        shopkeep.add_random_items(int(lvl/10 * 2))
        shop_description = "A nice looking store. It smells of flowers"
        shop = Room(description=shop_description,
                    room_level=lvl,
                    NPCs=[shopkeep])
        portal_door = shop.add_door()
        portal_door.description = "A big red, glowing portal"
        return shop

    def generate_room(self, lvl=0) -> Room:
        """Create a new room with a random (1-3) amount of doors."""
        if ((lvl) % 10) == 0 and lvl != 0:
            return self.generate_shop(lvl)

        new_room = Room(room_level=lvl)
        # to add enemies
        for _ in range(0, 3):
            new_enemy = Enemy(description=f"Enemy {_}")
            new_enemy.scale(new_room.room_level)
            new_room.NPCs.append(new_enemy)

        door_color_list = ["green", "shady", "pink", "red", "purple"]
        for _ in range(0, randint(1, 4)):
            door_color = door_color_list[randint(0, len(door_color_list) - 1)]
            door_color_list.remove(door_color)
            new_door = new_room.add_door()
            new_door.description = f"A {door_color} door"

        return new_room
