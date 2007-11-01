#!

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys, types
import items


def on_motion(x, y):
	global current_item
	current_item.on_motion(x, y)


def on_display():
	global current_item
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	current_item.on_display()
	glutSwapBuffers()


def on_idle():
	global current_item
	if current_item.on_idle():
		glutPostRedisplay()	


def on_reshape(width, height):
	global current_item
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	current_item.on_reshape(width, height)


def on_item(value):
	global item_list, current_item
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	del current_item
	current_item = item_list[value]()
	on_reshape(glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT))
	glutPostRedisplay()


def create_menu(i):
	global item_list
	k = i.keys()
	k.sort()
	id = glutCreateMenu(on_item)
	for key in k:
		if isinstance(i[key], types.DictionaryType):
			subid = create_menu(i[key])
			glutSetMenu(id)
			glutAddSubMenu(key, subid)
		else:
			glutAddMenuEntry(key, len(item_list))
			item_list.append(i[key])
	return id
	

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
window = glutCreateWindow('set')
glutDisplayFunc(on_display)
glutIdleFunc(on_idle)
glutReshapeFunc(on_reshape)
glutMotionFunc(on_motion)

item_list = []

create_menu(items.get_items())
glutAttachMenu(GLUT_RIGHT_BUTTON)

current_item = item_list[0]()

glutMainLoop()
