/*
# BUILD api_versions [0x10b]
*/

%module sprite

%{
/**
 *
 * GL.SGIX.sprite Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:03 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SGIX\057sprite.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_sprite)
DECLARE_VOID_EXT(glSpriteParameteriSGIX, (GLenum pname, GLint param), (pname, param))
DECLARE_VOID_EXT(glSpriteParameterfSGIX, (GLenum pname, GLfloat param), (pname, param))
DECLARE_VOID_EXT(glSpriteParameterivSGIX, (GLenum pname, const GLint* param), (pname, param))
DECLARE_VOID_EXT(glSpriteParameterfvSGIX, (GLenum pname, const GLfloat* param), (pname, param))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIX_sprite)
	"glSpriteParameteriSGIX",
	"glSpriteParameterfSGIX",
	"glSpriteParameterivSGIX",
	"glSpriteParameterfvSGIX",
#endif
	NULL
};

#define glInitSpriteSGIX() InitExtension("GL_SGIX_sprite", proc_names)
%}

int glInitSpriteSGIX();
DOC(glInitSpriteSGIX, "glInitSpriteSGIX() -> bool")

void glSpriteParameteriSGIX(GLenum pname, GLint param);
DOC(glSpriteParameteriSGIX, "glSpriteParameteriSGIX(pname, param) -> None")

void glSpriteParameterfSGIX(GLenum pname, GLfloat param);
DOC(glSpriteParameterfSGIX, "glSpriteParameterfSGIX(pname, param) -> None")

void glSpriteParameterivSGIX(GLenum pname, const GLint* param);
DOC(glSpriteParameterivSGIX, "glSpriteParameterivSGIX(pname, params) -> None")

void glSpriteParameterfvSGIX(GLenum pname, const GLfloat* param);
DOC(glSpriteParameterfvSGIX, "glSpriteParameterfvSGIX(pname, params) -> None")


%{
PyObject *__info()
{
	if (glInitSpriteSGIX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();




#define GL_SPRITE_SGIX                    0x8148
#define GL_SPRITE_MODE_SGIX               0x8149
#define GL_SPRITE_AXIS_SGIX               0x814A
#define GL_SPRITE_TRANSLATION_SGIX        0x814B
#define GL_SPRITE_AXIAL_SGIX              0x814C
#define GL_SPRITE_OBJECT_ALIGNED_SGIX     0x814D
#define GL_SPRITE_EYE_ALIGNED_SGIX        0x814E
