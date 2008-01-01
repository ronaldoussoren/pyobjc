/*
# BUILD api_versions [0x103]
*/

%module transpose_matrix

#define __version__ "$Revision: 1.26.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057transpose_matrix.txt"

%{
/**
 *
 * GL.ARB.transpose_matrix Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_transpose_matrix)
DECLARE_VOID_EXT(glLoadTransposeMatrixfARB, (const GLfloat* matrix), (matrix))
DECLARE_VOID_EXT(glLoadTransposeMatrixdARB, (const GLdouble* matrix), (matrix))
DECLARE_VOID_EXT(glMultTransposeMatrixfARB, (const GLfloat* matrix), (matrix))
DECLARE_VOID_EXT(glMultTransposeMatrixdARB, (const GLdouble* matrix), (matrix))
#endif
%}

void glLoadTransposeMatrixfARB(const GLfloat* matrix);
DOC(glLoadTransposeMatrixfARB, "glLoadTransposeMatrixfARB(matrix) -> None")


void glLoadTransposeMatrixdARB(const GLdouble* matrix);
DOC(glLoadTransposeMatrixdARB, "glLoadTransposeMatrixdARB(matrix) -> None")

void glMultTransposeMatrixfARB(const GLfloat* matrix);
DOC(glMultTransposeMatrixfARB, "glMultTransposeMatrixfARB(matrix) -> None")


void glMultTransposeMatrixdARB(const GLdouble* matrix);
DOC(glMultTransposeMatrixdARB, "glMultTransposeMatrixdARB(matrix) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_transpose_matrix)
	"glLoadTransposeMatrixfARB",
	"glLoadTransposeMatrixdARB",
	"glMultTransposeMatrixfARB",
	"glMultTransposeMatrixdARB",
#endif
	NULL
};

#define glInitTransposeMatrixARB() InitExtension("GL_ARB_transpose_matrix", proc_names)
%}

int glInitTransposeMatrixARB();
DOC(glInitTransposeMatrixARB, "glInitTransposeMatrixARB() -> bool")

%{
PyObject *__info()
{
	if (glInitTransposeMatrixARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_TRANSPOSE_MODELVIEW_MATRIX_ARB 0x84E3
#define GL_TRANSPOSE_PROJECTION_MATRIX_ARB 0x84E4
#define GL_TRANSPOSE_TEXTURE_MATRIX_ARB 0x84E5
#define GL_TRANSPOSE_COLOR_MATRIX_ARB 0x84E6
