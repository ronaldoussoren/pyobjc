import string
__version__ = string.split('$Revision: 1.6 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:30 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/clip_volume_hint.txt'
__api_version__ = 0x104

GL_CLIP_VOLUME_CLIPPING_HINT_EXT = 0x80F0

def glInitClipVolumeHintEXT():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_EXT_clip_volume_hint")


def __info():
	if glInitClipVolumeHintEXT():
		return []
