/*
# BUILD api_versions [0x100]
*/

%module register_combiners2

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057NV\057register_combiners2.txt"

%{
/**
 *
 * GL.NV.register_combiners2 Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_NV_register_combiners2)
DECLARE_VOID_EXT(glCombinerStageParameterfvNV, (GLenum stage, GLenum pname, const GLfloat *params), (stage, pname, params))
DECLARE_VOID_EXT(glGetCombinerStageParameterfvNV,\
	(GLenum stage, GLenum pname, GLfloat *params),\
	(stage, pname, params))
#endif
%}

void glCombinerStageParameterfvNV(GLenum stage, GLenum pname, const GLfloat *params);
DOC(glCombinerStageParameterfvNV, "glCombinerStageParameterfvNV(stage, pname, params) -> None")

void glGetCombinerStageParameterfvNV(GLenum stage, GLenum pname, GLfloat params[4]);
DOC(glGetCombinerStageParameterfvNV, "glGetCombinerStageParameterfvNV(stage, pname) -> params")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_register_combiners2)
	"glCombinerStageParameterfvNV",
	"glGetCombinerStageParameterfvNV",
#endif
	NULL
};

#define glInitRegisterCombiners2NV() InitExtension("GL_NV_register_combiners2", proc_names)
%}

int glInitRegisterCombiners2NV();
DOC(glInitRegisterCombiners2NV, "glInitRegisterCombiners2NV() -> bool")


%{
PyObject *__info()
{
	if (glInitRegisterCombiners2NV())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PER_STAGE_CONSTANTS_NV                         0x8535
