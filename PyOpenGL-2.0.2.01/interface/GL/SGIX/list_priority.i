/*
# BUILD api_versions [0x103]
*/

%module list_priority

#define __version__ "$Revision: 1.16.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057list_priority.txt"

%{
/**
 *
 * GL.SGIX.list_priority Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_list_priority)
DECLARE_VOID_EXT(glListParameterfSGIX, (GLuint list, GLenum pname, GLfloat param), (list, pname, param))
DECLARE_VOID_EXT(glListParameterfvSGIX, (GLuint list, GLenum pname, const GLfloat *v), (list, pname, v))
DECLARE_VOID_EXT(glListParameteriSGIX, (GLuint list, GLenum pname, GLint param), (list, pname, param))
DECLARE_VOID_EXT(glListParameterivSGIX, (GLuint list, GLenum pname, const GLint *v), (list, pname, v))
DECLARE_VOID_EXT(glGetListParameterfvSGIX, (GLuint list, GLenum pname, GLfloat *params), (list, pname, params))
DECLARE_VOID_EXT(glGetListParameterivSGIX, (GLuint list, GLenum pname, GLint *params), (list, pname, params))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_list_priority)
	"glListParameterfSGIX",
	"glListParameterfvSGIX",
	"glListParameterivSGIX",
	"glListParameterivSGIX",
	"glGetListParameterfvSGIX",
	"glGetListParameterivSGIX",
#endif
	NULL
};

#define glInitListPrioritySGIX() InitExtension("GL_SGIX_list_priority", proc_names)
%}

int glInitListPrioritySGIX();
DOC(glInitListPrioritySGIX, "glInitListPrioritySGIX() -> bool")

void glListParameterfSGIX (GLuint list, GLenum pname, GLfloat param);
DOC(glListParameterfSGIX, "glListParameterfSGIX(list, pname, param) -> None")

void glListParameterfvSGIX (GLuint list, GLenum pname, const GLfloat *v);
DOC(glListParameterfvSGIX, "glListParameterfvSGIX(list, pname, params) -> None")

void glListParameteriSGIX (GLuint list, GLenum pname, GLint param);
DOC(glListParameteriSGIX, "glListParameteriSGIX(list, pname, param) -> None")

void glListParameterivSGIX (GLuint list, GLenum pname, const GLint *v);
DOC(glListParameterivSGIX, "glListParameterivSGIX(list, pname, params) -> None")


void glGetListParameterfvSGIX (GLuint list, GLenum pname, GLfloat params[4]);
DOC(glGetListParameterfvSGIX, "glGetListParameterfvSGIX(list, pname) -> params")

void glGetListParameterivSGIX (GLuint list, GLenum pname, GLint params[4]);
DOC(glGetListParameterivSGIX, "glGetListParameterivSGIX(list, pname) -> params")



%{
PyObject *__info()
{
	if (glInitListPrioritySGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
