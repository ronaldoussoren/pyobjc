# /*******************************************
# *                                          *
# *   Paul Frazee's Vertex Array Example     *
# *           nehe.gamedev.net               *
# *                2003                      *
# *                                          *
# *******************************************/
#
#
# NeHe Tutorial Lesson: 45 - Vertex Buffer Objects
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
# Make sure to get versions of Numeric, PyOpenGL, and PIL to match your
# version of python.
#
#
#
# PyOpenGL extension wrapper for GL_ARB_vertex_buffer_object is currently
# only availabel through cvs (no release build yet). When a new release
# is made of PyOpenGL updating this tutorial should be pretty easy.
# For now, in place of VBOs, vertex/texcoord arrays are used.
#
#


import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Numeric

import Image 				# PIL
import sys
# import win32api				# GetTickCount
import time				

# Note Yet Supported
# from OpenGL.GL.ARB.vertex_buffer_object import *
# http://oss.sgi.com/projects/ogl-sample/registry/ARB/vertex_buffer_object.txt




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

# PyOpenGL doesn't yet have the ARB for vertex_buffer_objects
NO_VBOS = True

g_fVBOSupported = False;							# // ARB_vertex_buffer_object supported?
g_pMesh = None;										# // Mesh Data
g_flYRot = 0.0;										# // Rotation
g_nFPS = 0
g_nFrames = 0;										# // FPS and FPS Counter
g_dwLastFPS = 0;									# // Last FPS Check Time	




class CVert:
	""" // Vertex Class """
	def __init__ (self, x = 0.0, y = 0.0, z = 0.0):
		self.x = 0											# // X Component
		self.y = 0											# // Y Component
		self.z = 0											# // Z Component

# // The Definitions Are Synonymous
CVec = CVert

class CTexCoord:
	""" // Texture Coordinate Class """
	def __init__ (self, u = 0.0, v = 0.0):
		self.u = u;											# // U Component
		self.v = v;											# // V Component

class CMesh:
	""" // Mesh Data """
	MESH_RESOLUTION = 4.0
	MESH_HEIGHTSCALE = 1.0

	def __init__ (self):
		self.m_nVertexCount = 0;								# // Vertex Count

		self.m_pVertices = None # Numeric.array ( (), 'f') 		# // Vertex Data array
		self.m_pVertices_as_string = None						# raw memory string for VertexPointer ()

		self.m_pTexCoords = None # Numeric.array ( (), 'f') 	# // Texture Coordinates array
		self.m_pTexCoords_as_string = None						# raw memory string for TexPointer ()

		self.m_nTextureId = None;								# // Texture ID

		# // Vertex Buffer Object Names
		self.m_nVBOVertices = None;								# // Vertex VBO Name
		self.m_nVBOTexCoords = None;							# // Texture Coordinate VBO Name

		# // Temporary Data
		self.m_pTextureImage = None;							# // Heightmap Data


	def LoadHeightmap( self, szPath, flHeightScale, flResolution ):
		""" // Heightmap Loader """

		# // Error-Checking
		# // Load Texture Data
		try:
			self.m_pTextureImage = Image.open (szPath)						 	# // Open The Image
		except:
			return False

		# // Generate Vertex Field
		sizeX = self.m_pTextureImage.size [0]
		sizeY = self.m_pTextureImage.size [1]
		self.m_nVertexCount = int ( sizeX * sizeY * 6 / ( flResolution * flResolution ) );
		# self.m_pVertices = Numeric.zeros ((self.m_nVertexCount * 3), 'f') 			# // Vertex Data
		# Non strings approach
		self.m_pVertices = Numeric.zeros ((self.m_nVertexCount, 3), 'f') 			# // Vertex Data
		self.m_pTexCoords = Numeric.zeros ((self.m_nVertexCount, 2), 'f') 			# // Texture Coordinates

		nZ = 0
		nIndex = 0
		nTIndex = 0
		half_sizeX = float (sizeX) / 2.0
		half_sizeY = float (sizeY) / 2.0
		flResolution_int = int (flResolution)
		while (nZ < sizeY):
			nX = 0
			while (nX < sizeY):
				for nTri in xrange (6):
					# // Using This Quick Hack, Figure The X,Z Position Of The Point
					flX = float (nX)
					if (nTri == 1) or (nTri == 2) or (nTri == 5):
						flX += flResolution
					flZ = float (nZ)
					if (nTri == 2) or (nTri == 4) or (nTri == 5):
						flZ += flResolution
					x = flX - half_sizeX
					y = self.PtHeight (int (flX), int (flZ)) * flHeightScale
					z = flZ - half_sizeY
					self.m_pVertices [nIndex, 0] = x
					self.m_pVertices [nIndex, 1] = y
					self.m_pVertices [nIndex, 2] = z
					self.m_pTexCoords [nTIndex, 0] = flX / sizeX
					self.m_pTexCoords [nTIndex, 1] =  flZ / sizeY
					nIndex += 1
					nTIndex += 1

				nX += flResolution_int
			nZ += flResolution_int

		self.m_pVertices_as_string = self.m_pVertices.tostring () 
		self.m_pTexCoords_as_string = self.m_pTexCoords.tostring () 

		# // Load The Texture Into OpenGL
		self.m_nTextureID = glGenTextures (1)						# // Get An Open ID
		glBindTexture( GL_TEXTURE_2D, self.m_nTextureID );			# // Bind The Texture
		glTexImage2D( GL_TEXTURE_2D, 0, 3, sizeX, sizeY, 0, GL_RGB, GL_UNSIGNED_BYTE, 
			self.m_pTextureImage.tostring ("raw", "RGB", 0, -1))
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
		glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);

		# // Free The Texture Data
		self.m_pTextureImage = None
		return True;

	def PtHeight (self, nX, nY):
		""" // Calculate The Position In The Texture, Careful Not To Overflow """
		sizeX = self.m_pTextureImage.size [0]
		sizeY = self.m_pTextureImage.size [1]
		if (nX >= sizeX or nY >= sizeY):
			return 0

		# Get The Red, Green, and Blue Components 
		# NOTE, Python Image library starts 0 at the top of the image - so to match the windows
		# code we reverse the Y order 
		pixel = self.m_pTextureImage.getpixel ((nX, sizeY - nY - 1))
		flR = float (pixel [0])
		flG = float (pixel [1])
		flB = float (pixel [2])
		pixel = self.m_pTextureImage.getpixel ((nY, nX))

		# // Calculate The Height Using The Luminance Algorithm
		return ( (0.299 * flR) + (0.587 * flG) + (0.114 * flB) );			


	def BuildVBOs (self):
		""" // Generate And Bind The Vertex Buffer """
		if (g_fVBOSupported):
			self.m_nVBOVertices = glGenBuffersARB( 1);						# // Get A Valid Name
			glBindBufferARB( GL_ARRAY_BUFFER_ARB, self.m_nVBOVertices );	# // Bind The Buffer
			# // Load The Data
			glBufferDataARB( GL_ARRAY_BUFFER_ARB, self.m_pVertices, GL_STATIC_DRAW_ARB );

			# // Generate And Bind The Texture Coordinate Buffer
			self.m_nVBOTexCoords = glGenBuffersARB( 1);						# // Get A Valid Name
			glBindBufferARB( GL_ARRAY_BUFFER_ARB, m_nVBOTexCoords );		# // Bind The Buffer
			# // Load The Data
			glBufferDataARB( GL_ARRAY_BUFFER_ARB, m_pTexCoords, GL_STATIC_DRAW_ARB );

			# // Our Copy Of The Data Is No Longer Necessary, It Is Safe In The Graphics Card
			self.m_pVertices = None
			self.m_pVertices = None;
			self.m_pTexCoords = None
			self.m_pTexCoords = None;
		return









def IsExtensionSupported (TargetExtension):
	""" Accesses the rendering context to see if it supports an extension.
		Note, that this test only tells you if the OpenGL library supports
		the extension. The PyOpenGL system might not actually support the extension.
	"""
	Extensions = glGetString (GL_EXTENSIONS)
	# python 2.3
	# if (not TargetExtension in Extensions):
	#	gl_supports_extension = False
	#	print "OpenGL does not support '%s'" % (TargetExtension)
	#	return False

	# python 2.2
	Extensions = Extensions.split ()
	found_extension = False
	for extension in Extensions:
		if extension == TargetExtension:
			found_extension = True
			break;
	if (found_extension == False):
		gl_supports_extension = False
		print "OpenGL rendering context does not support '%s'" % (TargetExtension)
		return False

	gl_supports_extension = True

	# Now determine if Python supports the extension
	# Exentsion names are in the form GL_<group>_<extension_name>
	# e.g.  GL_EXT_fog_coord 
	# Python divides extension into modules
	# g_fVBOSupported = IsExtensionSupported ("GL_ARB_vertex_buffer_object")
	# from OpenGL.GL.EXT.fog_coord import *
	if (TargetExtension [:3] != "GL_"):
		# Doesn't appear to following extension naming convention.
		# Don't have a means to find a module for this exentsion type.
		return False

	# extension name after GL_
	afterGL = TargetExtension [3:]
	try:
		group_name_end = afterGL.index ("_")
	except:
		# Doesn't appear to following extension naming convention.
		# Don't have a means to find a module for this exentsion type.
		return False

	group_name = afterGL [:group_name_end]
	extension_name = afterGL [len (group_name) + 1:]
	extension_module_name = "OpenGL.GL.%s" % (extension_name)

	try:
		__import__ (extension_module_name)
		print "PyOpenGL supports '%s'" % (TargetExtension)
	except:
		print "OpenGL rendering context supports '%s'" % (TargetExtension),
		print "however PyOpenGL (ver %s) does not." % (OpenGL.__version__)
		return False

	return True



# // Any GL Init Code & User Initialiazation Goes Here
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	global g_pMesh

	# // TUTORIAL
	# // Load The Mesh Data
	g_pMesh = CMesh ()
	if (not g_pMesh.LoadHeightmap ("Terrain.bmp",
		CMesh.MESH_HEIGHTSCALE, CMesh.MESH_RESOLUTION)):
		print "Error Loading Heightmap"
		sys.exit(1)
		return False

	# // Check for VBOs Supported
	g_fVBOSupported = IsExtensionSupported ("GL_ARB_vertex_buffer_object")
	if (g_fVBOSupported):
		# // Get Pointers To The GL Functions
		# In python, calling Init for the extension functions will
		# fill in the function pointers (really function objects)
		# so that we call the Extension.

		if (not glInitVertexBufferObjectARB ()):
			print "Help!  No GL_ARB_vertex_buffer_object"
			sys.exit(1)
			return False
		# Now we can call to gl*Buffer* ()
		# glGenBuffersARB
		# glBindBufferARB
		# glBufferDataARB
		# glDeleteBuffersARB
		g_pMesh.BuildVBOs 


	# Setup GL States
	glClearColor (0.0, 0.0, 0.0, 0.5);							# // Black Background
	glClearDepth (1.0);											# // Depth Buffer Setup
	glDepthFunc (GL_LEQUAL);									# // The Type Of Depth Testing
	glEnable (GL_DEPTH_TEST);									# // Enable Depth Testing
	glShadeModel (GL_SMOOTH);									# // Select Smooth Shading
	glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);			# // Set Perspective Calculations To Most Accurate
	glEnable(GL_TEXTURE_2D);									# // Enable Texture Mapping
	glColor4f (1.0, 6.0, 6.0, 1.0)

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
	gluPerspective(45.0, float(Width)/float(Height), 1, 1000.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


g_prev_draw_time = 0.0
# The main drawing function. 
def DrawGLScene():
	global g_dwLastFPS, g_nFPS, g_nFrames, g_pMesh, g_fVBOSupported, g_flYRot, g_prev_draw_time

	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);				# // Clear Screen And Depth Buffer
	glLoadIdentity ();													# // Reset The Modelview Matrix


	# // Get FPS
	# milliseconds = win32api.GetTickCount() 
	milliseconds = time.clock () * 1000.0
	if (milliseconds - g_dwLastFPS >= 1000):					# // When A Second Has Passed...
		# g_dwLastFPS = win32api.GetTickCount();				# // Update Our Time Variable
		g_dwLastFPS = time.clock () * 1000.0
		g_nFPS = g_nFrames;										# // Save The FPS
		g_nFrames = 0;											# // Reset The FPS Counter

		# // Build The Title String
		szTitle = "Lesson 45: NeHe & Paul Frazee's VBO Tut - %d Triangles, %d FPS" % (g_pMesh.m_nVertexCount / 3, g_nFPS );
		if ( g_fVBOSupported ):									# // Include A Notice About VBOs
			szTitle = szTitle + ", Using VBOs";
		else:
			szTitle = szTitle + ", Not Using VBOs";

		glutSetWindowTitle ( szTitle );							# // Set The Title

	g_nFrames += 1 												# // Increment Our FPS Counter
	rot = (milliseconds - g_prev_draw_time) / 1000.0 * 25
	g_prev_draw_time = milliseconds
	g_flYRot += rot 											# // Consistantly Rotate The Scenery

	# // Move The Camera
	glTranslatef( 0.0, -220.0, 0.0 );							# // Move Above The Terrain
	glRotatef( 10.0, 1.0, 0.0, 0.0 );							# // Look Down Slightly
	glRotatef( g_flYRot, 0.0, 1.0, 0.0 );						# // Rotate The Camera

	# // Enable Pointers
	glEnableClientState( GL_VERTEX_ARRAY );						# // Enable Vertex Arrays
	glEnableClientState( GL_TEXTURE_COORD_ARRAY );				# // Enable Texture Coord Arrays


	# // Set Pointers To Our Data
	if( g_fVBOSupported ):
		glBindBufferARB( GL_ARRAY_BUFFER_ARB, g_pMesh.m_nVBOVertices );
		glVertexPointer( 3, GL_FLOAT, 0, None );				# // Set The Vertex Pointer To The Vertex Buffer
		glBindBufferARB( GL_ARRAY_BUFFER_ARB, g_pMesh.m_nVBOTexCoords );
		glTexCoordPointer( 2, GL_FLOAT, 0, None );				# // Set The TexCoord Pointer To The TexCoord Buffer
	else:
		# You can use the pythonism glVertexPointerf (), which will convert the numarray into 
		# the needed memory for VertexPointer. This has two drawbacks however:
		#	1) This does not work in Python 2.2 with PyOpenGL 2.0.0.44 
		#	2) In Python 2.3 with PyOpenGL 2.0.1.07 this is very slow.
		# See the PyOpenGL documentation. Section "PyOpenGL for OpenGL Programmers" for details
		# regarding glXPointer API.
		# Also see OpenGLContext Working with Numeric Python
		# glVertexPointerf ( g_pMesh.m_pVertices ); 	# // Set The Vertex Pointer To Our Vertex Data
		# glTexCoordPointerf ( g_pMesh.m_pTexCoords ); 	# // Set The Vertex Pointer To Our TexCoord Data
		#
		#
		# The faster approach is to make use of an opaque "string" that represents the
		# the data (vertex array and tex coordinates in this case).
		glVertexPointer( 3, GL_FLOAT, 0, g_pMesh.m_pVertices_as_string);  	# // Set The Vertex Pointer To Our Vertex Data
		glTexCoordPointer( 2, GL_FLOAT, 0, g_pMesh.m_pTexCoords_as_string); 	# // Set The Vertex Pointer To Our TexCoord Data


	# // Render
	glDrawArrays( GL_TRIANGLES, 0, g_pMesh.m_nVertexCount );		# // Draw All Of The Triangles At Once

	# // Disable Pointers
	glDisableClientState( GL_VERTEX_ARRAY );					# // Disable Vertex Arrays
	glDisableClientState( GL_TEXTURE_COORD_ARRAY );				# // Disable Texture Coord Arrays

	glutSwapBuffers()													 # // Flush The GL Rendering Pipeline
	return True





# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
	global window

	# If escape is pressed, kill everything.
	if args[0] == ESCAPE:
		sys.exit ()
	return

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
	window = glutCreateWindow("Lesson 45: NeHe & Paul Frazee's VBO Tut")

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


