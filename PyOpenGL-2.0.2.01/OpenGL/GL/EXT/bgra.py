import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/bgra.txt'
__api_version__ = 0x104

GL_BGR_EXT = 0x80E0
GL_BGRA_EXT = 0x80E1

def glInitBgraEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_bgra")


def __info():
	if glInitBgraEXT():
		return []
