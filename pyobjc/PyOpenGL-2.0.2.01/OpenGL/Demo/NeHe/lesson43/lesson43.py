# NeHe Tutorial Lesson: 43 - FreeType fonts in OpenGL
#
# Ported to PyOpenGL 2.0 by Brian Leair 18 Jan 2004
#
# This code was created by Jeff Molofee 2000
#
# The port was based on the PyOpenGL tutorials and from 
# PyOpenGLContext (tests/glprint.py)
#
# If you've found this code useful, feel free to let me know 
# at (Brian Leair telcom_sage@yahoo.com).
#
# See original source and C based tutorial at http://nehe.gamedev.net
#
# Note:
# -----
# This code is not an ideal example of Pythonic coding or use of OO 
# techniques. It is a simple and direct exposition of how to use the 
# Open GL API in Python via the PyOpenGL package. It also uses GLUT, 
# a high quality platform independent library. Due to using these APIs, 
# this code is more like a C program using procedural programming.
#
# To run this example you will need:
# Python 	- www.python.org (v 2.3 as of 1/2004)
# PyOpenGL 	- pyopengl.sourceforge.net (v 2.0.1.07 as of 1/2004)
# Numeric Python	- (v.22 of "numpy" as of 1/2004) numpy.sourceforge.net
# Python Image Library	- http://www.pythonware.com/products/pil/ (v1.1.4 or later)
#
# Make sure to get versions of Numeric, PyOpenGL, and PIL to match your
# version of python.
#
#

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Imports specific to Lesson 43
import glFreeType 
from math import cos

import sys

# Python 2.2 defines these directly
try:
	True
except NameError:
	True = 1==1
	False = 1==0


# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

our_font = None

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	global our_font
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	glClearColor(0.0, 0.0, 0.0, 0.5)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glEnable(GL_TEXTURE_2D)				# Enables texture mapping
	glDepthFunc(GL_LEQUAL)				# The Type Of Depth Test To Do
	glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations

	# Currently omitting the wgl based font. See lesson13.py for example use of wgl font.
	# FYI, the ttf font file "Test.ttf" in lesson43 is the typeface "Arial Black Italic".
	# our_font = glFreeType.font_data ("ARBLI___.ttf", 16)
	our_font = glFreeType.font_data ("Test.ttf", 16)

	return True
	


# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
		Height = 1

	glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# // field of view, aspect ratio, near and far
	# This will squash and stretch our objects as the window is resized.
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

cnt1 = 0
# The main drawing function. 
def DrawGLScene():
	global cnt1
	global our_font

	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View 
	# Step back (away from objects)
	glTranslatef (0.0, 0.0, -1.0)

	# Currently - NYI - No WGL text
	# Blue Text
	# glColor3ub(0, 0, 0xff)
	#
	# // Position The WGL Text On The Screen
	# glRasterPos2f(-0.40f, 0.35f);
	# glPrint("Active WGL Bitmap Text With NeHe - %7.2f", cnt1);	

	# Red Text
	glColor3ub (0xff, 0, 0)

	glPushMatrix ()
	glLoadIdentity ()
	# Spin the text, rotation around z axe == will appears as a 2d rotation of the text on our screen
	glRotatef (cnt1, 0, 0, 1)
	glScalef (1, 0.8 + 0.3* cos (cnt1/5), 1)
	glTranslatef (-180, 0, 0)
	our_font.glPrint (320, 240, "Active FreeType Text - %7.2f" % (cnt1))
	glPopMatrix ()

	# //Uncomment this to test out print's ability to handle newlines.
	# our_font.glPrint (320, 240, "Here\nthere\nbe\n\nnewlines %f\n." % (cnt1))

	cnt1 += 0.051
	# cnt2 += 0.005

	glutSwapBuffers()
	return


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global window
	global our_font
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		our_font.release ()
		sys.exit()

def main():
	global window
	# pass arguments to init
	glutInit(sys.argv)

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	
	# get a 640 x 480 window 
	glutInitWindowSize(640, 480)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(0, 0)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("NeHe & Sven Olsen's TrueType Font Tutorial")

	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc(DrawGLScene)
	
	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)
	
	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)
	
	# Register the function called when the keyboard is pressed.  
	glutKeyboardFunc(keyPressed)

	# Initialize our window. 
	InitGL(640, 480)

	# Start Event Processing Engine	
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
	print "Hit ESC key to quit."
	main()
