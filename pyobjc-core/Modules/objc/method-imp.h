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
 * 1) Doesn't seem to useful to pass a SEL
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

NS_ASSUME_NONNULL_BEGIN

extern PyObject* PyObjCIMP_Type;

#define PyObjCIMP_Check(obj) PyObject_TypeCheck(obj, (PyTypeObject*)PyObjCIMP_Type)

extern _Nullable IMP PyObjCIMP_GetIMP(PyObject* self) __attribute__((warn_unused_result));
extern PyObjCMethodSignature* _Nullable PyObjCIMP_GetSignature(PyObject* self)
    __attribute__((warn_unused_result));
extern int PyObjCIMP_GetFlags(PyObject* self) __attribute__((warn_unused_result));
extern _Nullable SEL PyObjCIMP_GetSelector(PyObject* self)
    __attribute__((warn_unused_result));
extern ffi_cif* _Nullable PyObjCIMP_GetCIF(PyObject* self)
    __attribute__((warn_unused_result));
extern int PyObjCIMP_SetCIF(PyObject* self, ffi_cif* _Nullable cif)
    __attribute__((warn_unused_result));

extern int PyObjCIMP_SetUp(PyObject* module) __attribute__((warn_unused_result));

NS_ASSUME_NONNULL_END

#endif /* PyObjC_METHOD_IMP_H */
