/*
# BUILD api_versions [0x004]
*/

%module point_parameters

#define __version__ "$Revision: 1.27.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057point_parameters.txt"

%{
/**
 *
 * GL.ARB.point_parameters Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_point_parameters)
DECLARE_VOID_EXT(glPointParameterfARB, (GLenum pname, GLfloat param), (pname, param))
DECLARE_VOID_EXT(glPointParameterfvARB, (GLenum pname, const GLfloat* param), (pname, param))
#endif
%}

void glPointParameterfARB(GLenum pname, GLfloat param);
DOC(glPointParameterfARB, "glPointParameterfARB(pname, param) -> None")

void glPointParameterfvARB(GLenum pname, const GLfloat* param);
DOC(glPointParameterfvARB, "glPointParameterfvARB(pname, param) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_point_parameters)
	"glPointParameterfARB",
	"glPointParameterfvARB",
#endif
	NULL
};

#define glInitPointParametersARB() InitExtension("GL_ARB_point_parameters", proc_names)
%}

int glInitPointParametersARB();
DOC(glInitPointParametersARB, "glInitPointParametersARB() -> bool")

%{
PyObject *__info()
{
	if (glInitPointParametersARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_POINT_SIZE_MIN_ARB 0x8126
#define GL_POINT_SIZE_MAX_ARB 0x8127
#define GL_POINT_FADE_THRESHOLD_SIZE_ARB 0x8128
#define GL_POINT_DISTANCE_ATTENUATION_ARB 0x8129

