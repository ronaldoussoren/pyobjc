import string
__version__ = string.split('$Revision: 1.10 $')[1]
__date__ = string.join(string.split('$Date: 2001/08/10 18:42:33 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/misc_attribute.txt'
__api_version__ = 0x105

#don't know this value
GL_MISC_BIT_EXT = 0

def glInitMiscAttributeEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_misc_attribute")

glInitMiscAttribEXT = glInitMiscAttributeEXT

def __info():
	if glInitMiscAttributeEXT():
		return []
