import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/ycrcb.txt'
__api_version__ = 0x102

GL_YCRCB_422_SGIX = 0x81BB
GL_YCRCB_444_SGIX = 0x81BC

def glInitYcrcbSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_ycrcb")


def __info():
	if glInitYcrcbSGIX():
		return []
