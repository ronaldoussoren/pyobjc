/*
# BUILD api_versions [0x116]
*/

%module texture3D

#define __version__ "$Revision: 1.25.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057texture3D.txt"

%{
/**
 *
 * GL.EXT.texture3D Module for PyOpenGL
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


/*void glTexImage3DEXT (GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels); */
%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture3D)
DECLARE_VOID_EXT(glTexImage3DEXT,\
	(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid *pixels),\
	(target, level, internalFormat, width, height, depth, border, format, type, pixels))
#endif
%}

void glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const void *buffer);
DOC(glTexImage3DEXT, "glTexImage3DEXT(target, level, internalFormat, width, height, depth, border, format, type, pixels) -> None")

%{
void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const GLvoid* pixels)
{
	SetupPixelWrite(3);
	glTexImage3DEXT(target, level, internalFormat, width, height, depth, border, format, type, pixels);
}
%}

%name(glTexImage3DubEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_BYTE, const GLubyte *pixels);
DOC(glTexImage3DubEXT, "glTexImage3DubEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3DbEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_BYTE, const GLbyte *pixels);
DOC(glTexImage3DbEXT, "glTexImage3DbEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3DusEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_SHORT, const GLushort *pixels);
DOC(glTexImage3DusEXT, "glTexImage3DusEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3DsEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_SHORT, const GLshort *pixels);
DOC(glTexImage3DsEXT, "glTexImage3DsEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3DuiEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_UNSIGNED_INT, const GLuint *pixels);
DOC(glTexImage3DuiEXT, "glTexImage3DuiEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3DiEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_INT, const GLint *pixels);
DOC(glTexImage3DiEXT, "glTexImage3DiEXT(target, level, internalFormat, border, format, type, pixels) -> None")

%name(glTexImage3DfEXT) void __glTexImage3DEXT(GLenum target, GLint level, GLint internalFormat, GLsizei d_8_2, GLsizei d_8_1, GLsizei d_8_0, GLint border, GLenum format, GLenum type_FLOAT, const GLfloat *pixels);
DOC(glTexImage3DfEXT, "glTexImage3DfEXT(target, level, internalFormat, border, format, type, pixels) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture3D)
	"glTexImage3DEXT",
#endif
	NULL
};

#define glInitTexture3DEXT() InitExtension("GL_EXT_texture3D", proc_names)
%}

int glInitTexture3DEXT();
DOC(glInitTexture3DEXT, "glInitTexture3DEXT() -> bool")

%name(glInitTex3DEXT) int glInitTexture3DEXT();
DOC(glInitTex3DEXT, "glInitTex3DEXT() -> bool")


%{
#ifndef GL_EXT_texture3D
#define GL_MAX_3D_TEXTURE_SIZE_EXT          0x8073
#endif

PyObject *__info()
{
	if (glInitTexture3DEXT())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_3D_TEXTURE_SIZE_EXT", GL_MAX_3D_TEXTURE_SIZE_EXT, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



#define GL_PACK_SKIP_IMAGES_EXT             0x806B
#define GL_PACK_IMAGE_HEIGHT_EXT            0x806C
#define GL_UNPACK_SKIP_IMAGES_EXT           0x806D
#define GL_UNPACK_IMAGE_HEIGHT_EXT          0x806E

#define GL_TEXTURE_3D_EXT                   0x806F

#define GL_PROXY_TEXTURE_3D_EXT             0x8070

#define GL_TEXTURE_DEPTH_EXT                0x8071


#define GL_TEXTURE_WRAP_R_EXT               0x8072

#define GL_MAX_3D_TEXTURE_SIZE_EXT          0x8073
