from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLE import *
import items

class item(items.item):

	def __init__(self):
		items.item.__init__(self)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_LIGHTING)

		glEnable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_POSITION, (40.0, 40, 100.0, 0.0))
		glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.99, 0.99, 0.99, 1.0))

		glEnable(GL_LIGHT1)
		glLightfv(GL_LIGHT1, GL_POSITION, (-40.0, 40, 100.0, 0.0))
		glLightfv(GL_LIGHT1, GL_DIFFUSE, (0.99, 0.99, 0.99, 1.0))

		gleSetJoinStyle(TUBE_NORM_EDGE | TUBE_JN_ANGLE | TUBE_JN_CAP)
		

	def __del__(self):
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_COLOR_MATERIAL)	
		glDisable(GL_LIGHTING)

		glDisable(GL_LIGHT0)
		glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1, 0))
		glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

		glDisable(GL_LIGHT1)
		glLightfv(GL_LIGHT1, GL_POSITION, (0, 0, 1, 0))
		glLightfv(GL_LIGHT1, GL_DIFFUSE, (0, 0, 0, 0))


	def on_reshape(self, width, height):
		items.item.on_reshape(self, width, height)		
		glTranslatef(0.0, 0.0, -40.0)


	def on_display(self):
		items.item.on_display(self)
		glePolyCone(((-6.0, 6.0, 0.0),
					 (6.0, 6.0, 0.0),
					 (6.0, -6.0, 0.0),
					 (-6.0, -6.0, 0.0),
					 (-6.0, 6.0, 0.0),
					 (6.0, 6.0, 0.0)),
					((0.0, 0.0, 0.0),
					 (0.0, 0.8, 0.3),
					 (0.8, 0.3, 0.0),
					 (0.2, 0.3, 0.9),
					 (0.2, 0.8, 0.5),
					 (0.0, 0.0, 0.0)),
					(1, 1, 3, 0.5, 2, 1))
		