import string
__version__ = string.split('$Revision: 1.4 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/3DFX/3dfx_multisample.txt'
__api_version__ = 0x101


WGL_SAMPLE_BUFFERS_3DFX =			    0x2060
WGL_SAMPLES_3DFX =			    0x2061


def wglInitMultisample3DFX():
	from OpenGL.GL import __has_extension
	return __has_extension("WGL_3DFX_multisample")


def __info():
	if wglInitMultisample3DFX():
		return []
