/*
# BUILD api_versions [0x100]
*/

%module fence

#define __version__ "$Revision: 1.21.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057NV\057fence.txt"

%{
/**
 *
 * GL.NV.fence Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_NV_fence)
DECLARE_VOID_EXT(glGenFencesNV, (GLsizei n, GLuint *fences), (n, fences))
DECLARE_VOID_EXT(glDeleteFencesNV, (GLsizei n, const GLuint *fences), (n, fences))
DECLARE_VOID_EXT(glSetFenceNV, (GLuint fence, GLenum condition), (fence, condition))
DECLARE_VOID_EXT(glFinishFenceNV, (GLuint fence), (fence))
DECLARE_VOID_EXT(glGetFenceivNV, (GLuint fence, GLenum pname, GLint* params), (fence, pname, params))
DECLARE_EXT(glTestFenceNV, GLboolean, -1, (GLuint fence), (fence))
DECLARE_EXT(glIsFenceNV, GLboolean, -1, (GLuint fence), (fence))
#endif

PyObject* _glGenFencesNV (GLsizei n)
{
	GLuint* fences;
	PyObject* result = NULL;
	
	fences = PyMem_New(GLuint, n);
	glGenFencesNV(n, fences);
	if (!PyErr_Occurred()) result = _PyTuple_FromUnsignedIntArray(n, fences);

	PyMem_Del(fences);
	return result;
}
%}

%name(glGenFencesNV) PyObject* _glGenFencesNV(GLsizei n);
DOC(glGenFencesNV, "glGenFencesNV(n) -> None")

void glDeleteFencesNV(GLsizei n_1, const GLuint *fences);
DOC(glDeleteFencesNV, "glDeleteFencesNV(fences) -> None")

void glSetFenceNV(GLuint fence, GLenum condition);
DOC(glSetFenceNV, "glSetFenceNV(fence, condition) -> None")

void glFinishFenceNV(GLuint fence);
DOC(glFinishFenceNV, "glFinishFenceNV(fence) -> None")

void glGetFenceivNV(GLuint fence, GLenum pname, GLint params[4]);
DOC(glGetFenceivNV, "glGetFenceivNV(fence, pname) -> params")

GLboolean glTestFenceNV(GLuint fence);
DOC(glTestFenceNV, "glTestFenceNV(fence) -> bool")

GLboolean glIsFenceNV(GLuint fence);
DOC(glIsFenceNV, "glIsFenceNV(fence) -> bool")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_fence)
	"glGenFencesNV",
	"glDeleteFencesNV",
	"glSetFenceNV",
	"glFinishFenceNV",
	"glGetFenceivNV",
	"glTestFenceNV",
	"glIsFenceNV",
#endif
	NULL
};

#define glInitFenceNV() InitExtension("GL_NV_fence", proc_names)
%}

int glInitFenceNV();
DOC(glInitFenceNV, "glInitFenceNV() -> bool")


%{
PyObject *__info()
{
	if (glInitFenceNV())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_ALL_COMPLETED_NV                   0x84F2

#define GL_FENCE_STATUS_NV                    0x84F3
#define GL_FENCE_CONDITION_NV                 0x84F4
