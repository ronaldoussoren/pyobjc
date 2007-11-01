/*
# BUILD api_versions [0x101]
*/

%module multitexture

#define __version__ "$Revision: 1.40.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057multitexture.txt"

%{
/**
 *
 * GL.ARB.multitexture Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc


%include py_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_multitexture)
DECLARE_VOID_EXT(glMultiTexCoord1dARB, (GLenum unit, GLdouble s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1dvARB, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord1sARB, (GLenum unit, GLshort s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1fARB, (GLenum unit, GLfloat s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1fvARB, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord1iARB, (GLenum unit, GLint s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1ivARB, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord1svARB, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2dARB, (GLenum unit, GLdouble s, GLdouble t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2dvARB, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2fvARB, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2fARB, (GLenum unit, GLfloat s, GLfloat t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2iARB, (GLenum unit, GLint s, GLint t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2ivARB, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2sARB, (GLenum unit, GLshort s, GLshort t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2svARB, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3dARB, (GLenum unit, GLdouble s, GLdouble t, GLdouble u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3dvARB, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3fARB, (GLenum unit, GLfloat s, GLfloat t, GLfloat u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3fvARB, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3iARB, (GLenum unit, GLint s, GLint t, GLint u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3ivARB, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3sARB, (GLenum unit, GLshort s, GLshort t, GLshort u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3svARB, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4dARB, (GLenum unit, GLdouble s, GLdouble t, GLdouble u, GLdouble v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4dvARB, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4fARB, (GLenum unit, GLfloat s, GLfloat t, GLfloat u, GLfloat v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4fvARB, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4iARB, (GLenum unit, GLint s, GLint t, GLint u, GLint v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4ivARB, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4sARB, (GLenum unit, GLshort s, GLshort t, GLshort u, GLshort v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4svARB, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glActiveTextureARB, (GLenum unit), (unit))
DECLARE_VOID_EXT(glClientActiveTextureARB, (GLenum unit), (unit))
#endif
%}

void glMultiTexCoord1dARB(GLenum unit, GLdouble s);
DOC(glMultiTexCoord1dARB, "glMultiTexCoord1dARB(unit, s) -> None")

void glMultiTexCoord1dvARB(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord1dvARB, "glMultiTexCoord1dvARB(unit, v) -> None")

void glMultiTexCoord1fARB(GLenum unit, GLfloat s);
DOC(glMultiTexCoord1fARB, "glMultiTexCoord1fARB(unit, s) -> None")

void glMultiTexCoord1fvARB(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord1fvARB, "glMultiTexCoord1fvARB(unit, v) -> None")

void glMultiTexCoord1iARB(GLenum unit, GLint s);
DOC(glMultiTexCoord1iARB, "glMultiTexCoord1iARB(unit, s) -> None")

void glMultiTexCoord1ivARB(GLenum unit, const GLint *v);
DOC(glMultiTexCoord1ivARB, "glMultiTexCoord1ivARB(unit, v) -> None")

void glMultiTexCoord1sARB(GLenum unit, GLshort s);
DOC(glMultiTexCoord1sARB, "glMultiTexCoord1sARB(unit, s) -> None")

void glMultiTexCoord1svARB(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord1svARB, "glMultiTexCoord1svARB(unit, v) -> None")

void glMultiTexCoord2dARB(GLenum unit, GLdouble s, GLdouble t);
DOC(glMultiTexCoord2dARB, "glMultiTexCoord2dARB(unit, s, t) -> None")

void glMultiTexCoord2dvARB(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord2dvARB, "glMultiTexCoord2dvARB(unit, v) -> None")

void glMultiTexCoord2fARB(GLenum unit, GLfloat s, GLfloat t);
DOC(glMultiTexCoord2fARB, "glMultiTexCoord2fARB(unit, s, t) -> None")

void glMultiTexCoord2fvARB(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord2fvARB, "glMultiTexCoord2fvARB(unit, v) -> None")

void glMultiTexCoord2iARB(GLenum unit, GLint s, GLint t);
DOC(glMultiTexCoord2iARB, "glMultiTexCoord2iARB(unit, s, t) -> None")

void glMultiTexCoord2ivARB(GLenum unit, const GLint *v);
DOC(glMultiTexCoord2ivARB, "glMultiTexCoord2ivARB(unit, v) -> None")

void glMultiTexCoord2sARB(GLenum unit, GLshort s, GLshort t);
DOC(glMultiTexCoord2sARB, "glMultiTexCoord2sARB(unit, s, t) -> None")

void glMultiTexCoord2svARB(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord2svARB, "glMultiTexCoord2svARB(unit, v) -> None")

void glMultiTexCoord3dARB(GLenum unit, GLdouble s, GLdouble t, GLdouble u);
DOC(glMultiTexCoord3dARB, "glMultiTexCoord3dARB(unit, s, t, u) -> None")

void glMultiTexCoord3dvARB(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord3dvARB, "glMultiTexCoord3dvARB(unit, v) -> None")

void glMultiTexCoord3fARB(GLenum unit, GLfloat s, GLfloat t, GLfloat u);
DOC(glMultiTexCoord3fARB, "glMultiTexCoord3fARB(unit, s, t, u) -> None")

void glMultiTexCoord3fvARB(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord3fvARB, "glMultiTexCoord3fvARB(unit, v) -> None")

void glMultiTexCoord3iARB(GLenum unit, GLint s, GLint t, GLint u);
DOC(glMultiTexCoord3iARB, "glMultiTexCoord3iARB(unit, s, t, u) -> None")

void glMultiTexCoord3ivARB(GLenum unit, const GLint *v);
DOC(glMultiTexCoord3ivARB, "glMultiTexCoord3ivARB(unit, v) -> None")

void glMultiTexCoord3sARB(GLenum unit, GLshort s, GLshort t, GLshort u);
DOC(glMultiTexCoord3sARB, "glMultiTexCoord3sARB(unit, s, t, u) -> None")

void glMultiTexCoord3svARB(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord3svARB, "glMultiTexCoord3svARB(unit, v) -> None")

void glMultiTexCoord4dARB(GLenum unit, GLdouble s, GLdouble t, GLdouble u, GLdouble v);
DOC(glMultiTexCoord4dARB, "glMultiTexCoord4dARB(unit, s, t, u, v) -> None")

void glMultiTexCoord4dvARB(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord4dvARB, "glMultiTexCoord4dvARB(unit, v) -> None")

void glMultiTexCoord4fARB(GLenum unit, GLfloat s, GLfloat t, GLfloat u, GLfloat v);
DOC(glMultiTexCoord4fARB, "glMultiTexCoord4fARB(unit, s, t, u, v) -> None")

void glMultiTexCoord4fvARB(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord4fvARB, "glMultiTexCoord4fvARB(unit, v) -> None")

void glMultiTexCoord4iARB(GLenum unit, GLint s, GLint t, GLint u, GLint v);
DOC(glMultiTexCoord4iARB, "glMultiTexCoord4iARB(unit, s, t, u, v) -> None")

void glMultiTexCoord4ivARB(GLenum unit, const GLint *v);
DOC(glMultiTexCoord4ivARB, "glMultiTexCoord4ivARB(unit, v) -> None")

void glMultiTexCoord4sARB(GLenum unit, GLshort s, GLshort t, GLshort u, GLshort v);
DOC(glMultiTexCoord4sARB, "glMultiTexCoord4sARB(unit, s, t, u, v) -> None")

void glMultiTexCoord4svARB(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord4svARB, "glMultiTexCoord4svARB(unit, v) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc

void glActiveTextureARB(GLenum unit);
DOC(glActiveTextureARB, "glActiveTextureARB(unit) -> None")

void glClientActiveTextureARB(GLenum unit);
DOC(glClientActiveTextureARB, "glClientActiveTextureARB(unit) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_multitexture)
	"glMultiTexCoord1dARB",
	"glMultiTexCoord1dvARB",
	"glMultiTexCoord1fARB",
	"glMultiTexCoord1fvARB",
	"glMultiTexCoord1iARB",
	"glMultiTexCoord1ivARB",
	"glMultiTexCoord1sARB",
	"glMultiTexCoord1svARB",
	"glMultiTexCoord2dARB",
	"glMultiTexCoord2dvARB",
	"glMultiTexCoord2fARB",
	"glMultiTexCoord2fvARB",
	"glMultiTexCoord2iARB",
	"glMultiTexCoord2ivARB",
	"glMultiTexCoord2sARB",
	"glMultiTexCoord2svARB",
	"glMultiTexCoord3dARB",
	"glMultiTexCoord3dvARB",
	"glMultiTexCoord3fARB",
	"glMultiTexCoord3fvARB",
	"glMultiTexCoord3iARB",
	"glMultiTexCoord3ivARB",
	"glMultiTexCoord3sARB",
	"glMultiTexCoord3svARB",
	"glMultiTexCoord4dARB",
	"glMultiTexCoord4dvARB",
	"glMultiTexCoord4fARB",
	"glMultiTexCoord4fvARB",
	"glMultiTexCoord4iARB",
	"glMultiTexCoord4ivARB",
	"glMultiTexCoord4sARB",
	"glMultiTexCoord4svARB",
	"glActiveTextureARB",
	"glClientActiveTextureARB",
#endif
	NULL
};

#define glInitMultitextureARB() InitExtension("GL_ARB_multitexture", proc_names)
%}

int glInitMultitextureARB();
DOC(glInitMultitextureARB, "glInitMultitextureARB() -> bool")

%name(glInitMultiTexARB) int glInitMultitextureARB();
DOC(glInitMultiTexARB, "glInitMultiTexARB() -> bool")

%{
#ifndef GL_ARB_multitexture
#define GL_MAX_TEXTURE_UNITS_ARB          0x84E2
#endif

PyObject *__info()
{
	if (glInitMultitextureARB())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_TEXTURE_UNITS_ARB", GL_MAX_TEXTURE_UNITS_ARB, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_TEXTURE0_ARB                   0x84C0
#define GL_TEXTURE1_ARB                   0x84C1
#define GL_TEXTURE2_ARB                   0x84C2
#define GL_TEXTURE3_ARB                   0x84C3
#define GL_TEXTURE4_ARB                   0x84C4
#define GL_TEXTURE5_ARB                   0x84C5
#define GL_TEXTURE6_ARB                   0x84C6
#define GL_TEXTURE7_ARB                   0x84C7
#define GL_TEXTURE8_ARB                   0x84C8
#define GL_TEXTURE9_ARB                   0x84C9
#define GL_TEXTURE10_ARB                  0x84CA
#define GL_TEXTURE11_ARB                  0x84CB
#define GL_TEXTURE12_ARB                  0x84CC
#define GL_TEXTURE13_ARB                  0x84CD
#define GL_TEXTURE14_ARB                  0x84CE
#define GL_TEXTURE15_ARB                  0x84CF
#define GL_TEXTURE16_ARB                  0x84D0
#define GL_TEXTURE17_ARB                  0x84D1
#define GL_TEXTURE18_ARB                  0x84D2
#define GL_TEXTURE19_ARB                  0x84D3
#define GL_TEXTURE20_ARB                  0x84D4
#define GL_TEXTURE21_ARB                  0x84D5
#define GL_TEXTURE22_ARB                  0x84D6
#define GL_TEXTURE23_ARB                  0x84D7
#define GL_TEXTURE24_ARB                  0x84D8
#define GL_TEXTURE25_ARB                  0x84D9
#define GL_TEXTURE26_ARB                  0x84DA
#define GL_TEXTURE27_ARB                  0x84DB
#define GL_TEXTURE28_ARB                  0x84DC
#define GL_TEXTURE29_ARB                  0x84DD
#define GL_TEXTURE30_ARB                  0x84DE
#define GL_TEXTURE31_ARB                  0x84DF
#define GL_ACTIVE_TEXTURE_ARB             0x84E0
#define GL_CLIENT_ACTIVE_TEXTURE_ARB      0x84E1
#define GL_MAX_TEXTURE_UNITS_ARB          0x84E2

