import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/ir_instrument1.txt'
__api_version__ = 0x104

GL_IR_INSTRUMENT1_SGIX = 0x817F

def glInitIrInstrument1SGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_ir_instrument1")


def __info():
	if glInitIrInstrument1SGIX():
		return []
