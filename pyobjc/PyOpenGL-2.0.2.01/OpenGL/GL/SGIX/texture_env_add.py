import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_env_add.txt'
__api_version__ = 0x106

# don't know this value
GL_TEXTURE_ENV_BIAS_SGIX = 0


def glInitTextureEnvAddSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_texture_env_add")

glInitTexEnvAddSGIX = glInitTextureEnvAddSGIX

def __info():
	if glInitTextureEnvAddSGIX():
		return []
