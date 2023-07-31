from gasp import *
begin_graphics()
c = Circle((320, 200), 5)
move_to(c,(300,220)) 


class Robot:
    pass

fred = Robot()
fred.x = 100
fred.y = 200
print(fred.x, fred.y)

update_when ('key_pressed')
end_graphics()