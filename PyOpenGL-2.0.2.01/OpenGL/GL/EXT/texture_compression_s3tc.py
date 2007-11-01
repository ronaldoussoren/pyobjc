import string
__version__ = string.split('$Revision: 1.8 $')[1]
__date__ = string.join(string.split('$Date: 2001/11/17 14:12:34 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_compression_s3tc.txt'
__api_version__ = 0x007


GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 0x83F0
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 0x83F1
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 0x83F2
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 0x83F3

def glInitTextureCompressionS3tcEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_texture_compression_s3tc")

glInitTexCompressionS3tcEXT = glInitTextureCompressionS3tcEXT

def __info():
	if glInitTextureCompressionS3tcEXT():
		return []
