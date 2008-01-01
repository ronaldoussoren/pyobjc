/*
# BUILD api_versions [0x102]
*/

%module pixel_transform

%{
/**
 *
 * GL.EXT.pixel_transform Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057pixel_transform.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_pixel_transform)
DECLARE_VOID_EXT(glPixelTransformParameteriEXT, (GLenum target, GLenum pname, GLint param), (target, pname, param))
DECLARE_VOID_EXT(glPixelTransformParameterfEXT, (GLenum target, GLenum pname, GLfloat param), (target, pname, param))
DECLARE_VOID_EXT(glPixelTransformParameterivEXT, (GLenum target, GLenum pname, const GLint* param), (target, pname, param))
DECLARE_VOID_EXT(glPixelTransformParameterfvEXT, (GLenum target, GLenum pname, const GLfloat* param), (target, pname, param))
DECLARE_VOID_EXT(glGetPixelTransformParameterfvEXT, (GLenum target, GLenum pname, GLfloat* param), (target, pname, param))
DECLARE_VOID_EXT(glGetPixelTransformParameterivEXT, (GLenum target, GLenum pname, GLint* param), (target, pname, param))
#endif
%}

void glPixelTransformParameteriEXT(GLenum target, GLenum pname, GLint param);
DOC(glPixelTransformParameteriEXT, "glPixelTransformParameteriEXT(target, pname, param) -> None")

void glPixelTransformParameterfEXT(GLenum target, GLenum pname, GLfloat param);
DOC(glPixelTransformParameterfEXT, "glPixelTransformParameterfEXT(target, pname, param) -> None")

void glPixelTransformParameterivEXT(GLenum target, GLenum pname, const GLint* param);
DOC(glPixelTransformParameterivEXT, "glPixelTransformParameterivEXT(target, pname, params) -> None")

void glPixelTransformParameterfvEXT(GLenum target, GLenum pname, const GLfloat* param);
DOC(glPixelTransformParameterfvEXT, "glPixelTransformParameterfvEXT(target, pname, params) -> None")

void glGetPixelTransformParameterfvEXT(GLenum target, GLenum pname, GLfloat param[4]);
DOC(glGetPixelTransformParameterfvEXT, "glGetPixelTransformParameterfvEXT(target, pname) -> params")

void glGetPixelTransformParameterivEXT(GLenum target, GLenum pname, GLint param[4]);
DOC(glGetPixelTransformParameterivEXT, "glGetPixelTransformParameterivEXT(target, pname) -> params")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_pixel_transform)
	"glPixelTransformParameteriEXT",
	"glPixelTransformParameterfEXT",
	"glPixelTransformParameterivEXT",
	"glPixelTransformParameterfvEXT",
	"glGetPixelTransformParameterfvEXT",
	"glGetPixelTransformParameterivEXT",
#endif
	NULL
};

#define glInitPixelTransformEXT() InitExtension("GL_EXT_pixel_transform", proc_names)
%}

int glInitPixelTransformEXT();
DOC(glInitPixelTransformEXT, "glInitPixelTransformEXT() -> bool")


%{
#ifndef GL_EXT_pixel_transform
#define GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT         0x8337
#endif

PyObject *__info()
{
	if (glInitPixelTransformEXT())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT", GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PIXEL_MAG_FILTER_EXT                           0x8331
#define GL_PIXEL_MIN_FILTER_EXT                           0x8332
#define GL_PIXEL_CUBIC_WEIGHT_EXT                         0x8333

#define GL_CUBIC_EXT                                      0x8334

#define GL_AVERAGE_EXT                                    0x8335

#define GL_PIXEL_TRANSFORM_2D_EXT                         0x8330

#define GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT             0x8336
#define GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT         0x8337

#define GL_PIXEL_TRANSFORM_2D_MATRIX_EXT                  0x8338
