import string
__version__ = string.split('$Revision: 1.3 $')[1]
__date__ = string.join(string.split('$Date: 2001/09/26 16:36:36 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/OML/resample.txt'
__api_version__ = 0x100

GL_PACK_RESAMPLE_OML = 0x8984
GL_UNPACK_RESAMPLE_OML = 0x8985

GL_RESAMPLE_REPLICATE_OML = 0x8986
GL_RESAMPLE_ZERO_FILL_OML = 0x8987
GL_RESAMPLE_AVERAGE_OML = 0x8988

GL_RESAMPLE_DECIMATE_OML = 0x8989
GL_RESAMPLE_AVERAGE_OML = 0x8988

def glInitResampleOML():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_OML_resample")


def __info():
	if glInitResampleOML():
		return []
