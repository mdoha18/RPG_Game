from .npc import NPC
from pydantic import Field
from .jsonserializable import JsonSerializable
from .error_handler import Scanner as input_handler
import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .player import Player


class Shopkeeper(NPC, JsonSerializable):
    """
    Shopkeeper class that inherits from ABC NPC.
    This class will create an NPC that has some items
    for sale, which the player can buy once interacting.
    """

    npc_type: str = Field(default="Shopkeeper")
    goods: list[dict] = Field(default=[
            {"name": "Sword", "description": "+10 damage",
             "price": (10, 20), "damage": 10},
            {"name": "Healing Potion", "description": "fully heals you",
             "price": (30, 40)},
            {"name": "Shield", "description": "+25 health",
             "price": (100, 200), "armor": 25},
            {"name": "Armor", "description": "+50 health",
             "price": (200, 300), "armor": 50},
            {"name": "Upgraded Battle Axe", "description": "+50 damage",
             "price": (300, 400), "damage": 50}
    ])

    def interact(self, player: 'Player') -> None:
        print(f"You interact with the {self.inspect()}")
        print("Do you want to browse their goods?")
        print("  (0) Yes")
        print("  (1) No")
        shop_input = input_handler.read_int(input())
        match shop_input:
            case 0:
                self.open_shop(player)
            case 1:
                return
            case _:
                print("Please enter a valid input!")

    def open_shop(self, player: 'Player') -> None:
        """
        This method calls worker function
        that handle the shop interaction
        between the shopkeeper and the player.

        Arguments:
            player: player who engaged
                    with the shop.
        """
        self.shop_handler(player)

    def add_random_items(self, amount_of_items: int = 2) -> None:
        """
        Method adds a random amount of items to
        the shopkeeper's for sale items.

        Arguments:
            amount_of_items: int representing the
                             amount of items to add
        """
        additional_items = [
            {"name": "Orb of Stength", "description": "adds 20% damage",
             "price": [400, 600], "multiplier": 1.20},
            {"name": "Orb of Fortitude", "description": "adds 20% health",
             "price": [400, 600], "multiplier": 1.20},
            {"name": "Experience Potion",
             "description": "grants 1000 experience",
             "price": [600, 1000]},
            {"name": "Medicine", "description": "heals 1/4 of maximum health",
             "price": [10, 20]},
            {"name": "Sharpened Dagger", "description": "+20 damage",
             "price": [100, 200], "damage": 20}
        ]

        for _ in range(amount_of_items):
            item = random.choice(additional_items)
            self.goods.append(item)

        for item in self.goods:
            item['price'] = random.randint(*item['price'])

        self.goods.sort(key=lambda x: x['price'])

    def shop_handler(self, player: 'Player') -> None:
        """
        Method that handles the shop interaction.

        Arguments:
            player: player who engaged
                    with the shop.
        """
        print("You browse the shop's catalogue. You see:")
        if not self.goods:
            print("No items for sale.")
            return

        for index, item in enumerate(self.goods):
            print(f"  ({index}) {item['name']}: {item['description']}"
                  f" -- {item['price']} gold")

        print("Enter the number of the item you want to buy (-1: leave)")
        item_choice = input_handler.read_int(input())
        if item_choice == -1:
            print("You leave the shop.")
            return
        if item_choice > (len(self.goods) - 1):
            print("Invalid input! Try again.")
            self.shop_handler(player)
            return

        item = self.goods[item_choice]
        if player.gold >= item['price']:
            player.gold -= item['price']
            player.purchase_item(item)
            self.goods.remove(item)
            print(f"You bought a {str(item['name']).lower()} "
                  f"for {item['price']} gold.")
        else:
            print("You don't have enough gold to buy this item. "
                  f"You currently have {player.gold} gold.")
