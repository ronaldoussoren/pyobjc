import string
__version__ = string.split('$Revision: 1.4 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/wgl_depth_float.txt'
__api_version__ = 0x104


WGL_DEPTH_FLOAT_EXT = 0x2040


def wglInitDepthFloatEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("WGL_EXT_depth_float")


def __info():
	if wglInitDepthFloatEXT():
		return []
