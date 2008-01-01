import string
__version__ = string.split('$Revision: 1.7 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/shared_texture_palette.txt'
__api_version__ = 0x102


GL_SHARED_TEXTURE_PALETTE_EXT = 0x81FB

def glInitSharedTexturePaletteEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_shared_texture_palette")

glInitSharedTexPaletteEXT = glInitSharedTexturePaletteEXT

def __info():
	if glInitSharedTexturePaletteEXT():
		return []
