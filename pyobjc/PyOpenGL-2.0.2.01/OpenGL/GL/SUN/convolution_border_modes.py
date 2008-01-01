import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SUN/convolution_border_modes.txt'
__api_version__ = 0x103


GL_WRAP_BORDER_SUN = 				0x81D4

def glInitConvolutionBorderModesSUN():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SUN_convolution_border_modes")


def __info():
	if glInitConvolutionBorderModesSUN():
		return []
