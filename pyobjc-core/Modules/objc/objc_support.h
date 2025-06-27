/* Copyright (c) 1996,97,98 by Lele Gaifax. All Rights Reserved
 * Copyright (c) 2003-2021 Ronald Oussoren
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: objc_support.h,v
 * Revision: 1.16
 * Date: 1998/08/18 15:35:57
 *
 * Created Tue Sep 10 14:11:38 1996.
 *
 * TODO: the functions exported by this file should be changed, the names
 * should start with 'PyObjC' and should be the same as the names used in
 * pyobjc-api.h (where appropriate).
 */

#ifndef _objc_support_H
#define _objc_support_H

NS_ASSUME_NONNULL_BEGIN

extern BOOL PyObjC_signatures_compatible(const char* type1, const char* type2);
/* Returns True iff two typestrings are compatible:
 * - elements have same size
 * - 'id' is compatible with 'void*' and not with other types
 * - 'float'/'double' are not compatible with integer types.
 */

/*#F Takes a C value pointed by @var{datum} with its type encoded in
  @var{type}, that should be coming from an ObjC @encode directive,
  and returns an equivalent Python object where C structures and
  arrays are represented as tuples. */
extern PyObject* _Nullable pythonify_c_value(const char* type, const void* datum);
extern PyObject* _Nullable id_to_python(id _Nullable obj);
extern PyObject* _Nullable pythonify_c_return_value(const char* type, const void* datum);

extern PyObject* _Nullable pythonify_c_array_nullterminated(const char* type,
                                                            const void* datum,
                                                            BOOL        already_retained,
                                                            BOOL already_cfretained);

extern int depythonify_c_array_count(const char* type, Py_ssize_t count, BOOL strict,
                                     PyObject* value, void* datum, BOOL already_retained,
                                     BOOL already_cfretained);
extern Py_ssize_t c_array_nullterminated_size(PyObject* object,
                                              PyObject* _Nullable* _Nonnull seq);
extern int        depythonify_c_array_nullterminated(const char* type, Py_ssize_t count,
                                                     PyObject* value, void* datum,
                                                     BOOL already_retained,
                                                     BOOL already_cfretained);

/*#F Takes a Python object @var{arg} and translate it into a C value
  pointed by @var{datum} accordingly with the type specification
  encoded in @var{type}, that should be coming from an ObjC @encode
  directive.
  Returns NULL on success, or a static error string describing the
  error. */
extern int depythonify_c_value(const char* type, PyObject* arg, void* datum);
extern int depythonify_c_return_value(const char* type, PyObject* arg, void* datum);
extern int depythonify_python_object(PyObject* argument, id _Nullable* _Nonnull
                                     __attribute__((ns_returns_autoreleased)) datum);
extern int depythonify_c_return_array_count(const char* rettype, Py_ssize_t count,
                                            PyObject* arg, void* resp,
                                            BOOL already_retained,
                                            BOOL already_cfretained);
extern int depythonify_c_return_array_nullterminated(const char* rettype, PyObject* arg,
                                                     void* resp, BOOL already_retained,
                                                     BOOL already_cfretained);

extern Py_ssize_t PyObjCRT_SizeOfReturnType(const char* type) __attribute__((__pure__));
extern Py_ssize_t PyObjCRT_SizeOfType(const char* type) __attribute__((__pure__));
extern Py_ssize_t PyObjCRT_AlignOfType(const char* type) __attribute__((__pure__));
extern const char* _Nullable PyObjCRT_SkipTypeSpec(const char* type);
extern const char* _Nullable PyObjCRT_NextField(const char* type);
extern const char* PyObjCRT_SkipTypeQualifiers(const char* type);
extern Py_ssize_t  PyObjCRT_AlignedSize(const char* type) __attribute__((__pure__));
extern bool        PyObjCRT_IsValidEncoding(const char* type, Py_ssize_t type_length)
    __attribute__((__pure__));

extern const char* _Nullable PyObjCRT_RemoveFieldNames(char* buf, const char* type);

extern int PyObjCRT_RegisterVectorType(const char* typestr, PyObject* pytype);

NS_ASSUME_NONNULL_END

#endif /* _objc_support_H */
