/*
# BUILD api_versions [0x10e]
*/

%module multisample

%{
/**
 *
 * GL.SGIS.multisample Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057multisample.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_multisample)
DECLARE_VOID_EXT(glSampleMaskSGIS, (GLclampf value, GLboolean invert), (value, invert))
DECLARE_VOID_EXT(glSamplePatternSGIS, (GLenum pattern), (pattern))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_multisample)
	"glSampleMaskSGIS",
	"glSamplePatternSGIS",
#endif
	NULL
};

#define glInitMultisampleSGIS() InitExtension("GL_SGIS_multisample", proc_names)
%}

int glInitMultisampleSGIS();
DOC(glInitMultisampleSGIS, "glInitMultisampleSGIS() -> bool")

void glSampleMaskSGIS(GLclampf value, GLboolean invert);
DOC(glSampleMaskSGIS, "glSampleMaskSGIS(value, invert) -> None")

void glSamplePatternSGIS(GLenum pattern);
DOC(glSamplePatternSGIS, "glSamplePatternSGIS(pattern) -> None")

%{
PyObject *__info()
{
	if (glInitMultisampleSGIS())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_MULTISAMPLE_SGIS                0x809D
#define GL_SAMPLE_ALPHA_TO_MASK_SGIS       0x809E
#define GL_SAMPLE_ALPHA_TO_ONE_SGIS        0x809F
#define GL_SAMPLE_MASK_SGIS                0x80A0

#define GL_MULTISAMPLE_BIT_EXT		0x20000000

#define GL_1PASS_SGIS                      0x80A1
#define GL_2PASS_0_SGIS                    0x80A2
#define GL_2PASS_1_SGIS                    0x80A3
#define GL_4PASS_0_SGIS                    0x80A4
#define GL_4PASS_1_SGIS                    0x80A5
#define GL_4PASS_2_SGIS                    0x80A6
#define GL_4PASS_3_SGIS                    0x80A7

#define GL_SAMPLE_BUFFERS_SGIS             0x80A8
#define GL_SAMPLES_SGIS                    0x80A9
#define GL_SAMPLE_MASK_VALUE_SGIS          0x80AA
#define GL_SAMPLE_MASK_INVERT_SGIS         0x80AB
#define GL_SAMPLE_PATTERN_SGIS             0x80AC
