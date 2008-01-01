/*
# BUILD api_versions [0x10c]
*/

%module polygon_offset

#define __version__ "$Revision: 1.24.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com/projects/ogl-sample/registry/EXT/polygon_offset.txt"

%{
/**
 *
 * GL.EXT.polygon_offset Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_polygon_offset)
DECLARE_VOID_EXT(glPolygonOffsetEXT, (GLfloat factor, GLfloat bias), (factor, bias))
#endif
%}

void glPolygonOffsetEXT(GLfloat factor, GLfloat bias);
DOC(glPolygonOffsetEXT, "glPolygonOffsetEXT(factor, bias) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_polygon_offset)
	"glPolygonOffsetEXT",
#endif
	NULL
};

#define glInitPolygonOffsetEXT() InitExtension("GL_EXT_polygon_offset", proc_names)
%}

int glInitPolygonOffsetEXT();
DOC(glInitPolygonOffsetEXT, "glInitPolygonOffsetEXT() -> bool")



%{
PyObject *__info()
{
	if (glInitPolygonOffsetEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_POLYGON_OFFSET_EXT               0x8037

#define GL_POLYGON_OFFSET_FACTOR_EXT        0x8038
#define GL_POLYGON_OFFSET_BIAS_EXT          0x8039

