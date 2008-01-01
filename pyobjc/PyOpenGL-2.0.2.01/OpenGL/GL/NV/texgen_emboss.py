import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/texgen_emboss.txt'
__api_version__ = 0x100

GL_EMBOSS_MAP_NV = 0x855F

GL_EMBOSS_LIGHT_NV = 0x855D
GL_EMBOSS_CONSTANT_NV = 0x855E


def glInitTexgenEmbossNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_texgen_emboss")


def __info():
	if glInitTexgenEmbossNV():
		return []
