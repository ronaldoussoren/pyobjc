/*
# BUILD api_versions [0x100]
*/

%module vertex_array_object

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:50 $"
#define __api_version__ API_VERSION
#define __author__ "Mike C. Fletcher <mcfletch@users.sourceforge.net>"
#define __doc__ "Server-side Vertex Arrays and Storage Buffers\n\
\n\
    This extension defines an interface that allows multiple sets of\n\
    vertex array data to be cached in persistent server-side memory.\n\
    It is intended to allow client data to be stored in memory that\n\
    can be directly accessed by graphics hardware.\n\
\n\
	XXX Needs more error-checking and validation code!\n\
\n\
http:\057\057oss.sgi.com/projects/ogl-sample/registry/ATI/vertex_array_object.txt"

%{
/**
 *
 * GL.ATI.vertex_array_object Module for PyOpenGL
 * 
 * Date: September 2001
 *
 * Authors: Mike C. Fletcher <mcfletch@users.sourceforge.net>
 * 
***/
%}

%include util.inc
%include typemaps.i

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_ATI_vertex_array_object)

DECLARE_EXT( glNewObjectBufferATI, GLuint, 0, (GLsizei size, const GLvoid * pointer, GLenum usage), (size, pointer, usage ));
DECLARE_EXT( glIsObjectBufferATI, GLboolean, GL_FALSE, (GLuint buffer), (buffer));
DECLARE_VOID_EXT(glUpdateObjectBufferATI, (GLuint buffer, GLuint offset, GLsizei size, const GLvoid * pointer, GLenum preserve), (buffer, offset, size, pointer, preserve));
DECLARE_VOID_EXT(glGetObjectBufferfvATI, (GLuint buffer, GLenum pname, GLfloat * params), (buffer, pname, params));
DECLARE_VOID_EXT(glGetObjectBufferivATI, (GLuint buffer, GLenum pname, GLint * params), (buffer, pname, params));
DECLARE_VOID_EXT(glDeleteObjectBufferATI, (GLuint buffer), (buffer));
DECLARE_VOID_EXT(glArrayObjectATI, (GLenum array, GLint size, GLenum type, GLsizei stride, GLuint buffer, GLuint offset), (array, size, type, stride, buffer, offset));
DECLARE_VOID_EXT(glGetArrayObjectfvATI, (GLenum array, GLenum pname, GLfloat * params), (array, pname, params));
DECLARE_VOID_EXT(glGetArrayObjectivATI, (GLenum array, GLenum pname, GLint * params), (array, pname, params));

#ifdef GL_EXT_vertex_shader
/* XXX I don't have this extension, so haven't checked that anything works */
DECLARE_VOID_EXT(glVariantArrayObjectATI, (GLuint id, GLenum type, GLsizei stride, GLuint buffer, GLuint offset), (id,type, stride, buffer, offset));
DECLARE_VOID_EXT(glGetVariantArrayObjectfvATI, (GLuint id, GLenum pname, GLfloat * params), (id, pname, params));
DECLARE_VOID_EXT(glGetVariantArrayObjectivATI, (GLuint id, GLenum pname, GLint * params), (id, pname, params));
#endif GL_EXT_vertex_shader

#endif /* EXT_DEFINES_PROTO */

/* need a function to convert Python sequences to raw void * values */


%}

%typemap (python, in) const GLvoid * pointer {
	if ($input == Py_None) {
		/* XXX should disallow this for update object buffer */
		$1 = NULL;
	} else if (PyString_Check($input)) {
		/* strings are easy, just pass the data straight in */
		$1 = (void *)PyString_AsString( $input );
		/* XXX should check length here against arg0 to avoid mem-access errors */
	} else {
		PyErr_SetGLErrorMessage( GL_INVALID_VALUE, "Currently only support strings for vertex_array_object data sources");
		return NULL;
	}
}

GLuint glNewObjectBufferATI(GLsizei size, const GLvoid * pointer, GLenum usage);
DOC( glNewObjectBufferATI, "glNewObjectBufferATI(size, pointer, usage ) -> buffername\n\
\n\
	size -- minimum size of the buffer, implementation may\n\
		use a larger buffer, but not smaller.\n\
	pointer -- data with which to initialise the buffer.  May be\n\
		a string, or None to avoid initialisation of the buffer.\n\
	usage -- (enumeration) GL_STATIC_ATI or GL_DYNAMIC_ATI, \n\
		indicating to the system whether this data is likely to\n\
		be updated or not (i.e. an optimisation hint)\n\
	\n\
	returns the unsigned integer 'name' of the buffer which\n\
	must be used to refer to the buffer for all calls.");

GLboolean glIsObjectBufferATI(GLuint buffer);
DOC( glIsObjectBufferATI, "glIsObjectBufferATI( buffer ) -> bool\n\
\n\
	buffer -- buffer 'name' (an unsigned integer) being referenced\n\
		(returned by glNewObjectBufferATI)\n\
	\n\
	returns boolean indicating whether given integer specifies a\n\
	valid server-side buffer.");

void glUpdateObjectBufferATI(GLuint buffer, GLuint offset, GLsizei size, const GLvoid * pointer, GLenum preserve);
DOC( glUpdateObjectBufferATI, "glUpdateObjectBufferATI(buffer, offset, size, pointer, preserve) -> None\n\
\n\
	buffer -- buffer 'name' (an unsigned integer) being referenced\n\
		(returned by glNewObjectBufferATI)\n\
	offset -- (integer) offset into the buffer at which to begin copying\n\
	size -- amount of data to copy\n\
	pointer -- string from which to copy the data" )


void glGetObjectBufferfvATI(GLuint buffer, GLenum pname, GLfloat * OUTPUT);
DOC( glGetObjectBufferfvATI, "glGetObjectBufferfvATI(buffer, pname) -> float\n\
\n\
	buffer -- buffer 'name' (an unsigned integer) being referenced\n\
		(returned by glNewObjectBufferATI)\n\
	pname -- (enumeration) GL_OBJECT_BUFFER_SIZE_ATI or GL_OBJECT_BUFFER_USAGE_ATI\n\
		what property of the buffer to query\n\
\n\
	for GL_OBJECT_BUFFER_SIZE_ATI returns size of the server-\n\
		side buffer, which is at least the size of the size argument to\n\
		glNewObjectBufferATI, and will likely be larger.\n\
	for GL_OBJECT_BUFFER_USAGE_ATI returns either GL_STATIC_ATI or\n\
		GL_DYNAMIC_ATI" )

void glGetObjectBufferivATI(GLuint buffer, GLenum pname, GLint * OUTPUT);
DOC( glGetObjectBufferivATI, "glGetObjectBufferivATI(buffer, pname) -> int\n\
\n\
	buffer -- buffer 'name' (an unsigned integer) being referenced\n\
		(returned by glNewObjectBufferATI)\n\
	pname -- (enumeration) GL_OBJECT_BUFFER_SIZE_ATI or GL_OBJECT_BUFFER_USAGE_ATI\n\
		what property of the buffer to query\n\
\n\
	for GL_OBJECT_BUFFER_SIZE_ATI returns size of the server-\n\
		side buffer, which is at least the size of the size argument to\n\
		glNewObjectBufferATI, and will likely be larger.\n\
	for GL_OBJECT_BUFFER_USAGE_ATI returns either GL_STATIC_ATI or\n\
		GL_DYNAMIC_ATI" )

void glDeleteObjectBufferATI(GLuint buffer);
DOC( glDeleteObjectBufferATI, "glDeleteObjectBufferATI(buffer) -> None\n\
\n\
	buffer -- buffer 'name' (an unsigned integer) being referenced\n\
		(returned by glNewObjectBufferATI)\n\
	\n\
	Deallocates the server-side buffer" )

void glArrayObjectATI(GLenum array, GLint size, GLenum type, GLsizei stride, GLuint buffer, GLuint offset);
DOC( glArrayObjectATI, "glArrayObjectATI(array, size, type, stride, buffer, offset) -> None\n\
\n\
	array -- the drawing array-type to enable, acceptable values are\n\
		those seen in glEnableClientState: GL_COLOR_ARRAY, \n\
		GL_VERTEX_ARRAY, GL_NORMAL_ARRAY, etceteras\n\
	size -- number of elements to read from buffer into array, note\n\
		that these are in array-type units, not generally bytes, as\n\
		used to specify the size of the underlying buffer!\n\
	type -- base data-types to read from the buffer, GL_FLOAT, \n\
		GL_DOUBLE, GL_INT, etceteras\n\
	stride -- as seen in all vertex-array definition calls\n\
	buffer -- buffer 'name' (an unsigned integer) being referenced\n\
		as the source for the data in the array.\n\
	offset -- offset from the start of the buffer at which to begin\n\
		reading (in bytes)\n\
\n\
	Defines an array-drawing array using data from a server-side\n\
	buffer.\n\
\n\
	See:\n\
		glVertexArray,glColorArray,glNormalArray" )

void glGetArrayObjectfvATI(GLenum array, GLenum pname, GLfloat * OUTPUT);
DOC( glGetArrayObjectfvATI, "glGetArrayObjectfvATI(array, pname) -> float\n\
\n\
	array -- the drawing array-type to query, acceptable values are\n\
		those seen in glEnableClientState: GL_COLOR_ARRAY, \n\
		GL_VERTEX_ARRAY, GL_NORMAL_ARRAY, etceteras\n\
	pname -- (enumeration) ARRAY_OBJECT_BUFFER_ATI, or \n\
		ARRAY_OBJECT_OFFSET_ATI\n\
\n\
	for ARRAY_OBJECT_BUFFER_ATI, returns the buffer name of the buffer\n\
	bound to the given array\n\
\n\
	for ARRAY_OBJECT_OFFSET_ATI, returns the offset in bytes from the\n\
	start of the buffer at which the array begins reading data." )

void glGetArrayObjectivATI(GLenum array, GLenum pname, GLint * OUTPUT);
DOC( glGetArrayObjectivATI, "glGetArrayObjectivATI(array, pname) -> integer\n\
\n\
	array -- the drawing array-type to query, acceptable values are\n\
		those seen in glEnableClientState: GL_COLOR_ARRAY, \n\
		GL_VERTEX_ARRAY, GL_NORMAL_ARRAY, etceteras\n\
	pname -- (enumeration) ARRAY_OBJECT_BUFFER_ATI, or \n\
		ARRAY_OBJECT_OFFSET_ATI\n\
\n\
	for ARRAY_OBJECT_BUFFER_ATI, returns the buffer name of the buffer\n\
	bound to the given array\n\
\n\
	for ARRAY_OBJECT_OFFSET_ATI, returns the offset in bytes from the\n\
	start of the buffer at which the array begins reading data." )

#ifdef GL_EXT_vertex_shader
void glVariantArrayObjectATI(GLuint id, GLenum type, GLsizei stride, GLuint buffer, GLuint offset);
DOC( glVariantArrayObjectATI, "glVariantArrayObjectATI(id,type, stride, buffer, offset) -> None" )

void glGetVariantArrayObjectfvATI(GLuint id, GLenum pname, GLfloat * OUTPUT);
DOC( glGetVariantArrayObjectfvATI, "glGetVariantArrayObjectfvATI(id, pname) -> float" )

void glGetVariantArrayObjectivATI(GLuint id, GLenum pname, GLint * OUTPUT);
DOC( glGetVariantArrayObjectivATI, "glGetVariantArrayObjectivATI(id, pname) -> integer" )
#endif

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ATI_vertex_array_object)
	"glNewObjectBufferATI",
	"glIsObjectBufferATI",
	"glUpdateObjectBufferATI",
	"glGetObjectBufferfvATI",
	"glGetObjectBufferivATI",
	"glDeleteObjectBufferATI",
	"glArrayObjectATI",
	"glGetArrayObjectfvATI",
	"glGetArrayObjectivATI",
#ifdef GL_EXT_vertex_shader
	"glVariantArrayObjectATI",
	"glGetVariantArrayObjectfvATI",
	"glGetVariantArrayObjectivATI",
#endif
#endif
	NULL
};

#define glInitVertexArrayObjectATI() InitExtension("GL_ATI_vertex_array_object", proc_names)
%}

int glInitVertexArrayObjectATI();
DOC(glInitVertexArrayObjectATI, "glInitVertexArrayObjectATI() -> bool")

/* Accepted by the <usage> parameter of NewObjectBufferATI:*/

#ifndef GL_ATI_vertex_array_object
#define GL_STATIC_ATI                      0x8760
#define GL_DYNAMIC_ATI                     0x8761

/* Accepted by the <preserve> parameter of UpdateObjectBufferATI: */

#define GL_PRESERVE_ATI                    0x8762
#define GL_DISCARD_ATI                     0x8763

/*    Accepted by the <pname> parameter of GetObjectBufferivATI and
    GetObjectBufferfvATI: */

#define GL_OBJECT_BUFFER_SIZE_ATI          0x8764
#define GL_OBJECT_BUFFER_USAGE_ATI         0x8765

/*    Accepted by the <pname> parameter of GetArrayObjectivATI and
    GetArrayObjectfvATI: */

#define GL_ARRAY_OBJECT_BUFFER_ATI         0x8766
#define GL_ARRAY_OBJECT_OFFSET_ATI         0x8767

#endif


%{
PyObject *__info()
{
	if (glInitVertexArrayObjectATI())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

