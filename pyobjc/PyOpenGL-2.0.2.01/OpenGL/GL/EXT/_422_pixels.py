import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/422_pixels.txt'
__api_version__ = 0x102


GL_422_EXT =                             0x80CC
GL_422_REV_EXT =                         0x80CD
GL_422_AVERAGE_EXT =                     0x80CE
GL_422_REV_AVERAGE_EXT =                 0x80CF


def glInit422PixelsEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_422_pixels")


def __info():
	if glInit422PixelsEXT():
		return []
