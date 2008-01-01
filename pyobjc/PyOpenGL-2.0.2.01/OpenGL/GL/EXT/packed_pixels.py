import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/packed_pixels.txt'
__api_version__ = 0x115

GL_UNSIGNED_BYTE_3_3_2_EXT = 0x8032
GL_UNSIGNED_SHORT_4_4_4_4_EXT = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1_EXT = 0x8034
GL_UNSIGNED_INT_8_8_8_8_EXT = 0x8035
GL_UNSIGNED_INT_10_10_10_2_EXT = 0x8036

def glInitPackedPixelsEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_packed_pixels")


def __info():
	if glInitPackedPixelsEXT():
		return []
