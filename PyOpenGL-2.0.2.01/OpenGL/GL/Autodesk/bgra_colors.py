import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://www.autodesk.com/develop/devres/heidi/oglspecs.htm'
__api_version__ = 0x100

GL_BGRA_COLORS = 0x85D3 


def glInitBgraColorsAutodesk():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_Autodesk_bgra_colors")


def __info():
	if glInitBgraColorsAutodesk():
		return []
