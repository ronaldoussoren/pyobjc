import string
__version__ = string.split('$Revision: 1.1 $')[1]
__date__ = string.join(string.split('$Date: 2001/09/26 17:09:12 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/NV/copy_depth_to_color.txt'
__api_version__ = 0x100


GL_DEPTH_STENCIL_TO_RGBA_NV = 0x886E
GL_DEPTH_STENCIL_TO_BGRA_NV = 0x886F

        
def glInitCopyDepthToColorNV():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_NV_copy_depth_to_color")


def __info():
	if glInitCopyDepthToColorNV():
		return []
