/*
# BUILD api_versions [0x101]
*/

%module multimode_draw_arrays

#define __version__ "$Revision: 1.16.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057IBM\057multimode_draw_arrays.txt"

%{
/**
 *
 * GL.IBM.multimode_draw_arrays Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_IBM_multimode_draw_arrays)
DECLARE_VOID_EXT(glMultiModeDrawArraysIBM,\
(const GLenum *mode, const GLint *first, const GLsizei *count, GLsizei primcount, GLint modestride),\
(mode, first, count, primcount, modestride))
#endif

#define _glMultiModeDrawArraysIBM(mode, first, count, primcount) glMultiModeDrawArraysIBM(mode, first, count, primcount, sizeof(GLenum))
%}

%name(glMultiModeDrawArraysIBM) void _glMultiModeDrawArraysIBM(const GLenum *mode, const GLint *first, const GLsizei *count, GLsizei primcount);
DOC(glMultiModeDrawArraysIBM, "glMultiModeDrawArraysIBM(mode, first, count) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_IBM_multimode_draw_arrays)
	"glMultiModeDrawArraysIBM",
#endif
	NULL
};

#define glInitMultimodeDrawArraysIBM() InitExtension("GL_IBM_multimode_draw_arrays", proc_names)
%}

int glInitMultimodeDrawArraysIBM();
DOC(glInitMultimodeDrawArraysIBM, "glInitMultimodeDrawArraysIBM() -> bool")

%name(glInitMultiModeDrawArraysIBM) int glInitMultimodeDrawArraysIBM();
DOC(glInitMultiModeDrawArraysIBM, "glInitMultiModeDrawArraysIBM() -> bool")

%{
PyObject *__info()
{
	if (glInitMultimodeDrawArraysIBM())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

