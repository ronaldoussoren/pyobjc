#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


## example python/pyopengl script to do tiled texturemapping.
## By david konerding (dek@cgl.ucsf.edu)

import sys
from Image import *
from OpenGL.GL import *
from OpenGL.Tk import *
try:
	from Numeric import *
except:
	print "This demo requires the Numeric extension, sorry."
	sys.exit()
import math


const = math.pi
class checker:

	def makeImage(self):
		im = open(self.filename)
		self.imageWidth = im.size[0]
		self.imageHeight = im.size[1]
		self.image = im.tostring("raw", "RGBX", 0, -1)
		
	def display(self, event=None):
		glClearColor(0.0, 0.0, 0.0, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glBegin(GL_QUADS)


		glTexCoord2f(0.0, 0.0);		glVertex3f(0.0, 0.0, 0.0)
		glTexCoord2f(0.0, 2.0);		glVertex3f(0.0, 10., 0.0)
		glTexCoord2f(2.0, 2.0);		glVertex3f(10. , 10., 0.0)
		glTexCoord2f(2.0, 0.0);		glVertex3f(10., 0.0, 0.0)

		glEnd()
		glFlush()

	def SetupWindow(self):
		self.OglFrame = Frame()
		self.OglFrame.pack(side = 'top')
		self.QuitButton = Button(self.OglFrame, {'text':'Quit'})
		self.QuitButton.bind('<ButtonRelease-1>', sys.exit)
		self.QuitButton.pack({'side':'top'})
		self.ogl = Opengl(master=self.OglFrame, width = 500, height = 500, double = 1)
		self.ogl.pack(side = 'top', expand = 1, fill = 'both')
##		self.ogl.set_eyepoint(900.)
##		self.ogl.set_centerpoint(0, 0, 0)
		self.ogl.redraw = self.display


	def SetupTexture(self):
		self.makeImage()
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, self.imageWidth, self.imageHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE,  self.image)
##		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
##		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		glEnable(GL_TEXTURE_2D)
		glShadeModel(GL_FLAT)


	def __init__(self):
		try:
			self.filename = sys.argv[1]
		except:
			self.filename = "image.ppm"
			sys.stderr.write("usage: <name> ppmfilename\n")
			#sys.exit(1)
		self.SetupWindow()
		self.SetupTexture()
		self.ogl.mainloop()

if __name__ == '__main__':
	checker()


