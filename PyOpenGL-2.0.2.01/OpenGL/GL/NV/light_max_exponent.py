import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/light_max_exponent.txt'
__api_version__ = 0x100

GL_MAX_SHININESS_NV = 0x8504
GL_MAX_SPOT_EXPONENT_NV = 0x8505


def glInitLightMaxExponentNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_light_max_exponent")


def __info():
	if glInitLightMaxExponentNV():
		return [('GL_MAX_SHININESS_NV', GL_MAX_SHININESS_NV, 'i'),
		        ('GL_MAX_SPOT_EXPONENT_NV', GL_MAX_SPOT_EXPONENT_NV, 'i')]
