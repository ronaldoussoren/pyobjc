#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLE import *
from math import *
import maintest



SCALE = 0.8
TSCALE = 4

brand_points = map(lambda x: (0, 0, TSCALE*x), (0.1, 0.0, -5.0, -5.1))
brand_colors = ((1.0, 0.3, 0.0),)*4

points = ((-1.5, 2.0), (-0.75, 2.0), (-0.75, 1.38), (-0.5, 1.25), (0.88, 1.12), (1.0, 0.62), (1.12, 0.1), (0.5, -0.5), (0.2, -1.12),
          (0.3, -1.5), (-0.25, -1.45), (-1.06, -0.3), (-1.38, -0.3), (-1.65, -0.6), (-2.5, 0.5), (-1.5, 0.5), (-1.5, 2.0), (-0.75, 2.0))

tspine = map(lambda x: (TSCALE*x[0], TSCALE*x[1], 0), points)

texas_xsection = map(lambda x: (SCALE*x[0], SCALE*x[1]), points[1:])

tcolors = []

for i in range(len(texas_xsection)):
	tcolors.append((((i*33) % 255)/255.0, ((i*47) % 255)/255.0, ((i*89) % 255)/255.0))


texas_normal = []

for i in range(1, len(texas_xsection)):
	ax = texas_xsection[i][0] - texas_xsection[i-1][0]
	ay = texas_xsection[i][1] - texas_xsection[i-1][1]
	alen = sqrt (ax*ax + ay*ay)
	texas_normal.append((-ay / alen, ax / alen))

texas_normal.insert(0, texas_normal[-1])


def DrawStuff():
	global texas_xsection, texas_normal, tspine, tcolors, brand_points, brand_colors
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# set up some matrices so that the object spins with the mouse
	gleSetJoinStyle(TUBE_NORM_FACET | TUBE_JN_ANGLE | TUBE_CONTOUR_CLOSED | TUBE_JN_CAP)
	glPushMatrix ()
	glTranslatef (0.0, 0.0, -80.0)
	glRotatef (maintest.lastx, 0.0, 1.0, 0.0)
	glRotatef (maintest.lasty, 1.0, 0.0, 0.0)


	gleExtrusion(texas_xsection, texas_normal, None, tspine, tcolors)
	gleExtrusion(texas_xsection, texas_normal, None, brand_points, brand_colors)

	glPopMatrix ()

	glutSwapBuffers ()



maintest.main(DrawStuff)
