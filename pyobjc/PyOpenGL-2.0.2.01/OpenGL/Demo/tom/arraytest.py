#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/30 19:17:17 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

import sys
from OpenGL.GL import *
from OpenGL.Tk import *
try:
	from Numeric import *
except:
	print "This demo requires the Numeric extension, sorry."
	sys.exit()
from RandomArray import *

n=50

def shuffle(a,b):
	return ravel(transpose(reshape(concatenate([a,b]), (2,len(a)))))

def redraw(o):
	glClearColor(1, 1, 1, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glOrtho(-1, 1, -1, 1, -1, 1)
	glDisable(GL_LIGHTING)
	glDrawArrays(GL_LINE_LOOP, 0, n)
	glEnable(GL_LIGHTING)

def main():
	f = Frame()
	f.pack(side = 'top', expand = 1)
	quit = Button(f, text = 'Quit', command = sys.exit)
	quit.pack(side = 'top')
	o = Opengl(width = 400, height = 400, double = 1)
	a = arange(0,n)
	vertex = shuffle(cos(2*pi*a/n), sin(2*pi*a/n))
	vertex.shape = (n, 2)
#	vertex1 = shuffle(0.5*cos(2*pi*a/n), 0.5*sin(2*pi*a/n))
#	color=ones((n, 3), 'i')
#	color[0]=[1,0,0]
#	color[1]=[1,1,0]
#	color[1]=[1,0,0]
	color = random(n*3)
	color.shape = (n, 3)

	glVertexPointerd(vertex)
	glColorPointerd(color)
	glEnableClientState(GL_VERTEX_ARRAY)
	glEnableClientState(GL_COLOR_ARRAY)

	o.redraw = redraw
	o.pack(side = 'top', expand = 1, fill = 'both')
	o.mainloop()

main()
