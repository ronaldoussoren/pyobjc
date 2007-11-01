/*
# BUILD api_versions [0x100]
*/

%module pn_triangles

#define __version__ "$Revision: 1.1.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com/projects/ogl-sample/registry/ATI/pn_triangles.txt"

%{
/**
 *
 * GL.ATI.pn_triangles Module for PyOpenGL
 * 
 * Date: September 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc

%{
#ifndef GL_ATI_pn_triangles
#define GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI   0x87F1

#define GL_PN_TRIANGLES_POINT_MODE_ATI              0x87F2
#define GL_PN_TRIANGLES_NORMAL_MODE_ATI             0x87F3
#define GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI       0x87F4

#define GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI       0x87F5
#define GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI        0x87F6

#define GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI      0x87F7
#define GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI   0x87F8
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_ATI_pn_triangles)
DECLARE_VOID_EXT(glPNTrianglesiATI,\
	(GLenum pname, GLint param),\
	(pname, param))
DECLARE_VOID_EXT(glPNTrianglesfATI,\
	(GLenum pname, GLfloat param),\
	(pname, param))
#endif
%}

void glPNTrianglesiATI(GLenum pname, GLint param);
DOC(glPNTrianglesiATI, "glPNTrianglesiATI(pname, param) -> None")

void glPNTrianglesfATI(GLenum pname, GLfloat param);
DOC(glPNTrianglesfATI, "glPNTrianglesfATI(pname, param) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_ATI_pn_triangles)
	"glPNTrianglesiATI",
	"glPNTrianglesfATI",
#endif
	NULL
};

#define glInitPNTrianglesATI() InitExtension("GL_ATI_pn_triangles", proc_names)
%}

int glInitPNTrianglesATI();
DOC(glInitPNTrianglesATI, "glInitPNTrianglesATI() -> bool")

%{
PyObject *__info()
{
	if (glInitPNTrianglesATI())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI", GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI   0x87F1

#define GL_PN_TRIANGLES_POINT_MODE_ATI              0x87F2
#define GL_PN_TRIANGLES_NORMAL_MODE_ATI             0x87F3
#define GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI       0x87F4

#define GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI       0x87F5
#define GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI        0x87F6

#define GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI      0x87F7
#define GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI   0x87F8
