import string
__version__ = string.split('$Revision: 1.11 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_env_crossbar.txt'
__api_version__ = 0x100

GL_TEXTURE0_ARB = 0x84C0

def glInitTextureEnvCrossbarARB():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_ARB_texture_env_crossbar")

glInitTexEnvCrossbarARB = glInitTextureEnvCrossbarARB

def __info():
	if glInitTextureEnvCrossbarARB():
		return []

