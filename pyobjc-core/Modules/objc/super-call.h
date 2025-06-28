#ifndef PyObjC_SUPER_CALL_H
#define PyObjC_SUPER_CALL_H

NS_ASSUME_NONNULL_BEGIN
/*!
 * @header super-call.h
 * @abstract Finding the right functions to call Objective-C methods
 * @discussion
 *     This module deals with finding the correct function to call a method,
 *     both from Python to Objective-C and from Objective-C to python.
 *
 *     The default Python to Objective-C calls for 'normal' calls is good enough
 *     for most methods, but for some methods we need specialized functions.
 */

extern BOOL PyObjC_UpdatingMetaData;

extern int PyObjC_InitSuperCallRegistry(void);

typedef IMP _Nullable (*PyObjC_MakeIMPBlockFunc)(
    PyObject* _Nonnull callable, PyObjCMethodSignature* _Nonnull methinfo);

/*!
 * @function PyObjC_RegisterMethodMapping
 * @abstract Register a mapping for a specific method
 * @param aClass         Class for which this mapping is valid (+subclasses),
 *                       use Nil to specify all classes.
 * @param sel            The selector with a custom mapping
 * @param call_to_objc   Function for calling into Objective-C (from Python),
 *                      the default is 'PyObjCFFI_Caller'.
 * @param call_to_python Function for calling into Python (from Objective-C)
 * @result Returns 0 on success, -1 on error.
 */
extern int PyObjC_RegisterMethodMapping(_Nullable Class aClass, SEL sel,
                                        PyObjC_CallFunc         call_to_objc,
                                        PyObjC_MakeIMPBlockFunc call_to_python);

/*!
 * @function PyObjC_RegisterSignatureMapping
 * @abstract Register a mapping for methods with a specific signature
 * @param signature      An Objective-C method signature string
 * @param call_to_objc   Function for calling into Objective-C (from Python)
 * @param call_to_python Function for calling into Python (from Objective-C)
 * @result Returns 0 on success, -1 on failure
 */
extern int PyObjC_RegisterSignatureMapping(char* signature, PyObjC_CallFunc call_to_super,
                                           PyObjC_MakeIMPBlockFunc call_to_python);

/*!
 * @function PyObjC_FindCallFunc
 * @abstract Find the function to call into Objective-C
 * @param aClass     An Objective-C class
 * @param sel        A selector
 * @result Returns a function
 * @discussion
 *     This finds the function that can be used to call the Objective-C
 *     implementation of the specified method.
 */
extern PyObjC_CallFunc _Nullable PyObjC_FindCallFunc(Class aClass, SEL sel,
                                                     const char* signature);

/*!
 * @function PyObjC_MakeIMP
 * @abstract Create an IMP for calling the specified method from Objective-C
 * @param aClass  An Objective-C class
 * @param aSuperClass  An Objective-C super class
 * @param sel     A selector object
 * @param imp     The Python implementation for sel
 * @result  A method stub or NULL
 * @discussion
 *      Objective-C classes have method dispatch tables. This function creates
 *      and returns functions that can be used in these tables. The returned
 *      function will convert it's arguments to Python objects and call 'imp'.
 *      The result of 'imp' will be converted back to Objective-C.
 */
extern _Nullable IMP PyObjC_MakeIMP(Class aClass, _Nullable Class aSuperClass,
                                    PyObject* sel, PyObject* imp);

/*!
 * @constant PyObjCUnsupportedMethod_IMP
 * @discussion
 *     Use this as the 'call_to_python' argument to
 *     PyObjC_RegisterMethodMapping and PyObjC_RegisterSignatureMapping if
 *     the method cannot be implemented in Python.
 */
extern IMP PyObjCUnsupportedMethod_IMP(PyObject* _Nonnull callable,
                                       PyObjCMethodSignature* _Nonnull methinfo);

/*!
 * @constant PyOBjCUnsupportedMethod_Caller
 * @discussion
 *     Use this as the 'call_to_objc' argument to
 *     PyObjC_RegisterMethodMapping and PyObjC_RegisterSignatureMapping if
 *     the method cannot be called from Python.
 */
extern PyObject* _Nullable PyObjCUnsupportedMethod_Caller(
    PyObject*, PyObject*, PyObject* _Nonnull const* _Nullable, size_t);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_SUPER_CALL_H */
