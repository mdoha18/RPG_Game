from .error_handler import Scanner as input_handler
from .io_utils import Saver
from .player import Player
from pydantic import BaseModel, Field
from .world_generation import Generation


class Game(BaseModel):
    decisions: list[str] = Field(default=[
        "Look around",
        "Look for a way out",
        "Look for company",
        "QuickSave",
        "QuickLoad"
    ])

    def setup_game(self) -> Player:
        """Sets the RPG game up."""
        local_player = Player(name="Myself")

        first_room = Generation().generate_room()
        local_player.current_room = first_room
        return local_player

    def game_loop(self):
        """Game loop for the RPG game."""
        local_player = self.setup_game()
        while local_player.current_health > 0:  # game ends when player dies
            print("What do you want to do?")
            for item in range(len(self.decisions)):
                print(f"  ({item}) {self.decisions[item]}")

            user_input = input_handler.read_int(input())
            match user_input:
                case 0:
                    local_player.current_room.inspect()
                case 1:
                    self.door_interaction(local_player)
                case 2:
                    self.npc_interaction(local_player)
                case 3:
                    game_state = local_player.toJSON()
                    Saver.quick_save(game_state)
                    print("Saved game!")
                case 4:
                    loaded_state = Saver.quick_load()
                    if loaded_state:
                        local_player = Player.fromJSON(loaded_state)
                    print("Your save game was loaded!")
                case _:
                    print("Enter a valid interaction number!")
        print("Game Over! You've died.")

    def npc_interaction(self, player):
        npcs_list = player.current_room.NPCs
        print("You look if there’s someone here. You see:")
        if not npcs_list:
            print("There's no one in the room.")
            return
        for i, npc in enumerate(npcs_list):
            print(f"  ({i}) {npc.inspect()}.")
        print("Interact? (-1 : do nothing)")
        npc_input = input_handler.read_int(input())
        if npc_input == -1:
            print("You do not interact with anyone.")
            return
        elif npc_input > (len(npcs_list) - 1):
            print("Invalid input! Try again.")
            self.npc_interaction(player)
            return
        npcs_list[npc_input].interact(player)

    def door_interaction(self, player):
        doors_list = player.current_room.doors
        print("You look around for doors. You see:")
        if not doors_list:
            print("There are no doors.")
            return
        for i, door in enumerate(doors_list):
            print(f"  ({i}) {door.description}.")
        print("Which door do you take? (-1 : stay here)")
        door_input = input_handler.read_int(input())
        if door_input == -1:
            print("You stay in the room.")
            return
        elif door_input > (len(doors_list) - 1):
            print("Invalid input! Try again.")
            self.door_interaction(player)
            return
        doors_list[door_input].connected_room = (
            Generation().generate_room(
                player.current_room.room_level + 1
            )
        )
        doors_list[door_input].interact(player)
        print("You go through the door.")
