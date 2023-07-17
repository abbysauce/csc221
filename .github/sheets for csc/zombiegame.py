from gasp import *
from random import randint
def place_player():
    print("here I am!")
def move_player():
    print("I'm moving..")
    update_when ('key pressed')
begin_graphics()
finished = False
place_player(player_x, player_y)
while not finished:
  move_player()
end_graphics()
