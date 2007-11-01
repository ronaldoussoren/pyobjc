import string
__version__ = string.split('$Revision: 1.8 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_env_dot3.txt'
__api_version__ = 0x102


GL_DOT3_RGB_EXT =                                     0x8740
GL_DOT3_RGBA_EXT =                                    0x8741

def glInitTextureEnvDot3EXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_texture_env_dot3")

glInitTexEnvDot3EXT = glInitTextureEnvDot3EXT

def __info():
	if glInitTextureEnvDot3EXT():
		return []
