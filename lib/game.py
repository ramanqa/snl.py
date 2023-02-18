from lib.board import Board
from lib.player import Player
import uuid
import json
import random

class Game:

    def __init__(self, game_id=None):
        if(game_id):
            file = open(game_id + '.db')
            data = json.load(file)
            self.id = data['id']
            self.state = data['state']
            self.players = data['players']
            self.turn = data['turn']
            file.close()
        else:
            self.id = str(uuid.uuid4())
            self.state = 'Not Started'
            self.players = []
            self.turn = 0
            self.save()

    def save(self):
        file = open(self.id + '.db', 'w')
        json.dump(self.__dict__, file, indent=2)
        file.close()

    def __str__(self):
        return json.dumps(self.__dict__)

    def join(self, player_name):
        # check if player limit reached
        if(len(self.players) == 4):
            raise PlayersJoinLimitReachedException
        # check player name conflict
        for player in self.players:
            if(player['name'] == player_name):
                raise PlayerExistsException
        
        player_obj = Player(player_name)
        self.players.append(player_obj.__dict__)
        self.save()

        return player_obj.id

    def play_turn(self, player_id):
        # update gate state
        if(self.state == "Finished"):
            raise GameFinishedException

        self.state = "Running"

        # check player's turn
        turn_player = self.players[self.turn]
        if turn_player['id'] == player_id:
            # roll dice
            dice_roll = random.randint(1,6)

            # play turn
            board = Board()
            new_position = board.position(turn_player['position'], dice_roll)
            self.players[self.turn]['position'] = new_position['position']
            # reset turn
            self.turn += 1
            if(self.turn == len(self.players)):
                self.turn = 0
            if(new_position['position'] == 50):
                self.state = "Finished"
                self.save()
                return {"game_state": self.state, "player_id": player_id, "player_name": turn_player['name'], "winner": player_id, "position": new_position['position'], "cell_type": new_position["cell_type"], "dice_roll": dice_roll}
            
            self.save()
            return {"game_state": self.state, "player_id": player_id, "player_name": turn_player['name'], "position": new_position['position'], "cell_type": new_position["cell_type"], "dice_roll": dice_roll}

        else:
            raise InvalidTurnException
        

class PlayersJoinLimitReachedException(Exception):
    
    def __init__(self):
        super().__init__("PlayersJoinLimitReachedException: Game already has 4 players")


class PlayerExistsException(Exception):

    def __init__(self):
        super().__init__("PlayerExistsException: Player already exists in Game")


class InvalidTurnException(Exception):

    def __init__(self):
        super().__init__("InvalidTurnException: Player does not have turn")

class GameFinishedException(Exception):

    def __init__(self):
        super().__init__("GameFinishedException: Game is already over")
