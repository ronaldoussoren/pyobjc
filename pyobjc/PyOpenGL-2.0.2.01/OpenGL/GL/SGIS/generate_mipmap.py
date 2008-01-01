import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIS/generate_mipmap.txt'
__api_version__ = 0x106

GL_GENERATE_MIPMAP_SGIS = 0x8191
GL_GENERATE_MIPMAP_HINT_SGIS = 0x8192

def glInitGenerateMipmapSGIS():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIS_generate_mipmap")

glInitGenerateMipmapSGIS = glInitGenMipmapSGIS

def __info():
	if glInitGenerateMipmapSGIS():
		return []
