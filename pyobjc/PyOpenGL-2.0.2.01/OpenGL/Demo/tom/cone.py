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

def init():
  glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
  glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
  glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 0.0, 1.0, 1.0])
  glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)
  glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 1.0, 0.0, 1.0])
  glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
  glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
  glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0]);   
  glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)
  glDepthFunc(GL_LESS)
  glEnable(GL_DEPTH_TEST)


def redraw(o):
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glPushMatrix()
  glTranslatef(0, -1, 0)
  glRotatef(250, 1, 0, 0)
  glutSolidCone(1, 2, 50, 10)
  glPopMatrix()

def main():
  o = Opengl(width = 200, height = 200, double = 1, depth = 1)
  o.redraw = redraw
  o.autospin_allowed = 1
  o.pack(side = TOP, expand = YES, fill = BOTH)
  init()
  o.mainloop()

main()
