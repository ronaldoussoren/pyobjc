import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/packed_depth_stencil.txt'
__api_version__ = 0x100


GL_DEPTH_STENCIL_NV =                                0x84F9

GL_UNSIGNED_INT_24_8_NV =                            0x84FA


def glInitPackedDepthStencilNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_packed_depth_stencil")


def __info():
	if glInitPackedDepthStencilNV():
		return []
