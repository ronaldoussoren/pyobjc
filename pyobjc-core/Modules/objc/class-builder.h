#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

/*!
 * @header class-builder.h
 * @abstract Module for creating Objective-C classes
 * @discussion
 *    This module defines the functions that are used to create new
 *    classes in the Objective-C runtime for subclasses of NSObject.
 *
 *    The protocol for building a new class:
 *    1) Collect the necessary information (name, bases and class_dict)
 *    2) Call PyObjCClass_BuildClass
 *    3) Create the Python class (using type.__new__)
 *    4) Call PyObjCClass_FinishClass
 *
 *    If step 3 fails: call PyObjCClass_UnbuildClass
 *
 *    Note that it is not possible to remove classes from the Objective-C 
 *    runtime (at least with the Apple runtime, not sure about the GNU runtime).
 */

/*!
 * @function PyObjCClass_BuildClass
 * @abstract Create a new Objective-C class, but do not register it
 * @param super_class The super class for the new class
 * @param protocols   The list of protocols that the class conforms to
 * @param name        Name of the class
 * @param class_dict  The __dict__ for the new class
 * @result  Returns the newly created class, or nil.
 *
 * @discusssion
 *     This function builds a new class based on the information passed in
 *     the arguments. The methods and functions in the class_dict are 
 *     transformed into selector objects.
 *
 *     The function will fail if the class does not in fact implement the
 *     protocols in the protocol list, or does partially implement any other
 *     known (informal) protocol.
 */
Class PyObjCClass_BuildClass(
		Class super_class,  
		PyObject* protocols,
		char* name, 
		PyObject* class_dict,
		PyObject* meta_dict);

/*!
 * @function PyObjCClass_UnbuildClass
 * @abstract Undo the work of PyObjCClass_BuildClass
 * @param Class A class created by PyObjCClass_BuildClass
 * @result 0 on success, -1 on failure
 * @discussion
 *    This function destroys the class created by PyObjCClass_BuildClass. This
 *    function can only be called when PyObjCClass_FinishClass has not been 
 *    called for the class.
 *
 *    This limitation is necessary because it is not possible to remove classes
 *    from the Objetive-C runtime on MacOS X.
 */
int PyObjCClass_UnbuildClass(Class new_class);


/*!
 * @function PyObjCClass_FinishClass
 * @abstract Register the class in the Objective-C runtime
 * @param objc_class A class created by PyObjCClass_BuildClass
 * @result Returns 0 on success, -1 on failure.
 * @discussion
 *    This function updates the bookkeeping information for objc_class and
 *    then registers the class with the Objective-C runtime.
 */
int PyObjCClass_FinishClass(Class objc_class);

#endif /* OBJC_CLASS_BUILDER */
