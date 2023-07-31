from gasp import *
from random import randint
from time import sleep

class Player:
    pass
class Robot:
    pass

def place_robot():
    global robot
    robot= Robot()

    robot.x, robot.y = randint(0,63), randint(0,47)
    robot.shape = Box((10 * robot.x + 5, 10 * robot.y +5), 12, 12, filled=True, color = color.BLUE, thickness= 1)

def place_player():
    global player
    player= Player()

    player.x = randint(0, 63)
    player.y = randint(0, 47)
    player.shape = Circle((10 * player.x + 5, 10 * player.y +5), 5, filled=True, color = color.DEEPPINK, thickness = 3 )
    

def safely_place_player ():
    place_player()
    while player.x != robot.x and player.y != robot.y:
        place_player()


def move_player():
    global player

    key = update_when ('key_pressed')

    if key == 't':
      remove_from_screen(player.shape)
      safely_place_player()
      key = update_when('key_pressed')

    if key == 'd' and player.x < 63:
        player.x += 1
    elif key == 'c':
        if player.x < 63:
            player.x += 1
        if player.y >0:
            player.y -= 1
    elif key== 'z':
        if player.x < 63:
            player.x -= 1
        if player.y > 0:
            player.y -=1
    elif key == 'e' :
        if player.x<63:
            player.x += 1
        if player.y >0 :
            player.y += 1
    elif key == 'a':
        if player.x < 63 :
            player.x = player.x - 1
    elif key == 's':
        if player.y > 0:
            player.y = player.y + 1
    elif key == 'x':
        if player.y > 0:
            player.y = player.y - 1
    elif key == 'q' :
        if player.x<63:
            player.x -= 1
        if player.y >0 :
            player.y += 1

    move_to(player.shape, (10 * player.x + 5, 10 * player.y +5))

def move_robot():
    global robot
    if robot.y > player.y:
        robot.y -= 1
    if robot.y < player.y:
        robot.y += 1
    if robot.x > player.x:
        robot.x -= 1
    if robot.x < player.x:
        robot.x += 1
    move_to(robot.shape, (10 * robot.x, 10 * robot.y))

def check_collisions():
    global finished
    if robot.x== player.x and robot.y == player.y:
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
 