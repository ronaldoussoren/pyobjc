import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_lod_bias.txt'
__api_version__ = 0x103

GL_TEXTURE_LOD_BIAS_S_SGIX = 0x818E
GL_TEXTURE_LOD_BIAS_T_SGIX = 0x818F
GL_TEXTURE_LOD_BIAS_R_SGIX = 0x8190

def glInitTextureLodBiasSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_texture_lod_bias")

glInitTexLodBiasSGIX = glInitTextureLodBiasSGIX

def __info():
	if glInitTextureLodBiasSGIX():
		return []
