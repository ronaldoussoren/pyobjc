import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIS/texture_border_clamp.txt'
__api_version__ = 0x106

GL_CLAMP_TO_BORDER_SGIS = 0x812D

def glInitTextureBorderClampSGIS():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIS_texture_border_clamp")

glInitTexBorderClampSGIS = glInitTextureBorderClampSGIS

def __info():
	if glInitTextureBorderClampSGIS():
		return []
