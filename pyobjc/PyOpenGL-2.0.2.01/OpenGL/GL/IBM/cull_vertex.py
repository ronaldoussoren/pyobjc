import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/IBM/cull_vertex.txt'
__api_version__ = 0x104


GL_CULL_VERTEX_IBM = 103050

def glInitCullVertexIBM():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_IBM_cull_vertex")


def __info():
	if glInitCullVertexIBM():
		return []
