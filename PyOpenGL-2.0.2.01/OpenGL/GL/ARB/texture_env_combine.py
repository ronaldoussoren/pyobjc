import string
__version__ = string.split('$Revision: 1.10 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_env_combine.txt'
__api_version__ = 0x100

GL_COMBINE_ARB = 0x8570

GL_COMBINE_RGB_ARB = 0x8571
GL_COMBINE_ALPHA_ARB = 0x8572
GL_SOURCE0_RGB_ARB = 0x8580
GL_SOURCE1_RGB_ARB = 0x8581
GL_SOURCE2_RGB_ARB = 0x8582
GL_SOURCE0_ALPHA_ARB = 0x8588
GL_SOURCE1_ALPHA_ARB = 0x8589
GL_SOURCE2_ALPHA_ARB = 0x858A
GL_OPERAND0_RGB_ARB= 0x8590
GL_OPERAND1_RGB_ARB= 0x8591
GL_OPERAND2_RGB_ARB= 0x8592
GL_OPERAND0_ALPHA_ARB = 0x8598
GL_OPERAND1_ALPHA_ARB = 0x8599
GL_OPERAND2_ALPHA_ARB = 0x859A
GL_RGB_SCALE_ARB = 0x8573

GL_ADD_SIGNED_ARB = 0x8574
GL_INTERPOLATE_ARB = 0x8575
GL_SUBTRACT_ARB = 0x84E7

GL_CONSTANT_ARB = 0x8576
GL_PRIMARY_COLOR_ARB = 0x8577
GL_PREVIOUS_ARB = 0x8578

def glInitTextureEnvCombineARB():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_ARB_texture_env_combine")

glInitTexEnvCombineARB = glInitTextureEnvCombineARB

def __info():
	if glInitTextureEnvCombineARB():
		return []

