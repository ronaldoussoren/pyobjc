/*
# BUILD api_versions [0x11f]
*/

%module convolution

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057convolution.txt"

%{
/**
 *
 * GL.EXT.convolution Module for PyOpenGL
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
#ifndef GL_EXT_convolution
#define GL_CONVOLUTION_1D_EXT               0x8010
#define GL_CONVOLUTION_2D_EXT               0x8011
#define GL_SEPARABLE_2D_EXT                 0x8012
#define GL_CONVOLUTION_BORDER_MODE_EXT      0x8013
#define GL_CONVOLUTION_FILTER_SCALE_EXT     0x8014
#define GL_CONVOLUTION_FILTER_BIAS_EXT      0x8015
#define GL_REDUCE_EXT                       0x8016
#define GL_CONVOLUTION_FORMAT_EXT           0x8017
#define GL_CONVOLUTION_WIDTH_EXT            0x8018
#define GL_CONVOLUTION_HEIGHT_EXT           0x8019
#define GL_MAX_CONVOLUTION_WIDTH_EXT        0x801A
#define GL_MAX_CONVOLUTION_HEIGHT_EXT       0x801B

#define GL_POST_CONVOLUTION_RED_SCALE_EXT   0x801C
#define GL_POST_CONVOLUTION_GREEN_SCALE_EXT 0x801D
#define GL_POST_CONVOLUTION_BLUE_SCALE_EXT  0x801E
#define GL_POST_CONVOLUTION_ALPHA_SCALE_EXT 0x801F
#define GL_POST_CONVOLUTION_RED_BIAS_EXT    0x8020
#define GL_POST_CONVOLUTION_GREEN_BIAS_EXT  0x8021
#define GL_POST_CONVOLUTION_BLUE_BIAS_EXT   0x8022
#define GL_POST_CONVOLUTION_ALPHA_BIAS_EXT  0x8023
#endif
%}

%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_convolution)
DECLARE_VOID_EXT(glConvolutionParameteriEXT,\
	(GLenum target, GLenum pname, GLint param),\
	(target, pname, param))
DECLARE_VOID_EXT(glConvolutionParameterivEXT,\
	(GLenum target, GLenum pname, const GLint *param),\
	(target, pname, param))
DECLARE_VOID_EXT(glConvolutionParameterfEXT,\
	(GLenum target, GLenum pname, GLfloat param),\
	(target, pname, param))
DECLARE_VOID_EXT(glConvolutionParameterfvEXT,\
	(GLenum target, GLenum pname, const GLfloat *param),\
	(target, pname, param))
DECLARE_VOID_EXT(glGetConvolutionParameterivEXT,\
	(GLenum target, GLenum pname, GLint *params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetConvolutionParameterfvEXT,\
	(GLenum target, GLenum pname, GLfloat *params),\
	(target, pname, params))
DECLARE_VOID_EXT(glConvolutionFilter1DEXT,\
	(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid* image),\
	(target, internalformat, width, format, type, image))
DECLARE_VOID_EXT(glConvolutionFilter2DEXT,\
	(GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* image),\
	(target, internalformat, width, height, format, type, image))
DECLARE_VOID_EXT(glCopyConvolutionFilter1DEXT,\
	(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width),\
	(target, internalformat, x, y, width))
DECLARE_VOID_EXT(glCopyConvolutionFilter2DEXT,\
	(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height),\
	(target, internalformat, x, y, width, height))
DECLARE_VOID_EXT(glGetConvolutionFilterEXT,\
	(GLenum target, GLenum format, GLenum type, GLvoid* image),\
	(target, format, type, image))
DECLARE_VOID_EXT(glSeparableFilter2DEXT,\
	(GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, const void* row, const void* column),\
	(target, internalformat, width, height, format, type, row, column))
#endif
%}

void glConvolutionParameteriEXT(GLenum target, GLenum pname, GLint param);
DOC(glConvolutionParameteriEXT, "glConvolutionParameteriEXT(target, pname, param) -> None")

void glConvolutionParameterivEXT(GLenum target, GLenum pname, const GLint *param);
DOC(glConvolutionParameterivEXT, "glConvolutionParameterivEXT(target, pname, param[]) -> None")

void glConvolutionParameterfEXT(GLenum target, GLenum pname, GLfloat param);
DOC(glConvolutionParameterfEXT, "glConvolutionParameterfEXT(target, pname, param) -> None")

void glConvolutionParameterfvEXT(GLenum target, GLenum pname, const GLfloat *param);
DOC(glConvolutionParameterfvEXT, "glConvolutionParameterfvEXT(target, pname, param[]) -> None")

void glGetConvolutionParameterivEXT(GLenum target, GLenum pname, GLint params[4]);
DOC(glGetConvolutionParameterivEXT, "glGetConvolutionParameterivEXT(target, pname) -> params")

void glGetConvolutionParameterfvEXT(GLenum target, GLenum pname, GLfloat params[4]);
DOC(glGetConvolutionParameterfvsXT, "glGetConvolutionParameterfvEXT(target, pname) -> params")

void glConvolutionFilter1DEXT(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid* image);
DOC(glConvolutionFilter1DEXT, "glConvolutionFilter1DEXT(target, internalformat, width, format, type, image) -> None")

void glConvolutionFilter2DEXT(GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* image);
DOC(glConvolutionFilter2DEXT, "glConvolutionFilter2DEXT(target, internalformat, width, height, format, type, image) -> None")

void glCopyConvolutionFilter1DEXT(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width);
DOC(glCopyConvolutionFilter1DEXT, "glCopyConvolutionFilter1DEXT(target, internalformat, x, y, width) -> None")

void glCopyConvolutionFilter2DEXT(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glCopyConvolutionFilter2DEXT, "glCopyConvolutionFilter2DEXT(target, internalformat, x, y, width, height) -> None")

%{
int get_conv_dims(GLenum target, int dims[4])
{
	int rank = 0;

	switch (target)
	{
	case GL_CONVOLUTION_2D_EXT:
		glGetConvolutionParameterivEXT(target, GL_CONVOLUTION_HEIGHT_EXT, dims + rank++);
	case GL_CONVOLUTION_1D_EXT:
		glGetConvolutionParameterivEXT(target, GL_CONVOLUTION_WIDTH_EXT, dims + rank++);
	}
	
	return rank;
}

PyObject* _glGetConvolutionFilterEXT(GLenum target, GLenum format, GLenum type)
{
	PyObject* result;
	int size;
	GLint dims[4];
	int rank;
	void* data = NULL;
	
	rank = get_conv_dims(target, dims);	

	data = SetupRawPixelRead(format, type, rank, dims, &size);
	if (!data) return NULL;
	
	glGetConvolutionFilterEXT(target, format, type, data);
	result = PyString_FromStringAndSize((const char*)data, size);
	PyMem_Del(data);

	return result;
}

PyObject* __glGetConvolutionFilterEXT(GLenum target, GLenum format, GLenum type)
{
	int dims[5], rank;
	void* data;

	rank = get_conv_dims(target, dims);	

	data = SetupPixelRead(rank, format, type, dims);
	if (!data) return NULL;
	
	glGetConvolutionFilterEXT(target, format, type, data);
	
	return _PyObject_FromArray(type, (dims[rank] == 1) ? rank-1 : rank, dims, data, 1);
}
%}

%name(glGetConvolutionFilterEXT) PyObject *_glGetConvolutionFilterEXT(GLenum target, GLenum format, GLenum type);
DOC(glGetConvolutionFilterEXT, "glGetConvolutionFilterEXT(target, format, type) -> image")

void glSeparableFilter2DEXT(GLenum target, GLenum internalformat, GLsizei width, GLsizei height, GLenum format, GLenum type, const void* row, const void* column);
DOC(glSeparableFilter2DEXT, "glSeparableFilter2DEXT(target, internalformat, width, height, format, type, row, column) -> None")
/*
%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_convolution)
DECLARE_VOID_EXT(glConvolutionFilter1DEXT,\
	(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid* image),\
	(target, internalformat, width, format, type, image))
#endif
%}

void glConvolutionFilter1DEXT(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const GLvoid* image);
DOC(glConvolutionFilter1DEXT, "glConvolutionFilter1DEXT(target, internalformat, width, format, type, image) -> None")

    void GetSeparableFilterEXT(enum target,
			       enum format,
			       enum type,
			       void* row,
			       void* column,
			       void* span);
*/

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_convolution)
	"glConvolutionParameteriEXT",
	"glConvolutionParameterivEXT",
	"glConvolutionParameterfEXT",
	"glConvolutionParameterfvEXT",
	"glGetConvolutionParameterivEXT",
	"glGetConvolutionParameterfvEXT",
	"glConvolutionFilter1DEXT",
	"glConvolutionFilter2DEXT",
	"glCopyConvolutionFilter1DEXT",
	"glCopyConvolutionFilter2DEXT",
	"glGetConvolutionFilterEXT",
	"glSeparableFilter2DEXT",
#endif
	NULL
};

#define glInitConvolutionEXT() InitExtension("GL_EXT_convolution", proc_names)
%}

int glInitConvolutionEXT();
DOC(glInitConvolutionEXT, "glInitConvolutionEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitConvolutionEXT())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_CONVOLUTION_WIDTH_EXT", GL_MAX_CONVOLUTION_WIDTH_EXT, "i"));
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_CONVOLUTION_HEIGHT_EXT", GL_MAX_CONVOLUTION_HEIGHT_EXT, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_CONVOLUTION_1D_EXT               0x8010
#define GL_CONVOLUTION_2D_EXT               0x8011
#define GL_SEPARABLE_2D_EXT                 0x8012
#define GL_CONVOLUTION_BORDER_MODE_EXT      0x8013
#define GL_CONVOLUTION_FILTER_SCALE_EXT     0x8014
#define GL_CONVOLUTION_FILTER_BIAS_EXT      0x8015
#define GL_REDUCE_EXT                       0x8016
#define GL_CONVOLUTION_FORMAT_EXT           0x8017
#define GL_CONVOLUTION_WIDTH_EXT            0x8018
#define GL_CONVOLUTION_HEIGHT_EXT           0x8019
#define GL_MAX_CONVOLUTION_WIDTH_EXT        0x801A
#define GL_MAX_CONVOLUTION_HEIGHT_EXT       0x801B

#define GL_POST_CONVOLUTION_RED_SCALE_EXT   0x801C
#define GL_POST_CONVOLUTION_GREEN_SCALE_EXT 0x801D
#define GL_POST_CONVOLUTION_BLUE_SCALE_EXT  0x801E
#define GL_POST_CONVOLUTION_ALPHA_SCALE_EXT 0x801F
#define GL_POST_CONVOLUTION_RED_BIAS_EXT    0x8020
#define GL_POST_CONVOLUTION_GREEN_BIAS_EXT  0x8021
#define GL_POST_CONVOLUTION_BLUE_BIAS_EXT   0x8022
#define GL_POST_CONVOLUTION_ALPHA_BIAS_EXT  0x8023

