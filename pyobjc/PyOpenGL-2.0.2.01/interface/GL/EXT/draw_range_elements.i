/*
# BUILD api_versions [0x100]
*/

%module draw_range_elements

#define __version__ "$Revision: 1.18.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057draw_range_elements.txt"

%{
/**
 *
 * GL.EXT.draw_range_elements Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_draw_range_elements)
DECLARE_VOID_EXT(glDrawRangeElementsEXT,\
	(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const GLvoid *indices),\
	(mode, start, end, count, type, indices))
#endif
%}

void glDrawRangeElementsEXT(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *buffer);
DOC(glDrawRangeElementsEXT, "glDrawRangeElementsEXT(mode, start, end, count, type, indices) -> None")

%name(glDrawRangeElementsubEXT) void glDrawRangeElementsEXT(GLenum mode, GLuint start, GLuint end, GLsizei n_4, GLenum type_UNSIGNED_BYTE, const GLubyte *indices);
DOC(glDrawRangeElementsubEXT, "glDrawRangeElementsubEXT(mode, start, end, indices[]) -> None")

%name(glDrawRangeElementsusEXT) void glDrawRangeElementsEXT(GLenum mode, GLuint start, GLuint end, GLsizei n_4, GLenum type_UNSIGNED_SHORT, const GLushort *indices);
DOC(glDrawRangeElementsusEXT, "glDrawRangeElementsusEXT(mode, start, end, indices[]) -> None")

%name(glDrawRangeElementsuiEXT) void glDrawRangeElementsEXT(GLenum mode, GLuint start, GLuint end, GLsizei n_4, GLenum type_UNSIGNED_INT, const GLuint *indices);
DOC(glDrawRangeElementsuiEXT, "glDrawRangeElementsuiEXT(mode, start, end, indices[]) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_draw_range_elements)
	"glDrawRangeElementsEXT",
#endif
	NULL
};

#define glInitDrawRangeElementsEXT() InitExtension("GL_EXT_draw_range_elements", proc_names)
%}

int glInitDrawRangeElementsEXT();
DOC(glInitDrawRangeElementsEXT, "glInitDrawRangeElementsEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitDrawRangeElementsEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

