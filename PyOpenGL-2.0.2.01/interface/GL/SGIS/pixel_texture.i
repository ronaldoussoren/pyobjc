/*
# BUILD api_versions [0x100]
*/

%module pixel_texture

%{
/**
 *
 * GL.SGIS.pixel_texture Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057pixel_texture.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_pixel_texture)
DECLARE_VOID_EXT(glPixelTexGenParameteriSGIS, (GLenum pname, GLint param), (pname, param))
DECLARE_VOID_EXT(glPixelTexGenParameterfSGIS, (GLenum pname, GLfloat param), (pname, param))
DECLARE_VOID_EXT(glGetPixelTexGenParameterfvSGIS, (GLenum pname, GLfloat* param), (pname, param))
DECLARE_VOID_EXT(glGetPixelTexGenParameterivSGIS, (GLenum pname, GLint* param), (pname, param))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_pixel_texture)
	"glTextureColorMaskSGIS",
	"glPixelTexGenParameteriSGIS",
	"glPixelTexGenParameterfSGIS",
	"glGetPixelTexGenParameterivSGIS",
#endif
	NULL
};

#define glInitPixelTextureSGIS() InitExtension("GL_SGIS_pixel_texture", proc_names)
%}

int glInitPixelTextureSGIS();
DOC(glInitPixelTextureSGIS, "glInitPixelTextureSGIS() -> bool")

%name(glInitPixelTexSGIS) int glInitPixelTextureSGIS();
DOC(glInitPixelTexSGIS, "glInitPixelTexSGIS() -> bool")

void glPixelTexGenParameteriSGIS(GLenum pname, GLint param);
DOC(glPixelTexGenParameteriSGIS, "glPixelTexGenParameteriSGIS(pname, param) -> None")

void glPixelTexGenParameterfSGIS(GLenum pname, GLfloat param);
DOC(glPixelTexGenParameterfSGIS, "glPixelTexGenParameterfSGIS(pname, param) -> None")

void glGetPixelTexGenParameterfvSGIS(GLenum pname, GLfloat param[4]);
DOC(glGetPixelTexGenParameterfvSGIS, "glGetPixelTexGenParameterfvSGIS(pname) -> params")

void glGetPixelTexGenParameterivSGIS(GLenum pname, GLint param[4]);
DOC(glGetPixelTexGenParameterivSGIS, "glGetPixelTexGenParameterivSGIS(pname) -> params")


%{
PyObject *__info()
{
	if (glInitPixelTextureSGIS())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PIXEL_TEXTURE_SGIS                      0x8353

#define GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS          0x8354
#define GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS        0x8355

#define GL_PIXEL_GROUP_COLOR_SGIS                  0x8356


    