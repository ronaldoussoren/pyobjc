import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/vertex_preclip.txt'
__api_version__ = 0x100


GL_VERTEX_PRECLIP_SGIX = 0x83EE

GL_VERTEX_PRECLIP_HINT_SGIX = 0x83EF

def glInitVertexPreclipSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_vertex_preclip")


def __info():
	if glInitVertexPreclipSGIX():
		return []
