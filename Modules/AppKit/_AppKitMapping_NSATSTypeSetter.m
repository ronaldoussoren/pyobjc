/*
 * Special wrappers for NSATSTypesetter methods with 'difficult' arguments.
 *
 * TODO:
 * getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:
 * getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:
 * substituteGlyphsInRange:withGlyphs:
 *
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static int 
_pyobjc_install_NSATSTypesetter(void)
{
	Class classNSATSTypesetter = objc_lookUpClass("NSATSTypesetter");

	if (PyObjC_RegisterMethodMapping(
		classNSATSTypesetter,
		@selector(getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSATSTypesetter,
		@selector(getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSATSTypesetter,
		@selector(substituteGlyphsInRange:withGlyphs:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
