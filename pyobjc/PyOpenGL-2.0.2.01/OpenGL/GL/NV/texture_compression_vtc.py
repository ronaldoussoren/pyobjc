import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_compression_vtc.txt'
__api_version__ = 0x100


GL_COMPRESSED_RGB_S3TC_DXT1_EXT =                    0x83F0
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT =                   0x83F1
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT =                   0x83F2
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT =                   0x83F3

def glInitTextureCompressionVtcNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_texture_compression_vtc")

glInitTexCompressionVtcNV = glInitTextureCompressionVtcNV

def __info():
	if glInitTextureCompressionVtcNV():
		return []
