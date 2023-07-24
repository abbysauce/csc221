from gasp import *
from time import sleep

begin_graphics()
ball_x , ball_y= 5 , 5

while ball_x<635:
    ball= Circle((ball_x, ball_y), 5, filled=True)
    ball_x= ball_x + 4
    ball_y= ball_y + 3
    move_to
    sleep(0.02)
    remove_from_screen(ball)

end_graphics()
