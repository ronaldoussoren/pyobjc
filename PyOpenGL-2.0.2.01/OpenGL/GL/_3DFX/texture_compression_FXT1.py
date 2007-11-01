import string
__version__ = string.split('$Revision: 1.7 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/3DFX/texture_compression_FXT1.txt'
__api_version__ = 0x004


GL_COMPRESSED_RGB_FXT1_3DFX = 0x86B0
GL_COMPRESSED_RGBA_FXT1_3DFX = 0x86B1


# And GL's name mangling strategy produces yet another cryptic proto!
def glInitTextureCompressionFXT13DFX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_3DFX_texture_compression_FXT1")

glInitTexCompressionFXT13DFX = glInitTextureCompressionFXT13DFX

def __info():
	if glInitTexturenCompressionFXT13DFX():
		return []
