/*
# BUILD api_versions [0x101]
*/

%module misc_hints

%{
/**
 *
 * GL.PGI.misc_hints Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057PGI\057misc_hints.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_PGI_misc_hints)
DECLARE_VOID_EXT(glHintPGI, (GLenum target, GLint mode), (target, mode))
#endif
%}

void glHintPGI(GLenum target, GLint mode);
DOC(glHintPGI, "glHintPGI(target, mode) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_PGI_misc_hints)
	"glHintPGI",
#endif
	NULL
};

#define glInitMiscHintsPGI() InitExtension("GL_PGI_misc_hints", proc_names)
%}

int glInitMiscHintsPGI();
DOC(glInitMiscHintsPGI, "glInitMiscHintsPGI() -> bool")


%{
PyObject *__info()
{
	if (glInitMiscHintsPGI())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PREFER_DOUBLEBUFFER_HINT_PGI        107000
#define GL_STRICT_DEPTHFUNC_HINT_PGI           107030
#define GL_STRICT_LIGHTING_HINT_PGI            107031
#define GL_STRICT_SCISSOR_HINT_PGI             107032
#define GL_FULL_STIPPLE_HINT_PGI               107033
#define GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI      107011
#define GL_NATIVE_GRAPHICS_END_HINT_PGI        107012
#define GL_CONSERVE_MEMORY_HINT_PGI            107005
#define GL_RECLAIM_MEMORY_HINT_PGI             107006
#define GL_ALWAYS_FAST_HINT_PGI                107020
#define GL_ALWAYS_SOFT_HINT_PGI                107021
#define GL_ALLOW_DRAW_OBJ_HINT_PGI             107022
#define GL_ALLOW_DRAW_WIN_HINT_PGI             107023
#define GL_ALLOW_DRAW_FRG_HINT_PGI             107024
#define GL_ALLOW_DRAW_MEM_HINT_PGI             107025
#define GL_CLIP_NEAR_HINT_PGI                  107040
#define GL_CLIP_FAR_HINT_PGI                   107041
#define GL_WIDE_LINE_HINT_PGI                  107042
#define GL_BACK_NORMALS_HINT_PGI               107043

#define GL_NATIVE_GRAPHICS_HANDLE_PGI       107010

