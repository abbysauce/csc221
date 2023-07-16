from gasp import *
begin_graphics()
Circle((300,200),100)
Circle((260,220),15)
Circle((340,220),15)
Line((280, 170), (320,170))
Line((280,170),(300,220))
Arc((300, 200), 70, 225, 315)
Arc((340, 230), 30, 25)
Arc((260, 220), 15,7)
update_when('key_pressed')
end_graphics

