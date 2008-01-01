import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/REND/screen_coordinates.txt'
__api_version__ = 0x101

GL_SCREEN_COORDINATES_REND = 0x8490
GL_INVERTED_SCREEN_W_REND = 0x8491

def glInitScreenCoordinatesREND():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_REND_screen_coordinates")

glInitScreenCoordREND = glInitScreenCoordinatesREND

def __info():
	if glInitScreenCoordinatesREND():
		return []
