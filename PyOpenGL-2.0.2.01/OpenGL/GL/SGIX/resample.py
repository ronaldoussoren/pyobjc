import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/resample.txt'
__api_version__ = 0x100


GL_PACK_RESAMPLE_SGIX = 0x842E
GL_UNPACK_RESAMPLE_SGIX = 0x842F

GL_RESAMPLE_REPLICATE_SGIX = 0x8433
GL_RESAMPLE_ZERO_FILL_SGIX = 0x8434

GL_RESAMPLE_DECIMATE_SGIX = 0x8430


def glInitResampleSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_resample")


def __info():
	if glInitResampleSGIX():
		return []
