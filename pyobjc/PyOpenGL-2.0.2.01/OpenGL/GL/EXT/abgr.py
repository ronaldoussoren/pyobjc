import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/abgr.txt'
__api_version__ = 0x10a

GL_ABGR_EXT = 0x8000

def glInitAbgrEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_abgr")


def __info():
	if glInitAbgrEXT():
		return []
