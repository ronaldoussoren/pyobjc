/*
# BUILD api_versions [0x108]
*/

%module async

#define __version__ "$Revision: 1.16.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057async.txt"

%{
/**
 *
 * GL.SGIX.async Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_async)
DECLARE_VOID_EXT(glAsyncMarkerSGIX, (GLuint marker), (marker))
DECLARE_VOID_EXT(glDeleteAsyncMarkersSGIX, (GLuint marker, GLsizei range), (marker, range))
DECLARE_EXT(glFinishAsyncSGIX, GLint, 0, (GLuint *markerp), (markerp))
DECLARE_EXT(glPollAsyncSGIX, GLint, 0, (GLuint *markerp), (markerp))
DECLARE_EXT(glGenAsyncMarkersSGIX, GLuint, 0, (GLsizei range), (range))
DECLARE_EXT(glIsAsyncMarkerSGIX, GLboolean, 0, (GLuint marker), (marker))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_async)
	"glAsyncMarkerSGIX",
	"glDeleteAsyncMarkersSGIX",
	"glFinishAsyncSGIX",
	"glPollAsyncSGIX",
	"glGenAsyncMarkersSGIX",
	"glIsAsyncMarkerSGIX",
#endif
	NULL
};

#define glInitAsyncSGIX() InitExtension("GL_SGIX_async", proc_names)
%}

int glInitAsyncSGIX();
DOC(glInitAsyncSGIX, "glInitAsyncSGIX() -> bool")

void glAsyncMarkerSGIX(GLuint marker);
DOC(glAsyncMarkerSGIX, "glAsyncMarkerSGIX(marker) -> None")

void glDeleteAsyncMarkersSGIX(GLuint marker, GLsizei range);
DOC(glDeleteAsyncMarkersSGIX, "glDeleteAsyncMarkersSGIX(marker, range) -> None")

%{
PyObject *_glFinishAsyncSGIX()
{
	GLuint marker;
	
	if (glFinishAsyncSGIX(&marker)) return PyInt_FromLong(marker);
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(glFinishAsyncSGIX) PyObject *_glFinishAsyncSGIX();
DOC(glFinishAsyncSGIX, "glFinishAsyncSGIX() -> None | marker")

%{
PyObject *_glPollAsyncSGIX()
{
	GLuint marker;
	
	if (glPollAsyncSGIX(&marker)) return PyInt_FromLong(marker);
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

%name(glPollAsyncSGIX) PyObject *_glPollAsyncSGIX();
DOC(glPollAsyncSGIX, "glPollAsyncSGIX() -> None | marker")

GLuint glGenAsyncMarkersSGIX(GLsizei range);
DOC(glGenAsyncMarkersSGIX, "glGenAsyncMarkersSGIX(range) -> marker")

GLuint glIsAsyncMarkerSGIX(GLuint marker);
DOC(glIsAsyncMarkerSGIX, "glIsAsyncMarkerSGIX(marker) -> bool")


%{
PyObject *__info()
{
	if (glInitAsyncSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_ASYNC_MARKER_SGIX		0x8329
