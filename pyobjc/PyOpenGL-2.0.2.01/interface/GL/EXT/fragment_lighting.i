/*
# BUILD api_versions [0x101]
*/

%module fragment_lighting

#define __version__ "$Revision: 1.17.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057fragment_lighting.txt"

%{
/**
 *
 * GL.EXT.fragment_lighting Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include py_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_fragment_lighting)
DECLARE_VOID_EXT(glFragmentMaterialfEXT, (GLenum face, GLenum pname, GLfloat param), (face, pname, param))
DECLARE_VOID_EXT(glFragmentMaterialfvEXT, (GLenum face, GLenum pname, const GLfloat *v), (face, pname, v))
DECLARE_VOID_EXT(glFragmentMaterialiEXT, (GLenum face, GLenum pname, GLint param), (face, pname, param))
DECLARE_VOID_EXT(glFragmentMaterialivEXT, (GLenum face, GLenum pname, const GLint *v), (face, pname, v))
DECLARE_VOID_EXT(glFragmentLightModelfEXT, (GLenum pname, GLfloat param), (pname, param))
DECLARE_VOID_EXT(glFragmentLightModelfvEXT, (GLenum pname, const GLfloat *v), (pname, v))
DECLARE_VOID_EXT(glFragmentLightModeliEXT, (GLenum pname, GLint param), (pname, param))
DECLARE_VOID_EXT(glFragmentLightModelivEXT, (GLenum pname, const GLint *v), (pname, v))
DECLARE_VOID_EXT(glFragmentLightfEXT, (GLenum light, GLenum pname, GLfloat param), (light, pname, param))
DECLARE_VOID_EXT(glFragmentLightfvEXT, (GLenum light, GLenum pname, const GLfloat *v), (light, pname, v))
DECLARE_VOID_EXT(glFragmentLightiEXT, (GLenum light, GLenum pname, GLint param), (light, pname, param))
DECLARE_VOID_EXT(glFragmentLightivEXT, (GLenum light, GLenum pname, const GLint *v), (light, pname, v))
DECLARE_VOID_EXT(glGetFragmentLightfvEXT, (GLenum light, GLenum pname, GLfloat *params), (light, pname, params))
DECLARE_VOID_EXT(glGetFragmentLightivEXT, (GLenum light, GLenum pname, GLint *params), (light, pname, params))
DECLARE_VOID_EXT(glFragmentColorMaterialEXT, (GLenum face, GLenum mode), (face, mode))
DECLARE_VOID_EXT(glGetFragmentMaterialfvEXT, (GLenum face, GLenum pname, GLfloat *params), (face, pname, params))
DECLARE_VOID_EXT(glGetFragmentMaterialivEXT, (GLenum face, GLenum pname, GLint *params), (face, pname, params))
DECLARE_VOID_EXT(glLightEnviEXT, (GLenum pname, GLint param), (pname, param))
#endif
%}

void glFragmentMaterialfEXT (GLenum face, GLenum pname, GLfloat param);
DOC(glFragmentMaterialfEXT, "glFragmentMaterialfEXT(face, pname, param) -> None")

void glFragmentMaterialfvEXT (GLenum face, GLenum pname, const GLfloat *v);
DOC(glFragmentMaterialfvEXT, "glFragmentMaterialfvEXT(face, pname, params) -> None")

void glFragmentMaterialiEXT (GLenum face, GLenum pname, GLint param);
DOC(glFragmentMaterialiEXT, "glFragmentMaterialiEXT(face, pname, param) -> None")

void glFragmentMaterialivEXT (GLenum face, GLenum pname, const GLint *v);
DOC(glFragmentMaterialivEXT, "glFragmentMaterialivEXT(face, pname, params) -> None")



/* turn the exception handler on */
%include gl_exception_handler.inc

void glFragmentLightModelfEXT (GLenum pname, GLfloat param);
DOC(glFragmentLightModelfEXT, "glFragmentLightModelfEXT(pname, param) -> None")

void glFragmentLightModelfvEXT (GLenum pname, const GLfloat *v);
DOC(glFragmentLightModelfvEXT, "glFragmentLightModelfvEXT(pname, params) -> None")

void glFragmentLightModeliEXT (GLenum pname, GLint param);
DOC(glFragmentLightModeliEXT, "glFragmentLightModeliEXT(pname, param) -> None")

void glFragmentLightModelivEXT (GLenum pname, const GLint *v);
DOC(glFragmentLightModelivEXT, "glFragmentLightModelivEXT(pname, params) -> None")

void glFragmentLightfEXT (GLenum light, GLenum pname, GLfloat param);
DOC(glFragmentLightfEXT, "glFragmentLightfEXT(light, pname, param) -> None")

void glFragmentLightfvEXT (GLenum light, GLenum pname, const GLfloat *v);
DOC(glFragmentLightfvEXT, "glFragmentLightfvEXT(light, pname, params) -> None")

void glFragmentLightiEXT (GLenum light, GLenum pname, GLint param);
DOC(glFragmentLightiEXT, "glFragmentLightiEXT(light, pname, param) -> None")

void glFragmentLightivEXT (GLenum light, GLenum pname, const GLint *v);
DOC(glFragmentLightivEXT, "glFragmentLightivEXT(light, pname, params) -> None")

void glGetFragmentLightfvEXT (GLenum light, GLenum pname, GLfloat params[4]);
DOC(glGetFragmentLightfvEXT, "glGetFragmentLightfvEXT(light, pname) -> params")

void glGetFragmentLightivEXT (GLenum light, GLenum pname, GLint params[4]);
DOC(glGetFragmentLightivEXT, "glGetFragmentLightivEXT(light, pname) -> params")

void glFragmentColorMaterialEXT (GLenum face, GLenum mode);
DOC(glFragmentColorMaterialEXT, "glFragmentColorMaterialEXT(face, mode) -> None")

void glGetFragmentMaterialfvEXT (GLenum face, GLenum pname, GLfloat params[4]);
DOC(glGetFragmentMaterialfvEXT, "glGetFragmentMaterialfvEXT(face, pname) -> params")

void glGetFragmentMaterialivEXT (GLenum face, GLenum pname, GLint params[4]);
DOC(glGetFragmentMaterialivEXT, "glGetFragmentMaterialivEXT(face, pname) -> params")

void glLightEnviEXT(GLenum pname, GLint param);
DOC(glLightEnviEXT, "glLightEnviEXT(pname, param) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_fragment_lighting)
	"glFragmentMaterialfEXT",
	"glFragmentMaterialfvEXT",
	"glFragmentMaterialiEXT",
	"glFragmentMaterialivEXT",
	"glFragmentLightModelfEXT",
	"glFragmentLightModelfvEXT",
	"glFragmentLightModeliEXT",
	"glFragmentLightModelivEXT",
	"glFragmentLightfEXT",
	"glFragmentLightfvEXT",
	"glFragmentLightiEXT",
	"glFragmentLightivEXT",
	"glGetFragmentLightfvEXT",
	"glGetFragmentLightivEXT",
	"glFragmentColorMaterialEXT",
	"glGetFragmentMaterialfvEXT",
	"glGetFragmentMaterialivEXT",
	"glLightEnviEXT",
#endif
	NULL
};

#define glInitFragmentLightingEXT() InitExtension("GL_EXT_fragment_lighting", proc_names)
%}

int glInitFragmentLightingEXT();
DOC(glInitFragmentLightingEXT, "glInitFragmentLightingEXT() -> bool")

%{
#ifndef GL_EXT_fragment_lighting
#define GL_MAX_FRAGMENT_LIGHTS_EXT                             0x8404
#define GL_MAX_ACTIVE_LIGHTS_EXT                               0x8405
#endif

PyObject *__info()
{
	if (glInitFragmentLightingEXT())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_FRAGMENT_LIGHTS_EXT", GL_MAX_FRAGMENT_LIGHTS_EXT, "i"));
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_ACTIVE_LIGHTS_EXT", GL_MAX_ACTIVE_LIGHTS_EXT, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_FRAGMENT_LIGHTING_EXT                               0x8400
#define GL_FRAGMENT_COLOR_MATERIAL_EXT                         0x8401

#define GL_FRAGMENT_COLOR_MATERIAL_FACE_EXT                    0x8402
#define GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_EXT               0x8403
#define GL_MAX_FRAGMENT_LIGHTS_EXT                             0x8404
#define GL_MAX_ACTIVE_LIGHTS_EXT                               0x8405
#define GL_CURRENT_RASTER_NORMAL_EXT                           0x8406

#define GL_LIGHT_ENV_MODE_EXT                                  0x8407

#define GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_EXT               0x8408
#define GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_EXT                   0x8409
#define GL_FRAGMENT_LIGHT_MODEL_AMBIENT_EXT                    0x840A
#define GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_EXT       0x840B

#define GL_FRAGMENT_LIGHT0_EXT                                 0x840C
#define GL_FRAGMENT_LIGHT1_EXT GL_FRAGMENT_LIGHT0_EXT+1
#define GL_FRAGMENT_LIGHT2_EXT GL_FRAGMENT_LIGHT0_EXT+2
#define GL_FRAGMENT_LIGHT3_EXT GL_FRAGMENT_LIGHT0_EXT+3
#define GL_FRAGMENT_LIGHT4_EXT GL_FRAGMENT_LIGHT0_EXT+4
#define GL_FRAGMENT_LIGHT5_EXT GL_FRAGMENT_LIGHT0_EXT+5
#define GL_FRAGMENT_LIGHT6_EXT GL_FRAGMENT_LIGHT0_EXT+6
#define GL_FRAGMENT_LIGHT7_EXT GL_FRAGMENT_LIGHT0_EXT+7
#define GL_FRAGMENT_LIGHT8_EXT GL_FRAGMENT_LIGHT0_EXT+8
#define GL_FRAGMENT_LIGHT9_EXT GL_FRAGMENT_LIGHT0_EXT+9
#define GL_FRAGMENT_LIGHT10_EXT GL_FRAGMENT_LIGHT0_EXT+10
#define GL_FRAGMENT_LIGHT11_EXT GL_FRAGMENT_LIGHT0_EXT+11
#define GL_FRAGMENT_LIGHT12_EXT GL_FRAGMENT_LIGHT0_EXT+12
#define GL_FRAGMENT_LIGHT13_EXT GL_FRAGMENT_LIGHT0_EXT+13
#define GL_FRAGMENT_LIGHT14_EXT GL_FRAGMENT_LIGHT0_EXT+14
#define GL_FRAGMENT_LIGHT15_EXT GL_FRAGMENT_LIGHT0_EXT+15
#define GL_FRAGMENT_LIGHT16_EXT GL_FRAGMENT_LIGHT0_EXT+16
#define GL_FRAGMENT_LIGHT17_EXT GL_FRAGMENT_LIGHT0_EXT+17
#define GL_FRAGMENT_LIGHT18_EXT GL_FRAGMENT_LIGHT0_EXT+18
#define GL_FRAGMENT_LIGHT19_EXT GL_FRAGMENT_LIGHT0_EXT+19
#define GL_FRAGMENT_LIGHT20_EXT GL_FRAGMENT_LIGHT0_EXT+20
#define GL_FRAGMENT_LIGHT21_EXT GL_FRAGMENT_LIGHT0_EXT+21
#define GL_FRAGMENT_LIGHT22_EXT GL_FRAGMENT_LIGHT0_EXT+22
#define GL_FRAGMENT_LIGHT23_EXT GL_FRAGMENT_LIGHT0_EXT+23
#define GL_FRAGMENT_LIGHT24_EXT GL_FRAGMENT_LIGHT0_EXT+24
#define GL_FRAGMENT_LIGHT25_EXT GL_FRAGMENT_LIGHT0_EXT+25
#define GL_FRAGMENT_LIGHT26_EXT GL_FRAGMENT_LIGHT0_EXT+26
#define GL_FRAGMENT_LIGHT27_EXT GL_FRAGMENT_LIGHT0_EXT+27
#define GL_FRAGMENT_LIGHT28_EXT GL_FRAGMENT_LIGHT0_EXT+28
#define GL_FRAGMENT_LIGHT29_EXT GL_FRAGMENT_LIGHT0_EXT+29
#define GL_FRAGMENT_LIGHT30_EXT GL_FRAGMENT_LIGHT0_EXT+30
#define GL_FRAGMENT_LIGHT31_EXT GL_FRAGMENT_LIGHT0_EXT+31

