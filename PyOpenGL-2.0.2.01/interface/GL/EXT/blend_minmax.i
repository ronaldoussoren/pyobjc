/*
# BUILD api_versions [0x103]
*/

%module blend_minmax

#define __version__ "$Revision: 1.22.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057blend_minmax.txt"

%{
/**
 *
 * GL.EXT.blend_minmax Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_blend_minmax)
DECLARE_VOID_EXT(glBlendEquationEXT, (GLenum mode), (mode))
#endif
%}

void glBlendEquationEXT(GLenum mode);
DOC(glBlendEquationEXT, "glBlendColorEXT(mode) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_blend_minmax)
	"glBlendEquationEXT",
#endif
	NULL
};

#define glInitBlendMinmaxEXT() InitExtension("GL_EXT_blend_minmax", proc_names)
%}

int glInitBlendMinmaxEXT();
DOC(glInitBlendMinmaxEXT, "glInitBlendMinmaxEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitBlendMinmaxEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_FUNC_ADD_EXT 0x8006
#define GL_MIN_EXT 0x8007
#define GL_MAX_EXT 0x8008

#define GL_BLEND_EQUATION_EXT 0x8009
