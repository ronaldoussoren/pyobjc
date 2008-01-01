import string
__version__ = string.split('$Revision: 1.8 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_lod_bias.txt'
__api_version__ = 0x100


GL_TEXTURE_FILTER_CONTROL_EXT = 0x8500

GL_TEXTURE_LOD_BIAS_EXT = 0x8501

def glInitTextureLodBiasEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_texture_lod_bias")

glInitTexLodBiasEXT = glInitTextureLodBiasEXT

def __info():
	if glInitTextureLodBiasEXT():
		return []
