#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception


import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/30 19:17:17 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'

from OpenGL.GL import *
from OpenGL.Tk import *

def new_file(self):
    print "opening new file"

def open_file(self):
    print "opening OLD file"

def print_something(self):
    print "picked a menu item"


class Demo:
	def __init__(self, root):
		self.mBar = Frame(root, relief=RAISED, borderwidth=2)
		self.mBar.pack(fill=X)
		demo = self.makeDemoMenu()
		self.mBar.tk_menuBar(demo)
		self.ogl = Opengl(width = 300, height = 300, double = 1, depth = 1)
		self.ogl.redraw = self.draw_lines
		self.ogl.set_centerpoint(30, 0, 0)
		self.ogl.set_eyepoint(140)
		self.ogl.pack(side = 'top', expand = 1, fill = 'both')
		self.ogl.grob = -1

	def makeDemoMenu(self):
		demo = Menubutton(self.mBar, text='Demos', underline=0)
		demo.pack(side=LEFT, padx="2m")
		demo.menu = Menu(demo)

		demo.menu.add_command(label='Blue', underline=0, command=self.set_blue)
		demo.menu.add_command(label='Lines', underline=0,command=self.set_lines)
		demo.menu.add_command(label='Text', underline=0,command=self.set_text)
   
		demo.menu.add('separator')
		demo.menu.add_command(label='Quit', underline=0, background='red', 
				    				 activebackground='green',
									 command=demo.quit)

		demo['menu'] = demo.menu
		return demo

	def draw_lines(self, ogl):
		glClearColor(0, 0, 0, 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glDisable(GL_LIGHTING)
		glBegin(GL_LINES)
		glColor3f(1,1,0)
		glVertex2f(0,-30)
		glColor3f(1,0,1)
		glVertex2f(60,30)
		glColor3f(1,0,0)
		glVertex2f(60,-30)
		glColor3f(0,0,1)
		glVertex2f(0,30)
		glEnd()
		glEnable(GL_LIGHTING)

	def set_lines(self):
		self.ogl.redraw = self.draw_lines
		self.ogl.tkRedraw()

	def draw_blue(self, ogl):
		glClearColor(0, 0, 1, 0)
		glClear(GL_COLOR_BUFFER_BIT)

	def set_blue(self):
		self.ogl.redraw = self.draw_blue
		self.ogl.tkRedraw()

	def draw_text(self, ogl):
		glClearColor(0, 0, 0.5, 0)
		glClear(GL_COLOR_BUFFER_BIT)
		if ogl.grob == -1:
			from logo import define_logo
			ogl.grob = glGenLists(1);
			glNewList(ogl.grob, GL_COMPILE_AND_EXECUTE);
			glMaterialfv(GL_FRONT, GL_DIFFUSE, [1, 0, 0, 0])
			define_logo()
			glEndList()
		else:
			glCallList(ogl.grob)

	def set_text(self):
		self.ogl.redraw = self.draw_text
		self.ogl.tkRedraw()

root = Tk()
d = Demo(root)
root.mainloop()
