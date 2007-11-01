import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/3DFX/3dfx_multisample.txt'
__api_version__ = 0x101


GL_MULTISAMPLE_3DFX = 			    0x86B2

GL_SAMPLE_BUFFERS_3DFX =			    0x86B3
GL_SAMPLES_3DFX =				    0x86B4

GL_MULTISAMPLE_BIT_3DFX =			    0x20000000


def glInitMultisample3DFX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_3DFX_multisample")


def __info():
	if glInitMultisample3DFX():
		return []
