#ifndef OBJC_SUPER_CALL_H
#define OBJC_SUPER_CALL_H
/*
 * Filename will probably be changed soon.
 *
 * This file, and the corresponding '.m' file, deal with finding the 
 * correct function to call a method, both from Python to Objective-C and
 * from Objective-C to python.
 *
 * The default Python to Objective-C calls for 'normal' calls is good enough
 * for most methods, in general problemetic methods are those with output 
 * parameters.
 *
 * Calling the superclass implementation is harder, and requires compile-time
 * generated stubs. The core module wil provide no such stubs, but relies on
 * extension modules to provide these (All stubs needed for Cocoa are part of
 * the pyobjc package).
 *
 * Calling from objective-C to python is simular in dificultie as super-calls.
 * The core module again provides no stubs, and again the Cocoa-related stubs
 * will be part of the pyobjc package.
 */
#include "pyobjc.h"

extern PyObject* ObjC_CallSuper(PyObject* meth, 
					PyObject* self, PyObject* args);
extern PyObject* ObjC_CallSelf(PyObject* meth, 
					PyObject* self, PyObject* args);

/* Registration database that allows overriding of the function used to
 * forward a call from python to objective-C
 */
typedef PyObject* (*ObjC_CallFunc_t)(
	PyObject* meth, PyObject* self, PyObject* args);

extern int ObjC_RegisterMethodMapping(Class class, SEL sel, 
	ObjC_CallFunc_t call_to_self,  /* Call method in self */
	ObjC_CallFunc_t call_to_super, /* Call method in super */
	IMP		    call_to_python
		/* IMP that can be used to forward call from objective-C to
		 * python.
		 */
	);

/* No 'call_to_self' here, if the default is not good enough  it should be
 * enhanced.
 */
extern int ObjC_RegisterSignatureMapping(
	char* signature,
	ObjC_CallFunc_t call_to_super,
	IMP		call_to_python);

extern IMP             ObjC_FindIMP(Class class, SEL sel);
extern IMP             ObjC_FindIMPForSignature(char* signature);
extern ObjC_CallFunc_t ObjC_FindSupercaller(Class class, SEL sel);
extern ObjC_CallFunc_t ObjC_FindSelfCaller(Class class, SEL sel);
extern void            ObjC_FindCaller(Class class, SEL sel, ObjC_CallFunc_t* call_self, ObjC_CallFunc_t* call_super);

#endif /* OBJC_SUPER_CALL_H */
