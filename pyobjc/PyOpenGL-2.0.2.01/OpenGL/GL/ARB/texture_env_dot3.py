import string
__version__ = string.split('$Revision: 1.10 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_env_dot3.txt'
__api_version__ = 0x100

GL_DOT3_RGB_ARB = 0x86AE
GL_DOT3_RGBA_ARB = 0x86AF

def glInitTextureEnvDot3ARB():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_ARB_texture_env_dot3")

glInitTexEnvDot3ARB = glInitTextureEnvDot3ARB

def __info():
	if glInitTextureEnvDot3ARB():
		return []

