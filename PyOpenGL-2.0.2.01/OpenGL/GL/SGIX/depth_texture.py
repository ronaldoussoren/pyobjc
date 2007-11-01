import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/depth_texture.txt'
__api_version__ = 0x105

GL_DEPTH_COMPONENT16_SGIX = 0x81A5
GL_DEPTH_COMPONENT24_SGIX = 0x81A6
GL_DEPTH_COMPONENT32_SGIX = 0x81A7


def glInitDepthTextureSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_depth_texture")

glInitDepthTexSGIX = glInitDepthTextureSGIX

def __info():
	if glInitDepthTextureSGIX():
		return []
