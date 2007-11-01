/*
# BUILD api_versions [0x101]
*/

%module tbuffer

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\0573DFX\057tbuffer.txt"

%{
/**
 *
 * GL._3DFX.tbuffer Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_3DFX_tbuffer)
DECLARE_VOID_EXT(glTbufferMask3DFX, (GLuint mask), (mask))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_3DFX_tbuffer)
	"glTbufferMask3DFX",
#endif
	NULL
};

#define glInitTbuffer3DFX() InitExtension("GL_3DFX_tbuffer", proc_names)

%}

void glTbufferMask3DFX(GLuint mask);
DOC(glTbufferMask3DFX, "glTbufferMask3DFX(mask) -> None")

int glInitTbuffer3DFX();
DOC(glInitTbuffer3DFX, "glInitTbuffer3DFX() -> bool")


%{
PyObject *__info()
{
	if (glInitTbuffer3DFX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
