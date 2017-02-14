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
		color = adjust_color(color)
		
def draw_line2(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	B = 2*B
	d = A+B
	A = 2*A
	
	x = x0
	y = y0
	
	while y <= y1:
		plot(screen,color,x,y)
		if d < 0:
			x+=1
			d+=A
		y+=1
		d+=B
		color = adjust_color(color)
	
def draw_line3(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	B = 2*B
	d = B-A
	A = 2*A
	
	x = x0
	y = y0
	
	while y <= y1:
		plot(screen,color,x,y)
		if d > 0:
			x-=1
			d-=A
		y+=1
		d+=B
		color = adjust_color(color)

def draw_line4(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = B-A
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
		color = adjust_color(color)
	
def draw_line5(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = 0-A-B
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
		color = adjust_color(color)
	
def draw_line6(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	B = 2*B
	d = 0-A-B
	A = 2*A
	
	x = x0
	y = y0
	
	while y >= y1:
		plot(screen,color,x,y)
		if d < 0:
			x-=1
			d-=A
		y-=1
		d-=B
		color = adjust_color(color)

def draw_line7(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	B = 2*B
	d = A-B
	A = 2*A
	
	x = x0
	y = y0
	
	while y >= y1:
		plot(screen,color,x,y)
		if d > 0:
			x+=1
			d+=A
		y-=1
		d-=B
		color = adjust_color(color)
		
def draw_line8(x0, y0, x1, y1, screen, color):
	A = y1-y0
	B = -1*(x1-x0)
	
	A = 2*A
	d = A-B
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
		color = adjust_color(color)
		
def adjust_color(color):
	ret = [ 0, 0, 0 ]
	ret[0] = color[0]
	ret[1] = color[1]
	ret[2] = color[2]
	if color[0] >= 255:
		ret[0] = 0
		if color[1] >= 255:
			ret[1] = 0
			if color[2] >= 255:
				ret[2] = 0
			else:
				ret[2]+=30
				if ret[2] > 255:
					ret[2] = 255
		else:
			ret[1]+=30
			if ret[1] > 255:
				ret[1] = 255
	else:
		ret[0]+=30
		if ret[0] > 255:
			ret[0] = 255
	i = 0
	return ret

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