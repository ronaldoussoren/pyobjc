/*
# BUILD api_versions [0x101]
*/

%module image_transform

%{
/**
 *
 * GL.HP.image_transform Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057HP\057image_transform.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_HP_image_transform)
DECLARE_VOID_EXT(glImageTransformParameteriHP, (GLenum target, GLenum pname, GLint param), (target, pname, param))
DECLARE_VOID_EXT(glImageTransformParameterfHP, (GLenum target, GLenum pname, GLfloat param), (target, pname, param))
DECLARE_VOID_EXT(glImageTransformParameterivHP, (GLenum target, GLenum pname, const GLint* param), (target, pname, param))
DECLARE_VOID_EXT(glImageTransformParameterfvHP, (GLenum target, GLenum pname, const GLfloat* param), (target, pname, param))
DECLARE_VOID_EXT(glGetImageTransformParameterfvHP, (GLenum target, GLenum pname, GLfloat* param), (target, pname, param))
DECLARE_VOID_EXT(glGetImageTransformParameterivHP, (GLenum target, GLenum pname, GLint* param), (target, pname, param))
#endif
%}

void glImageTransformParameteriHP(GLenum target, GLenum pname, GLint param);
DOC(glImageTransformParameteriHP, "glImageTransformParameteriHP(target, pname, param) -> None")

void glImageTransformParameterfHP(GLenum target, GLenum pname, GLfloat param);
DOC(glImageTransformParameterfHP, "glImageTransformParameterfHP(target, pname, param) -> None")

void glImageTransformParameterivHP(GLenum target, GLenum pname, const GLint* param);
DOC(glImageTransformParameterivHP, "glImageTransformParameterivHP(target, pname, params) -> None")

void glImageTransformParameterfvHP(GLenum target, GLenum pname, const GLfloat* param);
DOC(glImageTransformParameterfvHP, "glImageTransformParameterfvHP(target, pname, params) -> None")

void glGetImageTransformParameterfvHP(GLenum target, GLenum pname, GLfloat param[4]);
DOC(glGetImageTransformParameterfvHP, "glGetImageTransformParameterfvHP(target, pname) -> params")

void glGetImageTransformParameterivHP(GLenum target, GLenum pname, GLint param[4]);
DOC(glGetImageTransformParameterivHP, "glGetImageTransformParameterivHP(target, pname) -> params")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_HP_image_transform)
	"glImageTransformParameteriHP",
	"glImageTransformParameterfHP",
	"glImageTransformParameterivHP",
	"glImageTransformParameterfvHP",
	"glGetImageTransformParameterfvHP",
	"glGetImageTransformParameterivHP",
#endif
	NULL
};

#define glInitImageTransformHP() InitExtension("GL_HP_image_transform", proc_names)
%}

int glInitImageTransformHP();
DOC(glInitImageTransformHP, "glInitImageTransformHP() -> bool")


%{
PyObject *__info()
{
	if (glInitImageTransformHP())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



#define GL_IMAGE_SCALE_X_HP               0x8155
#define GL_IMAGE_SCALE_Y_HP               0x8156
#define GL_IMAGE_TRANSLATE_X_HP           0x8157
#define GL_IMAGE_TRANSLATE_Y_HP           0x8158
#define GL_IMAGE_ROTATE_ANGLE_HP          0x8159
#define GL_IMAGE_ROTATE_ORIGIN_X_HP       0x815A
#define GL_IMAGE_ROTATE_ORIGIN_Y_HP       0x815B
#define GL_IMAGE_MAG_FILTER_HP            0x815C
#define GL_IMAGE_MIN_FILTER_HP            0x815D
#define GL_IMAGE_CUBIC_WEIGHT_HP          0x815E
#define GL_CUBIC_HP                       0x815F
#define GL_AVERAGE_HP                     0x8160
#define GL_IMAGE_TRANSFORM_2D_HP          0x8161
#define GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP 0x8162
#define GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP 0x8163
