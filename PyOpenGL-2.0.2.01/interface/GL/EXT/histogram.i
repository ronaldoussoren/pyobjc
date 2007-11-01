/*
# BUILD api_versions [0x11f]
*/

%module histogram

#define __version__ "$Revision: 1.1.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057histogram.txt"

%{
/**
 *
 * GL.EXT.histogram Module for PyOpenGL
 * 
 * Date: October 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_histogram)
DECLARE_VOID_EXT(glHistogramEXT,\
	(GLenum target, GLsizei width, GLenum internalformat, GLboolean sink),\
	(target, width, internalformat, sink))
DECLARE_VOID_EXT(glResetHistogramEXT,\
	(GLenum target),\
	(target))
DECLARE_VOID_EXT(glGetHistogramEXT,\
	(GLenum target, GLboolean reset, GLenum format, GLenum type, GLvoid* values),\
	(target, reset, format, type, values))
DECLARE_VOID_EXT(glGetHistogramParameterivEXT,\
	(GLenum target, GLenum pname, GLint* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetHistogramParameterfvEXT,\
	(GLenum target, GLenum pname, GLfloat* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glMinmaxEXT,\
	(GLenum target, GLenum internalformat, GLboolean sink),\
	(target, internalformat, sink))
DECLARE_VOID_EXT(glResetMinmaxEXT,\
	(GLenum target),\
	(target))
DECLARE_VOID_EXT(glGetMinmaxEXT,\
	(GLenum target, GLboolean reset, GLenum format, GLenum type, GLvoid* values),\
	(target, reset, format, type, values))
DECLARE_VOID_EXT(glGetMinmaxParameterivEXT,\
	(GLenum target, GLenum pname, GLint* params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetMinmaxParameterfvEXT,\
	(GLenum target, GLenum pname, GLfloat* params),\
	(target, pname, params))
#endif
%}

void glResetHistogramEXT(GLenum target);
DOC(glResetHistogramEXT, "glResetHistogramEXT(target) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_histogram)
	"glHistogramEXT",
	"glResetHistogramEXT",
	"glGetHistogramEXT",
	"glGetHistogramParameterivEXT",
	"glGetHistogramParameterfvEXT",
	"glMinmaxEXT",
	"glResetMinmaxEXT",
	"glGetMinmaxEXT",
	"glGetMinmaxParameterivEXT",
	"glGetMinmaxParameterfvEXT",
#endif
	NULL
};

#define glInitHistogramEXT() InitExtension("GL_EXT_histogram", proc_names)
%}

int glInitHistogramEXT();
DOC(glInitHistogramEXT, "glInitHistogramEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitHistogramEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_HISTOGRAM_EXT			    0x8024

#define GL_PROXY_HISTOGRAM_EXT		    0x8025

#define GL_HISTOGRAM_WIDTH_EXT                 0x8026
#define GL_HISTOGRAM_FORMAT_EXT                0x8027
#define GL_HISTOGRAM_RED_SIZE_EXT              0x8028
#define GL_HISTOGRAM_GREEN_SIZE_EXT            0x8029
#define GL_HISTOGRAM_BLUE_SIZE_EXT             0x802A
#define GL_HISTOGRAM_ALPHA_SIZE_EXT            0x802B
#define GL_HISTOGRAM_LUMINANCE_SIZE_EXT        0x802C
#define GL_HISTOGRAM_SINK_EXT                  0x802D

#define GL_MINMAX_EXT			    0x802E

#define GL_MINMAX_FORMAT_EXT		    0x802F
#define GL_MINMAX_SINK_EXT			    0x8030

