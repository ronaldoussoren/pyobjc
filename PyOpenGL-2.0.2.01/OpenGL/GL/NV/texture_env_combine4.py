import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_env_combine4.txt'
__api_version__ = 0x102

GL_COMBINE4_NV = 0x8503

GL_SOURCE3_RGB_NV = 0x8583
GL_SOURCE3_ALPHA_NV = 0x858B
GL_OPERAND3_RGB_NV = 0x8593
GL_OPERAND3_ALPHA_NV = 0x859B


def glInitTextureEnvCombine4NV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_texture_env_combine4")

glInitTexEnvCombine4NV = glInitTextureEnvCombine4NV

def __info():
	if glInitTextureEnvCombine4NV():
		return []
