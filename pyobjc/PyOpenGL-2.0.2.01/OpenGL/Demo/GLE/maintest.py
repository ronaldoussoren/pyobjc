#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import sys
from OpenGL.GL import *
from OpenGL.GLE import *
from OpenGL.GLUT import *


lastx=0
lasty=0

# get notified of mouse motions
def MouseMotion (x, y):
	global lastx, lasty
	lastx = x
	lasty = y
	glutPostRedisplay ()


def JoinStyle (msg):
	sys.exit(0)


# set up a light 
lightOnePosition = (40.0, 40, 100.0, 0.0)
lightOneColor = (0.99, 0.99, 0.99, 1.0) 

lightTwoPosition = (-40.0, 40, 100.0, 0.0)
lightTwoColor = (0.99, 0.99, 0.99, 1.0) 


def main(DrawStuff):
	global glutDisplayFunc, glutMotionFunc
	# initialize glut 
	glutInit(sys.argv)
	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutCreateWindow("basic demo")
	glutDisplayFunc(DrawStuff)
	glutMotionFunc(MouseMotion)

	# create popup menu */
#	glutCreateMenu (JoinStyle)
#	glutAddMenuEntry ("Exit", 99)
#	glutAttachMenu (GLUT_MIDDLE_BUTTON)

	# initialize GL */
	glClearDepth (1.0)
	glEnable (GL_DEPTH_TEST)
	glClearColor (0.0, 0.0, 0.0, 0.0)
	glShadeModel (GL_SMOOTH)

	glMatrixMode (GL_PROJECTION)
	# roughly, measured in centimeters */
	glFrustum (-9.0, 9.0, -9.0, 9.0, 50.0, 150.0)
	glMatrixMode(GL_MODELVIEW)

	# initialize lighting */
	glLightfv (GL_LIGHT0, GL_POSITION, lightOnePosition)
	glLightfv (GL_LIGHT0, GL_DIFFUSE, lightOneColor)
	glEnable (GL_LIGHT0)
	glLightfv (GL_LIGHT1, GL_POSITION, lightTwoPosition)
	glLightfv (GL_LIGHT1, GL_DIFFUSE, lightTwoColor)
	glEnable (GL_LIGHT1)
	glEnable (GL_LIGHTING)
	glColorMaterial (GL_FRONT_AND_BACK, GL_DIFFUSE)
	glEnable (GL_COLOR_MATERIAL)

	glutMainLoop ()
