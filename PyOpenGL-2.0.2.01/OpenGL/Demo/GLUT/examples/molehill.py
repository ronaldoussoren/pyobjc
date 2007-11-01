#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

import string
__version__ = string.split('$Revision: 1.10 $')[1]
__date__ = string.join(string.split('$Date: 2002/12/31 04:13:56 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

#
# Ported to PyOpenGL 2.0 by Tarn Weisner Burton 10May2001

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glCallList(1)
	glutSwapBuffers()


def main():
	mat_red_diffuse = ( 0.7, 0.0, 0.1, 1.0 )
	mat_green_diffuse = ( 0.0, 0.7, 0.1, 1.0 )
	mat_blue_diffuse = ( 0.0, 0.1, 0.7, 1.0 )
	mat_yellow_diffuse = ( 0.7, 0.8, 0.1, 1.0 )
	mat_specular = ( 1.0, 1.0, 1.0, 1.0 )
	mat_shininess = 100.0
	knots = ( 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0 )

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow('molehill')

	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_AUTO_NORMAL)
	glEnable(GL_NORMALIZE)

	nurb = gluNewNurbsRenderer()
	# get a really good sampling
	gluNurbsProperty(nurb, GLU_SAMPLING_TOLERANCE, 5.0)
	gluNurbsProperty(nurb, GLU_DISPLAY_MODE, GLU_FILL)

	# Build control points for NURBS mole hills. 
	pts1 = []
	pts2 = []
	pts3 = []
	pts4 = []

	for u in range(4):
		pts1.append([])
		pts2.append([])
		pts3.append([])
		pts4.append([])
		for v in range(4):
			# Red. 
			pts1[u].append([2.0*u, 2.0*v, 0.0])
			if (u == 1 or u == 2) and (v == 1 or v == 2):
				pts1[u][v][2] = 6.0
	
			# Green. 
			pts2[u].append([2.0*u - 6.0, 2.0*v - 6.0, 0.0])
			if (u == 1 or u == 2) and (v == 1 or v == 2):
				if u == 1 and v == 1: 
					# Pull hard on single middle square. 
					pts2[u][v][2] = 15.0
				else:
					# Push down on other middle squares. 
					pts2[u][v][2] = -2.0
	
			# Blue.
			pts3[u].append([2.0*u - 6.0, 2.0*v, 0.0])
			if (u == 1 or u == 2) and (v == 1 or v == 2):
				if u == 1 and v == 2: 
					# Pull up on single middple square. 
					pts3[u][v][2] = 11.0
				else:
					# Pull up slightly on other middle squares.
					pts3[u][v][2] = 2.0
	
			# Yellow. 
			pts4[u].append([2.0*u, 2.0*v - 6.0, 0.0])
			if u != 0 and (v == 1 or v == 2):
				if v == 1: 
					# Push down front middle and right squares. 
					pts4[u][v][2] = -2.0
				else:
					# Pull up back middle and right squares. 
					pts4[u][v][2] = 5.0
	

	# Stretch up red's far right corner. 
	pts1[3][3][2] = 6.0
	# Pull down green's near left corner a little. 
	pts2[0][0][2] = -2.0
	# Turn up meeting of four corners. 
	pts1[0][0][2] = 1.0
	pts2[3][3][2] = 1.0
	pts3[3][0][2] = 1.0
	pts4[0][3][2] = 1.0
	
	glMatrixMode(GL_PROJECTION)
	gluPerspective(55.0, 1.0, 2.0, 24.0)
	glMatrixMode(GL_MODELVIEW)
	glTranslatef(0.0, 0.0, -15.0)
	glRotatef(330.0, 1.0, 0.0, 0.0)
	
	glNewList(1, GL_COMPILE)

	# Render red hill. 
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_red_diffuse)
	gluBeginSurface(nurb)
	gluNurbsSurface(nurb, knots, knots, pts1, GL_MAP2_VERTEX_3)
	gluEndSurface(nurb)

	# Render green hill. 
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_green_diffuse)
	gluBeginSurface(nurb)
	gluNurbsSurface(nurb, knots, knots, pts2, GL_MAP2_VERTEX_3)
	gluEndSurface(nurb)

	# Render blue hill. 
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_blue_diffuse)
	gluBeginSurface(nurb)
	gluNurbsSurface(nurb, knots, knots, pts3, GL_MAP2_VERTEX_3)
	gluEndSurface(nurb)

	# Render yellow hill. 
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_yellow_diffuse)
	gluBeginSurface(nurb)
	gluNurbsSurface(nurb, knots, knots, pts4, GL_MAP2_VERTEX_3)
	gluEndSurface(nurb)
	glEndList()

	glutDisplayFunc(display)


if __name__ == '__main__':
	try:
		GLU_VERSION_1_2
	except:
		print "Need GLU 1.2 to run this demo"
		sys.exit(1)
	main()
	glutMainLoop()

