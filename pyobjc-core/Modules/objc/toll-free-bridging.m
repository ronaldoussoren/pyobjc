/*
 *  This file defines support for "toll-free briging" between Python wrappers
 *  for CoreFoundation objecs and native Objective-C objects.
 */
#include "pyobjc.h"

#include <unistd.h>

#include "objc/objc.h"

#import <Foundation/NSURL.h>

#ifndef __OBJC2__
#include "pymactoolbox.h"
#endif

id 
PyObjC_CFTypeToID(PyObject* argument)
{
	/* Tollfree bridging of CF (some) objects  */
	id  val;

	if (PyObjCObject_Check(argument)) {
		val = PyObjCObject_GetObject(argument);
		return val;

	}

#ifndef __OBJC2__
	int r;

	/* Fall back to MacPython CFType support: */
	r = CFObj_Convert(argument, (CFTypeRef*)&val);
	if (r) return val;
	PyErr_Clear();
#endif

	return NULL;
}

/* 
 * NOTE: CFObj_New creates a CF wrapper for any CF object, however we have
 * better information for at least some types: it is impossible to see the
 * difference between mutable and immutable types using the CF API.
 *
 */
PyObject* 
PyObjC_IDToCFType(id argument __attribute__((__unused__)))
{
#ifndef __OBJC2__
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
#endif

	PyErr_SetString(PyExc_NotImplementedError, "jucky macpython");
	return NULL;
}
