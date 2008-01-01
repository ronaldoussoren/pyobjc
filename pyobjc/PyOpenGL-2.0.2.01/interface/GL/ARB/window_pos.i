/*
# BUILD api_versions [0x100]
*/

%module window_pos

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:50 $"
#define __api_version__ API_VERSION
#define __author__ "Mike C. Fletcher <mcfletch@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057window_pos.txt"

%{
/**
 *
 * GL.ARB.window_pos Module for PyOpenGL
 * 
 * Date October 2003
 *
 * Authors Mike C. Fletcher <mcfletch@users.sourceforge.net>
 * 

	Turns out there's a Mesa extension that's 90% the same as
	this extension.  Sigh.
***/
%}
#undef EXPORT_UTIL
%include util.inc
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_window_pos)

DECLARE_VOID_EXT(glWindowPos2dARB, (GLdouble x, GLdouble y), (x, y));
DECLARE_VOID_EXT(glWindowPos2dvARB, (const GLdouble * v), (v));

DECLARE_VOID_EXT(glWindowPos2fARB, (GLfloat x, GLfloat y), (x, y));
DECLARE_VOID_EXT(glWindowPos2fvARB, (const GLfloat * v), (v));

DECLARE_VOID_EXT(glWindowPos2iARB, (GLint x, GLint y), (x, y));
DECLARE_VOID_EXT(glWindowPos2ivARB, (const GLint * v), (v));

DECLARE_VOID_EXT(glWindowPos2sARB, (GLshort x, GLshort y), (x, y));
DECLARE_VOID_EXT(glWindowPos2svARB, (const GLshort * v), (v));

DECLARE_VOID_EXT(glWindowPos3dARB, (GLdouble x, GLdouble y, GLdouble z), (x, y, z));
DECLARE_VOID_EXT(glWindowPos3dvARB, (const GLdouble * v), (v));

DECLARE_VOID_EXT(glWindowPos3fARB, (GLfloat x, GLfloat y, GLfloat z), (x, y, z));
DECLARE_VOID_EXT(glWindowPos3fvARB, (const GLfloat * v), (v));

DECLARE_VOID_EXT(glWindowPos3iARB, (GLint x, GLint y, GLint z), (x, y, z));
DECLARE_VOID_EXT(glWindowPos3ivARB, (const GLint * v), (v));

DECLARE_VOID_EXT(glWindowPos3sARB, (GLshort x, GLshort y, GLshort z), (x, y, z));
DECLARE_VOID_EXT(glWindowPos3svARB, (const GLshort * v), (v));

#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_vertex_blend)
	"glWindowPos2dARB",
	"glWindowPos2dvARB",
	"glWindowPos2fARB",
	"glWindowPos2fvARB",
	"glWindowPos2iARB",
	"glWindowPos2ivARB",
	"glWindowPos2sARB",
	"glWindowPos2svARB",
	"glWindowPos3dARB",
	"glWindowPos3dvARB",
	"glWindowPos3fARB",
	"glWindowPos3fvARB",
	"glWindowPos3iARB",
	"glWindowPos3ivARB",
	"glWindowPos3sARB",
	"glWindowPos3svARB",
#endif
	NULL
};

#define glInitWindowPosARB() InitExtension("GL_ARB_window_pos", proc_names)
%}

int glInitWindowPosARB();
DOC(glInitWindowPosARB, "glInitWindowPosARB() -> bool")

%typemap(python,check) const GLdouble * v2, const GLfloat * v2, const GLint * v2, const GLshort * v2 {
	int array_check_size;
	/* XXX :( there's something wonky going on with SWIG, it won't accept
	input, source or anything else I can think of for referencing the
	original Python object, so I'm having to hard-code the "first argument"
	name in :( */
	array_check_size = _PyObject_Dimension( obj0, 0 ); /* 0th rank */
	if ( array_check_size != 2) {
		PyErr_SetGLErrorMessage( GL_INVALID_VALUE, "Incorrect vector length for glWindowPos2*v");
		return NULL;
	}
}
%typemap(python,check) const GLdouble * v3, const GLfloat * v3, const GLint * v3, const GLshort * v3 {
	int array_check_size;
	/* XXX See note in previous typemap */
	array_check_size = _PyObject_Dimension( obj0, 0 ); /* 0th rank */
	if ( array_check_size != 3) {
		PyErr_SetGLErrorMessage( GL_INVALID_VALUE, "Incorrect vector length for glWindowPos3*v");
		return NULL;
	}
}


void glWindowPos2dARB(GLdouble x, GLdouble y);
DOC( glWindowPos2dARB, "glWindowPos2dARB(x, y) -> None")
void glWindowPos2fARB(GLfloat x, GLfloat y);
DOC( glWindowPos2fARB, "glWindowPos2fARB(x, y) -> None")

void glWindowPos2iARB(GLint x, GLint y);
DOC( glWindowPos2iARB, "glWindowPos2iARB(x, y) -> None")
void glWindowPos2sARB(GLshort x, GLshort y);
DOC( glWindowPos2sARB, "glWindowPos2sARB(x, y) -> None")

void glWindowPos2dvARB(const GLdouble *v2);
DOC( glWindowPos2dvARB, "glWindowPos2dvARB(v) -> None")
void glWindowPos2fvARB(const GLfloat *v2);
DOC( glWindowPos2fvARB, "glWindowPos2fvARB(v) -> None")

void glWindowPos2ivARB(const GLint *v2);
DOC( glWindowPos2ivARB, "glWindowPos2ivARB(v) -> None")
void glWindowPos2svARB(const GLshort *v2);
DOC( glWindowPos2svARB, "glWindowPos2svARB(v) -> None")

void glWindowPos3dARB(GLdouble x, GLdouble y, GLdouble z);
DOC( glWindowPos3dARB, "glWindowPos3dARB(x, y, z) -> None")
void glWindowPos3fARB(GLfloat x, GLfloat y, GLfloat z);
DOC( glWindowPos3fARB, "glWindowPos3fARB(x, y, z) -> None")

void glWindowPos3iARB(GLint x, GLint y, GLint z);
DOC( glWindowPos3iARB, "glWindowPos3iARB(x, y, z) -> None")
void glWindowPos3sARB(GLshort x, GLshort y, GLshort z);
DOC( glWindowPos3sARB, "glWindowPos3sARB(x, y, z) -> None")

void glWindowPos3dvARB(const GLdouble *v3);
DOC( glWindowPos3dvARB, "glWindowPos3dvARB(v) -> None")
void glWindowPos3fvARB(const GLfloat *v3);
DOC( glWindowPos3fvARB, "glWindowPos3fvARB(v) -> None")

void glWindowPos3ivARB(const GLint *v3);
DOC( glWindowPos3ivARB, "glWindowPos3ivARB(v) -> None")
void glWindowPos3svARB(const GLshort *v3);
DOC( glWindowPos3svARB, "glWindowPos3svARB(v) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc

%{

PyObject *__info()
{
	if (glInitWindowPosARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


