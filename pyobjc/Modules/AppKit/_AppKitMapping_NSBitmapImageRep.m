/*
 * NSBitmapImageRep mappings for difficult methods:
 *
 * TODO:
 * -getBitMapDataPlanes:
 * -getTIFFCompressionTypes:count:
 * -initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static int 
_pyobjc_install_NSBitmapImageRep(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBitMapImageRep"), 
		@selector(getBitMapDataPlanes:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBitMapImageRep"), 
		@selector(getTIFFCompressionTypes:count:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSBitMapImageRep"), 
		@selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	return 0;
}
