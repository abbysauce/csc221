from gasp import *
from time import sleep
begin_graphics()
ball_x=5
ball_y=5
ball=Circle((ball_x, ball_y),5, color=color.BLUE, filled=True)
while ball_x<635:
   ball_x= ball_x + 4
   ball_y= ball_y + 3
   move_to(ball(ball_x, ball_y)) 
   sleep(0.02)
update_when("key_pressed")
end_graphics()
