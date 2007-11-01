import string
__version__ = string.split('$Revision: 1.5 $')[1]
__date__ = string.join(string.split('$Date: 2001/07/20 23:53:31 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/SGIX/clipmap.txt'
__api_version__ = 0x109

GL_LINEAR_CLIPMAP_LINEAR_SGIX     = 0x8170
GL_TEXTURE_CLIPMAP_CENTER_SGIX    = 0x8171
GL_TEXTURE_CLIPMAP_FRAME_SGIX     = 0x8172
GL_TEXTURE_CLIPMAP_OFFSET_SGIX    = 0x8173
GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX = 0x8174
GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX = 0x8175
GL_TEXTURE_CLIPMAP_DEPTH_SGIX     = 0x8176
GL_MAX_CLIPMAP_DEPTH_SGIX         = 0x8177
GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX = 0x8178
GL_NEAREST_CLIPMAP_NEAREST_SGIX   = 0x844D
GL_NEAREST_CLIPMAP_LINEAR_SGIX    = 0x844E
GL_LINEAR_CLIPMAP_NEAREST_SGIX    = 0x844F

def glInitClipmapSGIX():
	from OpenGL.GL import __has_extension
	return __has_extension("GL_SGIX_clipmap")


def __info():
	if glInitClipmapSGIX():
		return [('GL_MAX_CLIPMAP_DEPTH_SGIX', GL_MAX_CLIPMAP_DEPTH_SGIX, 'i')
		        ('GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX', GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX, 'i')]
