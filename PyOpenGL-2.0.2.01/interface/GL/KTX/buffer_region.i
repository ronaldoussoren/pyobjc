/*
# BUILD api_versions [0x100]
*/

%module buffer_region

#define __version__ "$Revision: 1.29.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057www.autodesk.com\057develop\057devres\057heidi\057oglspecs.htm"

%{
/**
 *
 * GL.KTX.buffer_region Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_KTX_buffer_region)
DECLARE_EXT(glBufferRegionEnabled, GLuint, -1, (), ())
DECLARE_EXT(glNewBufferRegion, GLuint, -1, (GLenum type), (type))
DECLARE_VOID_EXT(glDeleteBufferRegion, (GLuint region), (region))
DECLARE_VOID_EXT(glReadBufferRegion, (GLuint region, GLint x, GLint y, GLsizei width, GLsizei height), (region, x, y, width, height))
DECLARE_VOID_EXT(glDrawBufferRegion, (GLuint region, GLint x, GLint y, GLsizei width, GLsizei height, GLint xDest, GLint yDest), (region, x, y, width, height, xDest, yDest))
#endif
%}

GLuint glBufferRegionEnabled();
DOC(glBufferRegionEnabled, "glBufferRegionEnabled() -> bool")

GLuint glNewBufferRegion(GLenum type);
DOC(glNewBufferRegion, "glNewBufferRegion(type) -> handle")

void glDeleteBufferRegion(GLuint region);
DOC(glDeleteBufferRegion, "glDeleteBufferRegion(region) -> None")

void glReadBufferRegion(GLuint region, GLint x, GLint y, GLsizei width, GLsizei height);
DOC(glReadBufferRegion, "glReadBufferRegion(region, x, y, width, height) -> None")

void glDrawBufferRegion(GLuint region, GLint x, GLint y, GLsizei width, GLsizei height, GLint xDest, GLint yDest);
DOC(glDrawBufferRegion, "glDrawBufferRegion(region, x, y, width, height, xDest, yDest) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_KTX_buffer_region)
	"glBufferRegionEnabled",
	"glNewBufferRegion",
	"glDeleteBufferRegion",
	"glReadBufferRegion",
	"glDrawBufferRegion",
#endif
	NULL
};

#define glInitBufferRegionKTX() InitExtension("GL_KTX_buffer_region", proc_names)
%}

int glInitBufferRegionKTX();
DOC(glInitBufferRegionKTX, "glInitBufferRegionKTX() -> bool")


%{
PyObject *__info()
{
	if (glInitBufferRegionKTX())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_KTX_FRONT_REGION 0x0000
#define GL_KTX_BACK_REGION 0x0001
#define GL_KTX_Z_REGION 0x0002
#define GL_KTX_STENCIL_REGION 0x0003
