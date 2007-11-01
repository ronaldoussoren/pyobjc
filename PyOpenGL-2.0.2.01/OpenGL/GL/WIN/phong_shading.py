import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/WIN/phong_shading.txt'
__api_version__ = 0x100

GL_PHONG_WIN = 0x80EA
GL_PHONG_HINT_WIN = 0x80EB

def glInitPhongShadingWIN():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_WIN_phong_shading")


def __info():
	if glInitPhongShadingWIN():
		return []
