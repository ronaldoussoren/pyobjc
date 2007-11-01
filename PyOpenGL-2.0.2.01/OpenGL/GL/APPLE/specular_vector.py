import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/APPLE/specular_vector.txt'
__api_version__ = 0x101


GL_LIGHT_MODEL_SPECULAR_VECTOR_APPLE = 0x85B0

def glInitSpecularVectorAPPLE():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_APPLE_specular_vector")


def __info():
	if glInitSpecularVectorAPPLE():
		return []

