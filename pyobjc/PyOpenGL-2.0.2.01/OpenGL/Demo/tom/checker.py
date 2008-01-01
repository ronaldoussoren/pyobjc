#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/30 19:17:17 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.Tk import *
import sys

def redraw(o):
  glClearColor(1, 0, 1, 0)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glColor3f(0, 1, 0)
  #draw checkerboard
  N = 4
  glDisable(GL_LIGHTING)
  for x in range(-N, N):
    for y in range(-N, N):
      if (x + y) % 2 == 0:
	glColor3f(1, 1, 1)
      else:
	glColor3f(0, 0, 0)	
      glRectf(x, y, x + 1, y + 1)
  glEnable(GL_LIGHTING)

  glPushMatrix()
  glTranslatef(0., 0., 1.)
  glutSolidSphere(1.0,20,20)
  glPopMatrix()

def main():
  f = Frame()
  f.pack(side = 'top')
  o = Opengl(width = 200, height = 200, double = 1, depth = 1)
  o.redraw = redraw
  quit = Button(f, text = 'Quit', command = sys.exit)
  quit.pack({'side':'top', 'side':'left'})
  help = Button(f, text = 'Help', command = o.help)
  help.pack({'side':'top', 'side':'left'})
  reset = Button(f, text = 'Reset', command = o.reset)
  reset.pack({'side':'top', 'side':'left'})
  o.pack(side = 'top', expand = 1, fill = 'both')
  o.set_eyepoint(20.)
  o.mainloop()

main()
