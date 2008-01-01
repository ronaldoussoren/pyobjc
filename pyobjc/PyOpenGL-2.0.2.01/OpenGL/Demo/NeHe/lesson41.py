# NeHe Tutorial Lesson: 41 - Volumetric Fog
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
# This code is not an ideal example of Pythonic coding or use of OO techniques.  
# It is a simple and direct exposition of how to use the Open GL API in 
# Python via the PyOpenGL package. It also uses GLUT, a high quality 
# platform independent library. Due to using these APIs, this code is 
# more like a C program using procedural based programming.
#
# To run this example you will need:
# Python 	- www.python.org (v 2.3 as of 1/2004)
# PyOpenGL 	- pyopengl.sourceforge.net (v 2.0.1.07 as of 1/2004)
# Numeric Python	- (v.22 of "numpy" as of 1/2004) numpy.sourceforge.net
# Python Image Library	- http://www.pythonware.com/products/pil/
#
# Make sure to get versions of Numeric, PyOpenGL, and PIL to match your
# version of python.
#
#
#
#
# Topics demonstrated in this tutorial:
#	using PIL (Python Image Library) to load a texture from an image file 
# 		(see doc - http://www.pythonware.com/library/pil/handbook/index.htm)
#	accessing the extension FOG_COORDINATE_EXTENSION
# 		(see doc - http://pyopengl.sourceforge.net/documentation/opengl_diffs.html)
#

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Image 				# PIL
import sys
from OpenGL.GL.EXT.fog_coord import *



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
fogColor = (0.6, 0.3, 0.0, 1.0);								# // Fog Colour 
camz = None														# // Camera Z Depth
lastTickCount = 0.0

texture = None

def next_p2 (num):
	""" If num isn't a power of 2, will return the next higher power of two """
	rval = 1
	while (rval<num):
		rval <<= 1
	return rval


def BuildTexture (path):
	""" // Load Image And Convert To A Texture
	path can be a relative path, or a fully qualified path.
	returns False if the requested image couldn't loaded as a texture
	returns True and the texture ID if image was loaded
	"""
	# Catch exception here if image file couldn't be loaded
	try:
		# Note, NYI, path specified as URL's could be access using python url lib
		# OleLoadPicturePath () supports url paths, but that capability isn't critcial to this tutorial.
		Picture = Image.open (path)
	except:
		print "Unable to open image file '%s'." % (path)
		return False, 0

	glMaxTexDim = glGetIntegerv (GL_MAX_TEXTURE_SIZE)

	WidthPixels = Picture.size [0]
	HeightPixels = Picture.size [1]

	if ((WidthPixels > glMaxTexDim) or (HeightPixels > glMaxTexDim)):
		# The image file is too large. Shrink it to fit within the texture dimensions
		# support by our rendering context for a GL texture.
		# Note, Feel free to experiemnt and force a resize by placing a small val into
		# glMaxTexDim (e.g. 32,64,128).
		if (WidthPixels > HeightPixels):
			# Width is the domainant dimension.
			resizeWidthPixels = glMaxTexDim
			squash = float (resizeWidthPixels) / float (WidthPixels)
			resizeHeightPixels = int (HeighPixels * squash)
		else:
			resizeHeightPixels = glMaxTexDim
			squash = float (resizeHeightPixels) / float (HeightPixels)
			resizeWidthPixels = int (WidthPixels * squash)
	else:
		# // Resize Image To Closest Power Of Two
		if (WidthPixels > HeightPixels):
			# Width is the domainant dimension.
			resizeWidthPixels = next_p2 (WidthPixels)
			squash = float (resizeWidthPixels) / float (WidthPixels)
			resizeHeightPixels = int (HeighPixels * squash)
		else:
			resizeHeightPixels = next_p2 (HeightPixels)
			squash = float (resizeHeightPixels) / float (HeightPixels)
			resizeWidthPixels = int (WidthPixels * squash)
		# 
	# Resize the image to be used as a texture.
	# The Python image library provides a handy method resize (). 
	# Several filtering options are available.
	# If you don't specify a filtering option will default NEAREST
	Picture = Picture.resize ((resizeWidthPixels, resizeHeightPixels), Image.BICUBIC)
	lWidthPixels = next_p2 (resizeWidthPixels)
	lHeightPixels = next_p2 (resizeWidthPixels)
	# Now we create an image that has the padding needed
	newpicture = Image.new ("RGB", (lWidthPixels, lHeightPixels), (0, 0, 0))
	newpicture.paste (Picture)

	# Create a raw string from the image data - data will be unsigned bytes
	# RGBpad, no stride (0), and first line is top of image (-1)
	pBits = newpicture.tostring("raw", "RGBX", 0, -1)

	# // Typical Texture Generation Using Data From The Bitmap
	texid = glGenTextures(1);											# // Create The Texture
	glBindTexture(GL_TEXTURE_2D, texid);								# // Bind To The Texture ID
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);		# // (Modify This For The Type Of Filtering You Want)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);     # // (Modify This For The Type Of Filtering You Want)

	# // (Modify This If You Want Mipmaps)
	glTexImage2D(GL_TEXTURE_2D, 0, 3, lWidthPixels, lHeightPixels, 0, GL_RGBA, GL_UNSIGNED_BYTE, pBits);

	# Cleanup (python actually handles all memory for you, so this isn't necessary)
	# // Decrements IPicture Reference Count
	Picture = None
	newpicture = None
	return True, texid					# // Return True (All Good)


def Extension_Init ():
	""" Determine if the fog coord extentsion is availble """

	# After calling this, we will be able to invoke glFogCoordEXT ()
	if (not glInitFogCoordEXT ()):
		print "Help!  No GL_EXT_ForCoord"
		sys.exit(1)
		return False
	return True

# // Any GL Init Code & User Initialiazation Goes Here
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	global fogColor
	global camz

	if (not Extension_Init ()):			# // Check And Enable Fog Extension If Available
		return False;					# // Return False If Extension Not Supported

	if (not BuildTexture("wall.bmp")):						# // Load The Wall Texture
		return False;											# // Return False If Loading Failed

	glEnable(GL_TEXTURE_2D);									# // Enable Texture Mapping
	glClearColor (0.0, 0.0, 0.0, 0.5);							# // Black Background
	glClearDepth (1.0);											# // Depth Buffer Setup
	glDepthFunc (GL_LEQUAL);									# // The Type Of Depth Testing
	glEnable (GL_DEPTH_TEST);									# // Enable Depth Testing
	glShadeModel (GL_SMOOTH);									# // Select Smooth Shading
	glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);			# // Set Perspective Calculations To Most Accurate

	# // Set Up Fog 
	glEnable(GL_FOG);											# // Enable Fog
	glFogi(GL_FOG_MODE, GL_LINEAR);								# // Fog Fade Is Linear
	glFogfv(GL_FOG_COLOR, fogColor);							# // Set The Fog Color
	glFogf(GL_FOG_START,  0.0);									# // Set The Fog Start
	glFogf(GL_FOG_END,    1.0);									# // Set The Fog End
	glHint(GL_FOG_HINT, GL_NICEST);								# // Per-Pixel Fog Calculation
	glFogi(GL_FOG_COORDINATE_SOURCE_EXT, GL_FOG_COORDINATE_EXT) # // Set Fog Based On Vertice Coordinates

	camz =	-19.0;												# // Set Camera Z Position To -19.0f

	return True;												# // Return TRUE (Initialization Successful)


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


# The main drawing function. 
def DrawGLScene():
	global camz

	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);				# // Clear Screen And Depth Buffer
	glLoadIdentity ();													# // Reset The Modelview Matrix

	glTranslatef(0.0, 0.0, camz);										# // Move To Our Camera Z Position

	glBegin(GL_QUADS);													# // Back Wall
	glFogCoordfEXT( 1.0);	glTexCoord2f(0.0, 0.0);	glVertex3f(-2.5,-2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 0.0);	glVertex3f( 2.5,-2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 1.0);	glVertex3f( 2.5, 2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(0.0, 1.0);	glVertex3f(-2.5, 2.5,-15.0);
	# PyOpenGL 2.0.1.07 has a bug. Swig generated code for FogCoordfExt ()
	# uses wrong error check macro. Macro falsely sets exception due to
	# call during glBegin (). Fixed in later versions.
	try:
		glEnd();
	except:
		pass

	glBegin(GL_QUADS);													# // Floor
	glFogCoordfEXT( 1.0);	glTexCoord2f(0.0, 0.0);	glVertex3f(-2.5,-2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 0.0);	glVertex3f( 2.5,-2.5,-15.0);
	glFogCoordfEXT( 0.0);	glTexCoord2f(1.0, 1.0);	glVertex3f( 2.5,-2.5, 15.0);
	glFogCoordfEXT( 0.0);	glTexCoord2f(0.0, 1.0);	glVertex3f(-2.5,-2.5, 15.0);
	try:
		glEnd();
	except:
		pass

	glBegin(GL_QUADS);													# // Roof
	glFogCoordfEXT( 1.0);	glTexCoord2f(0.0, 0.0);	glVertex3f(-2.5, 2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 0.0);	glVertex3f( 2.5, 2.5,-15.0);
	glFogCoordfEXT( 0.0);	glTexCoord2f(1.0, 1.0);	glVertex3f( 2.5, 2.5, 15.0);
	glFogCoordfEXT( 0.0);	glTexCoord2f(0.0, 1.0);	glVertex3f(-2.5, 2.5, 15.0);
	try:
		glEnd();
	except:
		pass

	glBegin(GL_QUADS);													# // Right Wall
	glFogCoordfEXT( 0.0);	glTexCoord2f(0.0, 0.0);	glVertex3f( 2.5,-2.5, 15.0);
	glFogCoordfEXT( 0.0);	glTexCoord2f(0.0, 1.0);	glVertex3f( 2.5, 2.5, 15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 1.0);	glVertex3f( 2.5, 2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 0.0);	glVertex3f( 2.5,-2.5,-15.0);
	try:
		glEnd();
	except:
		pass

	glBegin(GL_QUADS);													# // Left Wall
	glFogCoordfEXT( 0.0);	glTexCoord2f(0.0, 0.0);	glVertex3f(-2.5,-2.5, 15.0);
	glFogCoordfEXT( 0.0);	glTexCoord2f(0.0, 1.0);	glVertex3f(-2.5, 2.5, 15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 1.0);	glVertex3f(-2.5, 2.5,-15.0);
	glFogCoordfEXT( 1.0);	glTexCoord2f(1.0, 0.0);	glVertex3f(-2.5,-2.5,-15.0);
	try:
		glEnd();
	except:
		pass

	glutSwapBuffers()													 # // Flush The GL Rendering Pipeline
	return True


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global window
	global camz
	global lastTickCount

	tickCount = glutGet (GLUT_ELAPSED_TIME)
	milliseconds = (tickCount - lastTickCount) 
	lastTickCount = tickCount
	if (milliseconds > 200):
		lastTickCount = tickCount
		milliseconds = 20

	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit ()
	if ((args[0] == GLUT_KEY_UP) and (camz < 14.0)):
			camz += milliseconds / 100.0 		# // Move Object Closer (Move Forwards Through Hallway)
	if (args[0] == GLUT_KEY_DOWN and camz > -19.0):
			camz -= milliseconds / 100.0 		# // Move Object Closer (Move Backwards Through Hallway)

	return

def main():
	global window, lastTickCount

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
	window = glutCreateWindow("NeHe's Volumetric Fog & IPicture Image Loading Tutorial")

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
	# The call setup glutSpecialFunc () is needed to receive 
	# "keyboard function or directional keys." 
	glutKeyboardFunc(keyPressed)
	glutSpecialFunc(keyPressed)

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
