/*
# BUILD api_versions [0x11f]
*/

%module detail_texture

%{
/**
 *
 * GL.SGIS.detail_texture Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057detail_texture.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_detail_texture)
DECLARE_VOID_EXT(glDetailTexFuncSGIS, (GLenum target, GLsizei n, const GLfloat* points), (target, n, points))
DECLARE_VOID_EXT(glGetDetailTexFuncSGIS, (GLenum target, GLfloat* points), (target, points))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_detail_texture)
	"glDetailTexFuncSGIS",
	"glGetDetailTexFuncSGIS",
#endif
	NULL
};

#define glInitDetailTextureSGIS() InitExtension("GL_SGIS_detail_texture", proc_names)
%}

int glInitDetailTextureSGIS();
DOC(glInitDetailTextureSGIS, "glInitDetailTextureSGIS() -> bool")

%name(glInitDetailTexSGIS) int glInitDetailTextureSGIS();
DOC(glInitDetailTexSGIS, "glInitDetailTexSGIS() -> bool")

void glDetailTexFuncSGIS(GLenum target, GLsizei n_2, const GLfloat* points);
DOC(glDetailTexFuncSGIS, "glDetailTexFuncSGIS(target, points) -> None")

%{
#ifndef GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS
#define GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS 0x809C
#endif

PyObject* _glGetDetailTexFuncSGIS(GLenum target)
{
	GLsizei n = 0;
	GLfloat *points;
	PyObject *result;
	
	glGetTexParameteriv(target, GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS, &n);
	points = PyMem_New(GLfloat, n);

	glGetDetailTexFuncSGIS(target, points);
	
	result = _PyTuple_FromFloatArray(n, points);
	PyMem_Del(points);
	
	return result;
}
%}

%name(glGetDetailTexFuncSGIS) PyObject* _glGetDetailTexFuncSGIS(GLenum target);
DOC(glGetDetailTexFuncSGIS, "glGetDetailTexFuncSGIS(target) -> points")


%{
PyObject *__info()
{
	if (glInitDetailTextureSGIS())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_DETAIL_TEXTURE_2D_SGIS         0x8095
#define GL_DETAIL_TEXTURE_2D_BINDING_SGIS 0x8096
#define GL_LINEAR_DETAIL_SGIS             0x8097
#define GL_LINEAR_DETAIL_ALPHA_SGIS       0x8098
#define GL_LINEAR_DETAIL_COLOR_SGIS       0x8099
#define GL_DETAIL_TEXTURE_LEVEL_SGIS      0x809A
#define GL_DETAIL_TEXTURE_MODE_SGIS       0x809B
#define GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS 0x809C
