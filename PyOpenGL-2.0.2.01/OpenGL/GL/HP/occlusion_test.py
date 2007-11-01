import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/HP/occlusion_test.txt'
__api_version__ = 0x100

GL_OCCLUSION_TEST_HP = 0x8165
GL_OCCLUSION_TEST_RESULT_HP = 0x8166


def glInitOcclusionTestHP():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_HP_occlusion_test")



def __info():
	if glInitOcclusionTestHP():
		return []
