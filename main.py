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

#NOAH
#N
draw_line(75,350,75,450,screen,color)
draw_line(75,450,125,350,screen,color)
draw_line(125,350,125,450,screen,color)

#O
draw_line(175,350,225,350,screen,color)
draw_line(175,450,225,450,screen,color)
draw_line(175,350,175,450,screen,color)
draw_line(225,350,225,450,screen,color)

#A
draw_line(275,350,275,450,screen,color)
draw_line(325,350,325,450,screen,color)
draw_line(275,450,325,450,screen,color)
draw_line(275,400,325,400,screen,color)

#H
draw_line(375,350,375,450,screen,color)
draw_line(425,350,425,450,screen,color)
draw_line(375,400,425,400,screen,color)

#FICHTER
#F
draw_line(50,50,50,150,screen,color)
draw_line(50,100,100,100,screen,color)
draw_line(50,150,100,150,screen,color)

#I
draw_line(107,50,157,50,screen,color)
draw_line(107,150,157,150,screen,color)
draw_line(132,50,132,150,screen,color)

#C
draw_line(164,50,214,50,screen,color)
draw_line(164,150,214,150,screen,color)
draw_line(164,50,164,150,screen,color)

#H
draw_line(271,50,271,150,screen,color)
draw_line(221,50,221,150,screen,color)
draw_line(221,100,271,100,screen,color)

#T
draw_line(278,150,328,150,screen,color)
draw_line(303,150,303,50,screen,color)

#E
draw_line(335,150,385,150,screen,color)
draw_line(335,100,385,100,screen,color)
draw_line(335,50,385,50,screen,color)
draw_line(335,50,335,150,screen,color)

#R
draw_line(392,50,392,150,screen,color)
draw_line(392,100,442,100,screen,color)
draw_line(392,150,442,150,screen,color)
draw_line(442,150,442,100,screen,color)
draw_line(435,100,450,50,screen,color)

save_extension(screen, 'img.png')
display(screen)