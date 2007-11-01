/*
# BUILD api_versions [0x100]
*/

%module envmap_bumpmap

#define __version__ "$Revision: 1.1.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com/projects/ogl-sample/registry/ATI/envmap_bumpmap.txt"

%{
/**
 *
 * GL.ATI.envmap_bumpmap Module for PyOpenGL
 * 
 * Date: September 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#ifndef GL_ATI_envmap_bumpmap
#define GL_BUMP_ROT_MATRIX_ATI            0x8775
    
#define GL_BUMP_ROT_MATRIX_SIZE_ATI       0x8776
#define GL_BUMP_NUM_TEX_UNITS_ATI         0x8777
#define GL_BUMP_TEX_UNITS_ATI             0x8778

#define GL_DUDV_ATI                       0x8779
#define GL_DU8DV8_ATI                     0x877A

#define GL_BUMP_ENVMAP_ATI                0x877B

#define GL_BUMP_TARGET_ATI                0x877C
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_ATI_envmap_bumpmap)
DECLARE_VOID_EXT(glTexBumpParameterivEXT,\
	(GLenum target, GLenum pname, const GLint *param),\
	(target, pname, param))
DECLARE_VOID_EXT(glTexBumpParameterfvEXT,\
	(GLenum target, GLenum pname, const GLfloat *param),\
	(target, pname, param))
DECLARE_VOID_EXT(glGetTexBumpParameterivEXT,\
	(GLenum target, GLenum pname, GLint *params),\
	(target, pname, params))
DECLARE_VOID_EXT(glGetTexBumpParameterfvEXT,\
	(GLenum target, GLenum pname, GLfloat *params),\
	(target, pname, params))
#endif
%}

void glTexBumpParameterivEXT(GLenum target, GLenum pname, const GLint *param);
DOC(glTexBumpParameterivEXT, "glTexBumpParameterivEXT(target, pname, param[]) -> None")

void glTexBumpParameterfvEXT(GLenum target, GLenum pname, const GLfloat *param);
DOC(glTexBumpParameterfvEXT, "glTexBumpParameterfvEXT(target, pname, param[]) -> None")

void glGetTexBumpParameterivEXT(GLenum target, GLenum pname, GLint params[16]);
DOC(glGetTexBumpParameterivEXT, "glGetTexBumpParameterivEXT(target, pname) -> params")

void glGetTexBumpParameterfvEXT(GLenum target, GLenum pname, GLfloat params[16]);
DOC(glGetTexBumpParameterfvsXT, "glGetTexBumpParameterfvEXT(target, pname) -> params")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ATI_envmap_bumpmap)
	"glTexBumpParameterivEXT",
	"glTexBumpParameterfvEXT",
	"glGetTexBumpParameterivEXT",
	"glGetTexBumpParameterfvEXT",
#endif
	NULL
};

#define glInitTexBumpmapATI() InitExtension("GL_ATI_envmap_bumpmap", proc_names)
%}

int glInitTexBumpmapATI();
DOC(glInitTexBumpmapATI, "glInitTexBumpEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitTexBumpmapATI())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_BUMP_ROT_MATRIX_SIZE_ATI", GL_BUMP_ROT_MATRIX_SIZE_ATI, "i"));
		PyList_Append(info, Py_BuildValue("sis", "GL_BUMP_NUM_TEX_UNITS_ATI", GL_BUMP_NUM_TEX_UNITS_ATI, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_BUMP_ROT_MATRIX_ATI            0x8775
    
#define GL_BUMP_ROT_MATRIX_SIZE_ATI       0x8776
#define GL_BUMP_NUM_TEX_UNITS_ATI         0x8777
#define GL_BUMP_TEX_UNITS_ATI             0x8778

#define GL_DUDV_ATI                       0x8779
#define GL_DU8DV8_ATI                     0x877A

#define GL_BUMP_ENVMAP_ATI                0x877B

#define GL_BUMP_TARGET_ATI                0x877C

