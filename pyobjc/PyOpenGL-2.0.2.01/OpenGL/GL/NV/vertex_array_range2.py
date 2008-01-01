import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/vertex_array_range2.txt'
__api_version__ = 0x100


GL_VERTEX_ARRAY_RANGE_WITHOUT_FLUSH_NV = 0x8533


def glInitVertexArrayRange2NV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_vertex_array_range2")


def __info():
	if glInitVertexArrayRange2NV():
		return []
