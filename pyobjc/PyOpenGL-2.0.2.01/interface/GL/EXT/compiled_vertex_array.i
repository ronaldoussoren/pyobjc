/*
# BUILD api_versions [0x103]
*/

%module compiled_vertex_array

#define __version__ "$Revision: 1.33.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057compiled_vertex_array.txt";

%{
/**
 *
 * GL.EXT.compiled_vertex_array Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_compiled_vertex_array)
DECLARE_VOID_EXT(glLockArraysEXT, (GLint first, GLsizei count), (first, count))
DECLARE_VOID_EXT(glUnlockArraysEXT, (), ())
#endif
%}

void glLockArraysEXT(GLint first, GLsizei count);
DOC(glLockArraysEXT, "glLockArraysEXT(first, count) -> None")


void glUnlockArraysEXT();
DOC(glUnlockArraysEXT, "glUnlockArraysEXT() -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_compiled_vertex_array)
	"glLockArraysEXT",
	"glUnlockArraysEXT",
#endif
	NULL
};

#define glInitCompiledVertexArrayEXT() InitExtension("GL_EXT_compiled_vertex_array", proc_names)
%}

int glInitCompiledVertexArrayEXT();
DOC(glInitCompiledVertexArrayEXT, "glInitCompiledVertexArrayEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitCompiledVertexArrayEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_ARRAY_ELEMENT_LOCK_FIRST_EXT   0x81A8
#define GL_ARRAY_ELEMENT_LOCK_COUNT_EXT   0x81A9

