/*
# BUILD api_versions [0x11b]
*/

%module texture_object

#define __version__ "$Revision: 1.7.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com/projects/ogl-sample/registry/EXT/texture_object.txt"

%{
/**
 *
 * GL.EXT.texture_object Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture_object)
DECLARE_EXT(glAreTexturesResidentEXT, GLboolean, 0, (GLsizei n, const GLuint* textures, GLboolean* residences), (n, textures, residences))
DECLARE_VOID_EXT(glBindTextureEXT, (GLenum target, GLuint texture), (target, texture))
DECLARE_VOID_EXT(glDeleteTexturesEXT, (GLsizei n, const GLuint* textures), (n, textures))
DECLARE_VOID_EXT(glGenTexturesEXT, (GLsizei n, GLuint* textures), (n, textures))
DECLARE_EXT(glIsTextureEXT, GLboolean, 0, (GLuint texture), (texture))
DECLARE_VOID_EXT(glPrioritizeTexturesEXT, (GLsizei n, const GLuint* textures, const GLclampf* priorities), (n, textures, priorities))
#endif
%}

/*GLboolean glAreTexturesResidentEXT(GLsizei n_1, const GLuint *textures, GLboolean * residences); */
%{
PyObject* _glAreTexturesResidentEXT(GLsizei n, const GLuint *textures)
{
	GLboolean *residences = PyMem_New(GLboolean, n);
	PyObject *result;
	
	glAreTexturesResidentEXT(n, textures, residences);
	result = _PyTuple_FromUnsignedCharArray(n, residences);
	
	PyMem_Del(residences);
	return result;
}
%}

%name(glAreTexturesResidentEXT) PyObject* _glAreTexturesResidentEXT(GLsizei n_1, const GLuint *textures);
DOC(glAreTexturesResidentEXT, "glAreTexturesResidentEXT(textures[]) -> residences")

void glBindTextureEXT(GLenum target, GLuint texture);
DOC(glBindTextureEXT, "glBindTextureEXT(target, texture) -> None")

void glDeleteTexturesEXT(GLsizei n_1, const GLuint *textures);
DOC(glDeleteTexturesEXT, "glDeleteTexturesEXT(textures[]) -> None")

/*void glGenTexturesEXT (GLsizei n, GLuint *textures); */
%{
PyObject* _glGenTexturesEXT (GLsizei n)
{
	GLuint* textures;
	PyObject* result;
	
	textures = PyMem_New(GLuint, n);
	glGenTexturesEXT(n, textures);
	result = _PyTuple_FromUnsignedIntArray(n, textures);

	PyMem_Del(textures);
	return result;
}
%}

%name(glGenTexturesEXT) PyObject* _glGenTexturesEXT (GLsizei n);
DOC(glGenTexturesEXT, "glGenTexturesEXT(n) -> textures")

GLboolean glIsTextureEXT (GLuint texture);
DOC(glIsTextureEXT, "glIsTextureEXT(texture) -> boolean")

void glPrioritizeTexturesEXT (GLsizei n_1, const GLuint *textures, const GLclampf *priorities);
DOC(glPrioritizeTexturesEXT, "glPrioritizeTexturesEXT(textures[], priorities[]) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture_object)
	"glAreTexturesResidentEXT",
	"glBindTextureEXT",
	"glDeleteTexturesEXT",
	"glGenTexturesEXT",
	"glIsTextureEXT",
	"glPrioritizeTexturesEXT",
#endif
	NULL
};

#define glInitTextureObjectEXT() InitExtension("GL_EXT_texture_object", proc_names)
%}

int glInitTextureObjectEXT();
DOC(glInitTextureObjectEXT, "glInitTextureObjectEXT() -> bool")

%name(glInitTexObjectEXT) int glInitTextureObjectEXT();
DOC(glInitTexObjectEXT, "glInitTexObjectEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitTextureObjectEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_TEXTURE_PRIORITY_EXT		0x8066

#define GL_TEXTURE_RESIDENT_EXT		0x8067

#define GL_TEXTURE_1D_BINDING_EXT		0x8068
#define GL_TEXTURE_2D_BINDING_EXT		0x8069
#define GL_TEXTURE_3D_BINDING_EXT		0x806A

