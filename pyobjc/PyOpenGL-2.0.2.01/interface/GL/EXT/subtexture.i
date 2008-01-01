/*
# BUILD api_versions [0x111]
*/

%module subtexture

#define __version__ "$Revision: 1.20.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057subtexture.txt"

%{
/**
 *
 * GL.EXT.subtexture Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_subtexture)
DECLARE_VOID_EXT(glTexSubImage1DEXT,\
	(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *buffer),\
	(target, level, xoffset, width, format, type, buffer))
DECLARE_VOID_EXT(glTexSubImage2DEXT,\
	(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels),\
	(target, level, xoffset, yoffset, width, height, format, type, pixels))
DECLARE_VOID_EXT(glTexSubImage3DEXT,\
	(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels),\
	(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels))
#endif
%}

/*void glTexSubImage1DEXT (GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid *pixels); */
void glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage1DEXT, "glTexSubImage1DEXT(target, level, xoffset, width, format, type, pixels) -> None")

%{
void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(1);
	glTexSubImage1DEXT(target, level, xoffset, width, format, type, pixels);
}
%}

%name(glTexSubImage1DubEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage1DubEXT, "glTexSubImage1DubEXT(target, level, xoffset, format, type, pixels) -> None")

%name(glTexSubImage1DbEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage1DbEXT, "glTexSubImage1DbEXT(target, level, xoffset, format, type, pixels) -> None")

%name(glTexSubImage1DusEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage1DusEXT, "glTexSubImage1DusEXT(target, level, xoffset, format, type, pixels) -> None")

%name(glTexSubImage1DsEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage1DsEXT, "glTexSubImage1DsEXT(target, level, xoffset, format, type, pixels) -> None")

%name(glTexSubImage1DuiEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage1DuiEXT, "glTexSubImage1DuiEXT(target, level, xoffset, format, type, pixels) -> None")

%name(glTexSubImage1DiEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage1DiEXT, "glTexSubImage1DiEXT(target, level, xoffset, format, type, pixels) -> None")

%name(glTexSubImage1DfEXT) void _glTexSubImage1DEXT(GLenum target, GLint level, GLint xoffset, GLsizei d_6_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage1DfEXT, "glTexSubImage1DfEXT(target, level, xoffset, format, type, pixels) -> None")

/*void glTexSubImage2DEXT (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid *pixels); */
void glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage2DEXT, "glTexSubImage2DEXT(target, level, xoffset, yoffset, width, height, format, type, pixels) -> None")

%{
void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(2);
	glTexSubImage2DEXT(target, level, xoffset, yoffset, width, height, format, type, pixels);
}
%}

%name(glTexSubImage2DubEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage2DubEXT, "glTexSubImage2DubEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

%name(glTexSubImage2DbEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage2DbEXT, "glTexSubImage2DbEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

%name(glTexSubImage2DusEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage2DusEXT, "glTexSubImage2DusEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

%name(glTexSubImage2DsEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage2DsEXT, "glTexSubImage2DsEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

%name(glTexSubImage2DuiEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage2DuiEXT, "glTexSubImage2DuiEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

%name(glTexSubImage2DiEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage2DiEXT, "glTexSubImage2DiEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

%name(glTexSubImage2DfEXT) void _glTexSubImage2DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei d_8_1, GLsizei d_8_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage2DfEXT, "glTexSubImage2DfEXT(target, level, xoffset, yoffset, format, type, pixels) -> None")

/*void glTexSubImage3DEXT (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid *pixels); */
void glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage3DEXT, "glTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels) -> None")

%{
void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(3);
	glTexSubImage3DEXT(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels);
}
%}

%name(glTexSubImage3DubEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage3DubEXT, "glTexSubImage3DubEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3DbEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage3DbEXT, "glTexSubImage3DbEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3DusEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage3DusEXT, "glTexSubImage3DusEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3DsEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage3DsEXT, "glTexSubImage3DsEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3DuiEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage3DuiEXT, "glTexSubImage3DuiEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3DiEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage3DiEXT, "glTexSubImage3DiEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")

%name(glTexSubImage3DfEXT) void _glTexSubImage3DEXT(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei d_9_2, GLsizei d_9_1, GLsizei d_9_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage3DfEXT, "glTexSubImage3DfEXT(target, level, xoffset, yoffset, zoffset, format, type, pixels) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_subtexture)
	"glTexSubImage1DEXT",
	"glTexSubImage2DEXT",
	"glTexSubImage3DEXT",
#endif
	NULL
};

#define glInitSubtextureEXT() InitExtension("GL_EXT_subtexture", proc_names)
%}

int glInitSubtextureEXT();
DOC(glInitSubtextureEXT, "glInitSubtextureEXT() -> bool")

%name(glInitSubTexEXT) int glInitSubtextureEXT();
DOC(glInitSubTexEXT, "glInitSubTexEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitSubtextureEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
