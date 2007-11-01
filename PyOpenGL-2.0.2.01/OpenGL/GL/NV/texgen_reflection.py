import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/texgen_reflection.txt'
__api_version__ = 0x100

GL_NORMAL_MAP_NV = 0x8511
GL_REFLECTION_MAP_NV = 0x8512

def glInitTexgenReflectionNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_texgen_reflection")


def __info():
	if glInitTexgenReflectionNV():
		return []
