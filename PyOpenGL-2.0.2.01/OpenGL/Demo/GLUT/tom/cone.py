"""GLUT replacement for the original checker.py demonstration code

Note:
	Has no navigation code ATM.
"""

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

__version__='$Revision: 1.1.2.1 $'[11:-2]
__date__ = '$Date: 2004/11/15 01:10:45 $'[6:-2]


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys

def drawCone( position = (0,-1,0), radius=1, height=2, slices=50,stacks=10 ):
	glPushMatrix()
	try:
		glTranslatef(*position)
		glRotatef(250, 1, 0, 0)
		glutSolidCone(radius, height, slices, stacks )
	finally:
		glPopMatrix()

def coneMaterial( ):
	"""Setup material for cone"""
	glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
	glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
	glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 0.0, 1.0, 1.0])
	glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)
def light():
	"""Setup light 0 and enable lighting"""
	glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 1.0, 0.0, 1.0])
	glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
	glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
	glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0]);   
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
def depth():
	"""Setup depth testing"""
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)

def display( swap=1, clear=1):
	"""Callback function for displaying the scene

	This defines a unit-square environment in which to draw,
	i.e. width is one drawing unit, as is height
	"""
	if clear:
		glClearColor(0.5, 0.5, 0.5, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# establish the projection matrix (perspective)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	x,y,width,height = glGetDoublev(GL_VIEWPORT)
	gluPerspective(
		45, # field of view in degrees
		width/float(height or 1), # aspect ratio
		.25, # near clipping plane
		200, # far clipping plane
	)

	# and then the model view matrix
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(
		0,1,5, # eyepoint
		0,0,0, # center-of-view
		0,1,0, # up-vector
	)
	light()
	depth()
	coneMaterial()

	rotation()
	drawCone()
	if swap:
		glutSwapBuffers()

def idle( ):
	glutPostRedisplay()

starttime = time.time()

def rotation( period = 10):
	"""Do rotation of the scene at given rate"""
	angle = (((time.time()-starttime)%period)/period)* 360
	glRotate( angle, 0,1,0)
	return angle

if __name__ == "__main__":
	print """You should see a high-resolution cone rotating slowly."""
	import sys
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow('Rotating Cone')
	glutDisplayFunc(display)
	glutIdleFunc(display)
	# note need to do this to properly render faceted geometry
	glutMainLoop()
