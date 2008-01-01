import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/blend_square.txt'
__api_version__ = 0x101


def glInitBlendSquareNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_blend_square")


def __info():
	if glInitBlendSquareNV():
		return []
