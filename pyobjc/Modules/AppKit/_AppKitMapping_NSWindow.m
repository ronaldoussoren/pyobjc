/*
 * Special wrappers for NSWindow methods with 'difficult' arguments.
 *
 * TODO
 * -graphicsPort
 * -initWithWindowRef:
 * -windowRef
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"



static int 
_pyobjc_install_NSWindow(void)
{
	Class classNSWindow = objc_lookUpClass("NSWindow");

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(graphicsPort),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(initWihtWindowRef),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(windowRef),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
