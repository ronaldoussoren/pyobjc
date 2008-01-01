import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/09/12 22:43:29 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/ARB/multisample.txt'
__api_version__ = 0x005

WGL_SAMPLE_BUFFERS_ARB = 0x2041
WGL_SAMPLES_ARB = 0x2042

def wglInitMultisampleARB():
	from OpenGL.GL import __has_extension
	return __has_extension("WGL_ARB_multisample")

def __info():
	if wglInitMultisampleARB():
		return []

