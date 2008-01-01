/*
# BUILD api_versions [0x102]
*/

%module multi_draw_arrays

%{
/**
 *
 * GL.EXT.multi_draw_arrays Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057multi_draw_arrays.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_multi_draw_arrays)
DECLARE_VOID_EXT(glMultiDrawArraysEXT,\
	(GLenum mode, GLint *first, GLsizei *count, GLsizei primcount),\
	(mode, first, count, primcount))
#endif

#define _glMultiDrawArraysEXT(mode, first, count, primcount) glMultiDrawArraysEXT(mode, (GLint*)first, (GLsizei*)count, primcount)
%}

%name(glMultiDrawArraysEXT) void _glMultiDrawArraysEXT(GLenum mode, const GLint *first, const GLsizei *count, GLsizei n_1);
DOC(glMultiDrawArraysEXT, "glMultiDrawArraysEXT(mode, firsts, counts) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_multi_draw_arrays)
	"glMultiDrawArraysEXT",
#endif
	NULL
};

#define glInitMultiDrawArraysEXT() InitExtension("GL_EXT_multi_draw_arrays", proc_names)
%}

int glInitMultiDrawArraysEXT();
DOC(glInitMultiDrawArraysEXT, "glInitMultiDrawArraysEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitMultiDrawArraysEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

