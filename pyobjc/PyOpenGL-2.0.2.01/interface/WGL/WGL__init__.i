/*
# BUILD api_versions [0x400]
# BUILD shadow 1
# BUILD macro_template 'WINVER >= 0x%(api_version)x'
# BUILD gl_platforms ['WGL']
# BUILD libs ['gdi32']
# BUILD api_version_check 1
*/

%module WGL__init__

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:21:40 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "This module provides access to the WGL API.\n\
\n\
Documentation:\n\
    MSDN:  http:\057\057msdn.microsoft.com/library/?url=/library/en-us/opengl/hh/opengl/ntopnglo_0e0o.asp?frame=true"

%{
/**
 *
 * WGL Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include WGL/util.inc

%include wgl_exception_handler.inc

/* OpenGL wgl prototypes */

/* Pixel format descriptor */
typedef struct tagPIXELFORMATDESCRIPTOR
{
 WORD nSize;
 WORD nVersion;
 DWORD dwFlags;
 BYTE iPixelType;
 BYTE cColorBits;
 BYTE cRedBits;
 BYTE cRedShift;
 BYTE cGreenBits;
 BYTE cGreenShift;
 BYTE cBlueBits;
 BYTE cBlueShift;
 BYTE cAlphaBits;
 BYTE cAlphaShift;
 BYTE cAccumBits;
 BYTE cAccumRedBits;
 BYTE cAccumGreenBits;
 BYTE cAccumBlueBits;
 BYTE cAccumAlphaBits;
 BYTE cDepthBits;
 BYTE cStencilBits;
 BYTE cAuxBuffers;
 BYTE iLayerType;
 BYTE bReserved;
 DWORD dwLayerMask;
 DWORD dwVisibleMask;
 DWORD dwDamageMask;
} PIXELFORMATDESCRIPTOR;

%{
PIXELFORMATDESCRIPTOR* new_PIXELFORMATDESCRIPTOR()
{
	PIXELFORMATDESCRIPTOR *result = PyMem_New(PIXELFORMATDESCRIPTOR, 1);
	memset(result, 0, sizeof(PIXELFORMATDESCRIPTOR));
	result->nSize = sizeof(PIXELFORMATDESCRIPTOR);
	result->nVersion = 1;
	return result;
}

void delete_PIXELFORMATDESCRIPTOR(PIXELFORMATDESCRIPTOR *x)
{
	PyMem_Del(x);
}
%}

%extend PIXELFORMATDESCRIPTOR
{
	PIXELFORMATDESCRIPTOR();
	~PIXELFORMATDESCRIPTOR();
}

/* pixel types */
#define PFD_TYPE_RGBA 0
#define PFD_TYPE_COLORINDEX 1

/* layer types */
#define PFD_MAIN_PLANE 0
#define PFD_OVERLAY_PLANE 1
#define PFD_UNDERLAY_PLANE (-1)

/* PIXELFORMATDESCRIPTOR flags */
#define PFD_DOUBLEBUFFER 0x00000001
#define PFD_STEREO 0x00000002
#define PFD_DRAW_TO_WINDOW 0x00000004
#define PFD_DRAW_TO_BITMAP 0x00000008
#define PFD_SUPPORT_GDI 0x00000010
#define PFD_SUPPORT_OPENGL 0x00000020
#define PFD_GENERIC_FORMAT 0x00000040
#define PFD_NEED_PALETTE 0x00000080
#define PFD_NEED_SYSTEM_PALETTE 0x00000100
#define PFD_SWAP_EXCHANGE 0x00000200
#define PFD_SWAP_COPY 0x00000400
#define PFD_SWAP_LAYER_BUFFERS 0x00000800
#define PFD_GENERIC_ACCELERATED 0x00001000
#define PFD_SUPPORT_DIRECTDRAW 0x00002000

/* PIXELFORMATDESCRIPTOR flags for use in ChoosePixelFormat only */
#define PFD_DEPTH_DONTCARE 0x20000000
#define PFD_DOUBLEBUFFER_DONTCARE 0x40000000
#define PFD_STEREO_DONTCARE 0x80000000

typedef struct _POINTFLOAT {
 FLOAT x;
 FLOAT y;
} POINTFLOAT, *PPOINTFLOAT;

%extend POINTFLOAT
{
	POINTFLOAT()
	{
		POINTFLOAT *result = PyMem_New(POINTFLOAT, 1);
		memset(result, 0, sizeof(POINTFLOAT));
		return result;
	}
	
	~POINTFLOAT()
	{
		PyMem_Del(self);
	}
}

typedef struct _GLYPHMETRICSFLOAT {
 FLOAT gmfBlackBoxX;
 FLOAT gmfBlackBoxY;
 POINTFLOAT gmfptGlyphOrigin;
 FLOAT gmfCellIncX;
 FLOAT gmfCellIncY;
} GLYPHMETRICSFLOAT;

%{
GLYPHMETRICSFLOAT* new_GLYPHMETRICSFLOAT()
{
	GLYPHMETRICSFLOAT *result = PyMem_New(GLYPHMETRICSFLOAT, 1);
	memset(result, 0, sizeof(GLYPHMETRICSFLOAT));
	return result;
}

void delete_GLYPHMETRICSFLOAT(GLYPHMETRICSFLOAT *x)
{
	PyMem_Del(x);
}
%}

%extend GLYPHMETRICSFLOAT
{
	GLYPHMETRICSFLOAT();
	~GLYPHMETRICSFLOAT();
}



#define WGL_FONT_LINES 0
#define WGL_FONT_POLYGONS 1
/* Layer plane descriptor */
typedef struct tagLAYERPLANEDESCRIPTOR { /* lpd */
 WORD nSize;
 WORD nVersion;
 DWORD dwFlags;
 BYTE iPixelType;
 BYTE cColorBits;
 BYTE cRedBits;
 BYTE cRedShift;
 BYTE cGreenBits;
 BYTE cGreenShift;
 BYTE cBlueBits;
 BYTE cBlueShift;
 BYTE cAlphaBits;
 BYTE cAlphaShift;
 BYTE cAccumBits;
 BYTE cAccumRedBits;
 BYTE cAccumGreenBits;
 BYTE cAccumBlueBits;
 BYTE cAccumAlphaBits;
 BYTE cDepthBits;
 BYTE cStencilBits;
 BYTE cAuxBuffers;
 BYTE iLayerPlane;
 BYTE bReserved;
 COLORREF crTransparent;
} LAYERPLANEDESCRIPTOR;

%{
LAYERPLANEDESCRIPTOR* new_LAYERPLANEDESCRIPTOR()
{
	LAYERPLANEDESCRIPTOR *result = PyMem_New(LAYERPLANEDESCRIPTOR, 1);
	memset(result, 0, sizeof(LAYERPLANEDESCRIPTOR));
	result->nSize = sizeof(LAYERPLANEDESCRIPTOR);
	result->nVersion = 1;
	return result;
}

void delete_LAYERPLANEDESCRIPTOR(LAYERPLANEDESCRIPTOR *x)
{
	PyMem_Del(x);
}
%}

%extend LAYERPLANEDESCRIPTOR
{
	LAYERPLANEDESCRIPTOR();
	~LAYERPLANEDESCRIPTOR();
}

/* LAYERPLANEDESCRIPTOR flags */
#define LPD_DOUBLEBUFFER 0x00000001
#define LPD_STEREO 0x00000002
#define LPD_SUPPORT_GDI 0x00000010
#define LPD_SUPPORT_OPENGL 0x00000020
#define LPD_SHARE_DEPTH 0x00000040
#define LPD_SHARE_STENCIL 0x00000080
#define LPD_SHARE_ACCUM 0x00000100
#define LPD_SWAP_EXCHANGE 0x00000200
#define LPD_SWAP_COPY 0x00000400
#define LPD_TRANSPARENT 0x00001000

#define LPD_TYPE_RGBA 0
#define LPD_TYPE_COLORINDEX 1

/* wglSwapLayerBuffers flags */
#define WGL_SWAP_MAIN_PLANE 0x00000001
#define WGL_SWAP_OVERLAY1 0x00000002
#define WGL_SWAP_OVERLAY2 0x00000004
#define WGL_SWAP_OVERLAY3 0x00000008
#define WGL_SWAP_OVERLAY4 0x00000010
#define WGL_SWAP_OVERLAY5 0x00000020
#define WGL_SWAP_OVERLAY6 0x00000040
#define WGL_SWAP_OVERLAY7 0x00000080
#define WGL_SWAP_OVERLAY8 0x00000100
#define WGL_SWAP_OVERLAY9 0x00000200
#define WGL_SWAP_OVERLAY10 0x00000400
#define WGL_SWAP_OVERLAY11 0x00000800
#define WGL_SWAP_OVERLAY12 0x00001000
#define WGL_SWAP_OVERLAY13 0x00002000
#define WGL_SWAP_OVERLAY14 0x00004000
#define WGL_SWAP_OVERLAY15 0x00008000
#define WGL_SWAP_UNDERLAY1 0x00010000
#define WGL_SWAP_UNDERLAY2 0x00020000
#define WGL_SWAP_UNDERLAY3 0x00040000
#define WGL_SWAP_UNDERLAY4 0x00080000
#define WGL_SWAP_UNDERLAY5 0x00100000
#define WGL_SWAP_UNDERLAY6 0x00200000
#define WGL_SWAP_UNDERLAY7 0x00400000
#define WGL_SWAP_UNDERLAY8 0x00800000
#define WGL_SWAP_UNDERLAY9 0x01000000
#define WGL_SWAP_UNDERLAY10 0x02000000
#define WGL_SWAP_UNDERLAY11 0x04000000
#define WGL_SWAP_UNDERLAY12 0x08000000
#define WGL_SWAP_UNDERLAY13 0x10000000
#define WGL_SWAP_UNDERLAY14 0x20000000
#define WGL_SWAP_UNDERLAY15 0x40000000

/*#if API_VERSION >= 1280
#define WGL_SWAPMULTIPLE_MAX 16

typedef struct _WGLSWAP
{
	HDC hdc;
	UINT uiFlags;
} WGLSWAP;


%{
WGLSWAP* new_WGLSWAP()
{
	WGLSWAP *result = PyMem_New(WGLSWAP, 1);
	memset(result, 0, sizeof(WGLSWAP));
	return result;
}

void delete_WGLSWAP(WGLSWAP *x)
{
	PyMem_Del(x);
}
%}

%extend WGLSWAP
{
	WGLSWAP();
	~WGLSWAP();
}

#endif*/


int ChoosePixelFormat(HDC hdc, PIXELFORMATDESCRIPTOR *ppfd);
DOC(ChoosePixelFormat, "ChoosePixelFormat(hdc, ppfd) -> int")

int DescribePixelFormat(HDC hdc, int iPixelFormat, UINT nBytes, PIXELFORMATDESCRIPTOR *ppfd);
DOC(DescribePixelFormat, "DescribePixelFormat(hdc, iPixelFormat, nBytes, ppfd) -> int")

/*UINT GetEnhMetaFilePixelFormat(HENHMETAFILE hemf, UINT cbBuffer, PIXELFORMATDESCRIPTOR *ppfd); */

int GetPixelFormat(HDC hdc);
DOC(GetPixelFormat, "GetPixelFormat(hdc) -> int")

BOOL SetPixelFormat(HDC hdc, int iPixelFormat, PIXELFORMATDESCRIPTOR *ppfd);
DOC(SetPixelFormat, "SetPixelFormat(hdc, iPixelFormat, ppfd) -> int")

BOOL SwapBuffers(HDC hdc);
DOC(SwapBuffers, "SwapBuffers(hdc) -> BOOL")

HGLRC wglCreateContext(HDC hdc);
DOC(wglCreateContext, "wglCreateContext(hdc) -> HGLRC")

HGLRC wglCreateLayerContext(HDC hdc, int iLayerPlane);
DOC(wglCreateLayerContext, "wglCreateLayerContext(hdc, iLayerPlane) -> HGLRC")

BOOL wglCopyContext(HGLRC hglrcSrc, HGLRC hglrcDst, UINT mask);
DOC(wglCopyContext, "wglCopyContext(hglrcSrc, hglrcDst, mask) -> BOOL")

BOOL wglDeleteContext(HGLRC hglrc);
DOC(wglDeleteContext, "wglDeleteContext(hglrc) -> BOOL")

BOOL wglDescribeLayerPlane(HDC hdc, int iPixelFormat, int iLayerPlane, UINT nBytes, LAYERPLANEDESCRIPTOR *plpd);
DOC(wglDescribeLayerPlane, "wglDescribeLayerPlane(hdc, iPixelFormat, iLayerPlane, nBytes, plpd) -> BOOL")

HGLRC wglGetCurrentContext(VOID);
DOC(wglGetCurrentContext, "wglGetCurrentContext() -> HGLRC");

HDC wglGetCurrentDC(VOID);
DOC(wglGetCurrentDC, "wglGetCurrentDC() -> HDC")

/*int wglGetLayerPaletteEntries(HDC hdc, int iLayerPlane, int iStart, int cEntries, COLORREF *pcr); */
%{
PyObject* _wglGetLayerPaletteEntries(HDC hdc, int iLayerPlane, int iStart, int cEntries)
{
	COLORREF *pcr = PyMem_New(COLORREF, cEntries);
	int n = wglGetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr);
	PyObject* result;
	
	if (n == 0)
	{
		Py_INCREF(Py_None);
		return Py_None;
	}
	
	result = _PyTuple_FromUnsignedIntArray(n, pcr);
	PyMem_Del(pcr);
	return result;
}
%}

%name(wglGetLayerPaletteEntries) PyObject* _wglGetLayerPaletteEntries(HDC hdc, int iLayerPlane, int iStart, int cEntries);
DOC(wglGetLayerPaletteEntries, "wglGetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr) -> cr")

PROC wglGetProcAddress(LPCSTR lpszProc);
DOC(wglGetProcAddress, "wglGetProcAddress(lpszProc) -> PROC")

BOOL wglMakeCurrent(HDC hdc, HGLRC hglrc);
DOC(wglMakeCurrent, "wglMakeCurrent(hdc, hglrc) -> BOOL")

BOOL wglRealizeLayerPalette(HDC hdc, int iLayerPlane, BOOL bRealize);
DOC(wglRealizeLayerPalette, "wglRealizeLayerPalette(hdc, iLayerPlane, bRealize) -> BOOL")

int wglSetLayerPaletteEntries(HDC hdc, int iLayerPlane, int iStart, int n_4, CONST COLORREF *pcr);
DOC(wglSetLayerPaletteEntries, "wglSetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr) -> int")

BOOL wglShareLists(HGLRC hglrc1, HGLRC hglrc2);
DOC(wglShareLists, "wglShareLists(hglrc1, hglrc2) -> BOOL")

BOOL wglSwapLayerBuffers(HDC hdc, UINT fuPlanes);
DOC(wglSwapLayerBuffers, "wglSwapLayerBuffers(hdc, fuPlanes) -> BOOL")

/*#if API_VERSION >= 1280 */
/*DWORD wglSwapMultipleBuffers(UINT, CONST WGLSWAP *); */
/*#endif */

BOOL wglUseFontBitmapsA(HDC hdc, DWORD first, DWORD count, DWORD listBase);
DOC(wglUseFontBitmapsA, "wglUseFontBitmapsA(hdc, first, count, listBase) -> BOOL")
BOOL wglUseFontBitmapsW(HDC hdc, DWORD first, DWORD count, DWORD listBase);
DOC(wglUseFontBitmapsW, "wglUseFontBitmapsW(hdc, first, count, listBase) -> BOOL")


%shadow %{
wglUseFontBitmaps = _WGL__init__.wglUseFontBitmapsA
%}


BOOL wglUseFontOutlinesA(HDC hdc, DWORD first, DWORD count, DWORD listBase, FLOAT deviation, FLOAT extrusion, int format, GLYPHMETRICSFLOAT *lpgmf);
DOC(wglUseFontOutlinesA, "wglUseFontOutlinesA(hdc, first, count, listBase, deviation, extrusion, formation, lpgmf) -> BOOL")
BOOL wglUseFontOutlinesW(HDC hdc, DWORD first, DWORD count, DWORD listBase, FLOAT deviation, FLOAT extrusion, int format, GLYPHMETRICSFLOAT *lpgmf);
DOC(wglUseFontOutlinesW, "wglUseFontOutlinesW(hdc, first, count, listBase, deviation, extrusion, formation, lpgmf) -> BOOL")

%shadow %{
wglUseFontOutlines = _WGL__init__.wglUseFontOutlinesA
%}


%shadow %{
def __info():
	return []
%}


%shadow %{
__api_version__ = _WGL__init__.__api_version__
__author__ = _WGL__init__.__author__
__date__ = _WGL__init__.__date__
__doc__ = _WGL__init__.__doc__
__version__ = _WGL__init__.__version__
%}
