/*
# BUILD api_versions [0x119]
*/

%module texture4D

#define __version__ "$Revision: 1.19.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIS\057texture4D.txt"

%{
/**
 *
 * GL.SGIS.texture4D Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_texture4D)
DECLARE_VOID_EXT(glTexImage4DSGIS,\
	(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLint border, GLenum format, GLenum type, const GLvoid *pixels),\
	(target, level, internalFormat, width, height, depth, extent, border, format, type, pixels))
DECLARE_VOID_EXT(glTexSubImage4DSGIS,\
	(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLenum format, GLenum type, const void *buffer),\
	(target, level, xoffset, yoffset, zoffset, woffset, width, height, depth, extent, format, type, buffer))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_texture4D)
	"glTexImage4DSGIS",
	"glTexSubImage4DSGIS",
#endif
	NULL
};

#define glInitTexture4DSGIS() InitExtension("GL_SGIS_texture4D", proc_names)
%}

int glInitTexture4DSGIS();
DOC(glInitTexture4DSGIS, "glInitTexture4DSGIS() -> bool")

%name(glInitTex4DSGIS) int glInitTexture4DSGIS();
DOC(glInitTex4DSGIS, "glInitTex4DSGIS() -> bool")


void glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLint border, GLenum format, GLenum type, const void *buffer);
DOC(glTexImage4DSGIS, "glTexImage4DSGIS(target, level, internalFormat, width, height, depth, extent, border, format, type, pixels) -> None")

%{
void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLint border, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(3);
	glTexImage4DSGIS(target, level, internalFormat, width, height, depth, extent, border, format, type, pixels);
}
%}

%name(glTexImage4DubSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexImage4DubEXT, "glTexImage4DubEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage4DbSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexImage4DbEXT, "glTexImage4DbEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage4DusSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexImage4DusEXT, "glTexImage4DusEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage4DsSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexImage4DsEXT, "glTexImage4DsEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage4DuiSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexImage4DuiEXT, "glTexImage4DuiEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage4DiSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexImage4DiEXT, "glTexImage4DiEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage4DfSGIS) void _glTexImage4DSGIS(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_3, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexImage4DfEXT, "glTexImage4DfEXT(target, level, internalFormat, border, format, type, pixels) -> None")


/*void glTexSubImage4DSGIS (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLenum format, GLenum type, const GLvoid *pixels); */
void glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLenum format, GLenum type, const void *buffer);
DOC(glTexSubImage4DSGIS, "glTexSubImage4DSGIS(target, level, xoffset, yoffset, zoffset, woffset, width, height, depth, extent, format, type, pixels) -> None")

%{
void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei extent, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(4);
	glTexSubImage4DSGIS(target, level, xoffset, yoffset, zoffset, woffset, width, height, depth, extent, format, type, pixels);
}
%}

%name(glTexSubImage4DubSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexSubImage4DubEXT, "glTexSubImage4DubEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")

%name(glTexSubImage4DbSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexSubImage4DbEXT, "glTexSubImage4DbEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")

%name(glTexSubImage4DusSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexSubImage4DusEXT, "glTexSubImage4DusEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")

%name(glTexSubImage4DsSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexSubImage4DsEXT, "glTexSubImage4DsEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")

%name(glTexSubImage4DuiSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexSubImage4DuiEXT, "glTexSubImage4DuiEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")

%name(glTexSubImage4DiSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexSubImage4DiEXT, "glTexSubImage4DiEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")

%name(glTexSubImage4DfSGIS) void _glTexSubImage4DSGIS(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint woffset, GLsizei d_10_3, GLsizei d_10_2, GLsizei d_10_1, GLsizei d_10_0, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexSubImage4DfEXT, "glTexSubImage4DfEXT(target, level, xoffset, yoffset, zoffset, woffset, format, type, pixels) -> None")


%{
#ifndef GL_SGIS_texture4D
#define GL_MAX_4D_TEXTURE_SIZE_SGIS          0x84E2
#endif

PyObject *__info()
{
	if (glInitTexture4DSGIS())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_4D_TEXTURE_SIZE_SGIS", GL_MAX_4D_TEXTURE_SIZE_SGIS, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PACK_SKIP_VOLUMES_SGIS         0x8130
#define GL_PACK_IMAGE_DEPTH_SGIS          0x8131
#define GL_UNPACK_SKIP_VOLUMES_SGIS       0x8132
#define GL_UNPACK_IMAGE_DEPTH_SGIS        0x8133
#define GL_TEXTURE_4D_SGIS                0x8134
#define GL_PROXY_TEXTURE_4D_SGIS          0x8135
#define GL_TEXTURE_4DSIZE_SGIS            0x8136
#define GL_TEXTURE_WRAP_Q_SGIS            0x8137
#define GL_MAX_4D_TEXTURE_SIZE_SGIS       0x8138
#define GL_TEXTURE_4D_BINDING_SGIS        0x814F
