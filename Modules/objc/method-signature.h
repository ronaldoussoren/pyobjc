#ifndef PyObjC_METHODSIGNATURE_H
#define PyObjC_METHODSIGNATURE_H

/*
 * A C implementation of the usefull (for us) part of NSMethodSignature.
 * This is both faster than NSMethodSignature, and has a more stable x-platform
 * interface.
 */

#include "pyobjc.h"

typedef struct {
	int   retainCount;
	int   nargs;
	const char* rettype;
	const char* signature;
	const char* argtype[1];
} PyObjCMethodSignature;

extern PyObjCMethodSignature* PyObjCMethodSignature_FromSignature(
		const char* sig);
extern void PyObjCMethodSignature_Free(PyObjCMethodSignature* sig);

extern char*
PyObjC_NSMethodSignatureToTypeString(
	NSMethodSignature* sig, char* buf, size_t buflen);


#endif /* PyObjC_METHODSIGNATURE_H */
