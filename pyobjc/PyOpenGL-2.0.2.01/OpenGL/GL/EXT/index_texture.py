import string
__version__ = string.split('$Revision: 1.8 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/index_texture.txt'
__api_version__ = 0x104


def glInitIndexTextureEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_index_texture")

glInitIndexTexEXT = glInitIndexTextureEXT

def __info():
	if glInitIndexTextureEXT():
		return []
