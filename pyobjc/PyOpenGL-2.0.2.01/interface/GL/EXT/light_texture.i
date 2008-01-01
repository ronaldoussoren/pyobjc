/*
# BUILD api_versions [0x100]
*/

%module light_texture

#define __version__ "$Revision: 1.22.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057light_texture.txt"

%{
/**
 *
 * GL.EXT.light_texture Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_light_texture)
DECLARE_VOID_EXT(glApplyTextureEXT, (GLenum mode), (mode))
DECLARE_VOID_EXT(glTextureLightEXT, (GLenum mode), (mode))
DECLARE_VOID_EXT(glTextureMaterialEXT, (GLenum face, GLenum mode), (face, mode))
#endif
%}

void glApplyTextureEXT(GLenum mode);
DOC(glApplyTextureEXT, "glApplyTextureEXT(mode) -> None")

void glTextureLightEXT(GLenum mode);
DOC(glTextureLightEXT, "glTextureLightEXT(mode) -> None")

void glTextureMaterialEXT(GLenum face, GLenum mode);
DOC(glTextureMaterialEXT, "glTextureMaterialEXT(face, mode) -> None")


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_light_texture)
	"glApplyTextureEXT",
	"glTextureLightEXT",
	"glTextureMaterialEXT",
#endif
	NULL
};

#define glInitLightTextureEXT() InitExtension("GL_EXT_light_texture", proc_names)
%}

int glInitLightTextureEXT();
DOC(glInitLightTextureEXT, "glInitLightTextureEXT() -> bool")

%name(glInitLightTexEXT) int glInitLightTextureEXT();
DOC(glInitLightTexEXT, "glInitLightTexEXT() -> bool")

%{
PyObject *__info()
{
	if (glInitLightTextureEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_FRAGMENT_MATERIAL_EXT                       0x8349
#define GL_FRAGMENT_NORMAL_EXT                         0x834A
#define GL_FRAGMENT_DEPTH_EXT                          0x8452
#define GL_FRAGMENT_COLOR_EXT                          0x834C

#define GL_ATTENUATION_EXT                             0x834D
#define GL_SHADOW_ATTENUATION_EXT                      0x834E

#define GL_TEXTURE_APPLICATION_MODE_EXT                0x834F
#define GL_TEXTURE_LIGHT_EXT                           0x8350
#define GL_TEXTURE_MATERIAL_FACE_EXT                   0x8351
#define GL_TEXTURE_MATERIAL_PARAMETER_EXT              0x8352