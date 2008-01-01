/*
# BUILD api_versions [0x103]
*/

%module blend_func_separate

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057blend_func_separate.txt"

%{
/**
 *
 * GL.EXT.blend_func_separate Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_blend_func_separate)
DECLARE_VOID_EXT(glBlendFuncSeparateEXT,\
	(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha),\
	(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha))
#endif
%}

void glBlendFuncSeparateEXT(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha);
DOC(glBlendFuncSeparateEXT, "glBlendFuncSeparateEXT(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_blend_func_separate)
	"glBlendFuncSeparateEXT",
#endif
	NULL
};

#define glInitBlendFuncSeparateEXT() InitExtension("GL_EXT_blend_func_separate", proc_names)
%}

int glInitBlendFuncSeparateEXT();
DOC(glInitBlendFuncSeparateEXT, "glInitBlendFuncSeparateEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitBlendFuncSeparateEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_BLEND_DST_RGB_EXT                  0x80C8
#define GL_BLEND_SRC_RGB_EXT                  0x80C9
#define GL_BLEND_DST_ALPHA_EXT                0x80CA
#define GL_BLEND_SRC_ALPHA_EXT                0x80CB

