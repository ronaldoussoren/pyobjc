import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIS/texture_edge_clamp.txt'
__api_version__ = 0x106

GL_CLAMP_TO_EDGE_SGIS = 0x812F

def glInitTextureEdgeClampSGIS():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIS_texture_edge_clamp")

glInitTexEdgeClampSGIS = glInitTextureEdgeClampSGIS

def __info():
	if glInitTextureEdgeClampSGIS():
		return []
