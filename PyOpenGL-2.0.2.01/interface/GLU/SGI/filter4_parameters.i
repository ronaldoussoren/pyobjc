/*
# BUILD api_versions [0x100]
*/

%module filter4_parameters

%{
/**
 *
 * GLU.SGI.filter4_parameters Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.20.6.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGI\057filter4_parameters.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GLU_SGI_filter4_parameters)
DECLARE_EXT(gluTexFilterFuncSGI, GLint, 0, \
	(GLenum target, GLenum filtertype, const GLfloat *params, GLint n, GLfloat *weights),\
	(target, filtertype, params, n, weights))
#endif

PyObject *_gluTexFilterFuncSGI(GLenum target, GLenum filtertype, const GLfloat *params, GLint n)
{
	GLfloat *weights = PyMem_New(GLfloat, n);
	PyObject *result = NULL;
	GLint code = gluTexFilterFuncSGI(target, filtertype, params, n, weights);
	
	if (code)
	{
		PyMem_Del(weights);
		PyErr_SetGLUerror(code);
		return NULL;
	}
	
	result = _PyTuple_FromFloatArray(n, weights);
	PyMem_Del(weights);
	
	return result;
}
%}

%name(gluTexFilterFuncSGI) PyObject *_gluTexFilterFuncSGI(GLenum target, GLenum filtertype, const GLfloat *params, GLint n);
DOC(gluTexFilterFuncSGI, "gluTexFilterFuncSGI(target, filtertype, params, n) -> weights")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GLU_SGI_filter4_parameters)
	"gluTexFilterFuncSGI",
                             NULL,
                             NULL,
                             NULL,
#endif
	NULL
};

#define gluInitFilter4ParametersSGI() InitExtension("GLU_SGI_filter4_parameters", proc_names)
%}

int gluInitFilter4ParametersSGI();
DOC(gluInitFilter4ParametersSGI, "gluInitFilter4ParametersSGI() -> bool")

%{
PyObject *__info()
{
	if (gluInitFilter4ParametersSGI())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GLU_LAGRANGIAN_SGI                   100300
#define GLU_MITCHELL_NETRAVALI_SGI           100301
