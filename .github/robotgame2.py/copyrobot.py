from gasp import *
from random import randint
from time import sleep

def place_robot():
    global robot_x, robot_y, robot_shape

    robot_x, robot_y = randint(0,63), randint(0,47)
    robot_shape = Box((10 * robot_x + 5, 10 * robot_y +5), 12, 12, filled=True, color = color.BLUE, thickness= 1)

def place_player():
    global player_x, player_y, player_shape

    player_x = randint(0, 63)
    player_y = randint(0, 47)
    player_shape = Circle((10 * player_x + 5, 10 * player_y +5), 5, filled=True, color = color.DEEPPINK, thickness = 3 )
    

def safely_place_player ():
    place_player()
    while player_x != robot_x and player_y != robot_y:
        place_player()


def move_player():
    global player_x, player_y, player_shape

    key = update_when ('key_pressed')

    if key == 't':
      remove_from_screen(player_shape)
      safely_place_player()
      key = update_when('key_pressed')

    if key == 'd' and player_x < 63:
        player_x += 1
    elif key == 'c':
        if player_x < 63:
            player_x += 1
        if player_y >0:
            player_y -= 1
    elif key== 'z':
        if player_x < 63:
            player_x -= 1
        if player_y > 0:
            player_y -=1
    elif key == 'e' :
        if player_x<63:
            player_x += 1
        if player_y >0 :
            player_y += 1
    elif key == 'a':
        if player_x < 63 :
            player_x = player_x - 1
    elif key == 's':
        if player_y > 0:
            player_y = player_y + 1
    elif key == 'x':
        if player_y > 0:
            player_y = player_y - 1
    elif key == 'q' :
        if player_x<63:
            player_x -= 1
        if player_y >0 :
            player_y += 1

    move_to(player_shape, (10 * player_x + 5, 10 * player_y +5))

def move_robot():
    global robot_x, robot_y, robot_shape
    if robot_y > player_y:
        robot_y -= 1
    if robot_y < player_y:
        robot_y += 1
    if robot_x > player_x:
        robot_x -= 1
    if robot_x < player_x:
        robot_x += 1
    move_to(robot_shape, (10 * robot_x, 10 * robot_y))

def check_collisions():
    global finished
    if robot_x== player_x and robot_y == player_y:
        Text("You've been caught!", (300,200), size= 30, color=color.HOTPINK)
        sleep(2)
        finished = True



begin_graphics()
finished = False

place_robot()

place_player()

move_player()

move_robot()

check_collisions()

while not finished:
    move_player()
    move_robot()
    check_collisions()

end_graphics()
 