import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/pixel_texture_bits.txt'
__api_version__ = 0x10b


# don't know these values
GL_COLOR_TO_TEXTURE_COORD_SGIX = 0

GL_COLOR_BIT_PATTERN_SGIX = 0
GL_COLOR_VALUE_SGIX = 0


def glInitPixelTextureBitsSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_pixel_texture_bits")

glInitPixelTexBitsSGIX = glInitPixelTextureBitsSGIX

def __info():
	if glInitPixelTextureBitsSGIX():
		return []
