import uuid
import json

class Player:

    def __init__(self, player_name):
        self.name = player_name
        self.id = str(uuid.uuid4())
        self.position = 0

    def __str__(self):
        return json.dumps(self.__dict__)

    def join(self, board):
        ""
