import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/shadow.txt'
__api_version__ = 0x10f

GL_TEXTURE_COMPARE_SGIX           = 0x819A
GL_TEXTURE_COMPARE_OPERATOR_SGIX  = 0x819B
GL_TEXTURE_LEQUAL_R_SGIX          = 0x819C
GL_TEXTURE_GEQUAL_R_SGIX          = 0x819D


def glInitShadowSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_shadow")


def __info():
	if glInitShadowSGIX():
		return []
