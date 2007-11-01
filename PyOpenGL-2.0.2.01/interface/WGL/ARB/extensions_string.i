/*
# BUILD api_versions [0x100]
# BUILD gl_platforms ['WGL']
# BUILD libs ['gdi32']
*/

%module extensions_string

#define __version__ "$Revision: 1.35.6.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057wgl_extensions_string.txt"

%{
/**
 *
 * WGL.ARB.extensions_string Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(WGL_ARB_extensions_string)
DECLARE_EXT(wglGetExtensionsStringARB, const char*, NULL, (HDC hdc), (hdc))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(WGL_ARB_extensions_string)
	"wglGetExtensionsStringARB",
#endif
	NULL
};

#define wglInitExtensionsStringARB() InitExtension("WGL_ARB_extensions_string", proc_names)
%}

int wglInitExtensionsStringARB();
DOC(wglInitExtensionsStringARB, "wglInitExtensionsStringARB() -> bool")

const char *wglGetExtensionsStringARB(HDC hdc);
DOC(wglGetExtensionsStringARB, "wglGetExtensionsStringARB(hdc) -> string")

%{
PyObject *__info()
{
	if (wglInitExtensionsStringARB())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sss", "wglGetExtensionsStringARB", wglGetExtensionsStringARB(wglGetCurrentDC()), "e"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}

%}

PyObject *__info();

