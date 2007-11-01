/*
# BUILD api_versions [0x103]
*/

%module nurbs_tessellator
%include util.inc

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:21:33 $"
#define __api_version__ API_VERSION
#define __author__ "Tarn Weisner Burton <twburton@users.sourceforge.net>, Mike Fletcher <mcfletch@users.sourceforge.net>"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057EXT\057nurbs_tessellator.txt"

/* turn the exception handler on */
%include gl_exception_handler.inc

/* should be including the type-maps for the NURB objects here */

%{

#if !EXT_DEFINES_PROTO || !defined(GLU_EXT_nurbs_tessellator)
DECLARE_VOID_EXT(gluNurbsCallbackDataEXT, \
	(GLUnurbs* theNurb, void* userData),\
	(theNurb, userData))
#endif

#define __gluNurbsCallbackDataEXT(nobj, data) \
	gluNurbsCallbackDataEXT(nobj, (void*)data)

%}

void __gluNurbsCallbackDataEXT(GLUnurbs *nobj, PyObject *data);
DOC(__gluNurbsCallbackDataEXT, "gluNurbsCallbackDataEXT(nobj, data) -> None")

%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GLU_EXT_nurbs_tessellator)
	"gluNurbsCallbackDataEXT",
#endif
	NULL
};

#define gluInitNurbsTessellatorEXT() InitExtension("GLU_EXT_nurbs_tessellator", proc_names)
%}

int gluInitNurbsTessellatorEXT();
DOC(gluInitNurbsTessellatorEXT, "gluInitNurbsTessellatorEXT() -> bool")


%{
PyObject *__info()
{
	if (gluInitNurbsTessellatorEXT())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();


/* revert to the normal exception handler */
%include gl_exception_handler.inc


#define GLU_NURBS_MODE_EXT             100160
#define GLU_NURBS_TESSELLATOR_EXT      100161
#define GLU_NURBS_RENDERER_EXT         100162
#define GLU_NURBS_BEGIN_EXT	               100164
#define GLU_NURBS_VERTEX_EXT                   100165
#define GLU_NURBS_NORMAL_EXT                   100166
#define GLU_NURBS_COLOR_EXT                    100167
#define GLU_NURBS_TEXTURE_COORD_EXT            100168
#define GLU_NURBS_END_EXT                      100169
#define GLU_NURBS_BEGIN_DATA_EXT	       100170
#define GLU_NURBS_VERTEX_DATA_EXT              100171
#define GLU_NURBS_NORMAL_DATA_EXT              100172
#define GLU_NURBS_COLOR_DATA_EXT               100173
#define GLU_NURBS_TEXTURE_COORD_DATA_EXT       100174
#define GLU_NURBS_END_DATA_EXT                 100175
