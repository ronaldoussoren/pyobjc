import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/cmyka.txt'
__api_version__ = 0x111

GL_CMYK_EXT = 0x800C
GL_CMYKA_EXT = 0x800D
GL_PACK_CMYK_HINT_EXT = 0x800E
GL_UNPACK_CMYK_HINT_EXT = 0x800F

def glInitCmykaEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_cmyka")


def __info():
	if glInitCmykaEXT():
		return []
