import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/blend_subtract.txt'
__api_version__ = 0x104

GL_FUNC_SUBTRACT_EXT = 0x800A
GL_FUNC_REVERSE_SUBTRACT_EXT = 0x800B

def glInitBlendSubtractEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_blend_subtract")


def __info():
	if glInitBlendSubtractEXT():
		return []
