import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/async_pixel.txt'
__api_version__ = 0x107


GL_ASYNC_TEX_IMAGE_SGIX = 0x835C
GL_ASYNC_DRAW_PIXELS_SGIX = 0x835D
GL_ASYNC_READ_PIXELS_SGIX = 0x835E

GL_MAX_ASYNC_TEX_IMAGE_SGIX = 0x835F
GL_MAX_ASYNC_DRAW_PIXELS_SGIX = 0x8360
GL_MAX_ASYNC_READ_PIXELS_SGIX = 0x8361

def glInitAsyncPixelSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_async_pixel")


def __info():
	if glInitAsyncPixelSGIX():
		return [('GL_MAX_ASYNC_TEX_IMAGE_SGIX', GL_MAX_ASYNC_TEX_IMAGE_SGIX, 'i'),
		        ('GL_MAX_ASYNC_DRAW_PIXELS_SGIX', GL_MAX_ASYNC_DRAW_PIXELS_SGIX, 'i'),
		        ('GL_MAX_ASYNC_READ_PIXELS_SGIX', GL_MAX_ASYNC_READ_PIXELS_SGIX, 'i')]
