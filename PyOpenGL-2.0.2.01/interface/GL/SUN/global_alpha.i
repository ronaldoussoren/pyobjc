/*
# BUILD api_versions [0x107]
*/

%module global_alpha

%{
/**
 *
 * GL.SUN.global_alpha Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SUN\057global_alpha.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

	
%{
#if !EXT_DEFINES_PROTO || !defined(GL_SUN_global_alpha)
DECLARE_VOID_EXT(glGlobalAlphaFactorbSUN, (GLbyte factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactorsSUN, (GLshort factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactoriSUN, (GLint factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactorfSUN, (GLfloat factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactordSUN, (GLdouble factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactorubSUN, (GLubyte factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactorusSUN, (GLushort factor), (factor))
DECLARE_VOID_EXT(glGlobalAlphaFactoruiSUN, (GLuint factor), (factor))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SUN_global_alpha)
	"glGlobalAlphaFactorbSUN",
	"glGlobalAlphaFactorsSUN",
	"glGlobalAlphaFactoriSUN",
	"glGlobalAlphaFactorfSUN",
	"glGlobalAlphaFactordSUN",
	"glGlobalAlphaFactorubSUN",
	"glGlobalAlphaFactorusSUN",
	"glGlobalAlphaFactoruiSUN",
#endif
	NULL
};

#define glInitGlobalAlphaSUN() InitExtension("GL_SUN_global_alpha", proc_names)
%}


%{
PyObject *__info()
{
	if (glInitGlobalAlphaSUN())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


int glInitGlobalAlphaSUN();
DOC(glInitGlobalAlphaSUN, "glInitGlobalAlphaSUN() -> bool")

void glGlobalAlphaFactorbSUN(GLbyte factor);
DOC(glGlobalAlphaFactorbSUN, "glGlobalAlphaFactorbSUN(factor) -> None")

void glGlobalAlphaFactorsSUN(GLshort factor);
DOC(glGlobalAlphaFactorsSUN, "glGlobalAlphaFactorsSUN(factor) -> None")

void glGlobalAlphaFactoriSUN(GLint factor);
DOC(glGlobalAlphaFactoriSUN, "glGlobalAlphaFactoriSUN(factor) -> None")

void glGlobalAlphaFactorfSUN(GLfloat factor);
DOC(glGlobalAlphaFactorfSUN, "glGlobalAlphaFactorfSUN(factor) -> None")

void glGlobalAlphaFactordSUN(GLdouble factor);
DOC(glGlobalAlphaFactordSUN, "glGlobalAlphaFactordSUN(factor) -> None")

void glGlobalAlphaFactorubSUN(GLubyte factor);
DOC(glGlobalAlphaFactorubSUN, "glGlobalAlphaFactorubSUN(factor) -> None")

void glGlobalAlphaFactorusSUN(GLushort factor);
DOC(glGlobalAlphaFactorusSUN, "glGlobalAlphaFactorusSUN(factor) -> None")

void glGlobalAlphaFactoruiSUN(GLuint factor);
DOC(glGlobalAlphaFactoruiSUN, "glGlobalAlphaFactoriSUN(factor) -> None")


#define GL_GLOBAL_ALPHA_SUN 0x81D9

#define GL_GLOBAL_ALPHA_FACTOR_SUN 0x81DA
