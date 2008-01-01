/*
# BUILD api_versions [0x107]
*/

%module blend_color

#define __version__ "$Revision: 1.28.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057blend_color.txt"

%{
/**
 *
 * GL.EXT.blend_color Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_blend_color)
DECLARE_VOID_EXT(glBlendColorEXT, (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha), (red, green, blue, alpha))
#endif
%}

void glBlendColorEXT(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha);
DOC(glBlendColorEXT, "glBlendColorEXT(red, green, blue, alpha) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_blend_color)
	"glBlendColorEXT",
#endif
	NULL
};

#define glInitBlendColorEXT() InitExtension("GL_EXT_blend_color", proc_names)
%}

int glInitBlendColorEXT();
DOC(glInitBlendColorEXT, "glInitBlendColorEXT() -> bool")



%{
PyObject *__info()
{
	if (glInitBlendColorEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_CONSTANT_COLOR_EXT 0x8001
#define GL_ONE_MINUS_CONSTANT_COLOR_EXT 0x8002
#define GL_CONSTANT_ALPHA_EXT 0x8003
#define GL_ONE_MINUS_CONSTANT_ALPHA_EXT 0x8004

#define GL_BLEND_COLOR_EXT 0x8005
