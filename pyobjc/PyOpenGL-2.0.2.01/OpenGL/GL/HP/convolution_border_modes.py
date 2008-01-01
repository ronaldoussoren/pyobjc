import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/HP/convolution_border_modes.txt'
__api_version__ = 0x103


GL_IGNORE_BORDER_HP = 0x8150
GL_CONSTANT_BORDER_HP = 0x8151
GL_REPLICATE_BORDER_HP = 0x8153
GL_CONVOLUTION_BORDER_COLOR_HP = 0x8154


def glInitConvolutionBorderModesHP():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_HP_convolution_border_modes")


def __info():
	if glInitConvolutionBorderModesHP():
		return []

