import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/IBM/rasterpos_clip.txt'
__api_version__ = 0x100

GL_RASTER_POSITION_UNCLIPPED_IBM = 103010


def glInitRasterposClipIBM():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_IBM_rasterpos_clip")


def __info():
	if glInitRasterposClipIBM():
		return []
