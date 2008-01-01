import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/shadow_ambient.txt'
__api_version__ = 0x103

GL_SHADOW_AMBIENT_SGIX = 0x80BF


def glInitShadowAmbientSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_shadow_ambient")


def __info():
	if glInitShadowAmbientSGIX():
		return []
