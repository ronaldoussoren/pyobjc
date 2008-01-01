import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/WIN/specular_fog.txt'
__api_version__ = 0x100


GL_FOG_SPECULAR_TEXTURE_WIN = 0x80EC

def glInitSpecularFogWIN():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_WIN_specular_fog")


def __info():
	if glInitSpecularFogWIN():
		return []
