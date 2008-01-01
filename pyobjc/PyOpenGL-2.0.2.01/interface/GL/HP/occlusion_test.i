/*
# BUILD api_versions [0x101]
*/

%module occlusion_test

%{
/**
 *
 * GL.HP.occlusion_test Module for PyOpenGL
 * 
 * Date: May 2003
 * 
***/
%}

#define __version__ "$Revision: 1.1.4.1 $"
#define __date__ "$Date: 2004/11/14 23:19:05 $"
#define __api_version__ API_VERSION
#define __author__ "Mike Fletcher <mcfletch@rogers.com"
#define __doc__ "http:\057\057oss.sgi.com\057projects\057ogl-sample\057registry\057HP\057image_transform.txt"

%include util.inc

/* turn the exception handler on */
%include gl_exception_handler.inc


%{
static char *proc_names[] =
{
	NULL
};

#define glInitOcclusionTestHP() InitExtension("GL_HP_occlusion_test", proc_names)
%}

int glInitOcclusionTestHP();
DOC(glInitOcclusionTestHP, "glInitOcclusionTestHP() -> bool")


%{
PyObject *__info()
{
	if (glInitOcclusionTestHP())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();



#define GL_OCCLUSION_TEST_HP              0x8165
#define GL_OCCLUSION_TEST_RESULT_HP       0x8166
