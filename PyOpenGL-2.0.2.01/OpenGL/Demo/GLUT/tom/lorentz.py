"""GLUT replacement for the original lorentz.py demonstration code

This is the original lorentz.py demo, with a few changes to
run under GLUT and not require the TK examination widget
extensions.

Code is also broken up somewhat more, with the actual drawing
of the curve in its own function which can be called instead of
the display-list if desired.
"""

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

__version__='$Revision: 1.1.2.1 $'[11:-2]
__date__ = '$Date: 2004/11/15 01:10:45 $'[6:-2]


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

n, dt = 2000, 0.01
x, y, z = 0.01, 0.01, 0.01
frac = -1.0 * (8.0/3.0)

def lorentz(x, y, z, n=2000, dt=0.01):
	"""Generate Lorentz attractor as a Display-list"""
	target = glGenLists(1);
	glNewList(target, GL_COMPILE);
	try:
		drawLorentz( x,y,z,n,dt )
	finally:
		glEndList()
	return target
def drawLorentz( x, y, z, n=2000, dt=0.01):
	"""Do the actual drawing & calculation of lorentz"""
	glDisable(GL_LIGHTING)
	glBegin(GL_LINE_STRIP)

	glVertex3f(x, y, z)
	frac = -1.0 * (8.0/3.0)
	for i in range(0, n):
		xp = x + (-10.0 * x * dt + 10.0 * y * dt)
		yp = y + ( 28.0 * x * dt - y * dt - x * dt * z *dt)
		zp = z + ( frac * z * dt + x * dt * y * dt)
		x=xp
		y=yp
		z=zp
		glColor3f( i/float(n),i/float(n), 0 )
		glVertex3f(x, y, z)
	glEnd()

	glEnable(GL_LIGHTING)

LORENTZ_LIST = lorentz( 0.01, 0.01, 0.01 )

def display( ):
	"""Callback function for displaying the scene

	This defines a unit-square environment in which to draw,
	i.e. width is one drawing unit, as is height
	"""
	glClearColor(0.5, 0.5, 0.5, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# establish the projection matrix (perspective)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(
		45, # field of view in degrees
		glutGet(GLUT_WINDOW_WIDTH)/float(glutGet(GLUT_WINDOW_HEIGHT) or 1), # aspect ratio
		1, # near clipping plane
		30000, # far clipping plane
	)
	# and then the model view matrix
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(
		0,0,13000, # eyepoint
		0,0,2000, # center-of-view
		0,1,0, # up-vector
	)
	rotation()
	drawLorentz( 0.01, 0.01, 0.01 )
	#glCallList( LORENTZ_LIST )
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
	print """You should see a curved line representing a Lorentz
attractor, rendered in 3D, rotation about the origin."""
	import sys
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow('Lorentz Attractor Demo')
	glutDisplayFunc(display)
	glutIdleFunc(display)
	glutMainLoop()
