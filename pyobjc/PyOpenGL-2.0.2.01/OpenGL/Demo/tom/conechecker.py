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
from OpenGL.GLUT import *
import sys

def redraw_checker(o):
  glClearColor(1, 0, 1, 0)
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glColor3f(0, 1, 0)
  #draw checkerboard
  N = 4
  glDisable(GL_LIGHTING)
  for x in range(-N, N):
    for y in range(-N, N):
      if (x + y) % 2 == 0:
	glColor3f(1, 1, 0)
      else:
	glColor3f(0, 0, 0)	
      glRectf(x, y, x + 1, y + 1)
  glEnable(GL_LIGHTING)

  glPushMatrix()
  glTranslatef(0., 0., 1.)
  glutSolidSphere(1.0,20,20)
  glPopMatrix()

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


def redraw_cone(o):
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glPushMatrix()
  glTranslatef(0, -1, 0)
  glRotatef(250, 1, 0, 0)
  glutSolidCone(1, 2, 50, 10)
  glPopMatrix()

def main():
  f = Frame()
  f.pack(side = TOP)
  o1 = Opengl(width = 200, height = 200, double = 1, depth = 1)
  o1.redraw = redraw_checker
  quit = Button(f, text = 'Quit', command = sys.exit)
  quit.pack(side = TOP, expand=YES, fill=BOTH)
  o1.pack(side = TOP, expand = YES, fill = BOTH)
  o1.set_eyepoint(20.)

  o2 = Opengl(width = 200, height = 200, double = 1)
  o2.redraw = redraw_cone
  o2.autospin_allowed = 1
  o2.pack(side = TOP, expand = YES, fill = BOTH)
  init()

  o1.mainloop()

main()




