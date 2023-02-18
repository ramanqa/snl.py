import yaml

class Board:

    def __init__(self):
        with open('board.yaml', 'r') as file:
            self.board = yaml.safe_load(file)

    def position(self, oldx, dice_roll):
        newx = oldx + dice_roll
        if(newx>50):
            return {"position": oldx, "cell_type": "Blank"}
        new_pos = self.board['board'][newx]
        return {"position": new_pos['dx'], "cell_type": self.board['cell_type'][new_pos['cell_type']]}

class PositionException(Exception):

    def __init__(self):
        super().__init__("PositionException: Position is out of bounds")


