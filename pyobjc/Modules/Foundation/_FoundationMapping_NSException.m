#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"




static int 
_pyobjc_install_NSException(void)
{
	Class classNSException = objc_lookUpClass("NSException");
	if (classNSException == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSException,
		@selector(raise:format:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSException,
		@selector(raise:format:arguments:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
