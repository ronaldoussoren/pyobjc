import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/blend_alpha_minmax.txt'
__api_version__ = 0x103

GL_ALPHA_MIN_SGIX = 0x8320
GL_ALPHA_MAX_SGIX = 0x8321

def glInitBlendAphaMinmaxSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_blend_alpha_minmax")


def __info():
	if glInitBlendAphaMinmaxSGIX():
		return []
