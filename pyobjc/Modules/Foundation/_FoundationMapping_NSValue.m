/*
 * Special wrappers for NSValue methods with 'difficult' arguments.
 *
 * TODO:
 * -getValue:
 * -pointerValue:
 *
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

	

static int 
_pyobjc_install_NSValue(void)
{
	Class classNSValue = objc_lookUpClass("NSValue");
	if (classNSValue == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSValue,
		@selector(getValue:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSValue,
		@selector(pointerValue:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
