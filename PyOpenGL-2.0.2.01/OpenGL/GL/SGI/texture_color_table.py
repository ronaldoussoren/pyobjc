import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGI/texture_color_table.txt'
__api_version__ = 0x110

GL_TEXTURE_COLOR_TABLE_SGI = 0x80BC
GL_PROXY_TEXTURE_COLOR_TABLE_SGI = 0x80BD


def glInitTextureColorTableSGI():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGI_texture_color_table")

glInitTexColorTableSGI = glInitTextureColorTableSGI

def __info():
	if glInitTextureColorTableSGI():
		return []
