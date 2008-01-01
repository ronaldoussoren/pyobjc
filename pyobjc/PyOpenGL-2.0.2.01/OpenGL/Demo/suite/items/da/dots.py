from OpenGL.GL import *
from Numeric import *
from RandomArray import *
import items


MY_LIST = 1
NUMDOTS = 500
NUMDOTS2 = 600
MAX_AGE = 13
move_length = .005  # 1.0 = screen width
angle = 0		  # in radians
delta_angle = .2  # in radians
move_x = move_length*cos(angle)
move_y = move_length*sin(angle)


class item(items.item):

	def __init__(self):
		items.item.__init__(self)
		
		self.age = randint(0, MAX_AGE, (NUMDOTS,))
		self.x = random(NUMDOTS)*2-1
		self.y = random(NUMDOTS)*2-1
		

	def on_idle(self):
		return 1


	def on_reshape(self, width, height):
		glOrtho(0.0, 1.0, 0.0, 1.0, 0.0, 1.0)


	def on_display(self):
		items.item.on_display(self)
		
		glColor3f(1.0, 1.0, 0.0)
		self.x = self.x + move_x
		self.y = self.y + move_y
		self.age = self.age + 1
		which = greater(self.age, MAX_AGE)
		self.x = choose(which, (self.x, random(NUMDOTS)))
		self.y = choose(which, (self.y, random(NUMDOTS)))
		self.age = choose(which, (self.age, 0))
		self.x = choose(greater(self.x, 1.0), (self.x, self.x - 1.0))  # very cool - wraparound
		self.y = choose(greater(self.y, 1.0), (self.y, self.y - 1.0))
		x2 = random(NUMDOTS2)
		y2 = random(NUMDOTS2)
		v = concatenate((transpose(array([self.x, self.y])),
						 transpose(array([self.x - .005, self.y + .005])),
						 transpose(array([self.x + .005, self.y - .005])),
						 transpose(array([x2, y2]))))
		glVertexPointerd(v)
		glEnableClientState(GL_VERTEX_ARRAY)
		glDrawArrays(GL_POINTS, 0, len(v))
		glDisableClientState(GL_VERTEX_ARRAY)


	def on_motion(self, x, y):
		pass
	