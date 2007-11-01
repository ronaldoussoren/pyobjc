#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

import string
__version__ = string.split('$Revision: 1.7 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/30 19:17:17 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

try:
	from Numeric import *
except:
	print "This demo requires the Numeric extension, sorry"
	import sys
	sys.exit()
from RandomArray import *
import string, sys
from OpenGL.GL import *
from OpenGL.GLUT import *

MY_LIST=1
NUMDOTS = 500
NUMDOTS2 = 600
x = random(NUMDOTS)*2-1
y = random(NUMDOTS)*2-1
MAX_AGE = 13
age = randint(0,MAX_AGE,(NUMDOTS,))
move_length = .005  # 1.0 = screen width
angle = 0		  # in radians
delta_angle = .2  # in radians
move_x = move_length*cos(angle)
move_y = move_length*sin(angle)
halted = 0

def display(*args):
	global x, y, move_x, move_y, NUMDOTS, NUMDOTS2, MAX_AGE, age
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,0.0)
	x = x + move_x
	y = y + move_y
	age = age + 1
	which = greater(age, MAX_AGE)
	x = choose(which, (x, random(NUMDOTS)))
	y = choose(which, (y, random(NUMDOTS)))
	age = choose(which, (age, 0))
	x = choose(greater(x,1.0),(x,x-1.0))  # very cool - wraparound
	y = choose(greater(y,1.0),(y,y-1.0))
	x2 = random(NUMDOTS2)
	y2 = random(NUMDOTS2)
	v = concatenate((transpose(array([x,y])), transpose(array([x-.005,y+.005])), transpose(array([x+.005,y-.005])), transpose(array([x2,y2]))))
	glVertexPointerd(v)
	glEnableClientState(GL_VERTEX_ARRAY)
	glDrawArrays(GL_POINTS, 0, len(v))
	glDisableClientState(GL_VERTEX_ARRAY)
#	glVertexPointer(2, GL_FLOAT, None)
	glFlush()
	glutSwapBuffers()


def halt():
	pass

def keyboard(*args):
	sys.exit()

def mouse(button, state, x, y):
	global angle, delta_angle, move_x, move_y, move_length, halted
	if button == GLUT_LEFT_BUTTON:
		angle = angle + delta_angle
	elif button == GLUT_RIGHT_BUTTON:
		angle = angle - delta_angle
	elif button == GLUT_MIDDLE_BUTTON and state == GLUT_DOWN:
		if halted:
			glutIdleFunc(display)
			halted = 0
		else:
			glutIdleFunc(halt)
			halted = 1
	move_x = move_length * cos(angle)
	move_y = move_length * sin(angle)

def setup_viewport():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, 1.0, 0.0, 1.0, 0.0, 1.0)

def reshape(w, h):
	glViewport(0, 0, w, h)
	setup_viewport()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(300, 300)
	glutCreateWindow('Dots')
	setup_viewport()
	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutIdleFunc(display)
	glutMouseFunc(mouse)
	glutKeyboardFunc(keyboard)
	glutMainLoop()

print "Use the mouse buttons to control some of the dots."
print "Hit any key to quit."
main()



