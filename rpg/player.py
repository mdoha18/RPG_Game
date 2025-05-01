from pydantic import Field
from .jsonserializable import JsonSerializable
from .room import Room


class Player(JsonSerializable):
    name: str = Field(default="No Name")
    max_health: int = Field(default=20)
    health: int = Field(default=20)
    damage: int = Field(default=4)
    experience: int = Field(ge=0, default=0)
    level: int = Field(ge=0, default=1)
    next_level_exp: int = Field(ge=0, default=100)
    gold: int = Field(ge=0, default=0)
    inventory: list[dict] = Field(default=[
        {"index": "weapon", "weapon": "Fists", "damage": 0, "mult": 1},
        {"index": "armor", "armor": "Clothes", "value": 0, "mult": 1}
    ])
    current_room: 'Room' = Field(default=None)

    def player_stats(self) -> tuple[int, int]:
        """
        Player method that calculates the
        player's damage and health based on its
        raw attributes, items and multipliers.

        Return:
            tuple[int]: two intergers representing
                        the damage and health
        """
        player_damage = self.damage
        player_health = self.health

        for inventory_item in self.inventory:
            if inventory_item['index'] == 'weapon':
                player_damage = int((self.damage + inventory_item['damage']) * inventory_item['mult'])
            elif inventory_item['index'] == 'armor':
                player_health = int((self.max_health + inventory_item['value']) * inventory_item['mult'])

        return player_damage, player_health
    
    def damage_taken(self, amount):
        if amount >= self.health:
            self.health = 0
        else:
            self.health -= amount
        print(f"You have been attacked, you have {self.health} health left.")

    def gain_gold(self, gold_amount: int):
        print(f"Gained {gold_amount} gold!")
        self.gold += gold_amount

    def gain_experience(self, exp_amount: int):
        print(f"Gained {exp_amount} experience", end="")
        self.experience += exp_amount
        if self.experience >= self.next_level_exp:
            print(" and leveled up", end="")
            self.level_up()
        print("!")
        self.show_experience_bar()

    def level_up(self):
        self.level += 1
        self.damage += 2
        self.experience -= self.next_level_exp
        self.next_level_exp = int(self.next_level_exp * 1.3)
        #  Make sure that the player will level up multiple times if the
        #  gained experience is higher than two experience levels.
        if self.experience >= self.next_level_exp:
            self.level_up()

    def show_experience_bar(self):
        progress = int(20 * (self.experience / self.next_level_exp))
        bar = "[" + "#" * progress + "-" * (20 - progress) + "]"
        print(f"Level: {self.level} | Progress: {bar} "
              f"{self.experience}/{self.next_level_exp}")

    def purchase_item(self, item: dict) -> None:
        item_name = item['name']
        match item_name:
            case ("Sword" | "Sharpened Dagger" | "Upgraded Battle Axe"):
                for inventory_item in self.inventory:
                    if inventory_item['index'] == 'weapon':
                        inventory_item['weapon'] = item_name
                        if item['damage'] > inventory_item['damage']:
                            inventory_item['damage'] = item['damage']
                    break
            case ("Healing Potion" | "Experience Potion" | "Medicine"):
                if item_name == "Healing Potion":
                    self.health = self.max_health
                    print(f"You currently have {self.health} health.")
                elif item_name == "Medicine":
                    self.health += (0.25 * self.max_health)
                    print(f"You currently have {self.health} health.")
                else:
                    self.gain_experience(1000)
            case ("Shield" | "Armor"):
                for inventory_item in self.inventory:
                    if inventory_item['index'] == 'armor':
                        inventory_item['armor'] = item_name
                        inventory_item['value'] += item['armor']
                        break
            case ("Orb of Strength"):
                for inventory_item in self.inventory:
                    if inventory_item['weapon']:
                        inventory_item['mult'] += 0.2
            case ("Orb of Fortitude"):
                for inventory_item in self.inventory:
                    if inventory_item['armor']:
                        inventory_item['mult'] += 0.2
