#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLE import *
import maintest


# draw the polycone shape
def DrawStuff():
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# set up some matrices so that the object spins with the mouse
	gleSetJoinStyle (TUBE_NORM_EDGE | TUBE_JN_ANGLE | TUBE_JN_CAP)
	glPushMatrix ()
	glTranslatef (0.0, 0.0, -80.0)
	glRotatef (maintest.lastx, 0.0, 1.0, 0.0)
	glRotatef (maintest.lasty, 1.0, 0.0, 0.0)

	# Phew. FINALLY, Draw the polycone
	glePolyCone(((-6.0, 6.0, 0.0), (6.0, 6.0, 0.0), (6.0, -6.0, 0.0), (-6.0, -6.0, 0.0), (-6.0, 6.0, 0.0), (6.0, 6.0, 0.0)),
				((0.0, 0.0, 0.0), (0.0, 0.8, 0.3), (0.8, 0.3, 0.0), (0.2, 0.3, 0.9), (0.2, 0.8, 0.5), (0.0, 0.0, 0.0)), (1, 1, 3, 0.5, 2, 1))

	glPopMatrix ()

	glutSwapBuffers ()



maintest.main(DrawStuff)
