from .npc import NPC
from pydantic import Field
from .jsonserializable import JsonSerializable
import random


class Enemy(NPC, JsonSerializable):
    """This is the Enemy class that extends NPC and JsonSerializable"""
    npc_type: str = Field(default="Enemy")
    health: int = Field(default=10)
    damage: int = Field(default=1)

    def interact(self, player):
        """
        This method begins the interaction with player.

        Arguments:
            player:  player obj that interacts with enemy.
        """
        print(f"{self.description} challanged you to a fight.")
        self.combat(player)

    def combat(self, player):
        """
        This method is responsible for the player's
        combat with enemy.Combatting will end if player or
        enemy's health reaches 0.

        Arguments:
            player:  player obj that choses to fight the enemy

        """
        while self.health > 0 and player.health > 0:
            print(f"You are fighting {self.description}.")
            print("What will you do?")
            print("  (0) Attack")
            print("  (1) Run away")
            action = input("Choose your action: ")

            if action == "0":
                self.damage_taken(player.damage)
                if self.health <= 0:
                    print(f"You defeated the {self.description}!")
                    player.current_room.NPCs.remove(self)
                    self.grant_experience(player)
                    self.grant_gold(player)
                    return

                player.damage_taken(self.damage)
                if player.health <= 0:
                    return

            elif action == "1":
                print("You ran away!")
                return
            else:
                print("Invalid action. Please choose 0 to attack or 1 to run.")

    def damage_taken(self, amount):
        """
        This method is responsible for reducing enemy's
        health by damage amount until it is defeated.

        Arguments:
            amount: amount of damage player imposes on enemy

        """
        if amount >= self.health:
            self.health = 0
        else:
            self.health -= amount
        print(f"The {self.description} took {amount} damage"
              f" and has {self.health} health left.")

    def scale(self, room_number: int):
        """
        This method scales the enemy object's health and
        damage based on the current room it is in.

        Arguments:
            room_number = the current room's number
        """
        self.health *= int(1.10 ** room_number)
        self.damage *= int(1.05 ** room_number)

    def grant_experience(self, player):
        """
        This method grants the player experience after the
        player defeats the enemy object

        Arguments:
            player: player object that should
                    receive the experience.
        """
        room_number = player.current_room.room_level
        experience_points = int(40 * ((1 + room_number) ** 0.2))
        player.gain_experience(experience_points)

    def grant_gold(self, player):
        """
        This method grants the player gold after the
        player defeats the enemy object.

        Arguments:
            player: player object that should
                    receive the experience.
        """
        room_number = player.current_room.room_level
        random_base_gold = random.randint(1, 15)
        rewarded_gold = int(random_base_gold * ((1 + room_number) ** 0.9))
        player.gain_gold(rewarded_gold)
