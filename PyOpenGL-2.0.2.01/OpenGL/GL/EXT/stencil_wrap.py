import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/stencil_wrap.txt'
__api_version__ = 0x101


GL_INCR_WRAP_EXT = 0x8507
GL_DECR_WRAP_EXT = 0x8508

def glInitStencilWrapEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_stencil_wrap")


def __info():
	if glInitStencilWrapEXT():
		return []
