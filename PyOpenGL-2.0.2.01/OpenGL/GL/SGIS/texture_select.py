import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIS/texture_select.txt'
__api_version__ = 0x10b

GL_DUAL_ALPHA4_SGIS               = 0x8110
GL_DUAL_ALPHA8_SGIS               = 0x8111
GL_DUAL_ALPHA12_SGIS              = 0x8112
GL_DUAL_ALPHA16_SGIS              = 0x8113
GL_DUAL_LUMINANCE4_SGIS           = 0x8114
GL_DUAL_LUMINANCE8_SGIS           = 0x8115
GL_DUAL_LUMINANCE12_SGIS          = 0x8116
GL_DUAL_LUMINANCE16_SGIS          = 0x8117
GL_DUAL_INTENSITY4_SGIS           = 0x8118
GL_DUAL_INTENSITY8_SGIS           = 0x8119
GL_DUAL_INTENSITY12_SGIS          = 0x811A
GL_DUAL_INTENSITY16_SGIS          = 0x811B
GL_DUAL_LUMINANCE_ALPHA4_SGIS     = 0x811C
GL_DUAL_LUMINANCE_ALPHA8_SGIS     = 0x811D
GL_QUAD_ALPHA4_SGIS               = 0x811E
GL_QUAD_ALPHA8_SGIS               = 0x811F
GL_QUAD_LUMINANCE4_SGIS           = 0x8120
GL_QUAD_LUMINANCE8_SGIS           = 0x8121
GL_QUAD_INTENSITY4_SGIS           = 0x8122
GL_QUAD_INTENSITY8_SGIS           = 0x8123
GL_DUAL_TEXTURE_SELECT_SGIS       = 0x8124
GL_QUAD_TEXTURE_SELECT_SGIS       = 0x8125


def glInitTextureSelectSGIS():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIS_texture_select")

glInitTexSelectSGIS = glInitTextureSelectSGIS

def __info():
	if glInitTextureSelectSGIS():
		return []
