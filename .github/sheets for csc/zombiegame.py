
from gasp import *
from random import randint
begin_graphics()
c=Circle((320, 200), 5)
move_to(c, (300, 220))
player_x= randint(0,63)
player_y= randint(0,47)
def place_player():
    print("here I am!")
def move_player():
    print("I'm moving..")
    update_when('key_pressed')
Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
finished = False
place_player=((player_x, player_y), 5)
while not finished:
  move_player()
update_when('key_pressed')
end_graphics
