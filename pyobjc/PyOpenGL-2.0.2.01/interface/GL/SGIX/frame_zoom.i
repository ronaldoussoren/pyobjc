/*
# BUILD api_versions [0x104]
*/

%module frame_zoom

%{
/**
 *
 * GL.SGIX.frame_zoom Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057frame_zoom.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_frame_zoom)
DECLARE_VOID_EXT(glFrameZoomSGIX, (GLint factor), (factor))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_frame_zoom)
	"glFrameZoomSGIX",
#endif
	NULL
};

#define glInitFrameZoomSGIX() InitExtension("GL_SGIX_frame_zoom", proc_names)
%}

int glInitFrameZoomSGIX();
DOC(glInitFrameZoomSGIX, "glInitFrameZoomSGIX() -> bool")

void glFrameZoomSGIX(GLint factor);
DOC(glFrameZoomSGIX, "glFrameZoomSGIX(factor) -> None")

%{
#ifndef GL_SGIX_frame_zoom
#define GL_MAX_FRAMEZOOM_FACTOR_SGIX      0x818D
#endif

PyObject *__info()
{
	if (glInitFrameZoomSGIX())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_FRAMEZOOM_FACTOR_SGIX", GL_MAX_FRAMEZOOM_FACTOR_SGIX, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_FRAMEZOOM_SGIX                 0x818B
#define GL_FRAMEZOOM_FACTOR_SGIX          0x818C
#define GL_MAX_FRAMEZOOM_FACTOR_SGIX      0x818D
