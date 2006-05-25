#ifndef PyObjC_METHODSIGNATURE_H
#define PyObjC_METHODSIGNATURE_H
/*!
 * @header    method-signature.h
 * @abstract  A subset of NSMethodSignature, in C
 * @discussion
 * 	This module defines a C implementation of a subset of NSMethodSignature,
 * 	specifically the part of NSMethodSignature that is usefull for the
 * 	bridge.
 *
 *	Implemented because NSMethodSignature has a private constructor and
 *	because this interface is easier to use.
 *
 *	TODO: Check if we don't use NSMethodSignatures where we should use
 *	this type.
 */
#include "pyobjc.h"

/*
 * @struct PyObjCMethodSignature
 * @abstract The signature type
 * @field retainCount  Used for reference counting, don't modify this.
 * @field nargs        The number of arguments
 * @field rettype      The return type
 * @field signature    The entire signature string
 * @field argtype      Array of nargs signature strings (the arguments)
 * @discussion
 * 	Neither the rettype nor the argtypes are zero-terminated, all this
 * 	pointers point to substrings of signature.
 */
typedef struct {
	int retainCount;
	Py_ssize_t nargs;
	const char* rettype;
	const char* signature;
	const char* argtype[1];
} PyObjCMethodSignature;

/*!
 * @function PyObjCMethodSignature_FromSignature
 * @abstract Create a new signature
 * @param sig   An Objective-C signature string
 * @returns NULL or a PyObjCMethodSignature
 * @discussion
 * 	The 'sig' is copied into the return value.
 */
extern PyObjCMethodSignature* PyObjCMethodSignature_FromSignature(
		const char* sig);

/*!
 * @function PyObjCMethodSignature_Free
 * @abstract Free a method signature
 * @param sig  A signature
 * @discussion
 * 	This reduces the retainCount and frees the signature when that
 * 	count is 0.
 */
extern void PyObjCMethodSignature_Free(PyObjCMethodSignature* sig);

/*!
 * @function PyObjCMethodSignature_Retain
 * @abstract Increase the retainCount
 * @param sig  A signature
 */
static inline void PyObjCMethodSignature_Retain(PyObjCMethodSignature* sig)
{
	sig->retainCount++;
}

/*!
 * @function PyObjC_NSMethodSignatureToTypeString
 * @abstract Extract the signature string from an NSMethodSignature object
 * @param sig An NSMethodSignature object
 * @param buf The output buffer
 * @param buflen The length of 'buf'
 * @returns NULL or buf
 */
extern char*
PyObjC_NSMethodSignatureToTypeString(
	NSMethodSignature* sig, char* buf, size_t buflen);


#endif /* PyObjC_METHODSIGNATURE_H */
