/*
 * Special wrappers for NSString methods with 'difficult' arguments.
 *
 * TODO:
 * -getCString:maxLength:range:remainingRange:
 * -getCharacters:
 * -getCharacters:range:

 NSString_getCString_maxLength_range_remainingRange_
 NSString_getCharacters_
 NSString_getCharacters_range_

 *
 * Unsupported methods: 
 * -initWithCharactersNoCopy:length:freeWhenDone:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

	

static int 
_pyobjc_install_NSString(void)
{
	Class classNSString = objc_lookUpClass("NSString");

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(initWithCharactersNoCopy:length:freeWhenDone:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}


	return 0;
}
