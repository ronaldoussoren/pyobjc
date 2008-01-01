/*
# BUILD api_versions [0x102]
*/

%module constant_data

%{
/**
 *
 * GL.SUNX.constant_data Module for PyOpenGL
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
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SUNX\057constant_data.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_SUNX_constant_data)
DECLARE_VOID_EXT(glFinishTextureSUNX, (), ())
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SUNX_constant_data)
	"glFinishTextureSUNX",
#endif
	NULL
};

#define glInitConstantDataSUNX() InitExtension("GL_SUNX_constant_data", proc_names)
%}

int glInitConstantDataSUNX();
DOC(glInitConstantDataSUNX, "glInitConstantDataSUNX() -> bool")

void glFinishTextureSUNX();
DOC(glFinishTextureSUNX, "glFinishTextureSUNX() -> None")

%{
PyObject *__info()
{
	if (glInitConstantDataSUNX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_UNPACK_CONSTANT_DATA_SUNX		0x81D5
	
#define GL_TEXTURE_CONSTANT_DATA_SUNX		0x81D6	
