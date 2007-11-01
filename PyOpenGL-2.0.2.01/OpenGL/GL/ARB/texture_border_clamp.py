import string
__version__ = string.split('$Revision: 1.10 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_border_clamp.txt'
__api_version__ = 0x100

GL_CLAMP_TO_BORDER_ARB = 0x812D

def glInitTextureBorderClampARB():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_ARB_texture_border_clamp")

glInitTexBorderClampARB = glInitTextureBorderClampARB

def __info():
	if glInitTextureBorderClampARB():
		return []

