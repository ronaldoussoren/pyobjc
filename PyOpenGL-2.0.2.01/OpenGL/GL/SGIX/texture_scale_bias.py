import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_scale_bias.txt'
__api_version__ = 0x109

GL_POST_TEXTURE_FILTER_BIAS_SGIX = 0x8179
GL_POST_TEXTURE_FILTER_SCALE_SGIX = 0x817A

GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX = 0x817B
GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX = 0x817C

def glInitTextureScaleBiasSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_texture_scale_bias")

glInitTexScaleBiasSGIX = glInitTextureScaleBiasSGIX

def __info():
	if glInitTextureScaleBiasSGIX():
		return []
