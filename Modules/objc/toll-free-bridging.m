/*
 *  This file defines support for "toll-free briging" between Python wrappers
 *  for CoreFoundation objecs and native Objective-C objects.
 */
#include "pyobjc.h"

#include <unistd.h>

#include "objc/objc.h"

#ifdef MACOSX
#import <Foundation/NSURL.h>

#include "pymactoolbox.h"

id 
PyObjC_CFTypeToID(PyObject* argument)
{
	/* Tollfree bridging of CF (some) objects 
	 * This list of conversion functions is the complete list of such
	 * functions in Python 2.4.1
	 */
	int r;
	id  val;


	r = CFObj_Convert(argument, (CFTypeRef*)&val);
	if (r) return val;
	PyErr_Clear();
	return NULL;
}

/* 
 * NOTE: CFObj_New creates a CF wrapper for any CF object, however we have
 * better information for at least some types: it is impossible to see the
 * difference between mutable and immutable types using the CF API.
 *
 */
PyObject* 
PyObjC_IDToCFType(id argument)
{
	CFTypeRef typeRef = (CFTypeRef)argument;
	CFTypeID typeID = CFGetTypeID(argument);

    /*
     * This function has a net reference count of 0 as the CF wrapper
     * does not retain, but will do a CFRelease when the Python proxy
     * goes away.
     */
	CFRetain(typeRef);

	/* This could be more efficient, could cache... */
	if (typeID == CFStringGetTypeID()) {
		return CFMutableStringRefObj_New((CFMutableStringRef)argument);
	} else if (typeID == CFArrayGetTypeID()) {
		return CFMutableArrayRefObj_New((CFMutableArrayRef)argument);
	} else if (typeID == CFDictionaryGetTypeID()) {
		return CFMutableDictionaryRefObj_New((CFMutableDictionaryRef)argument);
	} else if (typeID == CFURLGetTypeID()) {
		return CFURLRefObj_New((CFURLRef)argument);
/*
 * TODO: This is in Python 2.5, Fix the #if at some point
 */
#if 0
	} else if (typeID == CFDataGetTypeID()) {
		return CFMutableDataRefObj_New((CFMutableDataRef)argument);
#endif
	}
	return CFObj_New((CFTypeRef)argument);
}


#else

static const char dummy; /* Make sure this is valid C on GNUstep */

#endif /* MACOSX */
