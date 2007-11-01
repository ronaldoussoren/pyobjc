/*
# BUILD api_versions [0x110]
*/

%module vertex_array

#define __version__ "$Revision: 1.7.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com/projects/ogl-sample/registry/EXT/vertex_array.txt"

%{
/**
 *
 * GL.EXT.vertex_array Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_vertex_array)
DECLARE_VOID_EXT(glArrayElementEXT, (GLint i), (i))
DECLARE_VOID_EXT(glColorPointerEXT, (GLint size, GLenum type, GLsizei stride, GLsizei count, const void* pointer), (size, type, stride, count, pointer))
DECLARE_VOID_EXT(glDrawArraysEXT, (GLenum mode, GLint first, GLsizei count), (mode, first, count))
DECLARE_VOID_EXT(glEdgeFlagPointerEXT, (GLsizei stride, GLsizei count, const GLboolean* pointer), (stride, count, pointer))
DECLARE_VOID_EXT(glIndexPointerEXT, (GLenum type, GLsizei stride, GLsizei count, const void* pointer), (type, stride, count, pointer))
DECLARE_VOID_EXT(glNormalPointerEXT, (GLenum type, GLsizei stride, GLsizei count, const void* pointer), (type, stride, count, pointer))
DECLARE_VOID_EXT(glTexCoordPointerEXT, (GLint size, GLenum type, GLsizei stride, GLsizei count, const void* pointer), (size, type, stride, count, pointer))
DECLARE_VOID_EXT(glVertexPointerEXT, (GLint size, GLenum type, GLsizei stride, GLsizei count, const void* pointer), (size, type, stride, count, pointer))
#endif

#ifndef GL_EXT_vertex_array
#define GL_VERTEX_ARRAY_POINTER_EXT       0x808E
#define GL_NORMAL_ARRAY_POINTER_EXT       0x808F
#define GL_COLOR_ARRAY_POINTER_EXT        0x8090
#define GL_INDEX_ARRAY_POINTER_EXT        0x8091
#define GL_TEXTURE_COORD_ARRAY_POINTER_EXT 0x8092
#define GL_EDGE_FLAG_ARRAY_POINTER_EXT    0x8093
#endif
%}


%include py_exception_handler.inc

/*
# glArrayElement
# 
# Python binding unchanged from spec.
*/

void glArrayElementEXT(GLint i);
DOC(glArrayElementEXT, "glArrayElementEXT(index) -> None")


%include gl_exception_handler.inc

%{
void _glColorPointerEXT(GLint size, GLenum type, GLsizei stride, GLsizei count, GLvoid *pointer)
{
	decrementPointerLock(GL_COLOR_ARRAY_POINTER_EXT);
	acquire(pointer);
	glColorPointerEXT(size, type, stride, count, pointer);
}
%}

%name(glColorPointerEXT) void _glColorPointerEXT(GLint size, GLenum type, GLsizei stride, GLsizei count, void *pointer);
DOC(glColorPointerEXT, "glColorPointerEXT(size, type, stride, count, pointer) -> None")

%name(glColorPointerubEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLsizei d_3_0, GLubyte* pointer);
DOC(glColorPointerubEXT, "glColorPointerubEXT(pointer[][]) -> None")

%name(glColorPointerbEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLsizei d_3_0, GLbyte* pointer);
DOC(glColorPointerbEXT, "glColorPointerbEXT(pointer[][]) -> None")

%name(glColorPointerusEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLsizei d_3_0, GLushort* pointer);
DOC(glColorPointerusEXT, "glColorPointerusEXT(pointer[][]) -> None")

%name(glColorPointersEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLsizei d_3_0, GLshort* pointer);
DOC(glColorPointersEXT, "glColorPointersEXT(pointer[][]) -> None")

%name(glColorPointeruiEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_UNSIGNED_INT, GLsizei stride_0, GLsizei d_3_0, GLuint* pointer);
DOC(glColorPointeruiEXT, "glColorPointeruiEXT(pointer[][]) -> None")

%name(glColorPointeriEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLsizei d_3_0, GLint* pointer);
DOC(glColorPointeriEXT, "glColorPointeriEXT(pointer[][]) -> None")

%name(glColorPointerfEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLsizei d_3_0, GLfloat *pointer);
DOC(glColorPointerfEXT, "glColorPointerfEXT(pointer[][]) -> None")

%name(glColorPointerdEXT) void _glColorPointerEXT(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLsizei d_3_0, GLdouble *pointer);
DOC(glColorPointerdEXT, "glColorPointerdEXT(pointer[][]) -> None")



void glDrawArraysEXT (GLenum mode, GLint first, GLsizei count);
DOC(glDrawArraysEXT, "glDrawArraysEXT(mode, first, count) -> None")


/*void glEdgeFlagPointerEXT (GLsizei stride, const GLvoid *pointer); */
%{
void _glEdgeFlagPointerEXT(GLsizei stride, GLsizei count, GLvoid *pointer)
{
	decrementPointerLock(GL_EDGE_FLAG_ARRAY_POINTER_EXT);
	acquire(pointer);
	glEdgeFlagPointerEXT(stride, count, pointer);
}
%}

%name(glEdgeFlagPointerEXT) void _glEdgeFlagPointerEXT(GLsizei stride, GLsizei count, void *pointer);
DOC(glEdgeFlagPointerEXT, "glEdgeFlagPointerEXT(stride, pointer) -> None")

%name(glEdgeFlagPointerbEXT) void _glEdgeFlagPointerEXT(GLsizei stride_0, GLsizei d_2_0, GLbyte* pointer);
DOC(glEdgeFlagPointerbEXT, "glEdgeFlagPointerbEXT(pointer[]) -> None")


/*void glIndexPointerEXT (GLenum type, GLsizei stride, GLsizei count, const GLvoid *pointer); */
%{
void _glIndexPointerEXT(GLenum type, GLsizei stride, GLsizei count, GLvoid *pointer)
{
	decrementPointerLock(GL_INDEX_ARRAY_POINTER_EXT);
	acquire(pointer);
	glIndexPointerEXT(type, stride, count, pointer);
}
%}

%name(glIndexPointerEXT) void _glIndexPointerEXT(GLenum type, GLsizei stride, GLsizei count, void *pointer);
DOC(glIndexPointerEXT, "glIndexPointerEXT(type, stride, count, pointer) -> None")

%name(glIndexPointerubEXT) void _glIndexPointerEXT(GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLsizei d_3_0, GLubyte* pointer);
DOC(glIndexPointerubEXT, "glIndexPointerubEXT(pointer[]) -> None")

%name(glIndexPointerbEXT) void _glIndexPointerEXT(GLenum type_BYTE, GLsizei stride_0, GLsizei d_3_0, GLbyte* pointer);
DOC(glIndexPointerbEXT, "glIndexPointerubEXT(pointer[]) -> None")

%name(glIndexPointersEXT) void _glIndexPointerEXT(GLenum type_SHORT, GLsizei stride_0, GLsizei d_3_0, GLshort* pointer);
DOC(glIndexPointersEXT, "glIndexPointersEXT(pointer[]) -> None")

%name(glIndexPointeriEXT) void _glIndexPointerEXT(GLenum type_INT, GLsizei stride_0, GLsizei d_3_0, GLint* pointer);
DOC(glIndexPointeriEXT, "glIndexPointeriEXT(pointer[]) -> None")

%name(glIndexPointerfEXT) void _glIndexPointerEXT(GLenum type_FLOAT, GLsizei stride_0, GLsizei d_3_0, GLfloat* pointer);
DOC(glIndexPointerfEXT, "glIndexPointerfEXT(pointer[]) -> None")

%name(glIndexPointerdEXT) void _glIndexPointerEXT(GLenum type_DOUBLE, GLsizei stride_0, GLsizei d_3_0, GLdouble* pointer);
DOC(glIndexPointerdEXT, "glIndexPointerdEXT(pointer[]) -> None")



/*void glNormalPointerEXT (GLenum type, GLsizei stride, GLsizei count, const GLvoid *pointer); */
%{
void _glNormalPointerEXT(GLenum type, GLsizei stride, GLsizei count, GLvoid *pointer)
{
	decrementPointerLock(GL_NORMAL_ARRAY_POINTER_EXT);
	acquire(pointer);
	glNormalPointerEXT(type, stride, count, pointer);
}
%}

%name(glNormalPointerEXT) void _glNormalPointerEXT(GLenum type, GLsizei stride, GLsizei count, void *pointer);
DOC(glNormalPointerEXT, "glNormalPointerEXT(size, type, stride, count, pointer) -> None")

%name(glNormalPointerbEXT) void _glNormalPointerEXT(GLenum type_BYTE, GLsizei stride_0, GLsizei d_3_0, GLbyte* pointer);
DOC(glNormalPointerbEXT, "glNormalPointerubEXT(pointer[][3]) -> None")

%name(glNormalPointersEXT) void _glNormalPointerEXT(GLenum type_SHORT, GLsizei stride_0, GLsizei d_3_0, GLshort* pointer);
DOC(glNormalPointersEXT, "glNormalPointersEXT(pointer[][3]) -> None")

%name(glNormalPointeriEXT) void _glNormalPointerEXT(GLenum type_INT, GLsizei stride_0, GLsizei d_3_0, GLint* pointer);
DOC(glNormalPointeriEXT, "glNormalPointeriEXT(pointer[][3]) -> None")

%name(glNormalPointerfEXT) void _glNormalPointerEXT(GLenum type_FLOAT, GLsizei stride_0, GLsizei d_3_0, GLfloat* pointer);
DOC(glNormalPointerfEXT, "glNormalPointerfEXT(pointer[][3]) -> None")

%name(glNormalPointerdEXT) void _glNormalPointerEXT(GLenum type_DOUBLE, GLsizei stride_0, GLsizei d_3_0, GLdouble* pointer);
DOC(glNormalPointerdEXT, "glNormalPointerdEXT(pointer[][3]) -> None")


/*void glTexCoordPointerEXT (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer); */
%{
void _glTexCoordPointerEXT(GLint size, GLenum type, GLsizei stride, GLsizei count, GLvoid *pointer)
{
	decrementPointerLock(GL_TEXTURE_COORD_ARRAY_POINTER_EXT);
	acquire(pointer);
	glTexCoordPointerEXT(size, type, stride, count, pointer);
}
%}

%name(glTexCoordPointerEXT) void _glTexCoordPointerEXT(GLint size, GLenum type, GLsizei stride, GLsizei count, void *pointer);
DOC(glTexCoordPointerEXT, "glTexCoordPointerEXT(size, type, stride, count, pointer) -> None")

%name(glTexCoordPointerbEXT) void _glTexCoordPointerEXT(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLsizei d_3_0, GLbyte* pointer);
DOC(glTexCoordPointerbEXT, "glTexCoordPointerubEXT(pointer[][]) -> None")

%name(glTexCoordPointersEXT) void _glTexCoordPointerEXT(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLsizei d_3_0, GLshort* pointer);
DOC(glTexCoordPointersEXT, "glTexCoordPointersEXT(pointer[][]) -> None")

%name(glTexCoordPointeriEXT) void _glTexCoordPointerEXT(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLsizei d_3_0, GLint* pointer);
DOC(glTexCoordPointeriEXT, "glTexCoordPointeriEXT(pointer[][]) -> None")

%name(glTexCoordPointerfEXT) void _glTexCoordPointerEXT(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLsizei d_3_0, GLfloat* pointer);
DOC(glTexCoordPointerfEXT, "glTexCoordPointerfEXT(pointer[][]) -> None")

%name(glTexCoordPointerdEXT) void _glTexCoordPointerEXT(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLsizei d_3_0, GLdouble* pointer);
DOC(glTexCoordPointerdEXT, "glTexCoordPointerdEXT(pointer[][]) -> None")


/*void glVertexPointerEXT (GLint size, GLenum type, GLsizei stride, GLsizei count, const GLvoid *pointer); */
%{
void _glVertexPointerEXT(GLint size, GLenum type, GLsizei stride, GLsizei count, GLvoid *pointer)
{
	decrementPointerLock(GL_VERTEX_ARRAY_POINTER_EXT);
	acquire(pointer);
	glVertexPointerEXT(size, type, stride, count, pointer);
}
%}

%name(glVertexPointerEXT) void _glVertexPointerEXT(GLint size, GLenum type, GLsizei stride, GLsizei count, void *pointer);
DOC(glVertexPointerEXT, "glVertexPointerEXT(size, type, stride, count, pointer) -> None")

%name(glVertexPointerbEXT) void _glVertexPointerEXT(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLsizei d_3_0, GLbyte* pointer);
DOC(glVertexPointerbEXT, "glVertexPointerubEXT(pointer[][]) -> None")

%name(glVertexPointersEXT) void _glVertexPointerEXT(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLsizei d_3_0, GLshort* pointer);
DOC(glVertexPointersEXT, "glVertexPointersEXT(pointer[][]) -> None")

%name(glVertexPointeriEXT) void _glVertexPointerEXT(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLsizei d_3_0, GLint* pointer);
DOC(glVertexPointeriEXT, "glVertexPointeriEXT(pointer[][]) -> None")

%name(glVertexPointerfEXT) void _glVertexPointerEXT(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLsizei d_3_0, GLfloat* pointer);
DOC(glVertexPointerfEXT, "glVertexPointerfEXT(pointer[][]) -> None")

%name(glVertexPointerdEXT) void _glVertexPointerEXT(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLsizei d_3_0, GLdouble* pointer);
DOC(glVertexPointerdEXT, "glVertexPointerdEXT(pointer[][]) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_vertex_array)
	"glArrayElementEXT",
	"glColorPointerEXT",
	"glDrawArraysEXT",
	"glEdgeFlagPointerEXT",
	"glIndexPointerEXT",
	"glNormalPointerEXT",
	"glTexCoordPointerEXT",
	"glVertexPointerEXT",
#endif
	NULL
};

#define glInitVertexArrayEXT() InitExtension("GL_EXT_vertex_array", proc_names)
%}

int glInitVertexArrayEXT();
DOC(glInitVertexArrayEXT, "glInitVertexArrayEXT() -> bool")



%{
PyObject *__info()
{
	if (glInitVertexArrayEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_VERTEX_ARRAY_EXT               0x8074
#define GL_NORMAL_ARRAY_EXT               0x8075
#define GL_COLOR_ARRAY_EXT                0x8076
#define GL_INDEX_ARRAY_EXT                0x8077
#define GL_TEXTURE_COORD_ARRAY_EXT        0x8078
#define GL_EDGE_FLAG_ARRAY_EXT            0x8079

#define GL_DOUBLE_EXT                     0x140A

#define GL_VERTEX_ARRAY_SIZE_EXT          0x807A
#define GL_VERTEX_ARRAY_TYPE_EXT          0x807B
#define GL_VERTEX_ARRAY_STRIDE_EXT        0x807C
#define GL_VERTEX_ARRAY_COUNT_EXT         0x807D
#define GL_NORMAL_ARRAY_TYPE_EXT          0x807E
#define GL_NORMAL_ARRAY_STRIDE_EXT        0x807F
#define GL_NORMAL_ARRAY_COUNT_EXT         0x8080
#define GL_COLOR_ARRAY_SIZE_EXT           0x8081
#define GL_COLOR_ARRAY_TYPE_EXT           0x8082
#define GL_COLOR_ARRAY_STRIDE_EXT         0x8083
#define GL_COLOR_ARRAY_COUNT_EXT          0x8084
#define GL_INDEX_ARRAY_TYPE_EXT           0x8085
#define GL_INDEX_ARRAY_STRIDE_EXT         0x8086
#define GL_INDEX_ARRAY_COUNT_EXT          0x8087
#define GL_TEXTURE_COORD_ARRAY_SIZE_EXT   0x8088
#define GL_TEXTURE_COORD_ARRAY_TYPE_EXT   0x8089
#define GL_TEXTURE_COORD_ARRAY_STRIDE_EXT 0x808A
#define GL_TEXTURE_COORD_ARRAY_COUNT_EXT  0x808B
#define GL_EDGE_FLAG_ARRAY_STRIDE_EXT     0x808C
#define GL_EDGE_FLAG_ARRAY_COUNT_EXT      0x808D

#define GL_VERTEX_ARRAY_POINTER_EXT       0x808E
#define GL_NORMAL_ARRAY_POINTER_EXT       0x808F
#define GL_COLOR_ARRAY_POINTER_EXT        0x8090
#define GL_INDEX_ARRAY_POINTER_EXT        0x8091
#define GL_TEXTURE_COORD_ARRAY_POINTER_EXT 0x8092
#define GL_EDGE_FLAG_ARRAY_POINTER_EXT    0x8093

