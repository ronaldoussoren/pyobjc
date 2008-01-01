/*
# BUILD api_versions [0x101]
# BUILD macro_template 'defined(GL_VERSION_%(api_version_underscore)s)'
*/

%module swap_hint

%{
/**
 *
 * GL.WIN.swap_hint Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.33.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057msdn.microsoft.com\057library\057default.asp?URL=\057library\057psdk\057opengl\057glfunc01_16zy.htm"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_WIN_swap_hint)
DECLARE_VOID_EXT(glAddSwapHintRectWIN, (GLint x, GLint y, GLsizei width, GLsizei height), (x, y, width, height))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_WIN_swap_hint)
	"glAddSwapHintRectWIN",
#endif
	NULL
};

#define glInitSwapHintWIN() InitExtension("GL_WIN_swap_hint", proc_names)
%}

int glInitSwapHintWIN();
DOC(glInitSwapHintWIN, "glInitSwapHintWIN() -> bool")

void glAddSwapHintRectWIN(GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glAddSwapHintRectWIN, "glAddSwapHintRectWIN(x, y, width, height) -> None")


%{
PyObject *__info()
{
	if (glInitSwapHintWIN())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



