/*
 * NSFont mappings for difficult methods:
 *
 * TODO:
 * -positionsForCompositeSequence:numberOfGlyphs:pointArray:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static int 
_pyobjc_install_NSFont(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSFont"), 
		@selector(positionsForCompositeSequence:numberOfGlyphs:pointArray:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	return 0;
}
