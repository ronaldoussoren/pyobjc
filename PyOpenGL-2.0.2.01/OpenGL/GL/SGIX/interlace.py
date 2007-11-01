import string
__version__ = string.split('$Revision: 1.8 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/interlace.txt'
__api_version__ = 0x102

GL_INTERLACE_SGIX = 0x8094

def glInitInterlaceSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_interlace")


def __info():
	if glInitInterlaceSGIX():
		return []
