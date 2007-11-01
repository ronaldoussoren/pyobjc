import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/fog_distance.txt'
__api_version__ = 0x100

GL_FOG_DISTANCE_MODE_NV = 0x855A

GL_EYE_RADIAL_NV = 0x855B
GL_EYE_PLANE_ABSOLUTE_NV = 0x855C



def glInitFogDistanceNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_fog_distance")


def __info():
	if glInitFogDistanceNV():
		return []
