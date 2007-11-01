import string
__version__ = string.split('$Revision: 1.1 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:13:00 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/pixel_transform_color_table.txt'
__api_version__ = 0x101


# don't know these values
GL_PIXEL_TRANSFORM_COLOR_TABLE_EXT = 0

GL_PROXY_PIXEL_TRANSFORM_COLOR_TABLE_EXT = 0


def glInitPixelTransformColorTableEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_pixel_transform_color_table")


def __info():
	if glInitPixelTransformColorTableEXT():
		return []
