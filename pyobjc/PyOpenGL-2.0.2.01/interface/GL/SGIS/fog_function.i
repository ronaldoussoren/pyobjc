/*
# BUILD api_versions [0x100]
*/

%module fog_function

%{
/**
 *
 * GL.SGIS.fog_function Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057fog_function.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_fog_function)
DECLARE_VOID_EXT(glFogFuncSGIS, (GLsizei n, const GLfloat* points), (n, points))
DECLARE_VOID_EXT(glGetFogFuncSGIS, (GLfloat* points), (points))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_fog_function)
	"glFogFuncSGIS",
	"glGetFogFuncSGIS",
#endif
	NULL
};

#define glInitFogFunctionSGIS() InitExtension("GL_SGIS_fog_function", proc_names)
%}

int glInitFogFunctionSGIS();
DOC(glInitFogFunctionSGIS, "glInitFogFunctionSGIS() -> bool")

%name(glInitFogFuncSGIS) int glInitFogFunctionSGIS();
DOC(glInitFogFuncSGIS, "glInitFogFuncSGIS() -> bool")

void glFogFuncSGIS(GLsizei n_1, const GLfloat* points);
DOC(glFogFuncSGIS, "glFogFuncSGIS(points) -> None")

%{
#ifndef GL_FOG_FUNC_POINTS_SGIS
#define GL_FOG_FUNC_POINTS_SGIS 0x812B
#endif

PyObject* _glGetFogFuncSGIS()
{
	GLsizei n = 0;
	GLfloat *points;
	PyObject *result;
	
	glGetIntegerv(GL_FOG_FUNC_POINTS_SGIS, &n);
	points = PyMem_New(GLfloat, n);

	glGetFogFuncSGIS(points);
	
	result = _PyTuple_FromFloatArray(n, points);
	PyMem_Del(points);
	
	return result;
}
%}

%name(glGetFogFuncSGIS) PyObject* _glGetFogFuncSGIS();
DOC(glGetFogFuncSGIS, "glGetFogFuncSGIS() -> points")


%{
#ifndef GL_SGIS_fog_function
#define GL_MAX_FOG_FUNC_POINTS_SGIS          0x84E2
#endif

PyObject *__info()
{
	if (glInitFogFunctionSGIS())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_FOG_FUNC_POINTS_SGIS", GL_MAX_FOG_FUNC_POINTS_SGIS, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_FOG_FUNC_SGIS 0x812A

#define GL_FOG_FUNC_POINTS_SGIS 0x812B
#define GL_MAX_FOG_FUNC_POINTS_SGIS 0x812C
