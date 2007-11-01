/*
# BUILD api_versions [0x100]
*/

%module vertex_blend

#define __version__ "$Revision: 1.31.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:06 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057ARB\057vertex_blend.txt"

%{
/**
 *
 * GL.ARB.vertex_blend Module for PyOpenGL
 * 
 * Date May 2001
 *
 * Authors Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include py_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_vertex_blend)
DECLARE_VOID_EXT(glWeightbvARB, (GLint size, const GLbyte* weights), (size, weights))
DECLARE_VOID_EXT(glWeightubvARB, (GLint size, const GLubyte* weights), (size, weights))
DECLARE_VOID_EXT(glWeightsvARB, (GLint size, const GLshort* weights), (size, weights))
DECLARE_VOID_EXT(glWeightusvARB, (GLint size, const GLushort* weights), (size, weights))
DECLARE_VOID_EXT(glWeightivARB, (GLint size, const GLint* weights), (size, weights))
DECLARE_VOID_EXT(glWeightuivARB, (GLint size, const GLuint* weights), (size, weights))
DECLARE_VOID_EXT(glWeightfvARB, (GLint size, const GLfloat* weights), (size, weights))
DECLARE_VOID_EXT(glWeightdvARB, (GLint size, const GLdouble* weights), (size, weights))
DECLARE_VOID_EXT(glWeightPointerARB, (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer), (size, type, stride, pointer))
DECLARE_VOID_EXT(glWeightBlendARB, (GLint count), (count))
#endif

static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ARB_vertex_blend)
	"glSampleCoverageARB",
	"glWeightbvARB",
	"glWeightubvARB",
	"glWeightsvARB",
	"glWeightusvARB",
	"glWeightivARB",
	"glWeightuivARB",
	"glWeightfvARB",
	"glWeightdvARB",
	"glWeightPointerARB",
	"glWeightBlendARB",
#endif
	NULL
};

#define glInitVertexBlendARB() InitExtension("GL_ARB_vertex_blend", proc_names)
%}

int glInitVertexBlendARB();
DOC(glInitVertexBlendARB, "glInitVertexBlendARB() -> bool")


void glWeightbvARB(GLint n_1, const GLbyte* weights);
DOC(glWeightbvARB, "glWeightbvARB(weights) -> None")

void glWeightubvARB(GLint n_1, const GLubyte* weights);
DOC(glWeightubvARB, "glWeightubvARB(weights) -> None")

void glWeightsvARB(GLint n_1, const GLshort* weights);
DOC(glWeightsvARB, "glWeightsvARB(weights) -> None")

void glWeightusvARB(GLint n_1, const GLushort* weights);
DOC(glWeightusvARB, "glWeightusvARB(weights) -> None")

void glWeightivARB(GLint n_1, const GLint* weights);
DOC(glWeightivARB, "glWeightivARB(weights) -> None")

void glWeightuivARB(GLint n_1, const GLuint* weights);
DOC(glWeightuivARB, "glWeightuivARB(weights) -> None")

void glWeightfvARB(GLint n_1, const GLfloat* weights);
DOC(glWeightfvARB, "glWeightfvARB(weights) -> None")

void glWeightdvARB(GLint n_1, const GLdouble* weights);
DOC(glWeightdvARB, "glWeightdvARB(weights) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc


/*void glWeightPointerARB (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer); */

%{
#ifndef GL_WEIGHT_ARRAY_POINTER_ARB
#define GL_WEIGHT_ARRAY_POINTER_ARB 0x86AC
#endif

void _glWeightPointerARB(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_WEIGHT_ARRAY_POINTER_ARB);
	acquire(pointer);
	glWeightPointerARB(size, type, stride, pointer);
}
%}

%name(glWeightPointerARB) void _glWeightPointerARB(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glWeightPointerARB, "glWeightPointerARB(size, type, stride, pointer) -> None")

%name(glWeightPointerubARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_UNSIGNED_BYTE, GLsizei stride_0, GLubyte* pointer);
DOC(glWeightPointerubARB, "glWeightPointerubARB(pointer) -> None")

%name(glWeightPointerbARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glWeightPointerbARB, "glWeightPointerubARB(pointer) -> None")

%name(glWeightPointerusARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_UNSIGNED_SHORT, GLsizei stride_0, GLushort* pointer);
DOC(glWeightPointerusARB, "glWeightPointerusARB(pointer) -> None")

%name(glWeightPointersARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glWeightPointersARB, "glWeightPointersARB(pointer) -> None")

%name(glWeightPointeruiARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_UNSIGNED_INT, GLsizei stride_0, GLuint* pointer);
DOC(glWeightPointeruiARB, "glWeightPointeruiARB(pointer) -> None")

%name(glWeightPointeriARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glWeightPointeriARB, "glWeightPointeriARB(pointer) -> None")

%name(glWeightPointerfARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glWeightPointerfARB, "glWeightPointerfARB(pointer) -> None")

%name(glWeightPointerdARB) void _glWeightPointerARB(GLint d_3_1, GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glWeightPointerdARB, "glWeightPointerdARB(pointer) -> None")


void glWeightBlendARB(GLint count);
DOC(glWeightBlendARB, "glWeightBlendARB(count) -> None")

%{
#ifndef GL_ARB_vertex_blend
#define GL_MAX_VERTEX_UNITS_ARB          0x86A4
#endif


PyObject *__info()
{
	if (glInitVertexBlendARB())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_VERTEX_UNITS_ARB", GL_MAX_VERTEX_UNITS_ARB, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_MAX_VERTEX_UNITS_ARB 0x86A4
#define GL_ACTIVE_VERTEX_UNITS_ARB 0x86A5

#define GL_WEIGHT_SUM_UNITY_ARB 0x86A6
#define GL_VERTEX_BLEND_ARB 0x86A7

#define GL_MODELVIEW0_ARB 0x1700
#define GL_MODELVIEW1_ARB 0x850a
#define GL_MODELVIEW2_ARB 0x8722
#define GL_MODELVIEW3_ARB 0x8723
#define GL_MODELVIEW4_ARB 0x8724
#define GL_MODELVIEW5_ARB 0x8725
#define GL_MODELVIEW6_ARB 0x8726
#define GL_MODELVIEW7_ARB 0x8727
#define GL_MODELVIEW8_ARB 0x8728
#define GL_MODELVIEW9_ARB 0x8729
#define GL_MODELVIEW10_ARB 0x872A
#define GL_MODELVIEW11_ARB 0x872B
#define GL_MODELVIEW12_ARB 0x872C
#define GL_MODELVIEW13_ARB 0x872D
#define GL_MODELVIEW14_ARB 0x872E
#define GL_MODELVIEW15_ARB 0x872F
#define GL_MODELVIEW16_ARB 0x8730
#define GL_MODELVIEW17_ARB 0x8731
#define GL_MODELVIEW18_ARB 0x8732
#define GL_MODELVIEW19_ARB 0x8733
#define GL_MODELVIEW20_ARB 0x8734
#define GL_MODELVIEW21_ARB 0x8735
#define GL_MODELVIEW22_ARB 0x8736
#define GL_MODELVIEW23_ARB 0x8737
#define GL_MODELVIEW24_ARB 0x8738
#define GL_MODELVIEW25_ARB 0x8739
#define GL_MODELVIEW26_ARB 0x873A
#define GL_MODELVIEW27_ARB 0x873B
#define GL_MODELVIEW28_ARB 0x873C
#define GL_MODELVIEW29_ARB 0x873D
#define GL_MODELVIEW30_ARB 0x873E
#define GL_MODELVIEW31_ARB 0x873F
 
#define GL_CURRENT_WEIGHT_ARB 0x86A8 
 
#define GL_WEIGHT_ARRAY_TYPE_ARB 0x86A9
#define GL_WEIGHT_ARRAY_STRIDE_ARB 0x86AA
#define GL_WEIGHT_ARRAY_SIZE_ARB 0x86AB

#define GL_WEIGHT_ARRAY_POINTER_ARB 0x86AC

#define GL_WEIGHT_ARRAY_ARB 0x86AD
