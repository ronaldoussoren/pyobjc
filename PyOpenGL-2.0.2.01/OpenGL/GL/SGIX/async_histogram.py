import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/async_histogram.txt'
__api_version__ = 0x103


GL_ASYNC_HISTOGRAM_SGIX = 0x832C

GL_MAX_ASYNC_HISTOGRAM_SGIX = 0x832D


def glInitAsyncHistogramSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_async_histogram")


def __info():
	if glInitAsyncHistogramSGIX():
		return []
