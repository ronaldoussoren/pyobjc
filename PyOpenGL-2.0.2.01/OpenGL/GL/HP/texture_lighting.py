import string
__version__ = string.split('$Revision: 1.7 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/HP/texture_lighting.txt'
__api_version__ = 0x100

GL_TEXTURE_LIGHTING_MODE_HP = 0x8167
GL_TEXTURE_POST_SPECULAR_HP = 0x8168
GL_TEXTURE_PRE_SPECULAR_HP = 0x8169


def glInitTextureLightingHP():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_HP_texture_lighting")

glInitTexLightingHP = glInitTextureLightingHP

def __info():
	if glInitTextureLightingHP():
		return []
