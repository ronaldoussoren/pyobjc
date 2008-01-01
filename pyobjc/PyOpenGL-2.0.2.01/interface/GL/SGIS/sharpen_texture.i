/*
# BUILD api_versions [0x106]
*/

%module sharpen_texture

%{
/**
 *
 * GL.SGIS.sharpen_texture Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057sharpen_texture.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_sharpen_texture)
DECLARE_VOID_EXT(glSharpenTexFuncSGIS, (GLenum target, GLsizei n, const GLfloat* points), (target, n, points))
DECLARE_VOID_EXT(glGetSharpenTexFuncSGIS, (GLenum target, GLfloat* points), (target, points))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_sharpen_texture)
	"glSharpenTexFuncSGIS",
	"glGetSharpenTexFuncSGIS",
#endif
	NULL
};

#define glInitShapenTextureSGIS() InitExtension("GL_SGIS_sharpen_texture", proc_names)
%}

int glInitShapenTextureSGIS();
DOC(glInitShapenTextureSGIS, "glInitShapenTextureSGIS() -> bool")

%name(glInitShapenTexSGIS) int glInitShapenTextureSGIS();
DOC(glInitShapenTexSGIS, "glInitShapenTexSGIS() -> bool")

void glSharpenTexFuncSGIS(GLenum target, GLsizei n_2, const GLfloat* points);
DOC(glSharpenTexFuncSGIS, "glSharpenTexFuncSGIS(target, points) -> None")

%{
#ifndef GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS
#define GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS 0x80B0
#endif

PyObject* _glGetSharpenTexFuncSGIS(GLenum target)
{
	GLsizei n = 0;
	GLfloat *points;
	PyObject *result;
	
	glGetTexParameteriv(target, GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS, &n);
	points = PyMem_New(GLfloat, n);

	glGetSharpenTexFuncSGIS(target, points);
	
	result = _PyTuple_FromFloatArray(n, points);
	PyMem_Del(points);
	
	return result;
}
%}

%name(glGetSharpenTexFuncSGIS) PyObject* _glGetSharpenTexFuncSGIS(GLenum target);
DOC(glGetSharpenTexFuncSGIS, "glGetSharpenTexFuncSGIS(target) -> points")


%{
PyObject *__info()
{
	if (glInitShapenTextureSGIS())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_LINEAR_SHARPEN_SGIS            0x80AD
#define GL_LINEAR_SHARPEN_ALPHA_SGIS      0x80AE
#define GL_LINEAR_SHARPEN_COLOR_SGIS      0x80AF
#define GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS 0x80B0
