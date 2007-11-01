/*
# BUILD api_versions [0x102]
*/

%module window_pos

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057MESA\057window_pos.txt"

%{
/**
 *
 * GL.MESA.window_pos Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_MESA_window_pos)
DECLARE_VOID_EXT(glWindowPos2dMESA, (GLdouble x, GLdouble y), (x, y))
DECLARE_VOID_EXT(glWindowPos2fMESA, (GLfloat x, GLfloat y), (x, y))
DECLARE_VOID_EXT(glWindowPos2iMESA, (GLint x, GLint y), (x, y))
DECLARE_VOID_EXT(glWindowPos2sMESA, (GLshort x, GLshort y), (x, y))
DECLARE_VOID_EXT(glWindowPos3dMESA, (GLdouble x, GLdouble y, GLdouble z), (x, y, z))
DECLARE_VOID_EXT(glWindowPos3fMESA, (GLfloat x, GLfloat y, GLfloat z), (x, y, z))
DECLARE_VOID_EXT(glWindowPos3iMESA, (GLint x, GLint y, GLint z), (x, y, z))
DECLARE_VOID_EXT(glWindowPos3sMESA, (GLshort x, GLshort y, GLshort z), (x, y, z))
DECLARE_VOID_EXT(glWindowPos4dMESA, (GLdouble x, GLdouble y, GLdouble z, GLdouble w), (x, y, z, w))
DECLARE_VOID_EXT(glWindowPos4fMESA, (GLfloat x, GLfloat y, GLfloat z, GLfloat w), (x, y, z, w))
DECLARE_VOID_EXT(glWindowPos4iMESA, (GLint x, GLint y, GLint z, GLint w), (x, y, z, w))
DECLARE_VOID_EXT(glWindowPos4sMESA, (GLshort x, GLshort y, GLshort z, GLshort w), (x, y, z, w))
DECLARE_VOID_EXT(glWindowPos2dvMESA, (const GLdouble* p), (p))
DECLARE_VOID_EXT(glWindowPos2fvMESA, (const GLfloat* p), (p))
DECLARE_VOID_EXT(glWindowPos2ivMESA, (const GLint* p), (p))
DECLARE_VOID_EXT(glWindowPos2svMESA, (const GLshort* p), (p))
DECLARE_VOID_EXT(glWindowPos3dvMESA, (const GLdouble* p), (p))
DECLARE_VOID_EXT(glWindowPos3fvMESA, (const GLfloat* p), (p))
DECLARE_VOID_EXT(glWindowPos3ivMESA, (const GLint* p), (p))
DECLARE_VOID_EXT(glWindowPos3svMESA, (const GLshort* p), (p))
DECLARE_VOID_EXT(glWindowPos4dvMESA, (const GLdouble* p), (p))
DECLARE_VOID_EXT(glWindowPos4fvMESA, (const GLfloat* p), (p))
DECLARE_VOID_EXT(glWindowPos4ivMESA, (const GLint* p), (p))
DECLARE_VOID_EXT(glWindowPos4svMESA, (const GLshort* p), (p))
#endif
%}

void glWindowPos2dMESA(GLdouble x, GLdouble y);
DOC(glWindowPos2dMESA, "glWindowPos2dMESA(x, y) -> None")

void glWindowPos2fMESA(GLfloat x, GLfloat y);
DOC(glWindowPos2fMESA, "glWindowPos2fMESA(x, y) -> None")

void glWindowPos2iMESA(GLint x, GLint y);
DOC(glWindowPos2iMESA, "glWindowPos2iMESA(x, y) -> None")

void glWindowPos2sMESA(GLshort x, GLshort y);
DOC(glWindowPos2sMESA, "glWindowPos2sMESA(x, y) -> None")

void glWindowPos3dMESA(GLdouble x, GLdouble y, GLdouble z);
DOC(glWindowPos3dMESA, "glWindowPos3dMESA(x, y, z) -> None")

void glWindowPos3fMESA(GLfloat x, GLfloat y, GLfloat z);
DOC(glWindowPos3fMESA, "glWindowPos3fMESA(x, y, z) -> None")

void glWindowPos3iMESA(GLint x, GLint y, GLint z);
DOC(glWindowPos3iMESA, "glWindowPos3iMESA(x, y, z) -> None")

void glWindowPos3sMESA(GLshort x, GLshort y, GLshort z);
DOC(glWindowPos3sMESA, "glWindowPos3sMESA(x, y, z) -> None")

void glWindowPos4dMESA(GLdouble x, GLdouble y, GLdouble z, GLdouble w);
DOC(glWindowPos4dMESA, "glWindowPos4dMESA(x, y, z, w) -> None")

void glWindowPos4fMESA(GLfloat x, GLfloat y, GLfloat z, GLfloat w);
DOC(glWindowPos4fMESA, "glWindowPos4fMESA(x, y, z, w) -> None")

void glWindowPos4iMESA(GLint x, GLint y, GLint z, GLint w);
DOC(glWindowPos4iMESA, "glWindowPos4iMESA(x, y, z, w) -> None")

void glWindowPos4sMESA(GLshort x, GLshort y, GLshort z, GLshort w);
DOC(glWindowPos4sMESA, "glWindowPos4sMESA(x, y, z, w) -> None")

void glWindowPos2dvMESA(const GLdouble* p);
DOC(glWindowPos2dvMESA, "glWindowPos2dvMESA(p) -> None")

void glWindowPos2fvMESA(const GLfloat* p);
DOC(glWindowPos2fvMESA, "glWindowPos2fvMESA(p) -> None")

void glWindowPos2ivMESA(const GLint* p);
DOC(glWindowPos2ivMESA, "glWindowPos2ivMESA(p) -> None")

void glWindowPos2svMESA(const GLshort* p);
DOC(glWindowPos2svMESA, "glWindowPos2svMESA(p) -> None")

void glWindowPos3dvMESA(const GLdouble* p);
DOC(glWindowPos3dvMESA, "glWindowPos3dvMESA(p) -> None")

void glWindowPos3fvMESA(const GLfloat* p);
DOC(glWindowPos3fvMESA, "glWindowPos3fvMESA(p) -> None")

void glWindowPos3ivMESA(const GLint* p);
DOC(glWindowPos3ivMESA, "glWindowPos3ivMESA(p) -> None")

void glWindowPos3svMESA(const GLshort* p);
DOC(glWindowPos3svMESA, "glWindowPos3svMESA(p) -> None")

void glWindowPos4dvMESA(const GLdouble* p);
DOC(glWindowPos4dvMESA, "glWindowPos4dvMESA(p) -> None")

void glWindowPos4fvMESA(const GLfloat* p);
DOC(glWindowPos4fvMESA, "glWindowPos4fvMESA(p) -> None")

void glWindowPos4ivMESA(const GLint* p);
DOC(glWindowPos4ivMESA, "glWindowPos4ivMESA(p) -> None")

void glWindowPos4svMESA(const GLshort* p);
DOC(glWindowPos4svMESA, "glWindowPos4svMESA(p) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_MESA_window_pos)
	"glWindowPos2dMESA",
	"glWindowPos2fMESA",
	"glWindowPos2iMESA",
	"glWindowPos2sMESA",
	"glWindowPos3dMESA",
	"glWindowPos3fMESA",
	"glWindowPos3iMESA",
	"glWindowPos3sMESA",
	"glWindowPos4dMESA",
	"glWindowPos4fMESA",
	"glWindowPos4iMESA",
	"glWindowPos4sMESA",
	"glWindowPos2dvMESA",
	"glWindowPos2fvMESA",
	"glWindowPos2ivMESA",
	"glWindowPos2svMESA",
	"glWindowPos3dvMESA",
	"glWindowPos3fvMESA",
	"glWindowPos3ivMESA",
	"glWindowPos3svMESA",
	"glWindowPos4dvMESA",
	"glWindowPos4fvMESA",
	"glWindowPos4ivMESA",
	"glWindowPos4svMESA",
#endif
	NULL
};

#define glInitWindowPosMESA() InitExtension("GL_MESA_window_pos", proc_names)
%}

int glInitWindowPosMESA();
DOC(glInitWindowPosMESA, "glInitWindowPosMESA() -> bool")


%{
PyObject *__info()
{
	if (glInitWindowPosMESA())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


