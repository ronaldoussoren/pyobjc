/*
# BUILD api_versions [0x115]
*/

%module copy_texture

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057copy_texture.txt"

%{
/**
 *
 * GL.EXT.copy_texture Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_copy_texture)
DECLARE_VOID_EXT(glCopyTexImage1DEXT,\
	(GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLint border),\
	(target, level, internalFormat, x, y, width, border))
DECLARE_VOID_EXT(glCopyTexImage2DEXT,\
	(GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border),\
	(target, level, internalFormat, x, y, width, height, border))
DECLARE_VOID_EXT(glCopyTexSubImage1DEXT,\
	(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width),\
	(target, level, xoffset, x, y, width))
DECLARE_VOID_EXT(glCopyTexSubImage2DEXT,\
	(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height),\
	(target, level, xoffset, yoffset, x, y, width, height))
DECLARE_VOID_EXT(glCopyTexSubImage3DEXT,\
	(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height),\
	(target, level, xoffset, yoffset, zoffset, x, y, width, height))
#endif
%}

void glCopyTexImage1DEXT (GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLint border);
DOC(glCopyTexImage1DEXT, "glCopyTexImage1DEXT(target, level, internalFormat, x, y, width, border) -> None")

void glCopyTexImage2DEXT (GLenum target, GLint level, GLenum internalFormat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border);
DOC(glCopyTexImage2DEXT, "glCopyTexImage2DEXT(target, level, internalFormat, x, y, width, height, border) -> None")

void glCopyTexSubImage1DEXT (GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width);
DOC(glCopyTexSubImage1DEXT, "glCopyTexSubImage1DEXT(target, level, xoffset, x, y, width) -> None")

void glCopyTexSubImage2DEXT (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glCopyTexSubImage2DEXT, "glCopyTexSubImage2DEXT(target, level, xoffset, yoffset, x, y, width, height) -> None")

void glCopyTexSubImage3DEXT (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glCopyTexSubImage3DEXT, "glCopyTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, x, y, width, height) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_copy_texture)
	"glCopyTexSubImage1DEXT",
	"glCopyTexSubImage2DEXT",
	"glCopyTexSubImage3DEXT",
#endif
	NULL
};

#define glInitCopyTextureEXT() InitExtension("GL_EXT_copy_texture", proc_names)
%}

int glInitCopyTextureEXT();
DOC(glInitCopyTextureEXT, "glInitCopyTextureEXT() -> bool")

%name(glInitCopyTexEXT) int glInitCopyTextureEXT();
DOC(glInitCopyTexEXT, "glInitCopyTexEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitCopyTextureEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
