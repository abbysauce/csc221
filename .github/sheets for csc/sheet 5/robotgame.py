
from gasp import *
from random import randint
from time import sleep
begin_graphics()
c=Circle((320, 200), 5)
move_to(c, (300, 220))
player_x= randint(0,63)
player_y= randint(0,47)

def place_player():
    print("here I am!")
    place_player=((player_x, player_y), 5)

def move_player():
    print("I'm moving..")
    update_when('key_pressed')

pc=Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)

finished = False


while not finished:
  move_player()
update_when('key_pressed')
end_graphics
