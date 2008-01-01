import string
__version__ = string.split('$Revision: 1.7 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/index_array_formats.txt'
__api_version__ = 0x103

GL_IUI_V2F_EXT = 0x81AD
GL_IUI_V3F_EXT = 0x81AE
GL_IUI_N3F_V2F_EXT = 0x81AF
GL_IUI_N3F_V3F_EXT = 0x81B0
GL_T2F_IUI_V2F_EXT = 0x81B1
GL_T2F_IUI_V3F_EXT = 0x81B2
GL_T2F_IUI_N3F_V2F_EXT = 0x81B3
GL_T2F_IUI_N3F_V3F_EXT = 0x81B4

def glInitIndexArrayFormatsEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_index_array_formats")


def __info():
	if glInitIndexArrayFormatsEXT():
		return []
