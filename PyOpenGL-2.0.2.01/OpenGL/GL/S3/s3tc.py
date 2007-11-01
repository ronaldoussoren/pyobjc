import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = ''
__api_version__ = 0x100

GL_RGB_S3TC = 0x83A0
GL_RGB4_S3TC = 0x83A1
GL_RGBA_S3TC = 0x83A2
GL_RGBA4_S3TC = 0x83A3


def glInitS3tcS3():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_S3_s3tc")


def __info():
	if glInitS3tcS3():
		return []
