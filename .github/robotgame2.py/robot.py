from gasp import *
from random import randint


def place_player():
    global player_x, player_y, player_shape

    player_x = randint(0, 63)
    player_y = randint(0, 47)
    player_shape = Circle((10 * player_x + 5, 10 * player_y +5), 5, filled=True)


def move_player():
    global player_x, player_y, player_shape

    key = update_when ('key_pressed')

    if key == 'd' and player_x < 63:
        player_x += 1
    elif key == 'c':
        if player_x < 63:
            player_x += 1
        if player_y >0:
            player_y -= 1
    move_to(player_shape, (10 * player_x + 5, 10 * player_y +5))
    

begin_graphics()
finished = False

place_player()

move_player()

while not finished:
    move_player()

end_graphics()
 
