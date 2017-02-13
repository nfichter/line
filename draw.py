from display import *

def draw_line1(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x <= x1:
		plot(screen,color,x,y)
		if d > 0:
			y+=1
			d+=B
		x+=1
		d+=A
		
def draw_line2(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x <= x1:
		plot(screen,color,x,y)
		if d < 0:
			x+=1
			d+=A
		y+=1
		d+=B
	
def draw_line3(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x >= x1:
		plot(screen,color,x,y)
		if d > 0:
			x-=1
			d-=A
		y+=1
		d+=B

def draw_line4(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x >= x1:
		plot(screen,color,x,y)
		if d < 0:
			y+=1
			d+=B
		x-=1
		d-=A
	
def draw_line5(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x >= x1:
		plot(screen,color,x,y)
		if d > 0:
			y-=1
			d-=B
		x-=1
		d-=A
	
def draw_line6(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x >= x1:
		plot(screen,color,x,y)
		if d < 0:
			x-=1
			d-=A
		y-=1
		d-=B

def draw_line7(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x <= x1:
		plot(screen,color,x,y)
		if d > 0:
			x+=1
			d+=A
		y-=1
		d-=B
		
def draw_line8(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A+B
	B = 2*B
	
	x = x0
	y = y0
	
	while x <= x1:
		plot(screen,color,x,y)
		if d < 0:
			y-=1
			d-=B
		x+=1
		d+=A

def draw_line_vert(x0, y0, x1, y1, screen, color):
	y = y0
	x = x0
	
	if y0 < y1:
		while y < y1:
			plot(screen,color,x,y)
			y+=1
	else:
		while y > y1:
			plot(screen,color,x,y)
			y-=1

def draw_line(x0, y0, x1, y1, screen, color):
	dx = x1-x0
	dy = y1-y0
	
	if x0 == x1:
		draw_line_vert(x0, y0, x1, y1, screen, color)
	
	if dx > 0:
		if dy > 0:
			if dy < dx:
				draw_line1(x0, y0, x1, y1, screen, color)
			else:
				draw_line2(x0, y0, x1, y1, screen, color)
		else:
			if dy*-1 < dx:
				draw_line8(x0, y0, x1, y1, screen, color)
			else:
				draw_line7(x0, y0, x1, y1, screen, color)
	else:
		if dy > 0:
			if dy > dx*-1:
				draw_line3(x0, y0, x1, y1, screen, color)
			else:
				draw_line4(x0, y0, x1, y1, screen, color)
		else:
			if dy < dx:
				draw_line6(x0, y0, x1, y1, screen, color)
			else:
				draw_line5(x0, y0, x1, y1, screen, color)