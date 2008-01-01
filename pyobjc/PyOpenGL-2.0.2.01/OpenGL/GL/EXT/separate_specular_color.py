import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/separate_specular_color.txt'
__api_version__ = 0x103


GL_LIGHT_MODEL_COLOR_CONTROL_EXT = 0x81F8

GL_SINGLE_COLOR_EXT = 0x81F9
GL_SEPARATE_SPECULAR_COLOR_EXT = 0x81FA

def glInitSeparateSpecularColorEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_separate_specular_color")


def __info():
	if glInitSeparateSpecularColorEXT():
		return []
