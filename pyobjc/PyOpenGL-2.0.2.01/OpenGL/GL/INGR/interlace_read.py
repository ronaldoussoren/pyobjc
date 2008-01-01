import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/INGR/interlace_read.txt'
__api_version__ = 0x100


GL_INTERLACE_READ_INGR =                    0x8568


def glInitInterlaceReadINGR():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_INGR_interlace_read")


def __info():
	if glInitInterlaceReadINGR():
		return []
