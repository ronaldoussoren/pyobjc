from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import items.GLUT.geometry


class item(items.GLUT.geometry.solid_item):

	def on_display(self):
		items.GLUT.geometry.solid_item.on_display(self)
		glutSolidTorus(0.15, 0.75, 20, 20)
		