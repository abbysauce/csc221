from gasp import *
from random import randint

player_x= randint(0,63)
player_y= randint(0,47)

def place_player():
    Circle((10 * player_x + 5, 10 * player_y +5), 5, filled=True)
    print("Here I am!")

def move_player():
    global player_x, player_y, player_shape

    key = update_when ('key_pressed')

    if key == '6' and player_x < 63:
        player_x += 1
    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y >0:
            player_y -= 1
    print("I'm moving...")

begin_graphics()
finished = False

place_player()

while not finished:
    move_player()

end_graphics()
 
