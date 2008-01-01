import string
__version__ = string.split('$Revision: 1.1 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/25 15:48:05 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://developer.nvidia.com/docs/IO/1174/ATT/nvOpenGLspecs.pdf'
__api_version__ = 0x106

GL_CLAMP_TO_EDGE_EXT = 0x812F

def glInitTextureEdgeClampEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_texture_edge_clamp")

glInitTexEdgeClampEXT = glInitTextureEdgeClampEXT

def __info():
	if glInitTextureEdgeClampEXT():
		return []
