import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/IBM/texture_mirrored_repeat.txt'
__api_version__ = 0x102


GL_MIRRORED_REPEAT_IBM = 0x8370


def glInitTextureMirroredRepeatIBM():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_IBM_texture_mirrored_repeat")

glInitTexMirroredRepeatIBM = glInitTextureMirroredRepeatIBM

def __info():
	if glInitTextureMirroredRepeatIBM():
		return []
