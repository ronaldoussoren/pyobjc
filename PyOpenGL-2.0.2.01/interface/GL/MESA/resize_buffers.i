/*
# BUILD api_versions [0x101]
*/

%module resize_buffers

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057MESA\057resize_buffers.txt"

%{
/**
 *
 * GL.MESA.resize_buffers Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_MESA_resize_buffers)
DECLARE_VOID_EXT(glResizeBuffersMESA, (), ())
#endif
%}

void glResizeBuffersMESA();
DOC(glResizeBuffersMESA, "glResizeBuffersMESA() -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_MESA_resize_buffers)
	"glResizeBuffersMESA",
#endif
	NULL
};

#define glInitResizeBuffersMESA() InitExtension("GL_MESA_resize_buffers", proc_names)
%}

int glInitResizeBuffersMESA();
DOC(glInitResizeBuffersMESA, "glInitResizeBuffersMESA() -> bool")


%{
PyObject *__info()
{
	if (glInitResizeBuffersMESA())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


