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
 * GL.EXT.color_table Module for PyOpenGL
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
DECLARE_VOID_EXT(glColorTableEXT,\
	(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void* table),\
	(target, internalformat, width, format, type, table))
DECLARE_VOID_EXT(glCopyColorTableEXT,\
	(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width),\
	(target, internalformat, x, y, width))
DECLARE_VOID_EXT(glColorTableParameterivEXT,\
	(GLenum target, GLenum pname, const GLint* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glColorTableParameterfvEXT,\
	(GLenum target, GLenum pname, const GLfloat* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetColorTableEXT,\
	(GLenum target, GLenum format, GLenum type, void* table),\
	(target, format, type, table))
DECLARE_VOID_EXT(glGetColorTableParameterivEXT,\
	(GLenum target, GLenum pname, GLint* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetColorTableParameterfvEXT,\
	(GLenum target, GLenum pname, GLfloat* params),\
	(target, pname, params))
#endif

#ifndef GL_COLOR_TABLE_WIDTH_EXT
#define GL_COLOR_TABLE_WIDTH_EXT 0x80D9
#endif
%}

void glColorTableEXT(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void* buffer);
DOC(glColorTableEXT, "glColorTableEXT(target, internalformat, width, format, type, table) -> None")

%{
void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei width, GLenum format, GLenum type, const void* table)
{
	SetupPixelWrite(1);
	glColorTableEXT(target, internalformat, width, format, type, table);
}
%}

%name(glColorTableubEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte* table);
DOC(glColorTableubEXT, "glColorTableubEXT(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTablebEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_BYTE, const GLbyte* table);
DOC(glColorTablebEXT, "glColorTablebEXT(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTableusEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort* table);
DOC(glColorTableusEXT, "glColorTableusEXT(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTablesEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_SHORT, const GLshort* table);
DOC(glColorTablesEXT, "glColorTablesEXT(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTableuiEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint* table);
DOC(glColorTableuiEXT, "glColorTableuiEXT(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTableiEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_INT, const GLint* table);
DOC(glColorTableiEXT, "glColorTableiEXT(target, internalFormat, format, table[] | table[][]) -> None")

%name(glColorTablefEXT) void _glColorTableEXT(GLenum target, GLenum internalformat, GLsizei d_5_0, GLenum format, GLenum type_FLOAT, const GLfloat* table);
DOC(glColorTablefEXT, "glColorTablefEXT(target, internalFormat, format, table[] | table[][]) -> None")

void glCopyColorTableEXT(GLenum target, GLenum internalformat, GLint x, GLint y, GLsizei width);
DOC(glCopyColorTableEXT, "glCopyColorTableEXT(target, internalformat, x, y, width) -> None")

void glColorTableParameterivEXT(GLenum target, GLenum pname, const GLint* params);
DOC(glColorTableParameterivEXT, "glColorTableParameterivEXT(target, pname, params) -> None")

void glColorTableParameterfvEXT(GLenum target, GLenum pname, const GLfloat* params);
DOC(glColorTableParameterfvEXT, "glColorTableParameterfvEXT(target, pname, params) -> None")

void glGetColorTableParameterivEXT(GLenum target, GLenum pname, GLint params[4]);
DOC(glGetColorTableParameterivEXT, "glGetColorTableParameterivEXT(target, pname) -> params")

void glGetColorTableParameterfvEXT(GLenum target, GLenum pname, GLfloat params[4]);
DOC(glGetColorTableParameterfvEXT, "glGetColorTableParameterfvEXT(target, pname) -> params")

%{
PyObject* _glGetColorTableEXT(GLenum target, GLenum format, GLenum type)
{
	PyObject* result;
	int size;
	GLint dims[1];
	void* data = NULL;
	
	glGetColorTableParameterivEXT(target, GL_COLOR_TABLE_WIDTH_EXT, dims);

	data = SetupRawPixelRead(format, type, 1, dims, &size);
	if (!data) return NULL;
	
	glGetColorTableEXT(target, format, type, data);
	result = PyString_FromStringAndSize((const char*)data, size);
	PyMem_Del(data);

	return result;
}
%}

%name(glGetColorTableEXT) PyObject* _glGetColorTableEXT(GLenum target, GLenum format, GLenum type);
DOC(glGetColorTableEXT, "glGetColorTableEXT(target, format, type) -> pixels")

%{
PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type)
{
	int dims[2];
	void* data;

	glGetColorTableParameterivEXT(target, GL_COLOR_TABLE_WIDTH_EXT, dims);

	data = SetupPixelRead(1, format, type, dims);
	if (!data) return NULL;

	glGetColorTableEXT(target, format, type, data);
	
	return _PyObject_FromArray(type, (dims[1] == 1) ? 1 : 2, dims, data, 1);
}
%}

%name(glGetColorTableubEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_UNSIGNED_BYTE);
DOC(glGetColorTableubEXT, "glGetColorTableubEXT(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTablebEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_BYTE);
DOC(glGetColorTablebEXT, "glGetColorTablebEXT(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTableusEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_UNSIGNED_SHORT);
DOC(glGetColorTableusEXT, "glGetColorTableusEXT(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTablesEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_SHORT);
DOC(glGetColorTablesEXT, "glGetColorTablesEXT(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTableuiEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_UNSIGNED_INT);
DOC(glGetColorTableuiEXT, "glGetColorTableuiEXT(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTableiEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_INT);
DOC(glGetColorTableiEXT, "glGetColorTableiEXT(target, format, type) -> pixels[] | pixels[][]")

%name(glGetColorTablefEXT) PyObject* __glGetColorTableEXT(GLenum target, GLenum format, GLenum type_FLOAT);
DOC(glGetColorTablefEXT, "glGetColorTablefEXT(target, format) -> pixels[] | pixels[][]")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_color_table)
	"glColorTableEXT",
	"glCopyColorTableEXT",
	"glColorTableParameterivEXT",
	"glColorTableParameterfvEXT",
	"glGetColorTableEXT",
	"glGetColorTableParameterivEXT",
	"glGetColorTableParameterfvEXT",
#endif
	NULL
};

#define glInitColorTableEXT() InitExtension("GL_EXT_color_table", proc_names)
%}

GLint glInitColorTableEXT();
DOC(glInitColorTableEXT, "glInitColorTableEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitColorTableEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_COLOR_TABLE_EXT					0x80D0
#define GL_POST_CONVOLUTION_COLOR_TABLE_EXT		0x80D1
#define GL_POST_COLOR_MATRIX_COLOR_TABLE_EXT		0x80D2

#define GL_PROXY_COLOR_TABLE_EXT				0x80D3
#define GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_EXT		0x80D4
#define GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_EXT		0x80D5

#define GL_COLOR_TABLE_SCALE_EXT				0x80D6
#define GL_COLOR_TABLE_BIAS_EXT				0x80D7

#define GL_COLOR_TABLE_FORMAT_EXT				0x80D8
#define GL_COLOR_TABLE_WIDTH_EXT				0x80D9
#define GL_COLOR_TABLE_RED_SIZE_EXT			0x80DA
#define GL_COLOR_TABLE_GREEN_SIZE_EXT			0x80DB
#define GL_COLOR_TABLE_BLUE_SIZE_EXT			0x80DC
#define GL_COLOR_TABLE_ALPHA_SIZE_EXT			0x80DD
#define GL_COLOR_TABLE_LUMINANCE_SIZE_EXT			0x80DE
#define GL_COLOR_TABLE_INTENSITY_SIZE_EXT			0x80DF
