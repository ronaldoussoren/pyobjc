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

def redraw(o):
  """The main scene redraw function."""

  # Clear the background and depth buffer.

  for i in range(0, len(o.spheres)):
    if i == o.picked_sphere:
      glMaterialfv(GL_FRONT, GL_DIFFUSE, [1., 1., 0., 0.])
    else:
      glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.3, 0.9, 0.3, 0.])
    s = o.spheres[i]
    glPushMatrix()
    glTranslatef(s[0], s[1], s[2])
    glutSolidSphere(1.4,20,20)
    glPopMatrix()

def pick(o, p1, p2, event=None):
  """A pick function.
  The end points of the picked line are passed as p1 and p2.
  glDistFromLine can be used to measure distances from the line."""

  inear = -1
  dmin = 1.e10

  for i in range(0, len(o.spheres)):
    s = o.spheres[i]
    d = glDistFromLine(s, p1, p2)

    if d < dmin:
      inear = i
      dmin = d

  o.picked_sphere = inear

  """If we want the viewer to redraw we return a true value."""

  return 1

#
# Demo starts here really.

import Tkinter, sys

o = Opengl(None, width = 200, height = 200, double = 1, depth = 1)
o.pack(expand = 1, fill = 'both')

o.redraw = redraw
o.pick = pick
o.set_centerpoint(-2., 35., 24.)
o.set_eyepoint(30.)

o.spheres = [
[-4.322, 30.55, 21.011],
[-4.394, 29.355, 21.739],
[-5.645, 28.807, 21.86],
[-3.288, 28.783, 22.252],
[-2.019, 29.274, 22.234],
[-0.974, 28.708, 22.785],
[-1.933, 30.569, 21.533],
[-0.758, 31.235, 21.496],
[-0.765, 32.405, 20.842],
[-1.944, 32.803, 20.217],
[-3.054, 32.324, 20.235],
[-3.083, 31.116, 20.898],
[0.64, 33.021, 20.684],
[0.578, 34.384, 20.488],
[1.308, 34.813, 19.227],
[-1.279, 37.203, 22.934],
[-0.862, 37.551, 21.655],
[-0.194, 36.854, 20.712],
[0.032, 35.404, 21.207],
[-0.553, 35.049, 22.533],
[-1.229, 35.834, 23.289],
[-1.965, 38.13, 23.541],
[-2.138, 39.337, 23.429],
[-2.925, 37.974, 24.419],
[-3.571, 38.572, 25.455],
[-3.41, 37.769, 26.744],
[-3.349, 36.58, 27.005],
[-3.607, 38.634, 27.799],
[-5.12, 38.852, 25.539],
[-5.745, 39.848, 24.643],
[-7.132, 39.91, 23.719],
[-7.29, 40.706, 22.617],
[-7.707, 39.325, 24.755]]

o.picked_sphere = -1
o.autospin_allowed = 1

l = Tkinter.Label(None, text = 'Press Shift-Button-1 over an\natom to highlight')
l.pack(side = 'top', expand = 1, fill = 'both')

# Enter the tk mainloop.

Tkinter.mainloop()

