from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import items.GLUT.geometry


class item(items.GLUT.geometry.solid_item):

	def __init__(self):
		items.GLUT.geometry.solid_item.__init__(self)
		glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 1)
		

	def __del__(self):
		items.GLUT.geometry.solid_item.__del__(self)
		glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 0)


	def on_display(self):
		items.GLUT.geometry.solid_item.on_display(self)
		glutSolidCone(1, 1, 20, 20)
