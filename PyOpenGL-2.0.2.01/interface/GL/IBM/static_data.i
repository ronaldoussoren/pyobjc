/*
# BUILD api_versions [0x102]
*/

%module static_data

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057IBM\057static_data.txt"

%{
/**
 *
 * GL.IBM.static_data Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_IBM_static_data)
DECLARE_VOID_EXT(glFlushStaticDataIBM, (GLenum target), (target))
#endif
%}

void glFlushStaticDataIBM(GLenum target);
DOC(glFlushStaticDataIBM, "glFlushStaticDataIBM(target) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_IBM_static_data)
	"glFlushStaticDataIBM",
#endif
	NULL
};

#define glInitStaticDataIBM() InitExtension("GL_IBM_static_data", proc_names)
%}

int glInitStaticDataIBM();
DOC(glInitStaticDataIBM, "glInitStaticDataIBM() -> bool")


%{
PyObject *__info()
{
	if (glInitStaticDataIBM())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();




#define GL_ALL_STATIC_DATA_IBM			103060
#define GL_STATIC_VERTEX_ARRAY_IBM			103061
