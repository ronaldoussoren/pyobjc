/*
 * Special wrappers for NSSimpleHorizontalTypesetter methods with 'difficult' 
 * arguments.
 *
 * TODO:
 * -baseOfTypesetterGlyphInfo
 * -layoutGlyphsInHorizontalLineFragment:baseline:
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static int 
_pyobjc_install_NSSimpleHorizontalTypesetter(void)
{
	Class classNSSimpleHorizontalTypesetter = objc_lookUpClass("NSSimpleHorizontalTypesetter");

	if (PyObjC_RegisterMethodMapping(
		classNSSimpleHorizontalTypesetter,
		@selector(baseOfTypesetterGlyphInfo),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSimpleHorizontalTypesetter,
		@selector(layoutGlyphsInHorizontalLineFragment_baseline:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
