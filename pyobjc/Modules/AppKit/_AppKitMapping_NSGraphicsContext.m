/*
 * NSGraphicsContext mappings for difficult methods:
 *
 * TODO:
 * -graphicsPort
 *
 * Unsupported:
 * -focusStack
 * -setFocusStack
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static int 
_pyobjc_install_NSGraphicsContext(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(focusStack),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(setFocusStack),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSGraphicsContext"), 
		@selector(graphicsPort),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	return 0;
}
