/*
 * Special wrappers for NSQuickDrawView methods with 'difficult' arguments.
 *
 * TODO:
 * -qdPort
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static int 
_pyobjc_install_NSQuickDrawView(void)
{
	Class classNSQuickDrawView = objc_lookUpClass("NSQuickDrawView");

	if (PyObjC_RegisterMethodMapping(
		classNSQuickDrawView,
		@selector(qdPort),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
