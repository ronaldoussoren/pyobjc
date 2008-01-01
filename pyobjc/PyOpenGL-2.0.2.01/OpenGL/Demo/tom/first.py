#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/30 19:17:17 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

from OpenGL.GL import *
from OpenGL.Tk import *

def redraw(o):
  glClearColor(0, 0, 1, 0)
  glClear(GL_COLOR_BUFFER_BIT)

o = Opengl(width = 200, height = 200, double = 1)
o.redraw = redraw
o.pack(side = 'top', expand = 1, fill = 'both')
o.mainloop()
