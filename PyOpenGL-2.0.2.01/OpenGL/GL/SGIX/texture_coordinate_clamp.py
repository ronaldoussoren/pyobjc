import string
__version__ = string.split('$Revision: 1.1 $')[1]
__date__ = string.join(string.split('$Date: 2001/09/26 16:46:27 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_coordinate_clamp.txt'
__api_version__ = 0x102


GL_TEXTURE_MAX_CLAMP_S_SGIX = 0x8369
GL_TEXTURE_MAX_CLAMP_T_SGIX = 0x836A
GL_TEXTURE_MAX_CLAMP_R_SGIX = 0x836B


def glInitTexCoordClampSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_texture_coordinate_clamp")


def __info():
	if glInitTexCoordClampSGIX():
		return []
