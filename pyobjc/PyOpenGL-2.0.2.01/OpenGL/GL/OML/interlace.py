import string
__version__ = string.split('$Revision: 1.3 $')[1]
__date__ = string.join(string.split('$Date: 2001/09/26 16:36:36 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/OML/interlace.txt'
__api_version__ = 0x100

GL_INTERLACE_OML = 0x8980
GL_INTERLACE_READ_OML = 0x8981

def glInitInterlaceOML():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_OML_interlace")


def __info():
	if glInitInterlaceOML():
		return []
