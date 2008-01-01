/*
# BUILD api_versions [0x106]
*/

%module triangle_list

%{
/**
 *
 * GL.SUN.triangle_list Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.21.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057SUN\057triangle_list.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
/* fix for SUN headers */
#if defined(GL_TRIANGLE_LIST_SUN) && !defined(GL_SUN_triangle_list)
#define GL_SUN_triangle_list 1
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_SUN_triangle_list)
DECLARE_VOID_EXT(glReplacementCodeuiSUN, (GLuint code), (code))
DECLARE_VOID_EXT(glReplacementCodeusSUN, (GLushort code), (code))
DECLARE_VOID_EXT(glReplacementCodeubSUN, (GLubyte code), (code))
DECLARE_VOID_EXT(glReplacementCodeuivSUN, (const GLuint* code), (code))
DECLARE_VOID_EXT(glReplacementCodeusvSUN, (const GLushort* code), (code))
DECLARE_VOID_EXT(glReplacementCodeubvSUN, (const GLubyte* code), (code))
DECLARE_VOID_EXT(glReplacementCodePointerSUN, (GLenum type, GLsizei stride, const void *buffer), (type, stride, buffer))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_SUN_triangle_list)
	"glReplacementCodeuiSUN",
	"glReplacementCodeusSUN",
	"glReplacementCodeubSUN",
	"glReplacementCodeuivSUN",
	"glReplacementCodeusvSUN",
	"glReplacementCodeubvSUN",
	"glReplacementCodePointerSUN",
#endif
	NULL
};

#define glInitTriangleListSUN() InitExtension("GL_SUN_triangle_list", proc_names)
%}

int glInitTriangleListSUN();
DOC(glInitTriangleListSUN, "glInitTriangleListSUN() -> bool")


%include py_exception_handler.inc


void glReplacementCodeuiSUN(GLuint code);
DOC(glReplacementCodeuiSUN, "glReplacementCodeuiSUN(code) -> None")

void glReplacementCodeusSUN(GLushort code);
DOC(glReplacementCodeusSUN, "glReplacementCodeusSUN(code) -> None")

void glReplacementCodeubSUN(GLubyte code);
DOC(glReplacementCodeubSUN, "glReplacementCodeubSUN(code) -> None")

void glReplacementCodeuivSUN(const GLuint* code);
DOC(glReplacementCodeuivSUN, "glReplacementCodeuivSUN(code) -> None")

void glReplacementCodeusvSUN(const GLushort* code);
DOC(glReplacementCodeusvSUN, "glReplacementCodeusvSUN(code) -> None")

void glReplacementCodeubvSUN(const GLubyte* code);
DOC(glReplacementCodeubvSUN, "glReplacementCodeubvSUN(code) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#ifndef GL_SUN_triangle_list
#define GL_REPLACEMENT_CODE_ARRAY_SUN		0x85C0
#endif

void _glReplacementCodePointerSUN(GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_REPLACEMENT_CODE_ARRAY_SUN);
	acquire(pointer);
	glReplacementCodePointerSUN(type, stride, pointer);
}
%}

%name(glReplacementCodePointerSUN) void _glReplacementCodePointerSUN(GLenum type, GLsizei stride, void *pointer);
DOC(glReplacementCodePointerSUN, "glReplacementCodePointerSUN(type, stride, pointer) -> None")

%name(glReplacementCodePointerubSUN) void _glReplacementCodePointerSUN(GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLubyte* pointer);
DOC(glReplacementCodePointerubSUN, "glReplacementCodePointerubSUN(pointer) -> None")

%name(glReplacementCodePointerusSUN) void _glReplacementCodePointerSUN(GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLushort* pointer);
DOC(glReplacementCodePointerusSUN, "glReplacementCodePointerusSUN(pointer) -> None")

%name(glReplacementCodePointeruiSUN) void _glReplacementCodePointerSUN(GLenum type_UNSIGNED_INT, GLsizei stride_0, GLuint* pointer);
DOC(glReplacementCodePointeruiSUN, "glReplacementCodePointeruiSUN(pointer) -> None")


%{
PyObject *__info()
{
	if (glInitTriangleListSUN())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_TRIANGLE_LIST_SUN			0x81D7

#define GL_REPLACEMENT_CODE_SUN			0x81D8

#define GL_RESTART_SUN				0x01
#define GL_REPLACE_MIDDLE_SUN			0x02
#define GL_REPLACE_OLDEST_SUN			0x03

#define GL_REPLACEMENT_CODE_ARRAY_SUN		0x85C0

#define GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN		0x85C1
#define GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN	0x85C2

#define GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN	0x85C3

#define GL_R1UI_V3F_SUN				0x85C4
#define GL_R1UI_C4UB_V3F_SUN			0x85C5
#define GL_R1UI_C3F_V3F_SUN			0x85C6
#define GL_R1UI_N3F_V3F_SUN			0x85C7
#define GL_R1UI_C4F_N3F_V3F_SUN			0x85C8
#define GL_R1UI_T2F_V3F_SUN			0x85C9
#define GL_R1UI_T2F_N3F_V3F_SUN			0x85CA
#define GL_R1UI_T2F_C4F_N3F_V3F_SUN		0x85CB

