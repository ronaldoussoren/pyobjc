# NeHe Tutorial Lesson: 44 - Lense Flare
#
# Ported to PyOpenGL 2.0 by Brian Leair 2004
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
# Python Image Library	- http://www.pythonware.com/products/pil/
#
# #########################################################
# Please note, don't use PyOpenGL older than 2.0.1.07.
# Older PyOpenGL had a bug glGetFloat () that prevents this 
# tutorial from working.
#
#


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Image					# PIL
try:
	import win32api				# GetTickCount ()
	gHaveWin32 = 1
except:
	gHaveWin32 = 0
import sys
import time						# clock ()
import os

from glCamera import *
from glFont import *


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

gInfoOn = False
gFrames = 0
gStartTime = -1
gCurrentTime = -1
gFPS = -1
gCamera = None

# //##################  NEW STUFF  ##################################

qobj = None					# //the quadric for our cylinder
gcylList = None


def LoadTexture (path):
	""" // Load Image And Convert To A Texture
	path can be a relative path, or a fully qualified path.
	returns tuple of status and ID:
	returns False if the requested image couldn't loaded as a texture
	returns True and the texture ID if image was loaded
	"""
	# Catch exception here if image file couldn't be loaded
	try:
		# Note, NYI, path specified as URL's could be access using python url lib
		# OleLoadPicturePath () supports url paths, but that capability isn't critcial to this tutorial.
		Picture = Image.open (path)
	except:
		return False, 0

	glMaxTexDim = glGetIntegerv (GL_MAX_TEXTURE_SIZE)

	WidthPixels = Picture.size [0]
	HeightPixels = Picture.size [1]

	if ((WidthPixels > glMaxTexDim) or (HeightPixels > glMaxTexDim)):
		# The image file is too large. Shrink it to fit within the texture dimensions
		# support by our rendering context for a GL texture.
		# Note, Feel free to experiemnt and force a resize by placing a small val into
		# glMaxTexDim (e.g. 32,64,128).
		raise RuntimeError, "Texture image (%d by %d) is larger than supported by GL %d." % (WidthPixels, HeightPixels, glMaxTexDim)

	# Create a raw string from the image data - data will be unsigned bytes
	# RGBpad, no stride (0), and first line is top of image (-1)
	pBits = Picture.tostring("raw", "RGBX", 0, -1)

	# // Typical Texture Generation Using Data From The Bitmap
	texid = glGenTextures(1);											# // Create The Texture
	glBindTexture(GL_TEXTURE_2D, texid);								# // Bind To The Texture ID
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);		# // (Modify This For The Type Of Filtering You Want)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);     # // (Modify This For The Type Of Filtering You Want)

	# // (Modify This If You Want Mipmaps)
	glTexImage2D(GL_TEXTURE_2D, 0, 3, WidthPixels, HeightPixels, 0, GL_RGBA, GL_UNSIGNED_BYTE, pBits);

	# Cleanup (this would all happen automatically upon return... just spelling it out)
	# // Decrements IPicture Reference Count
	Picture = None
	return True, texid					# // Return True (All Good)







# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	global gFont, gCamera, gStartTime, gcylList, qobj

	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	glClearColor(0.0, 0.0, 0.0, 0.5)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glDepthFunc(GL_LEQUAL)				# The Type Of Depth Test To Do
	glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations

	status, tex = LoadTexture (os.path.join("Art","Font.bmp"))
	if (status):
		gFont = glFont ()
		gFont.SetFontTexture (tex)
		gFont.SetWindowSize (1024, 768)
		gFont.BuildFont (1.0)
	else:
		raise RuntimeError, "Failed to build font 'Art\\Font.bmp'"


	gCamera = glCamera ()
	gCamera.m_MaxHeadingRate = 1.0;			# // Set our Maximum rates for the camera
	gCamera.m_MaxPitchRate = 1.0;			# // Set our Maximum rates for the camera
	gCamera.m_HeadingDegrees = 0.0;			# // Set our Maximum rates for the camera

	# // Try and load the HardGlow texture tell the user if we can't find it then quit
	status, gCamera.m_GlowTexture = LoadTexture(os.path.join("Art","HardGlow2.bmp"));
	if (not status):
		raise RuntimeError, "Failed to load Hard Glow texture."

	# // Try and load the BigGlow texture tell the user if we can't find it then quit
	status, gCamera.m_BigGlowTexture = LoadTexture(os.path.join("Art","BigGlow3.bmp"))
	if (not status):
		raise RuntimeError, "Failed to load Big Glow texture."

	# // Try and load the Halo texture tell the user if we can't find it then quit
	status, gCamera.m_HaloTexture = LoadTexture(os.path.join("Art","Halo3.bmp"))
	if (not status):
		raise RuntimeError, "Failed to load Halo texture."
	
	# // Try and load the Streaks texture tell the user if we can't find it then quit
	status, gCamera.m_StreakTexture = LoadTexture(os.path.join("Art","Streaks4.bmp"))
	if (not status):
		raise RuntimeError, "Failed to load Streaks texture."

	# //##################  NEW STUFF  ##################################

	# // Just create a cylinder that will be used as occluder object
	gcylList = glGenLists(1);
	qobj = gluNewQuadric();
	gluQuadricDrawStyle(qobj, GLU_FILL); 
	gluQuadricNormals(qobj, GLU_SMOOTH);
	glNewList(gcylList, GL_COMPILE);
	# List Start
	glEnable(GL_COLOR_MATERIAL);
	glColor3f(0.0, 0.0, 1.0);
	glEnable(GL_LIGHT0);
	glEnable(GL_LIGHTING);
	glTranslatef(0.0,0.0,-2.0);
	gluCylinder(qobj, 0.5, 0.5, 4.0, 15, 5);
	glDisable(GL_LIGHTING);
	glDisable(GL_LIGHT0);
	glDisable(GL_COLOR_MATERIAL);
	glEndList();
	# List End

	# if (gHaveWin32):
	#	gStartTime = win32api.GetTickCount () 	# // Get the time the app started
	gStartTime = time.clock ();				 	# // Get the time the app started

	return True									# // Initialization Went OK
	

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
		Height = 1

	glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# // field of view, aspect ratio, near and far
	# This will squash and stretch our objects as the window is resized.
	# Note that the near clip plane is 1 (hither) and the far plane is 1000 (yon)
	gluPerspective(45.0, float(Width)/float(Height), 1, 1000.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def DrawGLInfo ():
	global gCamera, gFont, gFrames, gCurrentTime, gCurrentTime, gStartTime, gFPS

	projMatrix = glGetFloatv(GL_PROJECTION_MATRIX);					# // Grab the projection matrix
	modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX);				# // Grab the modelview matrix

	# // Print out the cameras position
	glColor4f(1.0, 1.0, 1.0, 1.0);
	String = "m_Position............. = %.02f, %.02f, %.02f" % (gCamera.m_Position.x, gCamera.m_Position.y, gCamera.m_Position.z)
	gFont.glPrintf(10, 720, 1, String);
	
	# // Print out the cameras direction
	String = "m_DirectionVector...... = %.02f, %.02f, %.02f" % (gCamera.m_DirectionVector.i, gCamera.m_DirectionVector.j, gCamera.m_DirectionVector.k);
	gFont.glPrintf(10, 700, 1, String);
	
	# // Print out the light sources position
	String = "m_LightSourcePos....... = %.02f, %.02f, %.02f" % (gCamera.m_LightSourcePos.x, gCamera.m_LightSourcePos.y, gCamera.m_LightSourcePos.z);
	gFont.glPrintf(10, 680, 1, String);

	# // Print out the intersection point
	String = "ptIntersect............ = %.02f, %.02f, %.02f" % (gCamera.m_ptIntersect.x, gCamera.m_ptIntersect.y, gCamera.m_ptIntersect.z);
	gFont.glPrintf(10, 660, 1, String);

	# // Print out the vector that points from the light source to the camera
	String = "vLightSourceToCamera... = %.02f, %.02f, %.02f" % (gCamera.vLightSourceToCamera.i, gCamera.vLightSourceToCamera.j, gCamera.vLightSourceToCamera.k);
	gFont.glPrintf(10, 640, 1, String);

	# // Print out the vector that points from the light source to the intersection point.
	String = "vLightSourceToIntersect = %.02f, %.02f, %.02f" % (gCamera.vLightSourceToIntersect.i, gCamera.vLightSourceToIntersect.j, gCamera.vLightSourceToIntersect.k);
	gFont.glPrintf(10, 620, 1, String);

	# // Let everyone know the below matrix is the model view matrix
	String = "GL_MODELVIEW_MATRIX";
	gFont.glPrintf(10, 580, 1, String);
	
	# // Print out row 1 of the model view matrix
	String = "%.02f, %.02f, %.02f, %.02f" % (modelMatrix[0][0], modelMatrix[0][1], modelMatrix[0][2], modelMatrix[0][3]);
	gFont.glPrintf(10, 560, 1, String);

	# // Print out row 2 of the model view matrix
	String = "%.02f, %.02f, %.02f, %.02f" % (modelMatrix[1][0], modelMatrix[1][1], modelMatrix[1][2], modelMatrix[1][3]);
	gFont.glPrintf(10, 540, 1, String);

	# // Print out row 3 of the model view matrix
	String = "%.02f, %.02f, %.02f, %.02f" % (modelMatrix[2][0], modelMatrix[2][1], modelMatrix[2][2], modelMatrix[2][3]);
	gFont.glPrintf(10, 520, 1, String);

	# // Print out row 4 of the model view matrix
	String = "%.02f, %.02f, %.02f, %.02f" % (modelMatrix[3][0], modelMatrix[3][1], modelMatrix[3][2], modelMatrix[3][3]);
	gFont.glPrintf(10, 500, 1, String);

	# // Let everyone know the below matrix is the projection matrix
	String = "GL_PROJECTION_MATRIX";
	gFont.glPrintf(10, 460, 1, String);
	
	# // Print out row 1 of the projection view matrix
	String = "%.02f, %.02f, %.02f, %.02f" % (projMatrix[0][0], projMatrix[0][1], projMatrix[0][2], projMatrix[0][3]);
	gFont.glPrintf(10, 440, 1, String);

	# // Print out row 2 of the projection view matrix
	String = "%.02f, %.02f, %.02f, %.02f" % (projMatrix[1][0], projMatrix[1][1], projMatrix[1][2], projMatrix[1][3]);
	gFont.glPrintf(10, 420, 1, String);

	# // Print out row 3 of the projection view matrix
	String = "%.02f, %.02f, %.03f, %.03f" % (projMatrix[2][0], projMatrix[2][1], projMatrix[2][2], projMatrix[2][3]);
	gFont.glPrintf(10, 400, 1, String);

	# // Print out row 4 of the projection view matrix
	String = "%.02f, %.02f, %.03f, %.03f" % (projMatrix[3][0], projMatrix[3][1], projMatrix[3][2], projMatrix[3][3]);
	gFont.glPrintf(10, 380, 1, String);

	# // Let everyone know the below values are the Frustum clipping planes
	gFont.glPrintf(10, 320, 1, "FRUSTUM CLIPPING PLANES");

	# // Print out the right clipping plane
	String = "%.02f, %.02f, %.02f, %.02f" % (gCamera.m_Frustum[0][0], gCamera.m_Frustum[0][1], gCamera.m_Frustum[0][2], gCamera.m_Frustum[0][3]);
	gFont.glPrintf(10, 300, 1, String);

	# // Print out the left clipping plane
	String = "%.02f, %.02f, %.02f, %.02f" % (gCamera.m_Frustum[1][0], gCamera.m_Frustum[1][1], gCamera.m_Frustum[1][2], gCamera.m_Frustum[1][3]);
	gFont.glPrintf(10, 280, 1, String);

	# // Print out the bottom clipping plane
	String = "%.02f, %.02f, %.02f, %.02f" % (gCamera.m_Frustum[2][0], gCamera.m_Frustum[2][1], gCamera.m_Frustum[2][2], gCamera.m_Frustum[2][3]);
	gFont.glPrintf(10, 260, 1, String);

	# // Print out the top clipping plane
	String = "%.02f, %.02f, %.02f, %.02f" % (gCamera.m_Frustum[3][0], gCamera.m_Frustum[3][1], gCamera.m_Frustum[3][2], gCamera.m_Frustum[3][3]);
	gFont.glPrintf(10, 240, 1, String);

	# // Print out the far clipping plane
	String = "%.02f, %.02f, %.02f, %.02f" % (gCamera.m_Frustum[4][0], gCamera.m_Frustum[4][1], gCamera.m_Frustum[4][2], gCamera.m_Frustum[4][3]);
	gFont.glPrintf(10, 220, 1, String);

	# // Print out the near clipping plane
	String = "%.02f, %.02f, %.02f, %.02f" % (gCamera.m_Frustum[5][0], gCamera.m_Frustum[5][1], gCamera.m_Frustum[5][2], gCamera.m_Frustum[5][3]);
	gFont.glPrintf(10, 200, 1, String);

	if(gFrames >= 100):											# // if we are due for another FPS update
		# gCurrentTime = win32api.GetTickCount ();					# // Get the current time
		gCurrentTime = time.clock ();							# // Get the current time
		DiffTime = gCurrentTime - gStartTime;					# // Find the difference between the start and end times
		# gFPS = (gFrames / float (DiffTime)) * 1000.0;					# // Compute the FPS
		gFPS = (gFrames / float (DiffTime));					# // Compute the FPS
		gStartTime = gCurrentTime;								# // Set the current start time to the current time
		gFrames = 1;											# // Set the number of frames to 1
	else:
		gFrames += 1;											# // We are not due to for another update so add one to the frame count
	
	# // Print out the FPS
	String = "FPS %.02f" % (gFPS);
	gFont.glPrintf(10, 160, 1, String);
	return


def DrawGLScene ():
	""" // Here's Where We Do All The Drawing """
	global gCamera, gcylList, ginfoOn

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);		# // Clear Screen And Depth Buffer
	glLoadIdentity();										# // Reset The Current Modelview Matrix

	# // We want our light source to be 50 units if front 
	# // of the camera all the time to make it look like 
	# // it is infinately far away from the camera. We only
	# // do this to the z coordinate because we want to see
	# // the flares adjust if we fly in a straight line.
	gCamera.m_LightSourcePos.z = gCamera.m_Position.z - 50.0;


	# //##################### NEW STUFF ##########################
	# // Draw our cylinder and make it "do something"
	# // Of course we do that BEFORE testing for occlusion
	# // We need our depth buffer to be filled to check against occluder objects
	glPushMatrix();
	glLoadIdentity();
	glTranslatef(0.0, 0.0, -20.0);
	# glRotatef(win32api.GetTickCount () / 50.0, 0.3, 0.0, 0.0);
	# glRotatef(win32api.GetTickCount () / 50.0, 0.0, 0.5, 0.0);
	glRotatef((time.clock () * 1000.0) / 50.0, 0.3, 0.0, 0.0);
	glRotatef((time.clock () * 1000.0) / 50.0, 0.0, 0.5, 0.0);
	glCallList(gcylList);
	glPopMatrix();

	gCamera.SetPrespective();						# // Set our perspective/oriention on the world
	gCamera.RenderLensFlare();						# // Render the lens flare
	gCamera.UpdateFrustumFaster();					# // Update the frustum as fast as possible.
	
	# // Check to see if info has been toggled by 1,2
	if (gInfoOn):
		DrawGLInfo();								# // Info is on so draw the GL information.								

	glutSwapBuffers()
	return True


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global window, gCamera, gInfoOn, gFont, gcylList, qobj
	# If escape is pressed, kill everything.
	key = args [0]
	if key == ESCAPE:
		gFont.release ()
		gCamera.release ()
		gluDeleteQuadric (qobj)
		glDeleteLists (gcylList, 1)
		sys.exit ()

	if key == 'W' or key == 'w':
		gCamera.ChangePitch(-0.2);						# // Pitch the camera up 0.2 degrees

	if key == 'S' or key == 's':
		gCamera.ChangePitch(0.2);						# // Pitch the camera down 0.2 degrees
	
	if key == 'D' or key == 'd':
		gCamera.ChangeHeading(0.2);						# // Yaw the camera to the left
	
	if key == 'A' or key == 'a':
		gCamera.ChangeHeading(-0.2);					# // Yaw the camera to the right
	
	if key == 'Z' or key == 'z':
		gCamera.m_ForwardVelocity = 0.01;				# // Start moving the camera forward 0.01 units every frame

	if key == 'C' or key == 'c':
		gCamera.m_ForwardVelocity = -0.01;				# // Start moving the camera backwards 0.01 units every frame
	
	if key == 'X' or key == 'x':
		gCamera.m_ForwardVelocity = 0.0;				# // Stop the camera from moving.

	if args[0] == '1':
		gInfoOn = True;									# // Toggle info on
	
	if args[0] == '2':
		gInfoOn = False;								# // Toggle info off


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
	window = glutCreateWindow("Lens Flare Tutorial")

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

