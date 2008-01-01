# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import os, os.path, string

def __get_items(basedir, submodule):
	items = {}
	rootdir = apply(os.path.join, [basedir] + submodule)
	for item in os.listdir(rootdir):
		path = os.path.join(rootdir, item)
		name, ext = os.path.splitext(item)
		if os.path.isdir(path):
			subitems = __get_items(basedir, submodule + [item])
			if len(subitems):
				items[item] = subitems
		elif os.path.isfile(path) and name != '__init__' and ext == '.py':
			try:
				items[name] = getattr(__import__(string.join(submodule + [name], '.'), globals(), locals(), ['item']), 'item')
			except:
				pass
	return items		


def get_items():
	return __get_items(os.path.dirname(__file__), [])


class item:

	def __init__(self):
		self.phi = 0
		self.theta = 0


	def __del__(self):
		pass		


	def on_idle(self):
		return 0


	def on_reshape(self, width, height):
		gluPerspective(45.0, float(width)/float(max(1, height)), 0.1, 100.0)
	

	def on_display(self):
		glRotatef(self.phi, 0.0, 1.0, 0.0)
		glRotatef(self.theta, 1.0, 0.0, 0.0)


	def on_motion(self, x, y):
		self.phi = x
		self.theta = y
		glutPostRedisplay()
