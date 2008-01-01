/*
# BUILD api_versions [0x100]
# BUILD gl_platforms ['WGL']
# BUILD libs ['gdi32']
*/

%module buffer_region

#define __version__ "$Revision: 1.35.6.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057wgl_buffer_region.txt"

%{
/**
 *
 * WGL.ARB.buffer_region Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(WGL_ARB_buffer_region)
DECLARE_EXT(wglCreateBufferRegionARB, HANDLE, 0, (HDC hdc, int iLayerPlane, UINT uType), (hdc, iLayerPlane, uType))
DECLARE_EXT(wglDeleteBufferRegionARB, HANDLE, 0, (HANDLE hRegion), (hRegion))
DECLARE_EXT(wglSaveBufferRegionARB, BOOL, 0, (HANDLE hRegion, int x, int y, int width, int height), (hRegion, x, y, width, height))
DECLARE_EXT(wglRestoreBufferRegionARB, BOOL, 0, (HANDLE hRegion, int x, int y, int width, int height, int xSrc, int ySrc), (hRegion, x, y, width, height, xSrc, ySrc))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(WGL_ARB_buffer_region)
	"wglCreateBufferRegionARB",
	"wglDeleteBufferRegionARB",
	"wglSaveBufferRegionARB",
	"wglRestoreBufferRegionARB",
#endif
	NULL
};

#define wglInitBufferRegionARB() InitExtension("WGL_ARB_buffer_region", proc_names)

%}

int wglInitBufferRegionARB();
DOC(wglInitBufferRegionARB, "wglInitBufferRegionARB() -> bool")

%{
PyObject *__info()
{
	if (wglInitBufferRegionARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

HANDLE wglCreateBufferRegionARB(HDC hdc, int iLayerPlane, UINT uType);
DOC(wglCreateBufferRegionARB, "wglCreateBufferRegionARB(hdc, iLayerPlane, uType) -> HANDLE")


VOID wglDeleteBufferRegionARB(HANDLE hRegion);
DOC(wglDeleteBufferRegionARB, "wglDeleteBufferRegionARB(hRegion) -> HANDLE")


BOOL wglSaveBufferRegionARB(HANDLE hRegion, int x, int y, int width, int height);
DOC(wglSaveBufferRegionARB, "wglSaveBufferRegionARB(hRegion, x, y, width, height) -> HANDLE")


BOOL wglRestoreBufferRegionARB(HANDLE hRegion, int x, int y, int width, int height, int xSrc, int ySrc);
DOC(wglRestoreBufferRegionARB, "wglRestoreBufferRegionARB(hRegion, x, y, width, height, xSrc, ySrc) -> BOOL")


