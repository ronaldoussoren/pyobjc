/*
# BUILD api_versions [0x100]
*/

%module matrix_palette

#define __version__ "$Revision: 1.30.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057matrix_palette.txt"

%{
/**
 *
 * GL.ARB.matrix_palette Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_matrix_palette)
DECLARE_VOID_EXT(glMatrixIndexbvARB, (GLint size, const GLbyte* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexubvARB, (GLint size, const GLubyte* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexsvARB, (GLint size, const GLshort* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexusvARB, (GLint size, const GLushort* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexivARB, (GLint size, const GLint* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexuivARB, (GLint size, const GLuint* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexfvARB, (GLint size, const GLfloat* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexdvARB, (GLint size, const GLdouble* weights), (size, weights))
DECLARE_VOID_EXT(glMatrixIndexPointerARB, (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer), (size, type, stride, pointer))
DECLARE_VOID_EXT(glCurrentPaletteMatrixARB, (GLint count), (count))
#endif
%}

void glMatrixIndexbvARB(GLint n_1, const GLbyte* weights);
DOC(glMatrixIndexbvARB, "glMatrixIndexbvARB(weights) -> None")

void glMatrixIndexubvARB(GLint n_1, const GLubyte* weights);
DOC(glMatrixIndexubvARB, "glMatrixIndexubvARB(weights) -> None")

void glMatrixIndexsvARB(GLint n_1, const GLshort* weights);
DOC(glMatrixIndexsvARB, "glMatrixIndexsvARB(weights) -> None")

void glMatrixIndexusvARB(GLint n_1, const GLushort* weights);
DOC(glMatrixIndexusvARB, "glMatrixIndexusvARB(weights) -> None")

void glMatrixIndexivARB(GLint n_1, const GLint* weights);
DOC(glMatrixIndexivARB, "glMatrixIndexivARB(weights) -> None")

void glMatrixIndexuivARB(GLint n_1, const GLuint* weights);
DOC(glMatrixIndexuivARB, "glMatrixIndexuivARB(weights) -> None")

void glMatrixIndexfvARB(GLint n_1, const GLfloat* weights);
DOC(glMatrixIndexfvARB, "glMatrixIndexfvARB(weights) -> None")

void glMatrixIndexdvARB(GLint n_1, const GLdouble* weights);
DOC(glMatrixIndexdvARB, "glMatrixIndexdvARB(weights) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc


/*void glMatrixIndexPointerARB (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer); */

%{
#ifndef GL_MATRIX_INDEX_ARRAY_POINTER_ARB
#define GL_MATRIX_INDEX_ARRAY_POINTER_ARB 0x8849
#endif

void _glMatrixIndexPointerARB(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_MATRIX_INDEX_ARRAY_POINTER_ARB);
	acquire(pointer);
	glMatrixIndexPointerARB(size, type, stride, pointer);
}
%}

%name(glMatrixIndexPointerARB) void _glMatrixIndexPointerARB(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glMatrixIndexPointerARB, "glMatrixIndexPointerARB(size, type, stride, pointer) -> None")

%name(glMatrixIndexPointerubARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLubyte* pointer);
DOC(glMatrixIndexPointerubARB, "glMatrixIndexPointerubARB(pointer) -> None")

%name(glMatrixIndexPointerbARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glMatrixIndexPointerbARB, "glMatrixIndexPointerubARB(pointer) -> None")

%name(glMatrixIndexPointerusARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLushort* pointer);
DOC(glMatrixIndexPointerusARB, "glMatrixIndexPointerusARB(pointer) -> None")

%name(glMatrixIndexPointersARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glMatrixIndexPointersARB, "glMatrixIndexPointersARB(pointer) -> None")

%name(glMatrixIndexPointeruiARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_UNSIGNED_INT, GLsizei stride_0, GLuint* pointer);
DOC(glMatrixIndexPointeruiARB, "glMatrixIndexPointeruiARB(pointer) -> None")

%name(glMatrixIndexPointeriARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glMatrixIndexPointeriARB, "glMatrixIndexPointeriARB(pointer) -> None")

%name(glMatrixIndexPointerfARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glMatrixIndexPointerfARB, "glMatrixIndexPointerfARB(pointer) -> None")

%name(glMatrixIndexPointerdARB) void _glMatrixIndexPointerARB(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glMatrixIndexPointerdARB, "glMatrixIndexPointerdARB(pointer) -> None")


void glCurrentPaletteMatrixARB(GLint count);
DOC(glCurrentPaletteMatrixARB, "glCurrentPaletteMatrixARB(count) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_matrix_palette)
	"glMatrixIndexbvARB",
	"glMatrixIndexubvARB",
	"glMatrixIndexsvARB",
	"glMatrixIndexusvARB",
	"glMatrixIndexivARB",
	"glMatrixIndexuivARB",
	"glMatrixIndexfvARB",
	"glMatrixIndexdvARB",
	"glMatrixIndexPointerARB",
	"glCurrentPaletteMatrixARB",
#endif
	NULL
};

#define glInitMatrixPaletteARB() InitExtension("GL_ARB_matrix_palette", proc_names)
%}

int glInitMatrixPaletteARB();
DOC(glInitMatrixPaletteARB, "glInitMatrixPaletteARB() -> bool")

%{
#ifndef GL_ARB_matrix_palette
#define GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB    0x8841
#define GL_MAX_PALETTE_MATRICES_ARB              0x8842
#endif

PyObject *__info()
{

	if (glInitMatrixPaletteARB())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB", GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB, "i"));
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_PALETTE_MATRICES_ARB", GL_MAX_PALETTE_MATRICES_ARB, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_MATRIX_PALETTE_ARB                    0x8840

#define GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB    0x8841
#define GL_MAX_PALETTE_MATRICES_ARB              0x8842
#define GL_CURRENT_PALETTE_MATRIX_ARB            0x8843
      
#define GL_MATRIX_INDEX_ARRAY_ARB                0x8844

#define GL_CURRENT_MATRIX_INDEX_ARB              0x8845
      
#define GL_MATRIX_INDEX_ARRAY_SIZE_ARB           0x8846
#define GL_MATRIX_INDEX_ARRAY_TYPE_ARB           0x8847
#define GL_MATRIX_INDEX_ARRAY_STRIDE_ARB         0x8848

#define GL_MATRIX_INDEX_ARRAY_POINTER_ARB        0x8849

