/*
# BUILD api_versions [0x100]
*/

%module vertex_weighting

#define __version__ "$Revision: 1.22.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057vertex_weighting.txt"

%{
/**
 *
 * GL.EXT.vertex_weighting Module for PyOpenGL
 * 
 * Date May 2001
 *
 * Authors Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc


/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_vertex_weighting)
DECLARE_VOID_EXT(glVertexWeightfvEXT, (const GLfloat* weights), (weights))
DECLARE_VOID_EXT(glVertexWeightfEXT, (GLfloat weight), (weight))
DECLARE_VOID_EXT(glVertexWeightPointerEXT, (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer), (size, type, stride, pointer))
#endif
%}

void glVertexWeightfvEXT(const GLfloat* weights);
DOC(glVertexWeightfvEXT, "glVertexWeightfvEXT(weights) -> None")

void glVertexWeightfEXT(GLfloat weight);
DOC(glVertexWeightfEXT, "glVertexWeightfEXT(weight) -> None")


/*void glVertexWeightPointerEXT (GLint size, GLenum type, GLsizei stride, const GLvoid *pointer); */
%{
#ifndef GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT
#define GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT 0x8510
#endif

void _glVertexWeightPointerEXT(GLint size, GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT);
	acquire(pointer);
	glVertexWeightPointerEXT(size, type, stride, pointer);
}
%}

%name(glVertexWeightPointerEXT) void _glVertexWeightPointerEXT(GLint size, GLenum type, GLsizei stride, void *pointer);
DOC(glVertexWeightPointerEXT, "glVertexWeightPointerEXT(size, type, stride, pointer) -> None")

%name(glVertexWeightPointerfEXT) void _glVertexWeightPointerEXT(GLint d_3_1, GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glVertexWeightPointerfEXT, "glVertexWeightPointerfEXT(pointer) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_vertex_weighting)
	"glVertexWeightfvEXT",
	"glVertexWeightfEXT",
	"glVertexWeightPointerEXT",
#endif
	NULL
};

#define glInitVertexWeightingEXT() InitExtension("GL_EXT_vertex_weighting", proc_names)
%}

int glInitVertexWeightingEXT();
DOC(glInitVertexWeightingEXT, "glInitVertexWeightingEXT() -> bool")



%{
PyObject *__info()
{
	if (glInitVertexWeightingEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_VERTEX_WEIGHTING_EXT                0x8509

#define GL_MODELVIEW0_EXT                      0x1700  /* alias to MODELVIEW enumerant */
#define GL_MODELVIEW1_EXT                      0x850a

#define GL_CURRENT_VERTEX_WEIGHT_EXT           0x850b
#define GL_VERTEX_WEIGHT_ARRAY_EXT             0x850c
#define GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT        0x850d
#define GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT        0x850e
#define GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT      0x850f
#define GL_MODELVIEW0_STACK_DEPTH_EXT          0x0BA3  /* alias to MODELVIEW_STACK_DEPTH */
#define GL_MODELVIEW1_STACK_DEPTH_EXT          0x8502

#define GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT     0x8510
