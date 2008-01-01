import string
__version__ = string.split('$Revision: 1.2.12.1 $')[1]
__date__ = string.join(string.split('$Date: 2005/01/03 00:10:48 $')[1:3], ' ')
__author__ = 'Tarn Weisner Burton <twburton@users.sourceforge.net>'
__doc__ = 'http://oss.sgi.com/projects/ogl-sample/registry/EXT/nurbs_tessellator.txt'
__api_version__ = 0x100

from OpenGL.GLU.GLU__init__ import __gluNurbsCallbackDataEXT, __gluInitNurbsTessellatorEXT
gluNurbsCallbackDataEXT = __gluNurbsCallbackDataEXT
gluInitNurbsTessellatorEXT = __gluInitNurbsTessellatorEXT

GLU_NURBS_MODE_EXT = 100160

GLU_NURBS_TESSELLATOR_EXT = 100161
GLU_NURBS_RENDERER_EXT = 100162
 
GLU_NURBS_BEGIN_EXT =	 100164
GLU_NURBS_VERTEX_EXT = 100165
GLU_NURBS_NORMAL_EXT = 100166
GLU_NURBS_COLOR_EXT = 100167
GLU_NURBS_TEXTURE_COORD_EXT = 100168
GLU_NURBS_END_EXT = 100169

GLU_NURBS_BEGIN_DATA_EXT =	 100170
GLU_NURBS_VERTEX_DATA_EXT = 100171
GLU_NURBS_NORMAL_DATA_EXT = 100172
GLU_NURBS_COLOR_DATA_EXT = 100173
GLU_NURBS_TEXTURE_COORD_DATA_EXT = 100174
GLU_NURBS_END_DATA_EXT = 100175



def __info():
	if gluInitNurbsTessellatorEXT():
		return []
