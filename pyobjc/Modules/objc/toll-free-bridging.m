/*
 *  This file defines support for "toll-free briging" between Python wrappers
 *  for CoreFoundation objecs and native Objective-C objects.
 *
 *  NOTE: It would be nice if we could move some of this logic into MacPython,
 *  keeping the lists of CF-wrappers synchronized is not a very pleasant 
 *  thought.
 */
#include "pyobjc.h"
#include "objc_support.h"
#include <unistd.h>
#include "objc/objc.h"

#ifdef MACOSX
#import <Foundation/NSURL.h>

#include "pymactoolbox.h"

id PyObjC_CFTypeToID(PyObject* argument)
{
	/* Tollfree bridging of CF (some) objects 
	 * This list of conversion functions is the complete list of such
	 * functions in Python 2.3b1
	 */
	int r;
	id  val;

#if PY_VERSION_HEX >= 0x020300B2

	r = CFObj_Convert(argument, (CFTypeRef*)&val);
	if (r) return val;
	PyErr_Clear();
	return NULL;

#else
	r = CFTypeRefObj_Convert(argument, (CFTypeRef*)&val);
	if (r) return val;

	r = CFStringRefObj_Convert(argument, (CFStringRef*)&val);
	if (r) return val;

	r = CFMutableStringRefObj_Convert(argument, (CFMutableStringRef*)&val);
	if (r) return val;

	r = CFArrayRefObj_Convert(argument, (CFArrayRef*)&val);
	if (r) return val;

	r = CFMutableArrayRefObj_Convert(argument, (CFMutableArrayRef*)&val);
	if (r) return val;
		
	r = CFDictionaryRefObj_Convert(argument, (CFDictionaryRef*)&val);
	if (r) return val;

	r = CFMutableDictionaryRefObj_Convert(argument, 
		(CFMutableDictionaryRef*)&val);
	if (r) return val;

	r = CFURLRefObj_Convert(argument, (CFURLRef*)&val);
	if (r) return val;

	PyErr_Clear();
	return NULL;
#endif
}

PyObject* PyObjC_IDToCFType(id argument)
{

	if ([argument isKindOfClass:[NSMutableString class]]) {
		return CFMutableStringRefObj_New((CFMutableStringRef)argument);
	}

	if ([argument isKindOfClass:[NSString class]]) {
		return CFStringRefObj_New((CFStringRef)argument);
	}
	
	if ([argument isKindOfClass:[NSMutableArray class]]) {
		return CFMutableArrayRefObj_New((CFMutableArrayRef)argument);
	}

	if ([argument isKindOfClass:[NSArray class]]) {
		return CFArrayRefObj_New((CFArrayRef)argument);
	}

	if ([argument isKindOfClass:[NSDictionary class]]) {
		return CFDictionaryRefObj_New((CFDictionaryRef)argument);
	}

	if ([argument isKindOfClass:[NSMutableDictionary class]]) {
		return CFMutableDictionaryRefObj_New(
				(CFMutableDictionaryRef)argument);
	}

	if ([argument isKindOfClass:[NSURL class]]) {
		return CFURLRefObj_New((CFURLRef)argument);
	}

	/* Apple doesn't say as much, but as NSArray and CFArray are toll-free
	 * bridged NSObject must also be toll-free bridged to a CoreFoundation
	 * type.  As is is not document which type this is, we use the most
	 * generic one.
	 */
#if PY_VERSION_HEX >= 0x020300B2
	return CFObj_New((CFTypeRef)argument);
#else
	return CFTypeRefObj_New((CFTypeRef)argument);
#endif 
}


#else

static const char dummy; /* Make sure this is valid C on GNUstep */

#endif /* MACOSX */



