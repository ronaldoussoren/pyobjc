/*
# BUILD api_versions [0x108]
*/

%module secondary_color

#define __version__ "$Revision: 1.25.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057secondary_color.txt"

%{
/**
 *
 * GL.EXT.secondary_color Module for PyOpenGL
 * 
 * Date May 2001
 *
 * Authors Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include py_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_secondary_color)
DECLARE_VOID_EXT(glSecondaryColor3ubEXT, (GLubyte red, GLubyte green, GLubyte blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3bEXT, (GLbyte red, GLbyte green, GLbyte blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3usEXT, (GLushort red, GLushort green, GLushort blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3sEXT, (GLshort red, GLshort green, GLshort blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3uiEXT, (GLuint red, GLuint green, GLuint blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3iEXT, (GLint red, GLint green, GLint blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3fEXT, (GLfloat red, GLfloat green, GLfloat blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3dEXT, (GLdouble red, GLdouble green, GLdouble blue), (red, green, blue))
DECLARE_VOID_EXT(glSecondaryColor3ubvEXT, (const GLubyte* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3bvEXT, (const GLbyte* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3usvEXT, (const GLushort* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3svEXT, (const GLshort* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3uivEXT, (const GLuint* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3ivEXT, (const GLint* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3fvEXT, (const GLfloat* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColor3dvEXT, (const GLdouble* coord), (coord))
DECLARE_VOID_EXT(glSecondaryColorPointerEXT, (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer), (size, type, stride, pointer))
#endif
%}

void glSecondaryColor3ubEXT(GLubyte red, GLubyte green, GLubyte blue);
DOC(glSecondaryColor3ubEXT, "glSecondaryColor3ubEXT(red, green, blue) -> None")

void glSecondaryColor3bEXT(GLbyte red, GLbyte green, GLbyte blue);
DOC(glSecondaryColor3bEXT, "glSecondaryColor3bEXT(red, green, blue) -> None")

void glSecondaryColor3usEXT(GLushort red, GLushort green, GLushort blue);
DOC(glSecondaryColor3usEXT, "glSecondaryColor3usEXT(red, green, blue) -> None")

void glSecondaryColor3sEXT(GLshort red, GLshort green, GLshort blue);
DOC(glSecondaryColor3sEXT, "glSecondaryColor3sEXT(red, green, blue) -> None")

void glSecondaryColor3uiEXT(GLuint red, GLuint green, GLuint blue);
DOC(glSecondaryColor3uiEXT, "glSecondaryColor3uiEXT(red, green, blue) -> None")

void glSecondaryColor3iEXT(GLint red, GLint green, GLint blue);
DOC(glSecondaryColor3iEXT, "glSecondaryColor3iEXT(red, green, blue) -> None")

void glSecondaryColor3fEXT(GLfloat red, GLfloat green, GLfloat blue);
DOC(glSecondaryColor3fEXT, "glSecondaryColor3fEXT(red, green, blue) -> None")

void glSecondaryColor3dEXT(GLdouble red, GLdouble green, GLdouble blue);
DOC(glSecondaryColor3dEXT, "glSecondaryColor3dEXT(red, green, blue) -> None")

void glSecondaryColor3ubvEXT(const GLubyte* coord);
DOC(glSecondaryColor3ubvEXT, "glSecondaryColor3ibvEXT(coord) -> None")

void glSecondaryColor3bvEXT(const GLbyte* coord);
DOC(glSecondaryColor3bvEXT, "glSecondaryColor3bvEXT(coord) -> None")

void glSecondaryColor3usvEXT(const GLushort* coord);
DOC(glSecondaryColor3usvEXT, "glSecondaryColor3usvEXT(coord) -> None")

void glSecondaryColor3svEXT(const GLshort* coord);
DOC(glSecondaryColor3svEXT, "glSecondaryColor3svEXT(coord) -> None")

void glSecondaryColor3uivEXT(const GLuint* coord);
DOC(glSecondaryColor3uivEXT, "glSecondaryColor3iuvEXT(coord) -> None")

void glSecondaryColor3ivEXT(const GLint* coord);
DOC(glSecondaryColor3ivEXT, "glSecondaryColor3ivEXT(coord) -> None")

void glSecondaryColor3fvEXT(const GLfloat* coord);
DOC(glSecondaryColor3fvEXT, "glSecondaryColor3fvEXT(coord) -> None")

void glSecondaryColor3dvEXT(const GLdouble* coord);
DOC(glSecondaryColor3dvEXT, "glSecondaryColor3dvEXT(coord) -> None")

/* turn the exception handler on */
%include gl_exception_handler.inc

/*void glSecondaryColorPointerEXT (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer); */

%{
#ifndef GL_SECONDARY_COLOR_ARRAY_POINTER_EXT
#define GL_SECONDARY_COLOR_ARRAY_POINTER_EXT 0x845D
#endif

void _glSecondaryColorPointerEXT(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_SECONDARY_COLOR_ARRAY_POINTER_EXT);
	acquire(pointer);
	glSecondaryColorPointerEXT(size, type, stride, pointer);
}
%}

%name(glSecondaryColorPointerEXT) void _glSecondaryColorPointerEXT(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glSecondaryColorPointerEXT, "glSecondaryColorPointerEXT(size, type, stride, pointer) -> None")

%name(glSecondaryColorPointerubEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_UNSIGNED_BTE, GLsizei stride_0, GLubyte* pointer);
DOC(glSecondaryColorPointerubEXT, "glSecondaryColorPointerubEXT(pointer) -> None")

%name(glSecondaryColorPointerbEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glSecondaryColorPointerbEXT, "glSecondaryColorPointerubEXT(pointer) -> None")

%name(glSecondaryColorPointerusEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLushort* pointer);
DOC(glSecondaryColorPointerusEXT, "glSecondaryColorPointerusEXT(pointer) -> None")

%name(glSecondaryColorPointersEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glSecondaryColorPointersEXT, "glSecondaryColorPointersEXT(pointer) -> None")

%name(glSecondaryColorPointeruiEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_UNSIGNED_INT, GLsizei stride_0, GLuint* pointer);
DOC(glSecondaryColorPointeruiEXT, "glSecondaryColorPointeruiEXT(pointer) -> None")

%name(glSecondaryColorPointeriEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glSecondaryColorPointeriEXT, "glSecondaryColorPointeriEXT(pointer) -> None")

%name(glSecondaryColorPointerfEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glSecondaryColorPointerfEXT, "glSecondaryColorPointerfEXT(pointer) -> None")

%name(glSecondaryColorPointerdEXT) void _glSecondaryColorPointerEXT(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glSecondaryColorPointerdEXT, "glSecondaryColorPointerdEXT(pointer) -> None")



%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_secondary_color)
	"glSecondaryColor3ubEXT",
	"glSecondaryColor3bEXT",
	"glSecondaryColor3usEXT",
	"glSecondaryColor3sEXT",
	"glSecondaryColor3uiEXT",
	"glSecondaryColor3iEXT",
	"glSecondaryColor3fEXT",
	"glSecondaryColor3dEXT",
	"glSecondaryColor3ubvEXT",
	"glSecondaryColor3bvEXT",
	"glSecondaryColor3usvEXT",
	"glSecondaryColor3svEXT",
	"glSecondaryColor3uivEXT",
	"glSecondaryColor3ivEXT",
	"glSecondaryColor3fvEXT",
	"glSecondaryColor3dvEXT",
	"glSecondaryColorPointerEXT",
#endif
	NULL
};

#define glInitSecondaryColorEXT() InitExtension("GL_EXT_secondary_color", proc_names)
%}

int glInitSecondaryColorEXT();
DOC(glInitSecondaryColorEXT, "glInitSecondaryColorEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitSecondaryColorEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_COLOR_SUM_EXT			    0x8458

#define GL_CURRENT_SECONDARY_COLOR_EXT	    0x8459
#define GL_SECONDARY_COLOR_ARRAY_SIZE_EXT	    0x845A
#define GL_SECONDARY_COLOR_ARRAY_TYPE_EXT	    0x845B
#define GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT    0x845C

#define GL_SECONDARY_COLOR_ARRAY_POINTER_EXT   0x845D

#define GL_SECONDARY_COLOR_ARRAY_EXT	    0x845E

