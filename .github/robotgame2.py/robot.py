from gasp import *
from random import randint

player_x= randint(0,63)
player_y= randint(0,47)

def place_player():
    Circle((10 * player_x + 5, 10 * player_y +5), 5, filled=True)
    print("Here I am!")

def move_player():
    print("I'm moving...")
    update_when('Key_pressed')


begin_graphics()
finished = False

place_player()


while not finished:
    move_player()

end_graphics()
 