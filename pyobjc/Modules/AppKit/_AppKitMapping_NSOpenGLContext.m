/*
 * Special wrappers for NSOpenGLContext methods with 'difficult' arguments.
 *
 * TODO:
 * -getValues:forParameter:
 * -setValues:forParameter:
 * -setOffScreen:width:height:rowbytes:
 * -CGLContextObj
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

#ifdef MACOSX 

/* 1. I can't manage to get a working OpenGL on my develbox
 * 2. Need to detect if OpenGL support is present
 */

#include <OpenGL/gl.h>

#endif


static int 
_pyobjc_install_NSOpenGLContext(void)
{
	Class classNSOpenGLContext = objc_lookUpClass("NSOpenGLContext");

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(CGLContextObj),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(getValues:forParameter:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(setValues:forParameter:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(setOffScreen:width:height:rowbytes:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
