import string
__version__ = string.split('$Revision: 1.12 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_env_add.txt'
__api_version__ = 0x106

def glInitTextureEnvAddEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_texture_env_add")

glInitTexEnvAddEXT = glInitTextureEnvAddEXT

def __info():
	if glInitTextureEnvAddEXT():
		return []
