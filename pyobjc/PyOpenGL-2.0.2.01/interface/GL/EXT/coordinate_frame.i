/*
# BUILD api_versions [0x103]
*/

%module coordinate_frame

#define __version__ "$Revision: 1.22.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057coordinate_frame.txt"

%{
/**
 *
 * GL.EXT.coordinate_frame Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_coordinate_frame)
DECLARE_VOID_EXT(glTangent3bEXT, (GLbyte x, GLbyte y, GLbyte z), (x, y, z))
DECLARE_VOID_EXT(glTangent3sEXT, (GLshort x, GLshort y, GLshort z), (x, y, z))
DECLARE_VOID_EXT(glTangent3iEXT, (GLint x, GLint y, GLint z), (x, y, z))
DECLARE_VOID_EXT(glTangent3fEXT, (GLfloat x, GLfloat y, GLfloat z), (x, y, z))
DECLARE_VOID_EXT(glTangent3dEXT, (GLdouble x, GLdouble y, GLdouble z), (x, y, z))
DECLARE_VOID_EXT(glTangent3bvEXT, (const GLbyte* coord), (coord))
DECLARE_VOID_EXT(glTangent3svEXT, (const GLshort* coord), (coord))
DECLARE_VOID_EXT(glTangent3ivEXT, (const GLint* coord), (coord))
DECLARE_VOID_EXT(glTangent3fvEXT, (const GLfloat* coord), (coord))
DECLARE_VOID_EXT(glTangent3dvEXT, (const GLdouble* coord), (coord))
DECLARE_VOID_EXT(glBinomial3bEXT, (GLbyte x, GLbyte y, GLbyte z), (x, y, z))
DECLARE_VOID_EXT(glBinomial3sEXT, (GLshort x, GLshort y, GLshort z), (x, y, z))
DECLARE_VOID_EXT(glBinomial3iEXT, (GLint x, GLint y, GLint z), (x, y, z))
DECLARE_VOID_EXT(glBinomial3fEXT, (GLfloat x, GLfloat y, GLfloat z), (x, y, z))
DECLARE_VOID_EXT(glBinomial3dEXT, (GLdouble x, GLdouble y, GLdouble z), (x, y, z))
DECLARE_VOID_EXT(glBinomial3bvEXT, (const GLbyte* coord), (coord))
DECLARE_VOID_EXT(glBinomial3svEXT, (const GLshort* coord), (coord))
DECLARE_VOID_EXT(glBinomial3ivEXT, (const GLint* coord), (coord))
DECLARE_VOID_EXT(glBinomial3fvEXT, (const GLfloat* coord), (coord))
DECLARE_VOID_EXT(glBinomial3dvEXT, (const GLdouble* coord), (coord))
DECLARE_VOID_EXT(glTangentPointerEXT, (GLenum type, GLsizei stride, const GLvoid *pointer), (type, stride, pointer))
DECLARE_VOID_EXT(glBinomialPointerEXT, (GLenum type, GLsizei stride, const GLvoid *pointer), (type, stride, pointer))
#endif
%}

void glTangent3bEXT(GLbyte x, GLbyte y, GLbyte z);
DOC(glTangent3bEXT, "glTangent3bEXT(x, y, z) -> None")

void glTangent3sEXT(GLshort x, GLshort y, GLshort z);
DOC(glTangent3sEXT, "glTangent3sEXT(x, y, z) -> None")

void glTangent3iEXT(GLint x, GLint y, GLint z);
DOC(glTangent3iEXT, "glTangent3iEXT(x, y, z) -> None")

void glTangent3fEXT(GLfloat x, GLfloat y, GLfloat z);
DOC(glTangent3fEXT, "glTangent3fEXT(x, y, z) -> None")

void glTangent3dEXT(GLdouble x, GLdouble y, GLdouble z);
DOC(glTangent3dEXT, "glTangent3dEXT(x, y, z) -> None")

void glTangent3bvEXT(const GLbyte* coord);
DOC(glTangent3bvEXT, "glTangent3bvEXT(coord) -> None")

void glTangent3svEXT(const GLshort* coord);
DOC(glTangent3svEXT, "glTangent3svEXT(coord) -> None")

void glTangent3ivEXT(const GLint* coord);
DOC(glTangent3ivEXT, "glTangent3ivEXT(coord) -> None")

void glTangent3fvEXT(const GLfloat* coord);
DOC(glTangent3fvEXT, "glTangent3fvEXT(coord) -> None")

void glTangent3dvEXT(const GLdouble* coord);
DOC(glTangent3dvEXT, "glTangent3dvEXT(coord) -> None")

/* glBinomial3 */
void glBinomial3bEXT(GLbyte x, GLbyte y, GLbyte z);
DOC(glBinomial3bEXT, "glBinomial3bEXT(x, y, z) -> None")

void glBinomial3sEXT(GLshort x, GLshort y, GLshort z);
DOC(glBinomial3sEXT, "glBinomial3sEXT(x, y, z) -> None")

void glBinomial3iEXT(GLint x, GLint y, GLint z);
DOC(glBinomial3iEXT, "glBinomial3iEXT(x, y, z) -> None")

void glBinomial3fEXT(GLfloat x, GLfloat y, GLfloat z);
DOC(glBinomial3fEXT, "glBinomial3fEXT(x, y, z) -> None")

void glBinomial3dEXT(GLdouble x, GLdouble y, GLdouble z);
DOC(glBinomial3dEXT, "glBinomial3dEXT(x, y, z) -> None")

void glBinomial3bvEXT(const GLbyte* coord);
DOC(glBinomial3bvEXT, "glBinomial3bvEXT(coord) -> None")

void glBinomial3svEXT(const GLshort* coord);
DOC(glBinomial3svEXT, "glBinomial3svEXT(coord) -> None")

void glBinomial3ivEXT(const GLint* coord);
DOC(glBinomial3ivEXT, "glBinomial3ivEXT(coord) -> None")

void glBinomial3fvEXT(const GLfloat* coord);
DOC(glBinomial3fvEXT, "glBinomial3fvEXT(coord) -> None")

void glBinomial3dvEXT(const GLdouble* coord);
DOC(glBinomial3dvEXT, "glBinomial3dvEXT(coord) -> None")


/* turn the exception handler on */
%include gl_exception_handler.inc

/*void glTangentPointerEXT (GLenum type, GLsizei stride, const GLvoid *pointer); */
%{
#ifndef GL_TANGENT_ARRAY_POINTER_EXT
#define GL_TANGENT_ARRAY_POINTER_EXT	0x8442
#endif

void _glTangentPointerEXT(GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_TANGENT_ARRAY_POINTER_EXT);
	acquire(pointer);
	glTangentPointerEXT(type, stride, pointer);
}
%}

%name(glTangentPointerEXT) void _glTangentPointerEXT(GLenum type, GLsizei stride, void *pointer);
DOC(glTangentPointerEXT, "glTangentPointerEXT(type, stride, pointer) -> None")

%name(glTangentPointerbEXT) void _glTangentPointerEXT(GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glTangentPointerbEXT, "glTangentPointerubEXT(pointer) -> None")

%name(glTangentPointersEXT) void _glTangentPointerEXT(GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glTangentPointersEXT, "glTangentPointersEXT(pointer) -> None")

%name(glTangentPointeriEXT) void _glTangentPointerEXT(GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glTangentPointeriEXT, "glTangentPointeriEXT(pointer) -> None")

%name(glTangentPointerfEXT) void _glTangentPointerEXT(GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glTangentPointerfEXT, "glTangentPointerfEXT(pointer) -> None")

%name(glTangentPointerdEXT) void _glTangentPointerEXT(GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glTangentPointerdEXT, "glTangentPointerdEXT(pointer) -> None")



/*void glBinomialPointerEXT (GLenum type, GLsizei stride, const GLvoid *pointer); */
%{
#ifndef GL_BINORMAL_ARRAY_POINTER_EXT
#define GL_BINORMAL_ARRAY_POINTER_EXT	0x8443
#endif

void _glBinomialPointerEXT(GLenum type, GLsizei stride, GLvoid *pointer)
{
	decrementPointerLock(GL_BINORMAL_ARRAY_POINTER_EXT);
	acquire(pointer);
	glBinomialPointerEXT(type, stride, pointer);
}
%}

%name(glBinomialPointerEXT) void _glBinomialPointerEXT(GLenum type, GLsizei stride, void *pointer);
DOC(glBinomialPointerEXT, "glBinomialPointerEXT(type, stride, pointer) -> None")

%name(glBinomialPointerbEXT) void _glBinomialPointerEXT(GLenum type_BYTE, GLsizei stride_0, GLbyte* pointer);
DOC(glBinomialPointerbEXT, "glBinomialPointerubEXT(pointer) -> None")

%name(glBinomialPointersEXT) void _glBinomialPointerEXT(GLenum type_SHORT, GLsizei stride_0, GLshort* pointer);
DOC(glBinomialPointersEXT, "glBinomialPointersEXT(pointer) -> None")

%name(glBinomialPointeriEXT) void _glBinomialPointerEXT(GLenum type_INT, GLsizei stride_0, GLint* pointer);
DOC(glBinomialPointeriEXT, "glBinomialPointeriEXT(pointer) -> None")

%name(glBinomialPointerfEXT) void _glBinomialPointerEXT(GLenum type_FLOAT, GLsizei stride_0, GLfloat* pointer);
DOC(glBinomialPointerfEXT, "glBinomialPointerfEXT(pointer) -> None")

%name(glBinomialPointerdEXT) void _glBinomialPointerEXT(GLenum type_DOUBLE, GLsizei stride_0, GLdouble* pointer);
DOC(glBinomialPointerdEXT, "glBinomialPointerdEXT(pointer) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(glInitCoordinateFrameEXT)
	"glTangent3bEXT",
	"glTangent3sEXT",
	"glTangent3iEXT",
	"glTangent3fEXT",
	"glTangent3dEXT",
	"glTangent3bvEXT",
	"glTangent3svEXT",
	"glTangent3ivEXT",
	"glTangent3fvEXT",
	"glTangent3dvEXT",
	"glBinomial3bEXT",
	"glBinomial3sEXT",
	"glBinomial3iEXT",
	"glBinomial3fEXT",
	"glBinomial3dEXT",
	"glBinomial3bvEXT",
	"glBinomial3svEXT",
	"glBinomial3ivEXT",
	"glBinomial3fvEXT",
	"glBinomial3dvEXT",
	"glTangentPointerEXT",
	"glBinomialPointerEXT",
#endif
	NULL
};

#define glInitCoordinateFrameEXT() InitExtension("GL_EXT_coordinate_frame", proc_names)
%}

int glInitCoordinateFrameEXT();
DOC(glInitCoordinateFrameEXT, "glInitCoordinateFrameEXT() -> bool")

%name(glInitCoordFrameEXT) int glInitCoordinateFrameEXT();
DOC(glInitCoordFrameEXT, "glInitCoordFrameEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitCoordinateFrameEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_TANGENT_ARRAY_EXT		0x8439
#define GL_BINORMAL_ARRAY_EXT		0x843A

#define GL_CURRENT_TANGENT_EXT		0x843B
#define GL_CURRENT_BINORMAL_EXT		0x843C
#define GL_TANGENT_ARRAY_TYPE_EXT		0x843E
#define GL_TANGENT_ARRAY_STRIDE_EXT	0x843F
#define GL_BINORMAL_ARRAY_TYPE_EXT		0x8440
#define GL_BINORMAL_ARRAY_STRIDE_EXT	0x8441

#define GL_MAP1_TANGENT_EXT		0x8444
#define GL_MAP2_TANGENT_EXT		0x8445
#define GL_MAP1_BINORMAL_EXT		0x8446
#define GL_MAP2_BINORMAL_EXT		0x8447

