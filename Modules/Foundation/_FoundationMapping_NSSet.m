/*
 * Special wrappers for NSSet methods with 'difficult' arguments.
 *
 * -initWithObjects:count:		[call, imp]
 * +setWithObjects:count:		[call, imp]
 *
 * Unsupported methods:
 * -initWithObjects:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static int 
_pyobjc_install_NSSet(void)
{
	Class classNSSet = objc_lookUpClass("NSSet");
	if (classNSSet == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
                @selector(initWithObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
                @selector(setWithObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
		@selector(setWithObjects:count:),
		call_clsWithObjects_count_,
		imp_clsWithObjects_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
		@selector(initWithObjects:count:),
		call_objWithObjects_count_,
		imp_objWithObjects_count_) < 0) {

		return -1;
	}

	return 0;
}
