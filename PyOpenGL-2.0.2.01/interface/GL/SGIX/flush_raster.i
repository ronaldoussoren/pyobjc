/*
# BUILD api_versions [0x104]
*/

%module flush_raster

%{
/**
 *
 * GL.SGIX.flush_raster Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057flush_raster.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_flush_raster)
DECLARE_VOID_EXT(glFlushRasterSGIX, (), ())
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_flush_raster)
	"glFlushRasterSGIX",
#endif
	NULL
};

#define glInitFlushRasterSGIX() InitExtension("GL_SGIX_flush_raster", proc_names)
%}

int glInitFlushRasterSGIX();
DOC(glInitFlushRasterSGIX, "glInitFlushRasterSGIX() -> bool")

void glFlushRasterSGIX();
DOC(glFlushRasterSGIX, "glFlushRasterSGIX() -> None")


%{
PyObject *__info()
{
	if (glInitFlushRasterSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
