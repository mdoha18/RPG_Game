import json


class DictEncoder(json.JSONEncoder):
    """This class is from lecture 9 using to check if object is natively
       JSON serializable it falls back to object's _dict_."""

    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return obj.__dict__
