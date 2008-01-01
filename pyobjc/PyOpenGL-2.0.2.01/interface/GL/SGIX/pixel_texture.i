/*
# BUILD api_versions [0x100]
*/

%module pixel_texture

%{
/**
 *
 * GL.SGIX.pixel_texture Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057sgi_pixel_texture.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_pixel_texture)
DECLARE_VOID_EXT(glPixelTexGenSGIX, (GLenum mode), (mode))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_pixel_texture)
	"glPixelTexGenSGIX",
#endif
	NULL
};

#define glInitPixelTextureSGIX() InitExtension("GL_SGIX_pixel_texture", proc_names)
%}

int glInitPixelTextureSGIX();
DOC(glInitPixelTextureSGIX, "glInitPixelTextureSGIX() -> bool")

%name(glInitPixelTexSGIX) int glInitPixelTextureSGIX();
DOC(glInitPixelTexSGIX, "glInitPixelTexSGIX() -> bool")

void glPixelTexGenSGIX(GLenum mode);
DOC(glPixelTexGenSGIX, "glPixelTexGenSGIX(mode) -> None")


%{
PyObject *__info()
{
	if (glInitPixelTextureSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PIXEL_TEX_GEN_SGIX                      0x8139
#define GL_PIXEL_TEX_GEN_MODE_SGIX                 0x832B