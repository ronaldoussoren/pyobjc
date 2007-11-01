#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

'''
lines.c from the Redbook examples.  
Converted to Python by Jason L. Petrone 6/00

/*
 *  lines.c
 *  This program demonstrates geometric primitives and
 *  their attributes.
*/



Copyright (c) 1993-1997, Silicon Graphics, Inc.
ALL RIGHTS RESERVED 
Permission to use, copy, modify, and distribute this software for 
any purpose and without fee is hereby granted, provided that the above
copyright notice appear in all copies and that both the copyright notice
and this permission notice appear in supporting documentation, and that 
the name of Silicon Graphics, Inc. not be used in advertising
or publicity pertaining to distribution of the software without specific,
written prior permission. 

THE MATERIAL EMBODIED ON THIS SOFTWARE IS PROVIDED TO YOU "AS-IS"
AND WITHOUT WARRANTY OF ANY KIND, EXPRESS, IMPLIED OR OTHERWISE,
INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY OR
FITNESS FOR A PARTICULAR PURPOSE.  IN NO EVENT SHALL SILICON
GRAPHICS, INC.  BE LIABLE TO YOU OR ANYONE ELSE FOR ANY DIRECT,
SPECIAL, INCIDENTAL, INDIRECT OR CONSEQUENTIAL DAMAGES OF ANY
KIND, OR ANY DAMAGES WHATSOEVER, INCLUDING WITHOUT LIMITATION,
LOSS OF PROFIT, LOSS OF USE, SAVINGS OR REVENUE, OR THE CLAIMS OF
THIRD PARTIES, WHETHER OR NOT SILICON GRAPHICS, INC.  HAS BEEN
ADVISED OF THE POSSIBILITY OF SUCH LOSS, HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, ARISING OUT OF OR IN CONNECTION WITH THE
POSSESSION, USE OR PERFORMANCE OF THIS SOFTWARE.

US Government Users Restricted Rights 
Use, duplication, or disclosure by the Government is subject to
restrictions set forth in FAR 52.227.19(c)(2) or subparagraph
(c)(1)(ii) of the Rights in Technical Data and Computer Software
clause at DFARS 252.227-7013 and/or in similar or successor
clauses in the FAR or the DOD or NASA FAR Supplement.
Unpublished-- rights reserved under the copyright laws of the
United States.  Contractor/manufacturer is Silicon Graphics,
Inc., 2011 N.  Shoreline Blvd., Mountain View, CA 94039-7311.

OpenGL(R) is a registered trademark of Silicon Graphics, Inc.

'''

import sys

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''
  sys.exit()

def drawOneLine(x1, y1, x2, y2):
  glBegin(GL_LINES)
  glVertex2f(x1, y1)
  glVertex2f(x2, y2)
  glEnd()


def init():
  glClearColor(0.0, 0.0, 0.0, 0.0)
  glShadeModel(GL_FLAT)

def display():
  glClear(GL_COLOR_BUFFER_BIT)

  # select white for all lines
  glColor3f(1.0, 1.0, 1.0)

  # in 1st row, 3 lines, each with a different stipple
  glEnable(GL_LINE_STIPPLE)

  glLineStipple (1, 0x0101)  #  dotted  
  drawOneLine (50.0, 125.0, 150.0, 125.0)
  glLineStipple (1, 0x00FF)  #  dashed 
  drawOneLine (150.0, 125.0, 250.0, 125.0);
  glLineStipple (1, 0x1C47)  #  dash/dot/dash
  drawOneLine (250.0, 125.0, 350.0, 125.0)

  # in 2nd row, 3 wide lines, each with different stipple 
  glLineWidth(5.0)
  glLineStipple(1, 0x0101)  #  dotted 
  drawOneLine(50.0, 100.0, 150.0, 100.0)
  glLineStipple(1, 0x00FF)  #  dashed
  drawOneLine(150.0, 100.0, 250.0, 100.0)
  glLineStipple(1, 0x1C47)  #  dash/dot/dash
  drawOneLine(250.0, 100.0, 350.0, 100.0)
  glLineWidth(1.0)

  # in 3rd row, 6 lines, with dash/dot/dash stipple  
  # as part of a single connected line strip        
  glLineStipple (1, 0x1C47)  # dash/dot/dash
  glBegin (GL_LINE_STRIP)
  for i in range(0, 7):
    glVertex2f(50.0 + (i * 50.0), 75.0)
  glEnd()

  # in 4th row, 6 independent lines with same stipple  */
  for i in range(0, 6):
    drawOneLine (50.0 + (i * 50.0), 50.0, 50.0 + ((i+1) * 50.0), 50.0)

  # in 5th row, 1 line, with dash/dot/dash stipple 
  # and a stipple repeat factor of 5               
  glLineStipple (5, 0x1C47)  #  dash/dot/dash 
  drawOneLine (50.0, 25.0, 350.0, 25.0)

  glDisable (GL_LINE_STIPPLE)
  glFlush ()

def reshape(w, h):
  glViewport(0, 0, w, h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0.0, w, 0.0, h)

def keyboard(key, x, y):
  if key == chr(27):
    sys.exit(0)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 150)
glutInitWindowPosition(100, 100)
glutCreateWindow('Lines')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()
