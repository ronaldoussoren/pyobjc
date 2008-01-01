/*
# BUILD api_versions [0x100]
# BUILD gl_platforms ['WGL']
# BUILD libs ['gdi32']
*/

%module extensions_string

#define __version__ "$Revision: 1.38.6.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057wgl_extensions_string.txt"

%{
/**
 *
 * WGL.EXT.extensions_string Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc
%include WGL/util.inc

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(WGL_EXT_extensions_string)
	"wglGetExtensionsStringEXT",
#endif
	NULL
};

#define wglInitExtensionsStringEXT() InitExtension("WGL_EXT_extensions_string", proc_names)
%}

%include wgl_exception_handler.inc

int wglInitExtensionsStringEXT();
DOC(wglInitExtensionsStringEXT, "wglInitExtensionsStringEXT() -> bool")

%{
#if !EXT_DEFINES_PROTO || !defined(WGL_EXT_extensions_string)
DECLARE_EXT(wglGetExtensionsStringEXT, const char*, NULL, (), ())
#endif
%}

%{
PyObject *__info()
{
	if (wglInitExtensionsStringEXT())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sss", "wglGetExtensionsStringEXT", wglGetExtensionsStringEXT(), "e"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

%name(wglGetExtensionsStringEXT) const char *wglGetExtensionsStringEXT();
DOC(wglGetExtensionsStringEXT, "wglGetExtensionsStringEXT() -> string")



