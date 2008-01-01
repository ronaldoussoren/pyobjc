#!/usr/bin/env python

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import sys
import string
import Numeric
import NumericPDB
import string
from OpenGL.GL import *
from OpenGL.Tk import *
import Image
import OglFrame

MAP="test.ppm"

class Surface:
	def SetupWindow(self):
		self.OglFrame = OglFrame.OglFrame(None, 
										  redraw=self.Display, 
										  depth=1,
										  double=1)
		self.OglFrame.ogl.set_background(0,0,0)

	def Display(self, event=None):
		glEnable(GL_DEPTH_TEST)
		glDepthMask(GL_TRUE)
		glEnable(GL_CULL_FACE)
		glCullFace(GL_BACK)

		if self.surface:
			glCallList(self.surfacelist)
		if self.bond:
			glCallList(self.bondlist)

	def SetupSurface(self):
		self.surfacelist = glGenLists(1)
		glNewList(self.surfacelist, GL_COMPILE);
		
		glEnable(GL_LIGHTING)
		glEnable(GL_BLEND)

		color1 = color2 = color3 = (1,1,1,1)
		glColorMaterial(GL_FRONT, GL_DIFFUSE)
		glEnable(GL_COLOR_MATERIAL)
		glBegin(GL_TRIANGLES)
		for i in range(len(self.faces)):

			tri = self.faces[i]
			vert1 = tuple(self.vert[tri[0]-1])
			vert2 = tuple(self.vert[tri[1]-1])
			vert3 = tuple(self.vert[tri[2]-1])
			norm1 = tuple(self.norm[tri[0]-1])
			norm2 = tuple(self.norm[tri[1]-1])
			norm3 = tuple(self.norm[tri[2]-1])

			color = self.colorlist[self.nearest[tri[0]-1]-1]
			glColor3f(color[0], color[1], color[2])
			glNormal3fv(norm1)
			glVertex3fv(vert1)

			color = self.colorlist[self.nearest[tri[1]-1]-1]
			glColor3f(color[0], color[1], color[2])
			glNormal3fv(norm2)
			glVertex3fv(vert2)

			color = self.colorlist[self.nearest[tri[2]-1]-1]
			glColor3f(color[0], color[1], color[2])
			glNormal3fv(norm3)
			glVertex3fv(vert3)

		glEnd()
		glDisable(GL_LIGHTING)
		glDisable(GL_BLEND)
		glEndList()

		self.surface=1

	def SetupBonds(self):
		self.bond=1
		self.bondlist = glGenLists(1)
		glNewList(self.bondlist, GL_COMPILE);
		glDisable(GL_LIGHTING)
		glDisable(GL_BLEND)
		glBegin(GL_LINES)
		for i in self.topol:
			at1, at2 = i[0], i[1]
			color = self.colorlist2[at1]
			apply(glColor3f, tuple(color))
			glVertex3f(self.crd[at1][0], \
						self.crd[at1][1], \
						self.crd[at1][2])
			color = self.colorlist2[at2]
			apply(glColor3f, tuple(color))
			glVertex3f(self.crd[at2][0], \
						self.crd[at2][1], \
						self.crd[at2][2])
		glEnd()
		glEnable(GL_BLEND)
		glEndList()

	def ReadSurface(self):
		f = open(self.facefile)
		l = f.readlines()
		data = string.split(l[2])
		numfaces = string.atoi(data[0])
		spheres = string.atoi(data[1])
		probe_r = string.atof(data[2])
		density = string.atof(data[3])
		print "Numfaces, spheres, probe_r, density"
		print numfaces, spheres, probe_r, density

		self.faces = Numeric.zeros((numfaces, 3))
		for i in range(numfaces):
			data = string.split(l[i+3])
			self.faces[i] = map(string.atoi, data[:3])
		f.close()

		f = open(self.vertfile)
		l = f.readlines()
		data = string.split(l[2])
		vertices = string.atoi(data[0])
		spheres = string.atoi(data[1])
		probe_r = string.atof(data[2])
		density = string.atof(data[3])
		print "Vertices, spheres, probe_r, density"
		print vertices, spheres, probe_r, density
		f.close()

		self.vert = Numeric.zeros((vertices, 3), Numeric.Float)
		self.norm = Numeric.zeros((vertices, 3), Numeric.Float)
		self.nearest = Numeric.zeros((vertices))
		for i in range(vertices):
			data = string.split(l[i+3])
			self.vert[i] = map(string.atof, data[:3])
			self.norm[i] = map(string.atof, data[3:6])
			self.nearest[i] = string.atoi(data[7])

		vcen = Numeric.add.reduce(self.vert)/len(self.vert)
		self.OglFrame.ogl.set_centerpoint(vcen[0], vcen[1], vcen[2])
		

	def ReadPDB(self):
		p = NumericPDB.PDB(self.pdbfile)
		atomlist = map(lambda x: x.atom, p.records)
		k = self.colordict.keys()
		self.colorlist = []
		self.maplist = []
		for i in atomlist:
			if i[0] in k:
				self.colorlist.append(self.colordict[i[0]])
				self.maplist.append(self.mapdict[i[0]])
			else:
				print "unfound atom type:", i
				self.colorlist.append(self.colordict['U'])
				self.maplist.append(self.mapdict['U'])


	def MakeImage(self):
		im = Image.open(self.map)
		self.imageWidth = im.size[0]
		self.imageHeight = im.size[1]
		self.image = im.tostring("raw", "RGBX", 0, -1)

	def __init__(self, facefile="1crn.face", vertfile="1crn.vert", pdbfile="1crn.pdb"):
		self.facefile = facefile
		self.vertfile = vertfile
		self.pdbfile = pdbfile

		self.map = MAP

		alpha = 1
		self.colordict = {'C':[.5,.5,.5,alpha], 'O':[1,0,0,alpha], 'N':[0,0,1,alpha], 'S':[1,1,0,alpha], 'P':[1,0,1,alpha],'H':[1,1,1,alpha], 'U':[0,0,0,alpha]}
		self.mapdict = {'C':0.5, 'O':.9, 'N':0.1, 'S':0.5, 'P':0.5,'H':0.5, 'U':0.5}
		self.surface = None
		self.bond = None
		self.SetupWindow()



		self.ReadPDB()
		self.MakeImage()
		self.ReadSurface()
		self.SetupSurface()


##		self.OglFrame.ogl.tkRedraw()
##		out=tkinter.dooneevent(tkinter.DONT_WAIT)
##		while (out):
##			out=tkinter.dooneevent(tkinter.DONT_WAIT)
##		self.OglFrame.Photo()

		self.OglFrame.mainloop()


if __name__ == '__main__':
	s = Surface()
