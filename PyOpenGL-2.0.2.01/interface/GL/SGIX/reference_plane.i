/*
# BUILD api_versions [0x105]
*/

%module reference_plane

%{
/**
 *
 * GL.SGIX.reference_plane Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057reference_plane.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_reference_plane)
DECLARE_VOID_EXT(glReferencePlaneSGIX, (const GLdouble *equation), (equation))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_reference_plane)
	"glReferencePlaneSGIX",
#endif
	NULL
};

#define glInitReferencePlaneSGIX() InitExtension("GL_SGIX_reference_plane", proc_names)
%}

int glInitReferencePlaneSGIX();
DOC(glInitReferencePlaneSGIX, "glInitReferencePlaneSGIX() -> bool")

void glReferencePlaneSGIX(const GLdouble *equation);
DOC(glReferencePlaneSGIX, "glReferencePlaneSGIX(equation) -> None")


%{
PyObject *__info()
{
	if (glInitReferencePlaneSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_REFERENCE_PLANE_SGIX           0x817D
#define GL_REFERENCE_PLANE_EQUATION_SGIX  0x817E
