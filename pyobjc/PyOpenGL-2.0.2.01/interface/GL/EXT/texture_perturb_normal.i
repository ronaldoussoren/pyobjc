/*
# BUILD api_versions [0x100]
*/

%module texture_perturb_normal

%{
/**
 *
 * GL.EXT.texture_perturb_normal Module for PyOpenGL
 * 
 * Date: May 2001
 *
 * Authors: Tarn Weisner Burton <twburton@users.sourceforge.net>
 * 
***/
%}

#define __version__ "$Revision: 1.18.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057texture_perturb_normal.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture_perturb_normal)
DECLARE_VOID_EXT(glTextureNormalEXT, (GLenum mode), (mode))
#endif
%}

void glTextureNormalEXT(GLenum mode);
DOC(glTextureNormalEXT, "glTextureNormalEXT(mode) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_texture_perturb_normal)
	"glTextureNormalEXT",
#endif
	NULL
};

#define glInitTexturePerturbNormalEXT() InitExtension("GL_EXT_texture_perturb_normal", proc_names)
%}

int glInitTexturePerturbNormalEXT();
DOC(glInitTexturePerturbNormalEXT, "glInitTexturePerturbNormalEXT() -> bool")

%name(glInitTexPerturbNormalEXT) int glInitTexturePerturbNormalEXT();
DOC(glInitTexPerturbNormalEXT, "glInitTexPerturbNormalEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitTexturePerturbNormalEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_PERTURB_EXT				0x85AE

#define GL_TEXTURE_NORMAL_EXT			0x85AF