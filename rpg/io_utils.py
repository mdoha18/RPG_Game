import os
import json


class Saver:
    directory: str = 'savedgames'

    @classmethod
    def check_directory(cls):
        if not os.path.exists(cls.directory):
            os.makedirs(cls.directory, exist_ok=True)

    @classmethod
    def quick_save(cls, game_status: dict, file: str = 'quicksave.json'):
        cls.check_directory()
        path = os.path.join(cls.directory, file)
        try:
            with open(path, 'w') as file:
                json.dump(game_status, file)
        except json.JSONEncodeError:
            raise ValueError("Could not serialize data to save")

    @classmethod
    def quick_load(cls, file: str = 'quicksave.json'):
        cls.check_directory()
        path = os.path.join(cls.directory, file)
        if not os.path.exists(path):
            print("Choose '(3) QuickSave' first, before trying to load game")
            return None
        with open(path, 'r') as file:
            state = json.load(file)
        return state
