from lib.board import Board
from lib.game import Game
from lib.player import Player

import json

game = Game()

p1 = game.join("A")
p2 = game.join("B")
p3 = game.join("C")
p4 = game.join("D")

for i in range(0,100):
    print("==: " + str(i) + " >>")
    for x in range(1,5):
        print(eval("game.play_turn(p"+str(x)+")"))
