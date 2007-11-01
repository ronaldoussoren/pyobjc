/*
# BUILD api_versions [0x101]
*/

%module multitexture

#define __version__ "$Revision: 1.23.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057www.pseudonymz.demon.co.uk/multitexture.spec"

%{
/**
 *
 * GL.SGIS.multitexture Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

#define GL_TEXTURE0_SGIS                   0x835F
#define GL_TEXTURE1_SGIS                   0x8360
#define GL_TEXTURE2_SGIS                   0x8361
#define GL_TEXTURE3_SGIS                   0x8362
#define GL_TEXTURE4_SGIS                   0x8363
#define GL_TEXTURE5_SGIS                   0x8364
#define GL_TEXTURE6_SGIS                   0x8365
#define GL_TEXTURE7_SGIS                   0x8366
#define GL_TEXTURE8_SGIS                   0x8367
#define GL_TEXTURE9_SGIS                   0x8368
#define GL_TEXTURE10_SGIS                  0x8369
#define GL_TEXTURE11_SGIS                  0x836A
#define GL_TEXTURE12_SGIS                  0x836B
#define GL_TEXTURE13_SGIS                  0x836C
#define GL_TEXTURE14_SGIS                  0x836D
#define GL_TEXTURE15_SGIS                  0x836E
#define GL_TEXTURE16_SGIS                  0x836F
#define GL_TEXTURE17_SGIS                  0x8370
#define GL_TEXTURE18_SGIS                  0x8371
#define GL_TEXTURE19_SGIS                  0x8372
#define GL_TEXTURE20_SGIS                  0x8373
#define GL_TEXTURE21_SGIS                  0x8374
#define GL_TEXTURE22_SGIS                  0x8375
#define GL_TEXTURE23_SGIS                  0x8376
#define GL_TEXTURE24_SGIS                  0x8377
#define GL_TEXTURE25_SGIS                  0x8378
#define GL_TEXTURE26_SGIS                  0x8379
#define GL_TEXTURE27_SGIS                  0x837A
#define GL_TEXTURE28_SGIS                  0x837B
#define GL_TEXTURE29_SGIS                  0x837C
#define GL_TEXTURE30_SGIS                  0x837D
#define GL_TEXTURE31_SGIS                  0x837E

#define GL_SELECTED_TEXTURE_SGIS		0x835C
#define GL_SELECTED_TEXTURE_COORD_SET_SGIS	0x835D
#define GL_MAX_TEXTURES_SGIS			0x835E
#define GL_TEXTURE_COORD_SET_SOURCE_SGIS	0x8363

%include gl_exception_handler.inc


/*extern void APIENTRY glMultiTexCoord1dSGIS (GLenum, GLdouble); */
%{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_multitexture)
DECLARE_VOID_EXT(glMultiTexCoord1dSGIS, (GLenum unit, GLdouble s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1dvSGIS, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord1fSGIS, (GLenum unit, GLfloat s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1fvSGIS, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord1iSGIS, (GLenum unit, GLint s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1ivSGIS, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord1sSGIS, (GLenum unit, GLshort s), (unit, s))
DECLARE_VOID_EXT(glMultiTexCoord1svSGIS, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2dSGIS, (GLenum unit, GLdouble s, GLdouble t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2dvSGIS, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2fSGIS, (GLenum unit, GLfloat s, GLfloat t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2fvSGIS, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2iSGIS, (GLenum unit, GLint s, GLint t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2ivSGIS, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord2sSGIS, (GLenum unit, GLshort s, GLshort t), (unit, s, t))
DECLARE_VOID_EXT(glMultiTexCoord2svSGIS, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3dSGIS, (GLenum unit, GLdouble s, GLdouble t, GLdouble u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3dvSGIS, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3fSGIS, (GLenum unit, GLfloat s, GLfloat t, GLfloat u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3fvSGIS, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3iSGIS, (GLenum unit, GLint s, GLint t, GLint u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3ivSGIS, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord3sSGIS, (GLenum unit, GLshort s, GLshort t, GLshort u), (unit, s, t, u))
DECLARE_VOID_EXT(glMultiTexCoord3svSGIS, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4dSGIS, (GLenum unit, GLdouble s, GLdouble t, GLdouble u, GLdouble v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4dvSGIS, (GLenum unit, const GLdouble *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4fSGIS, (GLenum unit, GLfloat s, GLfloat t, GLfloat u, GLfloat v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4fvSGIS, (GLenum unit, const GLfloat *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4iSGIS, (GLenum unit, GLint s, GLint t, GLint u, GLint v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4ivSGIS, (GLenum unit, const GLint *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoord4sSGIS, (GLenum unit, GLshort s, GLshort t, GLshort u, GLshort v), (unit, s, t, u, v))
DECLARE_VOID_EXT(glMultiTexCoord4svSGIS, (GLenum unit, const GLshort *v), (unit, v))
DECLARE_VOID_EXT(glMultiTexCoordPointerSGIS,\
	(GLenum target, GLint size, GLenum type, GLsizei stride, const void *pointer),\
	(target, size, type, stride, pointer))
DECLARE_VOID_EXT(glSelectTextureSGIS, (GLenum target), (target))
DECLARE_VOID_EXT(glSelectTextureCoordSetSGIS, (GLenum target), (target))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SGIS_multitexture)
	"glMultiTexCoord1dSGIS",
	"glMultiTexCoord1dvSGIS",
	"glMultiTexCoord1fSGIS",
	"glMultiTexCoord1fvSGIS",
	"glMultiTexCoord1iSGIS",
	"glMultiTexCoord1ivSGIS",
	"glMultiTexCoord1sSGIS",
	"glMultiTexCoord1svSGIS",
	"glMultiTexCoord2dSGIS",
	"glMultiTexCoord2dvSGIS",
	"glMultiTexCoord2fSGIS",
	"glMultiTexCoord2fvSGIS",
	"glMultiTexCoord2iSGIS",
	"glMultiTexCoord2ivSGIS",
	"glMultiTexCoord2sSGIS",
	"glMultiTexCoord2svSGIS",
	"glMultiTexCoord3dSGIS",
	"glMultiTexCoord3dvSGIS",
	"glMultiTexCoord3fSGIS",
	"glMultiTexCoord3fvSGIS",
	"glMultiTexCoord3iSGIS",
	"glMultiTexCoord3ivSGIS",
	"glMultiTexCoord3sSGIS",
	"glMultiTexCoord3svSGIS",
	"glMultiTexCoord4dSGIS",
	"glMultiTexCoord4dvSGIS",
	"glMultiTexCoord4fSGIS",
	"glMultiTexCoord4fvSGIS",
	"glMultiTexCoord4iSGIS",
	"glMultiTexCoord4ivSGIS",
	"glMultiTexCoord4sSGIS",
	"glMultiTexCoord4svSGIS",
	"glMultiTexCoordPointerSGIS",
	"glSelectTextureSGIS",
	"glSelectTextureCoordSetSGIS",
#endif
	NULL
};

#define glInitMultitextureSGIS() InitExtension("GL_SGIS_multitexture", proc_names)
%}

int glInitMultitextureSGIS();
DOC(glInitMultitextureSGIS, "glInitMultitextureSGIS() -> bool")

%name(glInitMultiTexSGIS) int glInitMultitextureSGIS();
DOC(glInitMultiTexSGIS, "glInitMultiTexSGIS() -> bool")

%include py_exception_handler.inc

void glMultiTexCoord1dSGIS(GLenum unit, GLdouble s);
DOC(glMultiTexCoord1dSGIS, "glMultiTexCoord1dSGIS(unit, s) -> None")


/*extern void APIENTRY glMultiTexCoord1dvSGIS (GLenum, const GLdouble *); */
void glMultiTexCoord1dvSGIS(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord1dvSGIS, "glMultiTexCoord1dvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord1fSGIS (GLenum, GLfloat); */
void glMultiTexCoord1fSGIS(GLenum unit, GLfloat s);
DOC(glMultiTexCoord1fSGIS, "glMultiTexCoord1fSGIS(unit, s) -> None")


/*extern void APIENTRY glMultiTexCoord1fvSGIS (GLenum, const GLfloat *); */
void glMultiTexCoord1fvSGIS(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord1fvSGIS, "glMultiTexCoord1fvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord1iSGIS (GLenum, GLint); */
void glMultiTexCoord1iSGIS(GLenum unit, GLint s);
DOC(glMultiTexCoord1iSGIS, "glMultiTexCoord1iSGIS(unit, s) -> None")


/*extern void APIENTRY glMultiTexCoord1ivSGIS (GLenum, const GLint *); */
void glMultiTexCoord1ivSGIS(GLenum unit, const GLint *v);
DOC(glMultiTexCoord1ivSGIS, "glMultiTexCoord1ivSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord1sSGIS (GLenum, GLshort); */
void glMultiTexCoord1sSGIS(GLenum unit, GLshort s);
DOC(glMultiTexCoord1sSGIS, "glMultiTexCoord1sSGIS(unit, s) -> None")


/*extern void APIENTRY glMultiTexCoord1svSGIS (GLenum, const GLshort *); */
void glMultiTexCoord1svSGIS(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord1svSGIS, "glMultiTexCoord1svSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord2dSGIS (GLenum, GLdouble, GLdouble); */
void glMultiTexCoord2dSGIS(GLenum unit, GLdouble s, GLdouble t);
DOC(glMultiTexCoord2dSGIS, "glMultiTexCoord2dSGIS(unit, s, t) -> None")


/*extern void APIENTRY glMultiTexCoord2dvSGIS (GLenum, const GLdouble *); */
void glMultiTexCoord2dvSGIS(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord2dvSGIS, "glMultiTexCoord2dvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord2fSGIS (GLenum, GLfloat, GLfloat); */
void glMultiTexCoord2fSGIS(GLenum unit, GLfloat s, GLfloat t);
DOC(glMultiTexCoord2fSGIS, "glMultiTexCoord2fSGIS(unit, s, t) -> None")


/*extern void APIENTRY glMultiTexCoord2fvSGIS (GLenum, const GLfloat *); */
void glMultiTexCoord2fvSGIS(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord2fvSGIS, "glMultiTexCoord2fvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord2iSGIS (GLenum, GLint, GLint); */
void glMultiTexCoord2iSGIS(GLenum unit, GLint s, GLint t);
DOC(glMultiTexCoord2iSGIS, "glMultiTexCoord2iSGIS(unit, s, t) -> None")


/*extern void APIENTRY glMultiTexCoord2ivSGIS (GLenum, const GLint *); */
void glMultiTexCoord2ivSGIS(GLenum unit, const GLint *v);
DOC(glMultiTexCoord2ivSGIS, "glMultiTexCoord2ivSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord2sSGIS (GLenum, GLshort, GLshort); */
void glMultiTexCoord2sSGIS(GLenum unit, GLshort s, GLshort t);
DOC(glMultiTexCoord2sSGIS, "glMultiTexCoord2sSGIS(unit, s, t) -> None")


/*extern void APIENTRY glMultiTexCoord2svSGIS (GLenum, const GLshort *); */
void glMultiTexCoord2svSGIS(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord2svSGIS, "glMultiTexCoord2svSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord3dSGIS (GLenum, GLdouble, GLdouble, GLdouble); */
void glMultiTexCoord3dSGIS(GLenum unit, GLdouble s, GLdouble t, GLdouble u);
DOC(glMultiTexCoord3dSGIS, "glMultiTexCoord3dSGIS(unit, s, t, u) -> None")


/*extern void APIENTRY glMultiTexCoord3dvSGIS (GLenum, const GLdouble *); */
void glMultiTexCoord3dvSGIS(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord3dvSGIS, "glMultiTexCoord3dvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord3fSGIS (GLenum, GLfloat, GLfloat, GLfloat); */
void glMultiTexCoord3fSGIS(GLenum unit, GLfloat s, GLfloat t, GLfloat u);
DOC(glMultiTexCoord3fSGIS, "glMultiTexCoord3fSGIS(unit, s, t, u) -> None")


/*extern void APIENTRY glMultiTexCoord3fvSGIS (GLenum, const GLfloat *); */
void glMultiTexCoord3fvSGIS(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord3fvSGIS, "glMultiTexCoord3fvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord3iSGIS (GLenum, GLint, GLint, GLint); */
void glMultiTexCoord3iSGIS(GLenum unit, GLint s, GLint t, GLint u);
DOC(glMultiTexCoord3iSGIS, "glMultiTexCoord3iSGIS(unit, s, t, u) -> None")


/*extern void APIENTRY glMultiTexCoord3ivSGIS (GLenum, const GLint *); */
void glMultiTexCoord3ivSGIS(GLenum unit, const GLint *v);
DOC(glMultiTexCoord3ivSGIS, "glMultiTexCoord3ivSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord3sSGIS (GLenum, GLshort, GLshort, GLshort); */
void glMultiTexCoord3sSGIS(GLenum unit, GLshort s, GLshort t, GLshort u);
DOC(glMultiTexCoord3sSGIS, "glMultiTexCoord3sSGIS(unit, s, t, u) -> None")


/*extern void APIENTRY glMultiTexCoord3svSGIS (GLenum, const GLshort *); */
void glMultiTexCoord3svSGIS(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord3svSGIS, "glMultiTexCoord3svSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord4dSGIS (GLenum, GLdouble, GLdouble, GLdouble, GLdouble); */
void glMultiTexCoord4dSGIS(GLenum unit, GLdouble s, GLdouble t, GLdouble u, GLdouble v);
DOC(glMultiTexCoord4dSGIS, "glMultiTexCoord4dSGIS(unit, s, t, u, v) -> None")


/*extern void APIENTRY glMultiTexCoord4dvSGIS (GLenum, const GLdouble *); */
void glMultiTexCoord4dvSGIS(GLenum unit, const GLdouble *v);
DOC(glMultiTexCoord4dvSGIS, "glMultiTexCoord4dvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord4fSGIS (GLenum, GLfloat, GLfloat, GLfloat, GLfloat); */
void glMultiTexCoord4fSGIS(GLenum unit, GLfloat s, GLfloat t, GLfloat u, GLfloat v);
DOC(glMultiTexCoord4fSGIS, "glMultiTexCoord4fSGIS(unit, s, t, u, v) -> None")


/*extern void APIENTRY glMultiTexCoord4fvSGIS (GLenum, const GLfloat *); */
void glMultiTexCoord4fvSGIS(GLenum unit, const GLfloat *v);
DOC(glMultiTexCoord4fvSGIS, "glMultiTexCoord4fvSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord4iSGIS (GLenum, GLint, GLint, GLint, GLint); */
void glMultiTexCoord4iSGIS(GLenum unit, GLint s, GLint t, GLint u, GLint v);
DOC(glMultiTexCoord4iSGIS, "glMultiTexCoord4iSGIS(unit, s, t, u, v) -> None")


/*extern void APIENTRY glMultiTexCoord4ivSGIS (GLenum, const GLint *); */
void glMultiTexCoord4ivSGIS(GLenum unit, const GLint *v);
DOC(glMultiTexCoord4ivSGIS, "glMultiTexCoord4ivSGIS(unit, v) -> None")


/*extern void APIENTRY glMultiTexCoord4sSGIS (GLenum, GLshort, GLshort, GLshort, GLshort); */
void glMultiTexCoord4sSGIS(GLenum unit, GLshort s, GLshort t, GLshort u, GLshort v);
DOC(glMultiTexCoord4sSGIS, "glMultiTexCoord4sSGIS(unit, s, t, u, v) -> None")


/*extern void APIENTRY glMultiTexCoord4svSGIS (GLenum, const GLshort *); */
void glMultiTexCoord4svSGIS(GLenum unit, const GLshort *v);
DOC(glMultiTexCoord4svSGIS, "glMultiTexCoord4svSGIS(unit, v) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc

/*void glMultiTexCoordPointerSGIS(GLenum target, GLint size, GLenum type, GLsizei stride, const void *pointer); */

void glSelectTextureSGIS(GLenum target);

void glSelectTextureCoordSetSGIS(GLenum target);

%{
#ifndef GL_SGIS_multitexture
#define GL_MAX_TEXTURES_SGIS          0x835E
#endif

PyObject *__info()
{
	if (glInitMultitextureSGIS())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_TEXTURES_SGIS", GL_MAX_TEXTURES_SGIS, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


