#ifndef PyObjC_STRUCT_WRAPPER
#define PyObjC_STRUCT_WRAPPER
/*!
 * @header struct-wrapper.h
 * @abstract Creation of mutable struct-like types
 * @discussion
 *      This module defines a function that can be used to create
 *      types for mutable struct-like types. 
 *
 *      The struct-like type has the following properties:
 *
 *      - Fields can be accessed by name or index (e.g. instances can be
 *        used as mutable tuples)
 *      - Instances are not hasable
 *      - Instances can be pickled
 *      - Instances can be compared with sequences, and will compare equal
 *        to a tuple with equal values for the fields.
 *
 *      This module also defines a pair of functions to integrate this 
 *      functionality in PyObjC, that is to make it possible to translate
 *      C structs to instances of these struct-like types.
 */

/*!
 * @function PyObjC_MakeStructType
 * @abstract Create a mutable struct-like type
 * @param name       Name of the type, should include the module name
 * @param doc        Docstring for the type
 * @param tpinit     Optional __init__ method for the type
 * @param numFields  Number of fields in the type
 * @param fieldnames Field names, there should be exactly numFields names.
 * @result Returns a newly allocated type or NULL
 * @discussion
 *    The name, doc and fieldnames should be pointers to static strings,
 *    this function will not copy them.
 *
 *    If tpinit is NULL the type will have a default __init__ that initializes
 *    the fields to None and uses its arguments to optionally initiaze the
 *    fields. 
 *
 */
PyObject* PyObjC_MakeStructType(
	const char* name,
	const char* doc,
	initproc tpinit,
	Py_ssize_t numFields,
	const char** fieldnames,
	const char* typestr);


/*!
 * @function PyObjC_RegisterStructType
 * @abstract Create a new struct-like type and register it with the bridge
 * @param signature  Objective-C signature for the struct
 * @param name       Name of the type, should include the module name
 * @param doc        Docstring for the type
 * @param tpinit     Optional __init__ method for the type
 * @param numFields  Number of fields in the type
 * @param fieldnames Field names, there should be exactly numFields names.
 * @result Returns a newly allocated type or NULL
 * @discussion
 *    This function calls PyObjC_MakeStructType(name, doc, tpinit, numFields, 
 *    fieldnames) and then adds the created type to an internal lookup table.
 *
 *    PyObjC_CreateRegisteredStruct can then be used to create instances of
 *    the type.
 */
PyObject* PyObjC_RegisterStructType(
	const char* signature,
	const char* name,
	const char* doc,
	initproc tpinit,
	Py_ssize_t numFields,
	const char** fieldnames);

/*!
 * @function PyObjC_CreateRegisteredStruct
 * @param signature  An Objective-C signature for a struct type
 * @param len        Length of the signature string
 * @param objc_signature 
 *                If not null this will be set to the signature that
 *                was used to register the struct type. This might include
 *                type codes that are private to PyObjC (such as _C_NSBOOL)
 *
 * @result A new instance or NULL
 * @discussion
 *     This function will not set an error when it cannot find or create
 *     a wrapper for the specified Objective-C type.
 *
 *     The returned instance is uninitialized, all fields are NULL. The 
 *     __init__ method has not been called.
 */     
PyObject* PyObjC_CreateRegisteredStruct(const char* signature, Py_ssize_t len, const char** objc_signature);

#endif /* PyObjC_STRUCT_MEMBER */
