/*
# BUILD api_versions [0x103]
# BUILD gl_platforms ['WGL']
# BUILD libs ['gdi32']
*/

%module swap_control

#define __version__ "$Revision: 1.35.6.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057wgl_swap_control.txt"

%{
/**
 *
 * WGL.EXT.swap_control Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc
%include WGL/util.inc

%include wgl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(WGL_EXT_swap_control)
DECLARE_EXT(wglSwapIntervalEXT, int, 0, (int interval), (interval))
DECLARE_EXT(wglGetSwapIntervalEXT, int, -1, (), ())
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(WGL_EXT_swap_control)
	"wglSwapIntervalEXT",
	"wglGetSwapIntervalEXT",
#endif
	NULL
};

#define wglInitSwapControlARB() InitExtension("WGL_EXT_swap_control", proc_names)
%}

int wglInitSwapControlARB();
DOC(wglInitSwapControlARB, "wglInitSwapControlARB() -> bool")

%{
PyObject *__info()
{
	if (wglInitSwapControlARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

int wglSwapIntervalEXT(int interval);
DOC(wglSwapIntervalEXT, "wglSwapIntervalEXT(interval) -> BOOL")

int wglGetSwapIntervalEXT();
DOC(wglGetSwapIntervalEXT, "wglGetSwapIntervalEXT() -> int")


