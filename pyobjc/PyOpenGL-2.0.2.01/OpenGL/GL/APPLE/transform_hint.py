import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/APPLE/transform_hint.txt'
__api_version__ = 0x102


GL_TRANSFORM_HINT_APPLE = 0x85B1

def glInitTransformHintAPPLE():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_APPLE_transform_hint")


def __info():
	if glInitTransformHintAPPLE():
		return []

