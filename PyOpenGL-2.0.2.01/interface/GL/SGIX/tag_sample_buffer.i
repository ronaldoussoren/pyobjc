/*
# BUILD api_versions [0x102]
*/

%module tag_sample_buffer

%{
/**
 *
 * GL.SGIX.tag_sample_buffer Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057tag_sample_buffer.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_tag_sample_buffer)
DECLARE_VOID_EXT(glTagSampleBufferSGIX, (), ())
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_tag_sample_buffer)
	"glTagSampleBufferSGIX",
#endif
	NULL
};

#define glInitTagSampleBufferSGIX() InitExtension("GL_SGIX_tag_sample_buffer", proc_names)
%}

int glInitTagSampleBufferSGIX();
DOC(glInitTagSampleBufferSGIX, "glInitTagSampleBufferSGIX() -> bool")

void glTagSampleBufferSGIX();
DOC(glTagSampleBufferSGIX, "glTagSampleBufferSGIX() -> None")


%{
PyObject *__info()
{
	if (glInitTagSampleBufferSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



#define GL_REFERENCE_PLANE_SGIX           0x817D
#define GL_REFERENCE_PLANE_EQUATION_SGIX  0x817E
