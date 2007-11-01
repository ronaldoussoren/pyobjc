/*
# BUILD api_versions [0x100]
*/

%module scene_marker

#define __version__ "$Revision: 1.21.6.1 $"
#define __date__ "$Date: 2004/11/14 23:19:04 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057scene_marker.txt"

%{
/**
 *
 * GL.EXT.scene_marker Module for PyOpenGL
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
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_scene_marker)
DECLARE_VOID_EXT(glBeginSceneEXT, (), ())
DECLARE_VOID_EXT(glEndSceneEXT, (), ())
#endif
%}

void glBeginSceneEXT();
DOC(glBeginSceneEXT, "glBeginSceneEXT() -> None")

void glEndSceneEXT();
DOC(glEndSceneEXT, "glEndSceneEXT() -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_EXT_scene_marker)
	"glBeginSceneEXT",
	"glEndSceneEXT",
#endif
	NULL
};

#define glInitSceneMarkerEXT() InitExtension("GL_EXT_scene_marker", proc_names)
%}

int glInitSceneMarkerEXT();
DOC(glInitSceneMarkerEXT, "glInitSceneMarkerEXT() -> bool")



%{
#ifndef GL_EXT_scene_marker
#define GL_SCENE_REQUIRED_EXT 0
#endif

PyObject *__info()
{
	if (glInitSceneMarkerEXT())
	{
		PyObject *info = PyList_New(0);
		PyList_Append(info, Py_BuildValue("sis", "GL_SCENE_REQUIRED_EXT", GL_SCENE_REQUIRED_EXT, "i"));
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


#define GL_SCENE_REQUIRED_EXT 0

