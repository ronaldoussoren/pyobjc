/*!
 * @header method-imp.h
 * @abstract wrapper for IMP
 *     
 * This module implements a wrapper for IMPs, that is the functions implementing
 * Objective-C methods. The module also provides wrappers for the two Cocoa
 * methods that return IMP's.
 *
 * The IMP interface has one odd feature: the selector argument should not
 * be provided when calling it from Python. The reason for this is pragmatic:
 * 1) Doesn't seem to usefull to pass a SEL
 * 2) Makes the implementation easier
 *
 * Actually calling into Objective-C is done by code that is shared with the
 * normal method calling mechanism. 
 *
 * TODO:
 * - Implement calling support in the special method wrappers
 * - Implement support for assigning an IMP to another class
 * - Implement support for using an IMP in inheritance
 */
#ifndef PyObjC_METHOD_IMP_H
#define PyObjC_METHOD_IMP_H

extern PyTypeObject PyObjCIMP_Type;

#define PyObjCIMP_Check(obj) PyObject_TypeCheck(obj, &PyObjCIMP_Type)

extern PyObject* PyObjCIMP_New(
		IMP imp, 
		SEL sel,
		PyObjC_CallFunc callfunc,
		PyObjCMethodSignature* signature,
		int flags);
extern IMP PyObjCIMP_GetIMP(PyObject* self);
extern PyObjC_CallFunc PyObjCIMP_GetCallFunc(PyObject* self);
extern PyObjCMethodSignature* PyObjCIMP_GetSignature(PyObject* self);
extern int PyObjCIMP_GetFlags(PyObject* self);
extern SEL PyObjCIMP_GetSelector(PyObject* self);

extern int PyObjCIMP_SetUpMethodWrappers(void);

#endif /* PyObjC_METHOD_IMP_H */
