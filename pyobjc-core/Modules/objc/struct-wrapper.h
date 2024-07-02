#ifndef PyObjC_STRUCT_WRAPPER
#define PyObjC_STRUCT_WRAPPER

NS_ASSUME_NONNULL_BEGIN

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
 * @param pack       Value of 'pragma pack', use -1 for default packing
 * @result Returns a newly allocated type or NULL
 * @discussion
 *    The name, doc and fieldnames should be pointers to static strings,
 *    this function will not copy them.
 *
 *    If tpinit is NULL the type will have a default __init__ that initializes
 *    the fields to None and uses its arguments to optionally initialize the
 *    fields.
 *
 */
PyObject* _Nullable PyObjC_MakeStructType(const char* name, const char* _Nullable doc,
                                          initproc _Nullable tpinit, Py_ssize_t numFields,
                                          const char* _Nonnull* _Nonnull fieldnames,
                                          const char* typestr, Py_ssize_t pack);

/*!
 * @function PyObjC_RegisterStructType
 * @abstract Create a new struct-like type and register it with the bridge
 * @param signature  Objective-C signature for the struct
 * @param name       Name of the type, should include the module name
 * @param doc        Docstring for the type
 * @param tpinit     Optional __init__ method for the type
 * @param numFields  Number of fields in the type
 * @param fieldnames Field names, there should be exactly numFields names.
 * @param pack       Value of 'pragma pack', use -1 for default packing
 * @result Returns a newly allocated type or NULL
 * @discussion
 *    This function calls PyObjC_MakeStructType(name, doc, tpinit, numFields,
 *    fieldnames) and then adds the created type to an internal lookup table.
 *
 *    PyObjC_CreateRegisteredStruct can then be used to create instances of
 *    the type.
 */
PyObject* _Nullable PyObjC_RegisterStructType(const char* signature, const char* name,
                                              const char* _Nullable doc,
                                              initproc _Nullable tpinit,
                                              Py_ssize_t numFields,
                                              const char* _Nonnull* _Nullable fieldnames,
                                              Py_ssize_t pack);

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
PyObject* _Nullable PyObjC_CreateRegisteredStruct(
    const char* signature, Py_ssize_t len, const char* _Nonnull* _Nullable objc_signature,
    Py_ssize_t* _Nullable pack);

/*!
 * @function PyObjC_RegisterStructAlias
 * @param signature  An Objective-C signature for a struct type
 * @param type       The type to use for wrapping this struct type,
 *                   this should be a type created with PyObjC_MakeStructType
 *                   for a struct with a compatible signature.
 * @result -1 on error, 0 on success.
 * @discussion
 *
 *     This function is used to ensure that there is only one
 *     wrapper type for C structures that are the same except for
 *     the struct tag and that are used for the same tasks.
 *
 *     An example of this are NSRect and CGRect (in 32-bit code
 *     this are two separate struct types, in 64-bit code NSRect
 *     is already an alias for CGRect). By using this function PyObjC
 *     ensures that NSRect is always an alias for CGRect in Python code.
 */
int PyObjC_RegisterStructAlias(const char* signature, PyObject* type);

/*!
 * @function PyObjC_FindRegisteredStruct
 * @param signature   An Objective-C signature for a struct type
 * @param len         Length of the signature string
 * @result A type registered with PyObjC_CreateRegisteredStruct or
 * PyObjC_RegisterStructAlias, or NULL when such a type cannot be found.
 *
 * @discussion
 *     This function will not set an error when it cannot find
 *     a wrapper for the specified Objective-C type.
 */
extern PyObject* _Nullable PyObjC_FindRegisteredStruct(const char* signature,
                                                       Py_ssize_t  len);

extern int PyObjC_SetStructField(PyObject* strval, Py_ssize_t inde, PyObject* value);
extern PyObject* _Nullable StructAsTuple(PyObject* strval);

extern PyTypeObject StructBase_Type;
#define PyObjCStruct_Check(obj) PyObject_TypeCheck(obj, &StructBase_Type)

NS_ASSUME_NONNULL_END

#endif /* PyObjC_STRUCT_MEMBER */
