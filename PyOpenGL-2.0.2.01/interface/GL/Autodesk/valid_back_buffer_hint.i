/*
# BUILD api_versions [0x100]
*/

%module valid_back_buffer_hint

#define __version__ "$Revision: 1.29.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057www.autodesk.com\057develop\057devres\057heidi\057oglspecs.htm"

%{
/**
 *
 * GL.Autodesk.valid_back_buffer_hint Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_Autodesk_valid_back_buffer_hint)
DECLARE_VOID_EXT(glWindowBackBufferHint, (), ())
DECLARE_EXT(glValidBackBufferHint, GLboolean, 0, (GLint x, GLint y, GLsizei width, GLsizei height), (x, y, width, height))
#endif
%}

void glWindowBackBufferHint();
DOC(glWindowBackBufferHint, "glWindowBackBufferHint() -> None")

GLboolean glValidBackBufferHint(GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glValidBackBufferHint, "glValidBackBufferHint(x, y, width, height) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_Autodesk_valid_back_buffer_hint)
	"glWindowBackBufferHint",
	"glValidBackBufferHint",
#endif
	NULL
};

#define glInitValidBackBufferHintAutodesk() InitExtension("GL_Autodesk_valid_back_buffer_hint", proc_names)
%}

int glInitValidBackBufferHintAutodesk();
DOC(glInitValidBackBufferHintAutodesk, "glInitValidBackBufferHintAutodesk() -> bool")


%{
PyObject *__info()
{
	if (glInitValidBackBufferHintAutodesk())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
