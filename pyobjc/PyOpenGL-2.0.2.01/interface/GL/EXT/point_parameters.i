/*
# BUILD api_versions [0x106]
*/

%module point_parameters

#define __version__ "$Revision: 1.25.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057point_parameters.txt"

%{
/**
 *
 * GL.EXT.point_parameters Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_point_parameters)
DECLARE_VOID_EXT(glPointParameterfEXT, (GLenum pname, GLfloat param), (pname, param))
DECLARE_VOID_EXT(glPointParameterfvEXT, (GLenum pname, const GLfloat* param), (pname, param))
#endif
%}

void glPointParameterfEXT(GLenum pname, GLfloat param);
DOC(glPointParameterfEXT, "glPointParameterfEXT(pname, param) -> None")

void glPointParameterfvEXT(GLenum pname, const GLfloat* param);
DOC(glPointParameterfvEXT, "glPointParameterfvEXT(pname, param) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_point_parameters)
	"glPointParameterfEXT",
	"glPointParameterfvEXT",
#endif
	NULL
};

#define glInitPointParametersEXT() InitExtension("GL_EXT_point_parameters", proc_names)
%}

int glInitPointParametersEXT();
DOC(glInitPointParametersEXT, "glInitPointParametersEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitPointParametersEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_POINT_SIZE_MIN_EXT 0x8126
#define GL_POINT_SIZE_MAX_EXT 0x8127
#define GL_POINT_FADE_THRESHOLD_SIZE_EXT 0x8128
#define GL_POINT_DISTANCE_ATTENUATION_EXT 0x8129

