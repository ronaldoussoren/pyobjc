/*
# BUILD api_versions [0x106]
*/

%module fog_coord

#define __version__ "$Revision: 1.27.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057fog_coord.txt"

%{
/**
 *
 * GL.EXT.fog_coord Module for PyOpenGL
 * 
 * Date May 2001
 *
 * Authors Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include py_exception_handler.inc

/*void glFogCoordPointerEXT (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer); */

%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_fog_coord)
DECLARE_VOID_EXT(glFogCoordPointerEXT, (GLenum type, GLsizei stride, const GLvoid *pointer), (type, stride, pointer))
DECLARE_VOID_EXT(glFogCoordfEXT, (GLfloat coord), (coord))
DECLARE_VOID_EXT(glFogCoorddEXT, (GLdouble coord), (coord))
DECLARE_VOID_EXT(glFogCoordfvEXT, (const GLfloat* coord), (coord))
DECLARE_VOID_EXT(glFogCoorddvEXT, (const GLdouble* coord), (coord))
#endif
%}

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#ifndef GL_FOG_COORDINATE_ARRAY_POINTER_EXT
#define GL_FOG_COORDINATE_ARRAY_POINTER_EXT 0x8456
#endif

void _glFogCoordPointerEXT(GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_FOG_COORDINATE_ARRAY_POINTER_EXT);
	acquire(pointer);
	glFogCoordPointerEXT(type, stride, pointer);
}
%}

%name(glFogCoordPointerEXT) void _glFogCoordPointerEXT(GLenum type, GLsizei stride, void *pointer);
DOC(glFogCoordPointerEXT, "glFogCoordPointerEXT(type, stride, pointer) -> None")

%name(glFogCoordPointerubEXT) void _glFogCoordPointerEXT(GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLubyte* pointer);
DOC(glFogCoordPointerubEXT, "glFogCoordPointerubEXT(pointer) -> None")

%name(glFogCoordPointerbEXT) void _glFogCoordPointerEXT(GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glFogCoordPointerbEXT, "glFogCoordPointerubEXT(pointer) -> None")

%name(glFogCoordPointerusEXT) void _glFogCoordPointerEXT(GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLushort* pointer);
DOC(glFogCoordPointerusEXT, "glFogCoordPointerusEXT(pointer) -> None")

%name(glFogCoordPointersEXT) void _glFogCoordPointerEXT(GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glFogCoordPointersEXT, "glFogCoordPointersEXT(pointer) -> None")

%name(glFogCoordPointeruiEXT) void _glFogCoordPointerEXT(GLenum type_UNSIGNED_INT, GLsizei stride_0, GLuint* pointer);
DOC(glFogCoordPointeruiEXT, "glFogCoordPointeruiEXT(pointer) -> None")

%name(glFogCoordPointeriEXT) void _glFogCoordPointerEXT(GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glFogCoordPointeriEXT, "glFogCoordPointeriEXT(pointer) -> None")

%name(glFogCoordPointerfEXT) void _glFogCoordPointerEXT(GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glFogCoordPointerfEXT, "glFogCoordPointerfEXT(pointer) -> None")

%name(glFogCoordPointerdEXT) void _glFogCoordPointerEXT(GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glFogCoordPointerdEXT, "glFogCoordPointerdEXT(pointer) -> None")


void glFogCoordfEXT(GLfloat coord);
DOC(glFogCoordfEXT, "glFogCoordfEXT(coord) -> None")

void glFogCoorddEXT(GLdouble coord);
DOC(glFogCoorddEXT, "glFogCoorddEXT(coord) -> None")


void glFogCoordfvEXT(const GLfloat* coord);
DOC(glFogCoordfvEXT, "glFogCoordfvEXT(coord) -> None")

void glFogCoorddvEXT(const GLdouble* coord);
DOC(glFogCoorddvEXT, "glFogCoorddvEXT(coord) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_fog_coord)
	"glFogCoordPointerEXT",
	"glFogCoordfEXT",
	"glFogCoorddEXT",
	"glFogCoordfvEXT",
	"glFogCoorddvEXT",
#endif
	NULL
};

#define glInitFogCoordEXT() InitExtension("GL_EXT_fog_coord", proc_names)
%}

int glInitFogCoordEXT();
DOC(glInitFogCoordEXT, "glInitFogCoordEXT() -> bool")



%{
PyObject *__info()
{
	if (glInitFogCoordEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



#define GL_FOG_COORDINATE_SOURCE_EXT	    0x8450

#define GL_FOG_COORDINATE_EXT		    0x8451
#define GL_FRAGMENT_DEPTH_EXT		    0x8452

#define GL_CURRENT_FOG_COORDINATE_EXT	    0x8453
#define GL_FOG_COORDINATE_ARRAY_TYPE_EXT	    0x8454
#define GL_FOG_COORDINATE_ARRAY_STRIDE_EXT     0x8455

#define GL_FOG_COORDINATE_ARRAY_POINTER_EXT    0x8456

#define GL_FOG_COORDINATE_ARRAY_EXT	    0x8457
