/*
# BUILD api_versions [0x005]
*/

%module multisample

#define __version__ "$Revision: 1.26.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057multisample.txt"

%{
/**
 *
 * GL.ARB.multisample Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_multisample)
DECLARE_VOID_EXT(glSampleCoverageARB, (GLclampf value, GLboolean invert), (value, invert))
#endif
%}

void glSampleCoverageARB(GLclampf value, GLboolean invert);
DOC(glSampleCoverageARB, "glSampleCoverageARB(value, invert) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_multisample)
	"glSampleCoverageARB",
#endif
	NULL
};

#define glInitMultisampleARB() InitExtension("GL_ARB_multisample", proc_names)
%}

int glInitMultisampleARB();
DOC(glInitMultisampleARB, "glInitMultisampleARB() -> bool")

%{
PyObject *__info()
{
	if (glInitMultisampleARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_MULTISAMPLE_ARB 0x809D
#define GL_SAMPLE_ALPHA_TO_COVERAGE_ARB 0x809E
#define GL_SAMPLE_ALPHA_TO_ONE_ARB 0x809F
#define GL_SAMPLE_COVERAGE_ARB 0x80A0

#define GL_MULTISAMPLE_BIT_ARB 0x20000000

#define GL_SAMPLE_BUFFERS_ARB 0x80A8
#define GL_SAMPLES_ARB 0x80A9
#define GL_SAMPLE_COVERAGE_VALUE_ARB 0x80AA
#define GL_SAMPLE_COVERAGE_INVERT_ARB 0x80AB
