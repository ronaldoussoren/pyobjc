/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 * Copyright (2) 2003 Ronald Oussoren
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

/*#F Takes a C value pointed by @var{datum} with its type encoded in
  @var{type}, that should be coming from an ObjC @encode directive,
  and returns an equivalent Python object where C structures and
  arrays are represented as tuples. */
extern PyObject *pythonify_c_value (const char *type,
				    void *datum);
extern PyObject *pythonify_c_return_value (const char *type,
				    void *datum);

extern PyObject *pythonify_c_array_nullterminated(const char* type, void* datum, BOOL already_retained, BOOL already_cfretained);

extern int depythonify_c_array_count(const char* type, Py_ssize_t count, BOOL strict, PyObject* value, void* datum, BOOL already_retained, BOOL already_cfretained);
extern Py_ssize_t c_array_nullterminated_size(PyObject* object, PyObject** seq);
extern int depythonify_c_array_nullterminated(const char* type, Py_ssize_t count, PyObject* value, void* datum, BOOL already_retained, BOOL already_cfretained);

/*#F Takes a Python object @var{arg} and translate it into a C value
  pointed by @var{datum} accordingly with the type specification
  encoded in @var{type}, that should be coming from an ObjC @encode
  directive.
  Returns NULL on success, or a static error string describing the
  error. */
extern int depythonify_c_value (const char *type,
					PyObject *arg,
					void *datum);
extern int depythonify_c_return_value (const char *type,
					PyObject *arg,
					void *datum);

extern int depythonify_c_return_array_count(const char* rettype, Py_ssize_t count, PyObject* arg, void* resp, BOOL already_retained, BOOL already_cfretained);
extern int depythonify_c_return_array_nullterminated(const char* rettype, PyObject* arg, void* resp, BOOL already_retained, BOOL already_cfretained);


extern Py_ssize_t PyObjCRT_SizeOfReturnType(const char* type);
extern Py_ssize_t PyObjCRT_SizeOfType(const char *type);
extern Py_ssize_t PyObjCRT_AlignOfType(const char *type);
extern const char *PyObjCRT_SkipTypeSpec (const char *type);
extern const char* PyObjCRT_NextField(const char *type);
extern const char* PyObjCRT_SkipTypeQualifiers (const char* type);
extern Py_ssize_t PyObjCRT_AlignedSize (const char *type);


extern const char* PyObjCRT_RemoveFieldNames(char* buf, const char* type);

/*
 * Compatibility with pyobjc-api.h
 */
static inline id PyObjC_PythonToId(PyObject* value)
{
	id res;
	int r;

	r = depythonify_c_value(@encode(id), value, &res);
	if (r == -1) {
		return NULL;
	} else {
		return res;
	}
}

static inline PyObject* PyObjC_IdToPython(id value)
{
	PyObject* res;

	res = pythonify_c_value(@encode(id), &value);
	return res;
}

#endif /* _objc_support_H */
