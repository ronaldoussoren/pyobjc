/*
# BUILD api_versions [0x109]
*/

%module texture_filter4

%{
/**
 *
 * GL.SGIS.texture_filter4 Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057texture_filter4.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_texture_filter4)
DECLARE_VOID_EXT(glTexFilterFuncSGIS, (GLenum target, GLenum filter, GLsizei n, const GLfloat* points), (target, filter, n, points))
DECLARE_VOID_EXT(glGetTexFilterFuncSGIS, (GLenum target, GLenum filter, GLfloat* points), (target, filter, points))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_texture_filter4)
	"glTexFilterFuncSGIS",
	"glGetTexFilterFuncSGIS",
#endif
	NULL
};

#define glInitTextureFilter4SGIS() InitExtension("GL_SGIS_texture_filter4", proc_names)
%}

int glInitTextureFilter4SGIS();
DOC(glInitTextureFilter4SGIS, "glInitTextureFilter4SGIS() -> bool")

%name(glInitTexFilter4SGIS) int glInitTextureFilter4SGIS();
DOC(glInitTexFilter4SGIS, "glInitTexFilter4SGIS() -> bool")

void glTexFilterFuncSGIS(GLenum target, GLenum filter, GLsizei n_3, const GLfloat* points);
DOC(glTexFilterFuncSGIS, "glTexFilterFuncSGIS(target, filter, points) -> None")

%{
#ifndef GL_TEXTURE_FILTER4_SIZE_SGIS
#define GL_TEXTURE_FILTER4_SIZE_SGIS      0x8147
#endif

PyObject* _glGetTexFilterFuncSGIS(GLenum target, GLenum filter)
{
	GLsizei n = 0;
	GLfloat *points;
	PyObject *result;
	
	glGetTexParameteriv(target, GL_TEXTURE_FILTER4_SIZE_SGIS, &n);
	points = PyMem_New(GLfloat, n);

	glGetTexFilterFuncSGIS(target, filter, points);
	
	result = _PyTuple_FromFloatArray(n, points);
	PyMem_Del(points);
	
	return result;
}
%}

%name(glGetTexFilterFuncSGIS) PyObject* _glGetTexFilterFuncSGIS(GLenum target, GLenum filter);
DOC(glGetTexFilterFuncSGIS, "glGetTexFilterFuncSGIS(target) -> points")

%{
PyObject *__info()
{
	if (glInitTextureFilter4SGIS())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_FILTER4_SGIS                   0x8146
#define GL_TEXTURE_FILTER4_SIZE_SGIS      0x8147
