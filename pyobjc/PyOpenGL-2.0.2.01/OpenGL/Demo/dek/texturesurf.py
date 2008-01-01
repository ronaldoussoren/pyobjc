#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

## Texture mapping an image--- derived mainly from texturesurf.c (SGI demo)
## Notable feature: uses PIL to load a PPM image, which is then texturemapped
## to a bezier surface, using PyOpenGL.

## Note: your image needs to be RGBA, and the image
## dimensions must be powers of two, starting
## with 64 (ie, 64x64, 128x128, etc)

## also, I noticed that from certain directions the surface is
## partially transparent.  is there a bug in my code,
## or is it the way that OpenGL handles concave surfaces?
## if you figure it out, let me know.
## (it may invlve backface culling)

## Written by David Konerding (dek@cgl.ucsf.edu)
## You are free to modify and redistribute this code.



import sys
from Image import *
from OpenGL.GL import *
from OpenGL.Tk import *


## Control points for the bezier surface
ctrlpoints = [[[ -1.5, -1.5, 4.0], [-0.5, -1.5, 2.0], [0.5, -1.5,
	-1.0], [1.5, -1.5, 2.0]], [[-1.5, -0.5, 1.0], [-0.5, -0.5, 3.0], [0.5, -0.5,
	0.0], [1.5, -0.5, -1.0]], [[-1.5, 0.5, 4.0], [-0.5, 0.5, 0.0], [0.5, 0.5,
	3.0], [1.5, 0.5, 4.0]], [[-1.5, 1.5, -2.0], [-0.5, 1.5, -2.0], [0.5, 1.5,
	0.0], [1.5, 1.5, -1.0]]]

## Texture control points
texpts = [[[0.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [1.0, 1.0]]]

class Surface:
	def Display(self, event=None):
		glClearColor(0.0, 0.0, 0.0, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glCallList(self.list)

	def SetupWindow(self):
		self.OglFrame = Frame()
		self.OglFrame.pack(side = 'top')
		self.QuitButton = Button(self.OglFrame, {'text':'Quit'})
		self.QuitButton.bind('<ButtonRelease-1>', sys.exit)
		self.QuitButton.pack({'side':'top'})

	def SetupOpenGL(self):
		self.ogl = Opengl(master=self.OglFrame, width = 500, height = 500, double = 1, depth = 1)
		self.ogl.pack(side = 'top', expand = 1, fill = 'both')
		self.ogl.set_centerpoint(0, 0, 0)
		self.ogl.redraw = self.Display

## Note: only works for RGBA images where side length is power of 2
	def MakeImage(self, filename):
		im = open(filename)
		self.imageWidth = im.size[0]
		self.imageHeight = im.size[1]
		self.image = im.tostring("raw", "RGBX", 0, -1)
#		print self.imageWidth, self.imageHeight, self.imageWidth * self.imageHeight*4, len(self.image)


## this hunk of code handles the bezier mapping and texture mapping
	def Surface(self):
		glDisable(GL_CULL_FACE)
		glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, ctrlpoints)
		glMap2f(GL_MAP2_TEXTURE_COORD_2, 0, 1, 0, 1, texpts)
		glEnable(GL_MAP2_TEXTURE_COORD_2)
		glEnable(GL_MAP2_VERTEX_3)
		glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		print type(self.image)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, self.imageWidth, self.imageHeight, 0,
					 GL_RGBA, GL_UNSIGNED_BYTE, self.image)
		glEnable(GL_TEXTURE_2D)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_NORMALIZE)
		glShadeModel(GL_FLAT)


		self.list = glGenLists(1)
		glNewList(self.list, GL_COMPILE)
		glEvalMesh2(GL_FILL, 0, 20, 0, 20)
		glEndList()

	def __init__(self):
		try:
			filename = sys.argv[1]
		except:
			filename = "image.ppm"
			sys.stderr.write("usage: <name> ppmfilename\n")
			#sys.exit(1)

		self.SetupWindow()
		self.MakeImage(filename)
		self.SetupOpenGL()
		self.Surface()

		self.ogl.tkRedraw()
		self.ogl.mainloop()

if __name__ == '__main__':
	Surface()
		
demo = Surface
