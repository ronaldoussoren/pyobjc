import string
__version__ = string.split('$Revision: 1.9 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/09 19:30:29 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGI/color_matrix.txt'
__api_version__ = 0x108

GL_COLOR_MATRIX_SGI = 0x80B1
GL_COLOR_MATRIX_STACK_DEPTH_SGI = 0x80B2
GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI = 0x80B3

GL_POST_COLOR_MATRIX_RED_SCALE_SGI = 0x80B4
GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI = 0x80B5
GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI = 0x80B6
GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI = 0x80B7
GL_POST_COLOR_MATRIX_RED_BIAS_SGI = 0x80B8
GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI = 0x80B9
GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI = 0x80BA
GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI = 0x80BB


def glInitColorMatrixSGI():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGI_color_matrix")


def __info():
	if glInitColorMatrixSGI():
		return [('GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI', GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI, 'i')]
