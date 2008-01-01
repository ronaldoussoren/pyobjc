/*
# BUILD api_versions [0x104]
*/

%module index_func

#define __version__ "$Revision: 1.22.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057index_func.txt"

%{
/**
 *
 * GL.EXT.index_func Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_index_func)
DECLARE_VOID_EXT(glIndexFuncEXT, (GLenum func, GLfloat ref), (func, ref))
#endif
%}

void glIndexFuncEXT(GLenum func, GLfloat ref);
DOC(glIndexFuncEXT, "glIndexFuncEXT(func, ref) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_index_func)
	"glIndexFuncEXT",
#endif
	NULL
};

#define glInitIndexFuncEXT() InitExtension("GL_EXT_index_func", proc_names)
%}

int glInitIndexFuncEXT();
DOC(glInitIndexFuncEXT, "glInitIndexFuncEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitIndexFuncEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_INDEX_TEST_EXT                 0x81B5
#define GL_INDEX_TEST_FUNC_EXT            0x81B6
#define GL_INDEX_TEST_REF_EXT             0x81B7
