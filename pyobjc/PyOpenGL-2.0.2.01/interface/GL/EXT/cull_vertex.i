/*
# BUILD api_versions [0x103]
*/

%module cull_vertex

#define __version__ "$Revision: 1.24.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057cull_vertex.txt"

%{
/**
 *
 * GL.EXT.cull_vertex Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_cull_vertex)
DECLARE_VOID_EXT(glCullParameterfvEXT, (GLenum pname, GLfloat *params), (pname, params))
DECLARE_VOID_EXT(glCullParameterdvEXT, (GLenum pname, GLdouble *params), (pname, params))
#endif

#define _glCullParameterfvEXT(pname, params) glCullParameterfvEXT(pname, (GLfloat*)params)
%}

%name(glCullParameterfvEXT) void _glCullParameterfvEXT(GLenum pname, const GLfloat *params);
DOC(glCullParameterfvEXT, "glCullParameterfvEXT(pname, params) -> None")

%{
#define _glCullParameterdvEXT(pname, params) glCullParameterdvEXT(pname, (GLdouble*)params)
%}

%name(glCullParameterdvEXT) void _glCullParameterdvEXT(GLenum pname, const GLdouble *params);
DOC(glCullParameterdvEXT, "glCullParameterdvEXT(pname, params) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_cull_vertex)
	"glCullParameterfvEXT",
	"glCullParameterdvEXT",
#endif
	NULL
};

#define glInitCullVertexEXT() InitExtension("GL_EXT_cull_vertex", proc_names)
%}

int glInitCullVertexEXT();
DOC(glInitCullVertexEXT, "glInitCullVertexEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitCullVertexEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_CULL_VERTEX_EXT 0x81AA
#define GL_CULL_VERTEX_EYE_POSITION_EXT 0x81AB
#define GL_CULL_VERTEX_OBJECT_POSITION_EXT 0x81AC
