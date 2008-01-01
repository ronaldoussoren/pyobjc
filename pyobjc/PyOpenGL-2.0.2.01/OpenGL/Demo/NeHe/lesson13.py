#!


#
# Ported to PyOpenGL 2.0 by Brian Leair 18 Jan 2004
#
# This code was created by Jeff Molofee 2000
#
# The port was based on the PyOpenGL tutorial and from the PyOpenGLContext (tests/glprint.py)
#
# If you've found this code useful, please let me know (email Brian Leair at telcom_sage@yahoo.com).
#
# See original source and C based tutorial at http://nehe.gamedev.net
#
# Note:
# -----
# This code is not a good example of Python and using OO techniques.  It is a simple and direct
# exposition of how to use the Open GL API in Python via the PyOpenGL package.  It also uses GLUT,
# which in my opinion is a high quality library in that it makes my work simpler.  Due to using
# these APIs, this code is more like a C program using function based programming (which Python
# is in fact based upon, note the use of closures and lambda) than a "good" OO program.
#
# To run this code get and install OpenGL, GLUT, PyOpenGL (see http://www.python.org), and PyNumeric.
# Installing PyNumeric means having a C compiler that is configured properly, or so I found.  For 
# Win32 this assumes VC++, I poked through the setup.py for Numeric, and chased through disutils code
# and noticed what seemed to be hard coded preferences for VC++ in the case of a Win32 OS.
#
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.WGL import *	# wglUseFontBitmaps (), wglGetCurrentDC ()
import win32ui				# CreateFont (), CreateDCFromHandle ()
# import Numeric
from math import cos, sin
import sys


# *********************** Globals *********************** 
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
base = None


def BuildFont ():
	global base

	wgldc = wglGetCurrentDC ()
	hDC = win32ui.CreateDCFromHandle (wgldc)


	base = glGenLists(32+96);					# // Storage For 96 Characters, plus 32 at the start...

	# CreateFont () takes a python dictionary to specify the requested font properties. 
	font_properties = { "name" : "Courier New",
						"width" : 0 ,
						"height" : -24,
						"weight" : 800
						}
	font = win32ui.CreateFont (font_properties)
	# // Selects The Font We Want
	oldfont = hDC.SelectObject (font)
	# // Builds 96 Characters Starting At Character 32
	wglUseFontBitmaps (wgldc, 32, 96, base+32)
	# // reset the font
	hDC.SelectObject (oldfont)
	# // Delete The Font (python will cleanup font for us...)
	return

def KillFont ():
	""" // Delete The Font List
	"""
	global	base
	# // Delete All 96 Characters
	glDeleteLists (base, 32+96)
	return


def glPrint (str):
	""" // Custom GL "Print" Routine
	"""
	global base
	# // If THere's No Text Do Nothing
	if (str == None):
		return
	if (str == ""):
		return
	glPushAttrib(GL_LIST_BIT);							# // Pushes The Display List Bits
	try:
		glListBase(base);								# // Sets The Base Character to 32
		glCallLists(str)									# // Draws The Display List Text
	finally:
		glPopAttrib();										# // Pops The Display List Bits
	return


# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	glClearColor(0.0, 0.0, 0.0, 0.5)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glDepthFunc(GL_LEQUAL)				# The Type Of Depth Test To Do
	glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations

	BuildFont ()
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
cnt2 = 0
# The main drawing function. 
def DrawGLScene():
	global cnt1
	global cnt2

	# // Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	glLoadIdentity()					# // Reset The Current Modelview Matrix
	glTranslatef (0.0, 0.0, -1.0)		# // Move One Unit Into The Screen

	# // Pulsing Colors Based On Text Position
	glColor3f (1.0 * cos (cnt1), 1.0 * sin (cnt2), 1.0 -0.5 * cos (cnt1+cnt2))
	# // Position The Text On The Screen
	glRasterPos2f(-0.45+0.05* cos(cnt1), 0.32*sin(cnt2));
 	glPrint("Active OpenGL Text With NeHe - %7.2f" %(cnt1));	# // Print GL Text To The Screen
	cnt1+=0.051;										# // Increase The First Counter
	cnt2+=0.005;										# // Increase The First Counter
	glutSwapBuffers()
	return True


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global window
	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		KillFont ()
		sys.exit ()

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
	# to Python, remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("NeHe's Bitmap Font Tutorial")

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

	# We've told Glut the type of window we want, and we've told glut about
	# various functions that we want invoked (idle, resizing, keyboard events).
	# Glut has done the hard work of building up thw windows DC context and 
	# tying in a rendering context, so we are ready to start making immediate mode
	# GL calls.
	# Call to perform inital GL setup (the clear colors, enabling modes, and most releveant -
	# consturct the displays lists for the bitmap font.
	InitGL(640, 480)

	# Start Event Processing Engine	
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
	print "Hit ESC key to quit."
	main()

