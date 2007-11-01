#!/usr/bin/env python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import sys
import string
from OpenGL.GL import *
from OpenGL.Tk import *
from Numeric import *
import Image

WIDTH=800
HEIGHT=600

class OglFrame:
	def Redraw(self, event=None):
		glDisable(GL_LIGHTING)
		glBegin(GL_LINES)

## +x axis points left
		glColor3f(1,0,0)
		glVertex3fv([0,0,0])
		glVertex3fv(self.axispoints[0].tolist())

## +y axis points up
		glColor3f(0,1,0)
		glVertex3fv([0,0,0])
		glVertex3fv(self.axispoints[1].tolist())

## +z-axis points away
		glColor3f(0,0,1)
		glVertex3fv([0,0,0])
		glVertex3fv(self.axispoints[2].tolist())

		glEnd()

	def Photo(self, event=None):
		glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
		pixels = glReadPixels(0, 0, 
							   self.keywords['width'], self.keywords['height'], 
							   GL_RGBA, GL_UNSIGNED_BYTE)
		im = Image.new("RGB", (self.keywords['width'], self.keywords['height']))
		im.fromstring(pixels)
		im.save(self.imagename)

	def __init__(self, master=None, redraw=None, *arguments, **keywords):
		self.imagename="photo.ppm"
		self.master=master
		self.keywords = keywords
		self.OglFrame = Frame(self.master, width=320, height=200)
		self.OglFrame.pack(side = 'top', expand = 1, fill = 'both')
		self.keywords['double'] = 1
		self.ogl = Opengl(self.OglFrame, self.keywords)
		self.ogl.pack(side = 'top', expand = 1, fill = 'both')
		self.ogl.bind('<Shift-Button-2>', self.Photo)
		self.ogl.bind('<Button-2>',self.ogl.tkRecordMouse)
		self.ogl.bind('<B2-Motion>', self.ogl.tkTranslate)
		self.ogl.bind('<Button-1>', self.ogl.StartRotate)
		self.ogl.bind('<B1-Motion>', self.ogl.tkRotate)
		self.ogl.bind('<Button-3>', self.ogl.tkRecordMouse)
		self.ogl.bind('<B3-Motion>', self.ogl.tkScale)

		glBlendFunc(GL_SRC_ALPHA,  GL_ONE_MINUS_SRC_ALPHA);		
		glEnable(GL_BLEND);
		glEnable(GL_LINE_SMOOTH);

		self.ogl.set_background(0,0,0)

		if redraw == None:
			self.ogl.redraw=self.Redraw
		else:
			self.ogl.redraw=redraw

		self.mainloop=self.ogl.mainloop
		

		self.axispoints = identity((3))

if __name__ == '__main__':
	x= OglFrame(None, 
				None,
				width=320,
				height=200,
				double=1,
				depth=1)
	x.mainloop()
