import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/fog_offset.txt'
__api_version__ = 0x10c

GL_FOG_OFFSET_SGIX = 0x8198
GL_FOG_OFFSET_VALUE_SGIX = 0x8199

def glInitFogOffsetSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_fog_offset")


def __info():
	if glInitFogOffsetSGIX():
		return []
