/*
# BUILD api_versions [0x103]
*/

%module texture_compression

#define __version__ "$Revision: 1.34.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"

%include util.inc

%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_texture_compression)
DECLARE_VOID_EXT(glCompressedTexImage3DARB, (GLenum target, GLint level, GLenum internalformat,\
                                                                         GLsizei width, GLsizei height, GLsizei depth, GLint border,\
                                                                         GLsizei imageSize, const void *data),\
                                                                         (target, level, internalformat, width, height, depth, border, imageSize, data))
DECLARE_VOID_EXT(glCompressedTexImage2DARB, (GLenum target, GLint level, GLenum internalformat,\
                                                                         GLsizei width, GLsizei height, GLint border,\
                                                                         GLsizei imageSize, const void *data),\
                                                                         (target, level, internalformat, width, height, border, imageSize, data))
DECLARE_VOID_EXT(glCompressedTexImage1DARB, (GLenum target, GLint level, GLenum internalformat,\
                                                                         GLsizei width, GLint border,\
                                                                         GLsizei imageSize, const void *data),\
                                                                         (target, level, internalformat, width, border, imageSize, data))

/* note that these are _sub_ image API functions */
DECLARE_VOID_EXT(glCompressedTexSubImage3DARB, (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,\
                                                                         GLsizei width, GLsizei height, GLsizei depth, GLenum format,\
                                                                         GLsizei imageSize, const void *data),\
                                                                         (target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data))
DECLARE_VOID_EXT(glCompressedTexSubImage2DARB, (GLenum target, GLint level, GLint xoffset, GLint yoffset,
                                                                         GLsizei width, GLsizei height, GLenum format,\
                                                                         GLsizei imageSize, const void *data),\
                                                                         (target, level, xoffset, yoffset, width, height, format, imageSize, data))
DECLARE_VOID_EXT(glCompressedTexSubImage1DARB, (GLenum target, GLint level, GLint xoffset,
                                                                         GLsizei width, GLenum format,\
                                                                         GLsizei imageSize, const void *data),\
                                                                         (target, level, xoffset, width, format, imageSize, data))

/* back to regular full-image functions */
DECLARE_VOID_EXT(glGetCompressedTexImageARB, (GLenum target, GLint lod, GLvoid* image), (target, lod, image))
#endif
%}

%name(glCompressedTexImage3DARB) void glCompressedTexImage3DARB(GLenum target, GLint level, GLenum internalformat,
                                                                GLsizei width, GLsizei height, GLsizei depth, GLint border,
                                                                GLsizei n_8, const void *buffer);
DOC(glCompressedTexImage3DARB, "glCompressedTexImage3DARB(target, level, internalformat, width, height, depth, border, data) -> None")


%name(glCompressedTexImage2DARB) void glCompressedTexImage2DARB(GLenum target, GLint level, GLenum internalformat,
                                                                GLsizei width, GLsizei height, GLint border,
                                                                GLsizei n_7, const void *buffer);
DOC(glCompressedTexImage2DARB, "glCompressedTexImage2DARB(target, level, internalformat, width, height, border, data) -> None")


%name(glCompressedTexImage1DARB) void glCompressedTexImage1DARB(GLenum target, GLint level, GLenum internalformat,
                                                                 GLsizei width, GLint border,
                                                                 GLsizei n_6, const void *buffer);
DOC(glCompressedTexImage1DARB, "glCompressedTexImage1DARB(target, level, internalformat, width, border, data) -> None")


%name(glCompressedTexSubImage3DARB) void glCompressedTexSubImage3DARB(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset,
                                          	                      GLsizei width, GLsizei height, GLsizei depth, GLenum format,
                                                                 GLsizei n_10, const void *buffer);
DOC(glCompressedTexSubImage3DARB, "glCompressedTexSubImage3DARB(target, level, xoffset, yoffset, zoffset, width, height, depth, format, data) -> None")


%name(glCompressedTexSubImage2DARB) void glCompressedTexSubImage2DARB(GLenum target, GLint level, GLint xoffset, GLint yoffset,
                                                                 GLsizei width, GLsizei height, GLenum format,
                                                                 GLsizei n_8, const void *buffer);
DOC(glCompressedTexSubImage2DARB, "glCompressedTexSubImage2DARB(target, level, xoffset, yoffset, width, height, format, data) -> None")


%name(glCompressedTexSubImage1DARB) void glCompressedTexSubImage1DARB(GLenum target, GLint level, GLint xoffset,
                                                                 GLsizei width, GLint format,
                                                                 GLsizei n_6, const void *buffer);
DOC(glCompressedTexSubImage1DARB, "glCompressedTexSubImage1DARB(target, level, xoffset, width, format, data) -> None")

%{
#ifndef GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB
#define GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB 0x86A0
#endif

PyObject* _glGetCompressedTexImageARB(GLenum target, GLint lod)
{
	GLint size = -1;
	char *data;
	PyObject* result;
	
	glGetTexLevelParameteriv(target, lod, GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB, &size);
	if (size == -1)
	{
		PyErr_SetString(PyExc_ImportError, "No support for GL_ARB_texture_compression extension.");
		return NULL;
	}
	
	data = PyMem_Malloc(size);
	glGetCompressedTexImageARB(target, lod, (void*)data);
	result = PyString_FromStringAndSize(data, size);
	PyMem_Free(data);
	
	return result;
}
%}

%name(glGetCompressedTexImageARB) PyObject* _glGetCompressedTexImageARB(GLenum target, GLint lod);
DOC(glGetCompressedTexImageARB, "glGetCompressedTexImageARB(target, lod) -> image")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_texture_compression)
	"glCompressedTexImage3DARB",
	"glCompressedTexImage2DARB",
	"glCompressedTexImage1DARB",
	"glCompressedTexSubImage3DARB",
	"glCompressedTexSubImage2DARB",
	"glCompressedTexSubImage1DARB",
	"glGetCompressedTexImageARB",
#endif
	NULL
};

#define glInitTextureCompressionARB() InitExtension("GL_ARB_texture_compression", proc_names)
%}

int glInitTextureCompressionARB();
DOC(glInitTextureCompressionARB, "glInitTextureCompressionARB() -> bool")

%name(glInitTexCompressionARB) int glInitTextureCompressionARB();
DOC(glInitTexCompressionARB, "glInitTexCompressionARB() -> bool")

%{
PyObject *__info()
{
	if (glInitTextureCompressionARB())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_COMPRESSED_ALPHA_ARB 0x84E9
#define GL_COMPRESSED_LUMINANCE_ARB 0x84EA
#define GL_COMPRESSED_LUMINANCE_ALPHA_ARB 0x84EB
#define GL_COMPRESSED_INTENSITY_ARB 0x84EC
#define GL_COMPRESSED_RGB_ARB 0x84ED
#define GL_COMPRESSED_RGBA_ARB 0x84EE

#define GL_TEXTURE_COMPRESSION_HINT_ARB 0x84EF

#define GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB 0x86A0
#define GL_TEXTURE_COMPRESSED_ARB 0x86A1
#define GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB 0x86A2
#define GL_COMPRESSED_TEXTURE_FORMATS_ARB 0x86A3

