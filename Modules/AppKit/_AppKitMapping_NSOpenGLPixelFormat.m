/*
 * Special wrappers for NSOpenGLPixelFormat methods with 'difficult' arguments.
 *
 * TODO:
 * -getValues:forAttribute:forVirtualScreen:
 * -initWithAttributes:
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static int 
_pyobjc_install_NSOpenGLPixelFormat(void)
{
	Class classNSOpenGLPixelFormat = objc_lookUpClass("NSOpenGLPixelFormat");

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLPixelFormat,
		@selector(getValues:forAttribute:forVirtualScreen:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLPixelFormat,
		@selector(initWithAttributes:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
