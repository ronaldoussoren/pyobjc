import string
__version__ = string.split('$Revision: 1.7 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ATI/texture_mirror_once.txt'
__api_version__ = 0x003


GL_MIRROR_CLAMP_ATI =                      0x8742
GL_MIRROR_CLAMP_TO_EDGE_ATI =              0x8743

def glInitTextureMirrorOnceATI():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_ATI_texture_mirror_once")

glInitTexMirrorOnceATI = glInitTextureMirrorOnceATI

def __info():
	if glInitTextureMirrorOnceATI():
		return []
