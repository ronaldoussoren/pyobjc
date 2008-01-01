import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/object_space_tess.txt'
__api_version__ = 0x100

GLU_OBJECT_PARAMETRIC_ERROR_EXT = 100208 
GLU_OBJECT_PATH_LENGTH_EXT = 100209

def gluInitObjectSpaceTessEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GLU_EXT_object_space_tess")


def __info():
	if gluInitObjectSpaceTessEXT():
		return []
