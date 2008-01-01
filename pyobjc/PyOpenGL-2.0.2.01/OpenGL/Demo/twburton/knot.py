#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLE import *
from OpenGL.GLUT import *
from math import *
from Numeric import *
from random import *
import string


def loadKnot(filename):
	f = open(filename)
	curves = []
	points = []

	for line in f.readlines():
		if string.lower(line[:9]) == 'component':
			if len(points):
				curves.append(points)
				points = []
		else:
			try:
				points.append(array(map(float, line.split())))
			except:
				pass

	if len(points):
		curves.append(points)
		points = []

	f.close()

	return curves


def get_a(n):
	a = 2.0*ones(((n+3)/2-(n%2),), Float)
	a[0] = 1.0
	if not n % 2:
		a[-1] == 1.0

	return a/n


def eval_pos(s, n, a):
	return dot(a, cos(2*pi*s/n*array(range(len(a)), Float)))


def eval_loop(s, v, a):
	global n, S
	S = s
	n = len(v)
	b = fromfunction(lambda i, j: cos(2*pi/n*(S-i)*j), (n, len(a)))
	return matrixmultiply(matrixmultiply(b, a), v)


def refine(points):
	#~ import time
	#~ n = len(points)
	#~ a = get_a(n)
	#~ print a
	#~ s = map(lambda x: [float(x), 0.0], range(n))
	#~ s[0][1] = 1.0

	#~ now = time.time()
	#~ pos = 0
	#~ while pos < len(s):
		#~ next_pos = (pos + 1) % len(s)

		#~ if next_pos:
			#~ next_s = s[next_pos][0]
		#~ else:
			#~ next_s = len(points)

		#~ sample = (s[pos][0] + next_s)*0.5
		#~ exact = eval_pos(sample, n, a)
		#~ approx = (s[pos][1] + s[next_pos][1])*0.5
		#~ if abs(exact - approx) > 0.01:
			#~ s.insert(pos + 1, [sample, exact])
		#~ else:
			#~ pos = pos + 1
	#~ print time.time() - now
	#~ now = time.time()

	#~ p = []
	#~ for sample, pos in s:
		#~ p.append(eval_loop(sample, points, a))

	#~ print time.time() - now
	#~ return p
	p = []
	for i in range(len(points)):
		for j in range(10):
			s = j/10.0
			x = array([0.0, 0.0, 0.0])
			for k in range(-1, 3):
				m = 1.0
				for l in range(-1, 3):
					if l != k:
						m = m*(s-l)/(k-l)
				x = x + m*points[(k+i) % len(points)]
			p.append(x)
	return array(p)


class knotView:

	def __init__(self, filename, width = 640, height = 480):	
		self.knot = loadKnot(filename)

		self.colors = []
		for i in range(len(self.knot)):
			self.colors.append([random(), random(), random()])

		self.list = None
		self.phi = 0
		self.theta = 0

		min_x = [sys.maxint]*3
		max_x = [-sys.maxint]*3

		for loop in self.knot:
			for x in loop:
				min_x = map(min, min_x, x)
				max_x = map(max, max_x, x)

		center = map(lambda y, z: (y + z)*0.5, min_x, max_x)

		self.radius = 0.0

		for loop in self.knot:
#			print loop
			for x in loop:
				radius2 = 0.0
				for i in range(3):
					x[i] = x[i] - center[i]
					radius2 = radius2 + x[i]**2
				self.radius = max(self.radius, sqrt(radius2))

#		map(refine, self.knot)
		self.knot = map(refine, self.knot)

		glutInitWindowSize(width, height)
		self.win = glutCreateWindow(filename)

		glutDisplayFunc(self.onDisplay)
		glutReshapeFunc(self.onReshape)
		glutSpecialFunc(self.onSpecial)

		glClearColor(1.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glDepthFunc(GL_LESS)
		glEnable(GL_DEPTH_TEST)
		glShadeModel(GL_SMOOTH)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glEnable(GL_CULL_FACE)
	
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		gluPerspective(45.0, float(width)/max(float(height), 1.0), 0.1, 100.0)
		glTranslatef(0, 0.0, -30.0)
	
#		glEnable(GL_AUTO_NORMAL)
#		glEnable(GL_NORMALIZE)

		glMatrixMode(GL_MODELVIEW)


	def onDisplay(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glShadeModel(GL_SMOOTH)

		glLoadIdentity()
		glRotatef(self.theta, -1, 0, 0)
		glRotatef(self.phi, 0, 0, 1)

		if self.list is None:
			self.list = glGenLists(1)
			glNewList(self.list, GL_COMPILE_AND_EXECUTE)

			gleSetNumSides(50)
			gleSetJoinStyle(TUBE_JN_ANGLE | TUBE_CONTOUR_CLOSED | TUBE_NORM_PATH_EDGE )# | TUBE_NORM_FACET)

			glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
			glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, ( 1.0, 1.0, 1.0, 1.0 ))
			for i in range(len(self.knot)):
				glMaterialfv(GL_FRONT, GL_DIFFUSE, self.colors[i] + [1])
				loop = self.knot[i]
				glePolyCylinder(loop, None, self.radius/15.0)
			glEndList()
		else:
			glCallList(self.list)

		glutSwapBuffers()


	def onReshape(self, width, height):
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45.0, float(width)/max(float(height), 1.0), 0.1, 100.0)
		glTranslatef(0, 0.0, -30.0)
		glMatrixMode(GL_MODELVIEW)


	def onSpecial(self, key, x, y):
		if key == GLUT_KEY_LEFT:
			self.phi = (self.phi + 358) % 360
			glutPostRedisplay()
		elif key == GLUT_KEY_RIGHT:
			self.phi = (self.phi + 2) % 360
			glutPostRedisplay()
		elif key == GLUT_KEY_UP:
			self.theta = (self.theta + 358) % 360
			glutPostRedisplay()
		elif key == GLUT_KEY_DOWN:
			self.theta = (self.theta + 2) % 360
			glutPostRedisplay()
		
if __name__ == '__main__':
	import sys
	args = glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	views = []
	if len(args) == 1:
		args.append('8.10')                # use append()
	for file in args[1:]:                  # skip first parameter
		views.append(knotView(file))
	glutMainLoop()

