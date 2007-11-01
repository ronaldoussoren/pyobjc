/*
# BUILD api_versions [0x100]
# BUILD gl_platforms ['WGL']
# BUILD libs ['gdi32']
*/

%module pixel_format

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Mike Fletcher <mcfletch@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057wgl_pixel_format.txt"

%{
/**
 *
 * WGL.ARB.pixel_format Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Mike Fletcher <mcfletch@users.sourceforge.net>
 * 
***/
%}

%include util.inc
%include WGL/util.inc

%include wgl_exception_handler.inc

/* Typemaps for handling variable-length return-value array */

%{
#if !EXT_DEFINES_PROTO || !defined(WGL_ARB_pixel_format)
DECLARE_EXT(
wglGetPixelFormatAttribivARB, BOOL, 0, 
(HDC hdc,
	int iPixelFormat,
	int iLayerPlane,
	UINT nAttributes, /* extraneous, calculate from len(piAttributes) */
	const int *piAttributes,
	int *piValues /* calculate length from len(piAttributes), create and return */
),
(hdc, iPixelFormat, iLayerPlane, nAttributes, piAttributes, piValues)
)
DECLARE_EXT(
wglGetPixelFormatAttribfvARB, BOOL, 0, 
(HDC hdc,
	int iPixelFormat,
	int iLayerPlane,
	UINT nAttributes, /* extraneous, calculate from len(piAttributes) */
	const int *piAttributes,
	float *pfValues /* calculate length from len(piAttributes), create and return */
),
(hdc, iPixelFormat, iLayerPlane, nAttributes, piAttributes, pfValues)
)
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(WGL_ARB_pixel_format)
	"wglGetPixelFormatAttribivARB",
#endif
	NULL
};

#define wglInitPixelFormatARB() InitExtension("WGL_ARB_pixel_format", proc_names)
%}

%{
#define __wglGetPixelFormatAttribXvARB(CHR,TYPE,LONG_TYPE,PY_FROM_LONG,ARRAY_TYPE) PyObject * __wglGetPixelFormatAttrib##CHR##vARB( \
	HDC hdc, \
	int iPixelFormat,\
	int iLayerPlane,\
	PyObject *piAttributes\
) {\
	/* Wrapper for wglGetPixelFormatAttrib{if}vARB\
\
	Extracts attributes from piAttributes,\
	allocates new result array as necessary, and\
	returns a raw integer if there's only one\
	attribute.\
	 */\
	int dims[1] = {0};\
	PyObject * result = NULL;\
	int nAttributes = 0;\
	int success = 0;\
	PyArrayObject * sourceArray = NULL;\
\
	/* specialise on result type */\
	TYPE single[1] = {0};\
	TYPE * resultArray = NULL;\
\
	sourceArray = (PyArrayObject *) PyArray_ContiguousFromObject(\
		piAttributes, \
		PyArray_INT,\
		1, \
		1\
	);\
	if (!sourceArray) {\
		PyErr_Format(\
			PyExc_TypeError,\
			"Could not convert piAttributes to unsigned int array"\
		);\
		return NULL;\
	}\
	nAttributes = sourceArray->dimensions[0];\
	/* now create the return-value array */\
	if (nAttributes == 1) {\
		/* make the target the single array defined above */\
		resultArray = single;\
	} else {\
		dims[0] = nAttributes;\
		/* specialise on result type */\
		result = PyArray_FromDims( 1, dims, ARRAY_TYPE );\
		if (result == NULL) {\
			PyErr_Format(\
				PyExc_MemoryError,\
				"Could not create result array"\
			);\
			return NULL;\
		}\
		/* specialise on result type */\
		resultArray = (TYPE *) (((PyArrayObject *)result)->data);\
	}\
	SetLastError(0);\
	/* specialise on result type */\
	success = wglGetPixelFormatAttrib##CHR##vARB( \
		hdc, iPixelFormat, \
		iLayerPlane, nAttributes, \
		(const int *)(sourceArray->data), \
		resultArray\
	);\
	if (success)  {\
		if (nAttributes == 1) {\
			/* specialise on result type */\
			return PY_FROM_LONG( (LONG_TYPE)(single[0]));\
		} else {\
			Py_INCREF( result );\
			return result;\
		}\
	} else {\
		if (WGLErrOccurred()) {\
			return NULL;\
		} else {\
			PyErr_Format(\
				PyExc_WindowsError,\
				"wglGetPixelFormatAttrib{if}vARB: no WGL error reported but return value was false\n"\
				"\t%d %d", (long)hdc, iLayerPlane\
			);\
			return NULL;\
		}\
	}\
}

__wglGetPixelFormatAttribXvARB( i, int, long, PyInt_FromLong, PyArray_INT );
/* something is wrong with the float version, always fails :( */
__wglGetPixelFormatAttribXvARB( f, FLOAT, double, PyFloat_FromDouble, PyArray_FLOAT );

%}



int wglInitPixelFormatARB();
DOC(wglInitPixelFormatARB, "wglInitPixelFormatARB() -> bool")

%{
PyObject *__info()
{
	if (wglInitPixelFormatARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

%name(wglGetPixelFormatAttribivARB) PyObject * __wglGetPixelFormatAttribivARB(
	HDC hdc, 
	int iPixelFormat,
	int iLayerPlane,
	PyObject * piAttributes
);
%name(wglGetPixelFormatAttribfvARB) PyObject * __wglGetPixelFormatAttribfvARB(
	HDC hdc, 
	int iPixelFormat,
	int iLayerPlane,
	PyObject * piAttributes
);


#define WGL_NUMBER_PIXEL_FORMATS_ARB		0x2000
#define WGL_DRAW_TO_WINDOW_ARB			0x2001
#define WGL_DRAW_TO_BITMAP_ARB			0x2002
#define WGL_ACCELERATION_ARB			0x2003
#define WGL_NEED_PALETTE_ARB			0x2004
#define WGL_NEED_SYSTEM_PALETTE_ARB		0x2005
#define WGL_SWAP_LAYER_BUFFERS_ARB		0x2006
#define WGL_SWAP_METHOD_ARB			0x2007
#define WGL_NUMBER_OVERLAYS_ARB			0x2008
#define WGL_NUMBER_UNDERLAYS_ARB		0x2009
#define WGL_TRANSPARENT_ARB			0x200A
#define WGL_TRANSPARENT_RED_VALUE_ARB		0x2037
#define WGL_TRANSPARENT_GREEN_VALUE_ARB		0x2038
#define WGL_TRANSPARENT_BLUE_VALUE_ARB		0x2039
#define WGL_TRANSPARENT_ALPHA_VALUE_ARB		0x203A
#define WGL_TRANSPARENT_INDEX_VALUE_ARB		0x203B
#define WGL_SHARE_DEPTH_ARB			0x200C
#define WGL_SHARE_STENCIL_ARB			0x200D
#define WGL_SHARE_ACCUM_ARB			0x200E
#define WGL_SUPPORT_GDI_ARB			0x200F
#define WGL_SUPPORT_OPENGL_ARB			0x2010
#define WGL_DOUBLE_BUFFER_ARB			0x2011
#define WGL_STEREO_ARB				0x2012
#define WGL_PIXEL_TYPE_ARB			0x2013
#define WGL_COLOR_BITS_ARB			0x2014
#define WGL_RED_BITS_ARB			0x2015
#define WGL_RED_SHIFT_ARB			0x2016
#define WGL_GREEN_BITS_ARB			0x2017
#define WGL_GREEN_SHIFT_ARB			0x2018
#define WGL_BLUE_BITS_ARB			0x2019
#define WGL_BLUE_SHIFT_ARB			0x201A
#define WGL_ALPHA_BITS_ARB			0x201B
#define WGL_ALPHA_SHIFT_ARB			0x201C
#define WGL_ACCUM_BITS_ARB			0x201D
#define WGL_ACCUM_RED_BITS_ARB			0x201E
#define WGL_ACCUM_GREEN_BITS_ARB		0x201F
#define WGL_ACCUM_BLUE_BITS_ARB			0x2020
#define WGL_ACCUM_ALPHA_BITS_ARB		0x2021
#define WGL_DEPTH_BITS_ARB			0x2022
#define WGL_STENCIL_BITS_ARB			0x2023
#define WGL_AUX_BUFFERS_ARB			0x2024

#define WGL_NO_ACCELERATION_ARB			0x2025
#define WGL_GENERIC_ACCELERATION_ARB		0x2026
#define WGL_FULL_ACCELERATION_ARB		0x2027

#define WGL_SWAP_EXCHANGE_ARB			0x2028
#define WGL_SWAP_COPY_ARB			0x2029
#define WGL_SWAP_UNDEFINED_ARB			0x202A

#define WGL_TYPE_RGBA_ARB			0x202B
#define WGL_TYPE_COLORINDEX_ARB			0x202C

