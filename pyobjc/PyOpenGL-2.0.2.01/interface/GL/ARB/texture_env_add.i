/*
# BUILD api_versions [0x101]
*/

%module texture_env_add

%{
/**
 *
 * GL.ARB.texture_env_add Module for PyOpenGL
 * 
 * Date: Oct 2004
 *
 * Authors: mcfletch@users.sourceforge.net
 * 
***/
%}

#define __version__ "$Revision: 1.1.2.2 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "mcfletch@users.sourceforge.net"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057texture_env_add.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
static char *proc_names[] =
{
	NULL
};

#define glInitTextureEnvAddARB() InitExtension("GL_ARB_texture_env_add", proc_names)
%}

int glInitTextureEnvAddARB();
DOC(glInitTextureEnvAddARB, "glInitTextureEnvAddARB() -> bool")


%{
PyObject *__info()
{
	if (glInitTextureEnvAddARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


