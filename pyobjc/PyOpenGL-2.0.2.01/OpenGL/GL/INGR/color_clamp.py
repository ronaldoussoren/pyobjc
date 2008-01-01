import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/INGR/color_clamp.txt'
__api_version__ = 0x101


GL_RED_MIN_CLAMP_INGR =                   0x8560
GL_GREEN_MIN_CLAMP_INGR =                 0x8561
GL_BLUE_MIN_CLAMP_INGR =                  0x8562
GL_ALPHA_MIN_CLAMP_INGR =                 0x8563
GL_RED_MAX_CLAMP_INGR =                   0x8564
GL_GREEN_MAX_CLAMP_INGR =                 0x8565
GL_BLUE_MAX_CLAMP_INGR =                  0x8566
GL_ALPHA_MAX_CLAMP_INGR =                 0x8567

GL_RED_MIN_CLAMP_INGR =                   0x8560
GL_GREEN_MIN_CLAMP_INGR =                 0x8561
GL_BLUE_MIN_CLAMP_INGR =                  0x8562
GL_ALPHA_MIN_CLAMP_INGR =                 0x8563
GL_RED_MAX_CLAMP_INGR =                   0x8564
GL_GREEN_MAX_CLAMP_INGR =                 0x8565
GL_BLUE_MAX_CLAMP_INGR =                  0x8566
GL_ALPHA_MAX_CLAMP_INGR =                 0x8567


def glInitColorClampINGR():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_INGR_color_clamp")



def __info():
	if glInitColorClampINGR():
		return []
