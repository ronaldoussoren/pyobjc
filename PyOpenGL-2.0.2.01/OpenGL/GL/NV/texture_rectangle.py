import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_rectangle.txt'
__api_version__ = 0x100


GL_TEXTURE_RECTANGLE_NV =                0x84F5

GL_TEXTURE_BINDING_RECTANGLE_NV  =        0x84F6

GL_PROXY_TEXTURE_RECTANGLE_NV =           0x84F7 

GL_MAX_RECTANGLE_TEXTURE_SIZE_NV =        0x84F8

def glInitTextureRectangleNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_texture_rectangle")

glInitTextureRectNV = glInitTextureRectangleNV
glInitTexRectNV = glInitTextureRectangleNV
glInitTexRectangleNV = glInitTextureRectangleNV

def __info():
	if glInitTextureRectangleNV():
		return [('GL_MAX_RECTANGLE_TEXTURE_SIZE_NV', GL_MAX_RECTANGLE_TEXTURE_SIZE_NV, 'i')]
