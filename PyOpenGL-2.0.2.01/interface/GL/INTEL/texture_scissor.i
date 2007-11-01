/*
# BUILD api_versions [0x101]
*/

%module texture_scissor

%{
/**
 *
 * GL.INTEL.texture_scissor Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057INTEL\057texture_scissor.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_INTEL_texture_scissor)
DECLARE_VOID_EXT(glTexScissorINTEL, (GLenum target, GLclampf tlow, GLclampf thigh), (target, tlow, thigh))
DECLARE_VOID_EXT(glTexScissorFuncINTEL, (GLenum target, GLenum lfunc, GLenum hfunc), (target, lfunc, hfunc))
#endif
%}

void glTexScissorINTEL(GLenum target, GLclampf tlow, GLclampf thigh);
DOC(glTexScissorINTEL, "glTexScissorINTEL(target, tlow, thigh) -> None")

void glTexScissorFuncINTEL(GLenum target, GLenum lfunc, GLenum hfunc);
DOC(glTexScissorFuncINTEL, "glTexScissorFuncINTEL(target, lfunc, hfunc) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_INTEL_texture_scissor)
	"glTexScissorINTEL",
	"glTexScissorFuncINTEL",
#endif
	NULL
};

#define glInitTextureScissorINTEL() InitExtension("GL_INTEL_texture_scissor", proc_names)
%}

int glInitTextureScissorINTEL();
DOC(glInitTextureScissorINTEL, "glInitTextureScissorINTEL() -> bool")

%name(glInitTexScissorINTEL) int glInitTextureScissorINTEL();
DOC(glInitTexScissorINTEL, "glInitTexScissorINTEL() -> bool")


%{
PyObject *__info()
{
	if (glInitTextureScissorINTEL())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



/* don't know these values */
#define GL_TEXTURE_SCISSOR_INTEL 0

#define GL_TEXTURE_SCISSOR_S_INTEL 0
#define GL_TEXTURE_SCISSOR_T_INTEL 0
#define GL_TEXTURE_SCISSOR_R_INTEL 0 