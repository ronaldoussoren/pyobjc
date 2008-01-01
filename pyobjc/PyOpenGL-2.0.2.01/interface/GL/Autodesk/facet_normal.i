/*
# BUILD api_versions [0x100]
*/

%module facet_normal

#define __version__ "$Revision: 1.28.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057www.autodesk.com\057develop\057devres\057heidi\057oglspecs.htm"

%{
/**
 *
 * GL.Autodesk.facet_normal Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

%include util.inc

%include py_exception_handler.inc

%{
#if !EXT_DEFINES_PROTO || !defined(GL_Autodesk_facet_normal)
DECLARE_VOID_EXT(glFacetNormal3b, (GLbyte nx, GLbyte ny, GLbyte nz), (nx, ny, nz))
DECLARE_VOID_EXT(glFacetNormal3d, (GLdouble nx, GLdouble ny, GLdouble nz), (nx, ny, nz))
DECLARE_VOID_EXT(glFacetNormal3f, (GLfloat nx, GLfloat ny, GLfloat nz), (nx, ny, nz))
DECLARE_VOID_EXT(glFacetNormal3i, (GLint nx, GLint ny, GLint nz), (nx, ny, nz))
DECLARE_VOID_EXT(glFacetNormal3s, (GLshort nx, GLshort ny, GLshort nz), (nx, ny, nz))
DECLARE_VOID_EXT(glFacetNormal3bv, (const GLbyte *v), (v))
DECLARE_VOID_EXT(glFacetNormal3dv, (const GLdouble *v), (v))
DECLARE_VOID_EXT(glFacetNormal3fv, (const GLfloat *v), (v))
DECLARE_VOID_EXT(glFacetNormal3iv, (const GLint *v), (v))
DECLARE_VOID_EXT(glFacetNormal3sv, (const GLshort *v), (v))
#endif
%}

void glFacetNormal3b (GLbyte nx, GLbyte ny, GLbyte nz);
DOC(glFacetNormal3b, "glFacetNormal3b(nx, ny, nz) -> None")

void glFacetNormal3d (GLdouble nx, GLdouble ny, GLdouble nz);
DOC(glFacetNormal3d, "glFacetNormal3d(nx, ny, nz) -> None")

void glFacetNormal3f (GLfloat nx, GLfloat ny, GLfloat nz);
DOC(glFacetNormal3f, "glFacetNormal3f(nx, ny, nz) -> None")

void glFacetNormal3i (GLint nx, GLint ny, GLint nz);
DOC(glFacetNormal3i, "glFacetNormal3i(nx, ny, nz) -> None")

void glFacetNormal3s (GLshort nx, GLshort ny, GLshort nz);
DOC(glFacetNormal3s, "glFacetNormal3s(nx, ny, nz) -> None")

void glFacetNormal3bv (const GLbyte *v);
DOC(glFacetNormal3bv, "glFacetNormal3bv(v) -> None")

void glFacetNormal3dv (const GLdouble *v);
DOC(glFacetNormal3dv, "glFacetNormal3dv(v) -> None")

void glFacetNormal3fv (const GLfloat *v);
DOC(glFacetNormal3fv, "glFacetNormal3fv(v) -> None")

void glFacetNormal3iv (const GLint *v);
DOC(glFacetNormal3iv, "glFacetNormal3iv(v) -> None")

void glFacetNormal3sv (const GLshort *v);
DOC(glFacetNormal3sv, "glFacetNormal3sv(v) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_Autodesk_facet_normal)
	"glFacetNormal3b",
	"glFacetNormal3d",
	"glFacetNormal3f",
	"glFacetNormal3i",
	"glFacetNormal3s",
	"glFacetNormal3bv",
	"glFacetNormal3dv",
	"glFacetNormal3fv",
	"glFacetNormal3iv",
	"glFacetNormal3sv",
#endif
	NULL
};

#define glInitFacetNormalAutodesk() InitExtension("GL_Autodesk_facet_normal", proc_names)
%}

int glInitFacetNormalAutodesk();
DOC(glInitFacetNormalAutodesk, "glInitFacetNormalAutodesk() -> bool")


%{
PyObject *__info()
{
	if (glInitFacetNormalAutodesk())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

#define GL_FACET_NORMAL 0x85D0 
