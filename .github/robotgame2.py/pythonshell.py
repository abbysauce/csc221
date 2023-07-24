from gasp import *
begin_graphics()
c = Circle((320, 200), 5)
move_to(c,(300,220))
update_when ('key_pressed')
end_graphics()