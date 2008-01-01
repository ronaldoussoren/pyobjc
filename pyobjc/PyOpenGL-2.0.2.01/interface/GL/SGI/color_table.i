/*
# BUILD api_versions [0x120]
*/

%module color_table

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGI\057color_table.txt"

%{
/**
 *
 * GL.SGI.color_table Module for PyOpenGL
 * 
 * Date: December 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_color_table)
DECLARE_VOID_EXT(glColorTableSGI,\
	(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void* table),\
	(target, internalformat, width, format, type, table))
DECLARE_VOID_EXT(glCopyColorTableSGI,\
	(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width),\
	(target, internalformat, x, y, width))
DECLARE_VOID_EXT(glColorTableParameterivSGI,\
	(GLenum target, GLenum pname, const GLint* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glColorTableParameterfvSGI,\
	(GLenum target, GLenum pname, const GLfloat* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetColorTableSGI,\
	(GLenum target, GLenum format, GLenum type, void* table),\
	(target, format, type, table))
DECLARE_VOID_EXT(glGetColorTableParameterivSGI,\
	(GLenum target, GLenum pname, GLint* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetColorTableParameterfvSGI,\
	(GLenum target, GLenum pname, GLfloat* params),\
	(target, pname, params))
#endif

#ifndef GL_COLOR_TABLE_WIDTH_SGI
#define GL_COLOR_TABLE_WIDTH_SGI 0x80D9
#endif
%}

void glColorTableSGI(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void* buffer);
DOC(glColorTableSGI, "glColorTableSGI(target, internalformat, width, format, type, table) -> None")

%{
void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void* table)
{
	SetupPixelWrite(1);
	glColorTableSGI(target, internalformat, width, format, type, table);
}
%}

%name(glColorTableubSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte* table);
DOC(glColorTableubSGI, "glColorTableubSGI(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTablebSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_BYTE, const GLbyte* table);
DOC(glColorTablebSGI, "glColorTablebSGI(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTableusSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort* table);
DOC(glColorTableusSGI, "glColorTableusSGI(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTablesSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_SHORT, const GLshort* table);
DOC(glColorTablesSGI, "glColorTablesSGI(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTableuiSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint* table);
DOC(glColorTableuiSGI, "glColorTableuiSGI(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTableiSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_INT, const GLint* table);
DOC(glColorTableiSGI, "glColorTableiSGI(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTablefSGI) void _glColorTableSGI(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_FLOAT, const GLfloat* table);
DOC(glColorTablefSGI, "glColorTablefSGI(target, internalFormat, format, table[] | table[][]) -> None")

void glCopyColorTableSGI(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width);
DOC(glCopyColorTableSGI, "glCopyColorTableSGI(target, internalformat, x, y, width) -> None")

void glColorTableParameterivSGI(GLenum target, GLenum pname, const GLint* params);
DOC(glColorTableParameterivSGI, "glColorTableParameterivSGI(target, pname, params) -> None")

void glColorTableParameterfvSGI(GLenum target, GLenum pname, const GLfloat* params);
DOC(glColorTableParameterfvSGI, "glColorTableParameterfvSGI(target, pname, params) -> None")

void glGetColorTableParameterivSGI(GLenum target, GLenum pname, GLint params[4]);
DOC(glGetColorTableParameterivSGI, "glGetColorTableParameterivSGI(target, pname) -> params")

void glGetColorTableParameterfvSGI(GLenum target, GLenum pname, GLfloat params[4]);
DOC(glGetColorTableParameterfvSGI, "glGetColorTableParameterfvSGI(target, pname) -> params")

%{
PyObject* _glGetColorTableSGI(GLenum target, GLenum format, GLenum type)
{
	PyObject* result;
	int size;
	GLint dims[1];
	void* data = NULL;
	
	glGetColorTableParameterivSGI(target, GL_COLOR_TABLE_WIDTH_SGI, dims);

	data = SetupRawPixelRead(format, type, 1, dims, &size);
	if (!data) return NULL;
	
	glGetColorTableSGI(target, format, type, data);
	result = PyString_FromStringAndSize((const char*)data, size);
	PyMem_Del(data);

	return result;
}
%}

%name(glGetColorTableSGI) PyObject* _glGetColorTableSGI(GLenum target, GLenum format, GLenum type);
DOC(glGetColorTableSGI, "glGetColorTableSGI(target, format, type) -> pixels")

%{
PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type)
{
	int dims[2];
	void* data;

	glGetColorTableParameterivSGI(target, GL_COLOR_TABLE_WIDTH_SGI, dims);

	data = SetupPixelRead(1, format, type, dims);
	if (!data) return NULL;

	glGetColorTableSGI(target, format, type, data);
	
	return _PyObject_FromArray(type, (dims[1] == 1) ? 1 : 2, dims, data, 1);
}
%}

%name(glGetColorTableubSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_UNSIGNED_BYTE);
DOC(glGetColorTableubSGI, "glGetColorTableubSGI(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTablebSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_BYTE);
DOC(glGetColorTablebSGI, "glGetColorTablebSGI(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTableusSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_UNSIGNED_SHORT);
DOC(glGetColorTableusSGI, "glGetColorTableusSGI(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTablesSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_SHORT);
DOC(glGetColorTablesSGI, "glGetColorTablesSGI(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTableuiSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_UNSIGNED_INT);
DOC(glGetColorTableuiSGI, "glGetColorTableuiSGI(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTableiSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_INT);
DOC(glGetColorTableiSGI, "glGetColorTableiSGI(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTablefSGI) PyObject* __glGetColorTableSGI(GLenum target, GLenum format, GLenum type_FLOAT);
DOC(glGetColorTablefSGI, "glGetColorTablefSGI(target, format) -> pixels[] | pixels[][]")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGI_color_table)
	"glColorTableSGI",
	"glCopyColorTableSGI",
	"glColorTableParameterivSGI",
	"glColorTableParameterfvSGI",
	"glGetColorTableSGI",
	"glGetColorTableParameterivSGI",
	"glGetColorTableParameterfvSGI",
#endif
	NULL
};

#define glInitColorTableSGI() InitExtension("GL_SGI_color_table", proc_names)
%}

GLint glInitColorTableSGI();
DOC(glInitColorTableSGI, "glInitColorTableSGI() -> bool")

%{
PyObject *__info()
{
	if (glInitColorTableSGI())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_COLOR_TABLE_SGI					0x80D0
#define GL_POST_CONVOLUTION_COLOR_TABLE_SGI		0x80D1
#define GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI		0x80D2

#define GL_PROXY_COLOR_TABLE_SGI				0x80D3
#define GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI		0x80D4
#define GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI		0x80D5

#define GL_COLOR_TABLE_SCALE_SGI				0x80D6
#define GL_COLOR_TABLE_BIAS_SGI				0x80D7

#define GL_COLOR_TABLE_FORMAT_SGI				0x80D8
#define GL_COLOR_TABLE_WIDTH_SGI				0x80D9
#define GL_COLOR_TABLE_RED_SIZE_SGI			0x80DA
#define GL_COLOR_TABLE_GREEN_SIZE_SGI			0x80DB
#define GL_COLOR_TABLE_BLUE_SIZE_SGI			0x80DC
#define GL_COLOR_TABLE_ALPHA_SIZE_SGI			0x80DD
#define GL_COLOR_TABLE_LUMINANCE_SIZE_SGI			0x80DE
#define GL_COLOR_TABLE_INTENSITY_SIZE_SGI			0x80DF
