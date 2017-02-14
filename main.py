from display import *
from draw import *
import time

screen = new_screen()
color = [ 255, 0, 0 ]

#normal cases
draw_line(250,250,450,350,screen,color)
draw_line(250,250,350,450,screen,color)
draw_line(250,250,150,450,screen,color)
draw_line(250,250,50,350,screen,color)
draw_line(250,250,50,150,screen,color)
draw_line(250,250,150,50,screen,color)
draw_line(250,250,350,50,screen,color)
draw_line(250,250,450,150,screen,color)

color = [0,255,0]

#edge cases
draw_line(250,250,450,250,screen,color)
draw_line(250,250,450,450,screen,color)
draw_line(250,250,250,450,screen,color)
draw_line(250,250,50,450,screen,color)
draw_line(250,250,50,250,screen,color)
draw_line(250,250,50,50,screen,color)
draw_line(250,250,250,50,screen,color)
draw_line(250,250,450,50,screen,color)

color = [0,0,255]

#N
draw_line(50,350,50,450,screen,color)
draw_line(50,450,100,350,screen,color)
draw_line(100,350,100,450,screen,color)

#O
draw_line(

save_extension(screen, 'img.png')
