#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"




static int 
_pyobjc_install_NSMutableString(void)
{
	Class classNSMutableString = objc_lookUpClass("NSMutableString");
	if (classNSMutableString == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSMutableString,
		@selector(appendFormat:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}


	return 0;
}
