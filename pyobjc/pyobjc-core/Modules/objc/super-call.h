#ifndef PyObjC_SUPER_CALL_H
#define PyObjC_SUPER_CALL_H
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

/*!
 * @constant PyObjC_MappingCount
 * @abstract The number of registered special mappings
 * @discussion
 *     This is NOT a constant, but there seems to be no way to mark up
 *     variables.
 *
 *     This value is used by the objc-class module to detect if the methods in
 *     a class should be regenerated.
 */
extern Py_ssize_t PyObjC_MappingCount;

extern BOOL PyObjC_UpdatingMetaData;


/*!
 * @function PyObjC_RegisterMethodMapping
 * @abstract Register a mapping for a specific method
 * @param aClass         Class for which this mapping is valid (+subclasses)
 * @param sel            The selector with a custom mapping
 * @param call_to_objc   Function for calling into Objective-C (from Python),
 * 	                 the default is 'PyObjCFFI_Caller'.
 * @param call_to_python Function for calling into Python (from Objective-C)
 * @result Returns 0 on success, -1 on error.
 */
extern int PyObjC_RegisterMethodMapping(
	Class aClass, 
	SEL sel, 
	PyObjC_CallFunc call_to_objc, 
	PyObjCFFI_ClosureFunc call_to_python
	);

/*!
 * @function PyObjC_RegisterSignatureMapping
 * @abstract Register a mapping for methods with a specific signature
 * @param signature      An Objective-C method signature string
 * @param call_to_objc   Function for calling into Objective-C (from Python)
 * @param call_to_python Function for calling into Python (from Objective-C)
 * @result Returns 0 on success, -1 on failure
 */
extern int PyObjC_RegisterSignatureMapping(
	char* signature,
	PyObjC_CallFunc call_to_super,
	PyObjCFFI_ClosureFunc call_to_python);

/*!
 * @function PyObjC_FindCallFunc
 * @abstract Find the function to call into Objective-C
 * @param aClass     An Objective-C class
 * @param sel        A selector
 * @result Returns a function or NULL
 * @discussion
 * 	This finds the function that can be used to call the Objective-C
 * 	implementation of the specified method.
 */
extern PyObjC_CallFunc PyObjC_FindCallFunc(Class aClass, SEL sel);

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
extern IMP PyObjC_MakeIMP(Class aClass, Class aSuperClass, PyObject* sel, PyObject* imp);

/*!
 * @constant PyObjCUnsupportedMethod_IMP
 * @discussion
 * 	Use this as the 'call_to_python' argument to 
 * 	PyObjC_RegisterMethodMapping and PyObjC_RegisterSignatureMapping if
 * 	the method cannot be implemented in Python.
 */
extern void PyObjCUnsupportedMethod_IMP(ffi_cif*, void*, void**, void*);

/*!
 * @constant PyOBjCUnsupportedMethod_Caller
 * @discussion
 * 	Use this as the 'call_to_objc' argument to 
 * 	PyObjC_RegisterMethodMapping and PyObjC_RegisterSignatureMapping if
 * 	the method cannot be called from Python.
 */
extern PyObject* PyObjCUnsupportedMethod_Caller(PyObject*, PyObject*, PyObject*);

#endif /* PyObjC_SUPER_CALL_H */
