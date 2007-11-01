/*
# BUILD api_versions [0x101]
*/

%module texture_color_mask

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057texture_color_mask.txt"

%{
/**
 *
 * GL.SGIS.texture_color_mask Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_texture_color_mask)
DECLARE_VOID_EXT(glTextureColorMaskSGIS, (GLboolean r, GLboolean g, GLboolean b, GLboolean a), (r, g, b, a))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_texture_color_mask)
	"glTextureColorMaskSGIS",
#endif
	NULL
};

#define glInitTextureColorMaskSGIS() InitExtension("GL_SGIS_texture_color_mask", proc_names)
%}

int glInitTextureColorMaskSGIS();
DOC(glInitTextureColorMaskSGIS, "glInitTextureColorMaskSGIS() -> bool")

%name(glInitTexColorMaskSGIS) int glInitTextureColorMaskSGIS();
DOC(glInitTexColorMaskSGIS, "glInitTexColorMaskSGIS() -> bool")

void glTextureColorMaskSGIS(GLboolean r, GLboolean g, GLboolean b, GLboolean a);
DOC(glTextureColorMaskSGIS, "glTextureColorMaskSGIS(r, g, b, a) -> None")

%{
PyObject *__info()
{
	if (glInitTextureColorMaskSGIS())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_TEXTURE_COLOR_WRITEMASK_SGIS		0x81EF
