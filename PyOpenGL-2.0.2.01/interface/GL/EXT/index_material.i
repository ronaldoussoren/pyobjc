/*
# BUILD api_versions [0x104]
*/

%module index_material

#define __version__ "$Revision: 1.22.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057index_material.txt"

%{
/**
 *
 * GL.EXT.index_material Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_index_material)
DECLARE_VOID_EXT(glIndexMaterialEXT, (GLenum face, GLenum mode), (face, mode))
#endif
%}

void glIndexMaterialEXT(GLenum face, GLenum mode);
DOC(glIndexMaterialEXT, "glIndexMaterialEXT(face, mode) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_index_material)
	"glIndexMaterialEXT",
#endif
	NULL
};

#define glInitIndexMaterialEXT() InitExtension("GL_EXT_index_material", proc_names)
%}

int glInitIndexMaterialEXT();
DOC(glInitIndexMaterialEXT, "glInitIndexMaterialEXT() -> bool")


%{
PyObject *__info()
{
	if (glInitIndexMaterialEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_INDEX_MATERIAL_EXT             0x81B8
#define GL_INDEX_MATERIAL_PARAMETER_EXT   0x81B9
#define GL_INDEX_MATERIAL_FACE_EXT        0x81BA
