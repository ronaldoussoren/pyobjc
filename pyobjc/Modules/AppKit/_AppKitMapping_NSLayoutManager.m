/*
 * Special wrappers for NSLayoutManager methods with 'difficult' arguments.
 *
 * TODO 
 *
 * -getGlyphs:range:
 * -getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:
 * -getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:
 * -rectArrayForCharacterRange:withinSelectedCharacterRange:inTextContainer:rectCount:
 * -rectArrayForGlyphRange:withinSelectedGlyphRange:inTextContainer:rectCount:
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"



static int 
_pyobjc_install_NSLayoutManager(void)
{
	Class classNSLayoutManager = objc_lookUpClass("NSLayoutManager");

	if (PyObjC_RegisterMethodMapping(
		classNSLayoutManager,
		@selector(getGlyphs:range:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
