from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#normal cases
draw_line(250,250,450,350,screen,color)
draw_line(250,250,350,450,screen,color)
draw_line(250,250,150,450,screen,color)
draw_line(250,250,50,350,screen,color)
draw_line(250,250,50,150,screen,color)
draw_line(250,250,150,50,screen,color)
draw_line(250,250,350,50,screen,color)
draw_line(250,250,450,150,screen,color)

#edge cases
draw_line(250,250,450,250,screen,color)
draw_line(250,250,450,450,screen,color)
draw_line(250,250,250,450,screen,color)
draw_line(250,250,50,450,screen,color)
draw_line(250,250,50,250,screen,color)
draw_line(250,250,50,50,screen,color)
draw_line(250,250,250,50,screen,color)
draw_line(250,250,450,50,screen,color)

save_extension(screen, 'img.png')
