/*
 * NSCoder mappings for special methods:
 * - encodeValueOfObjCType:at: 			[call, imp]
 * - decodeValueOfObjCType:at:			[call, imp]
 * - encodeArrayOfObjCType:count:at:		[call, imp]
 * - decodeArrayOfObjCType:count:at:		[call, imp]
 * - encodeBytes:length:			[call, imp]
 * - encodeBytes:length:forKey:			[call, imp]
 * - decodeBytesWithReturnedLength:		[call, imp]
 * - decodeBytesForKey:returnedLength:		[call, imp]
 *
 * Unsupported method:
 * - encodeValuesOfObjCTypes: 
 * - decodeValuesOfObjCTypes:
 *   These two require varargs parsing, might add this later on
 * - decodeBytesWithoutReturnedLength:
 *   Use ...WithReturnedLenght instead.
 *
 * XXX Check usage of self in upcalls, write unittests (including upcalls)
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"


static PyObject* 
call_NSCoder_encodeValueOfObjCType_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	PyObject* value;
	PyObject* result;
	void*     buf;
	int    size;
	int err;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "sO", &signature, &value)) {
		return NULL;
	}

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	err = PyObjC_PythonToObjC(signature, value, buf);
	if (err == -1) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					signature, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					signature, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	if (!PyErr_Occurred()) {
		result = Py_None;
		Py_INCREF(result);
	}

	return result;
}

static void 
imp_NSCoder_encodeValueOfObjCType_at_(
	void* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* signature = *(char**)args[2];
	void* buf = *(void**)args[3];

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;
	
	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0,  v);

	v = PyString_FromString(signature);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v);

	v = PyObjC_ObjCToPython(signature, buf);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (result != Py_None) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_TypeError, "Must return None");
		goto error;
	}

	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
}


static PyObject* 
call_NSCoder_encodeArrayOfObjCType_count_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	int   count;
	int   value_len, i;
	PyObject* value;
	PyObject* result;
	void*     buf;
	int    size;
	int err;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "siO", &signature, &count, &value)) {
		return NULL;
	}

	if (count < 0) {
		PyErr_SetString(PyExc_ValueError, "negative count");
		return NULL;
	}

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (!PySequence_Check(value)) {
		PyErr_SetString(PyExc_TypeError, "Need sequence of objects");
		return NULL;
	}

	value_len = PySequence_Size(value);
	if (value_len > count) {
		PyErr_SetString(PyExc_ValueError, "Inconsistent arguments");
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(signature, 
				PySequence_GetItem(value, i), 
				((char*)buf) + (size * i));
		if (err == -1) {
			return NULL;
		}
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,int, void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					signature, count, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					signature, count, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	if (!PyErr_Occurred()) {
		result = Py_None;
		Py_INCREF(result);
	}

	return result;
}

static void 
imp_NSCoder_encodeArrayOfObjCType_count_at_(
	void* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* signature = *(char**)args[2];
	unsigned count = *(unsigned*)args[3];
	void* buf = *(void**)args[4];

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyObject* values = NULL;
	int       size;
	int       i;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) goto error;

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyString_FromString(signature);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 2, v);

	values = PyTuple_New(count);
	if (values == NULL) goto error;

	for (i = 0; (unsigned)i < count; i++) {
		v = PyObjC_ObjCToPython(signature, ((char*)buf)+(i*size));
		if (v == NULL) goto error;
		PyTuple_SET_ITEM(values, i, v);
	}
	PyTuple_SET_ITEM(arglist, 3, values);
	values = NULL;

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		goto error;
	}
	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	Py_XDECREF(values);
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSCoder_decodeValueOfObjCType_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	PyObject* value;
	void*     buf;
	int    size;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "s", &signature)) {
		return NULL;
	}

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}


	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					signature, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					signature, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	value = PyObjC_ObjCToPython(signature, buf);
	if (value == NULL) {
		return NULL;
	}

	return value;
}

static void 
imp_NSCoder_decodeValueOfObjCType_at_(
	void* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* signature = *(char**)args[2];
	void* buf = *(void**)args[3];

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v;
	int err;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyString_FromString(signature);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	err = PyObjC_PythonToObjC(signature, result, buf);
	Py_DECREF(result);
	if (err == -1) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	return;
}

static PyObject* 
call_NSCoder_decodeArrayOfObjCType_count_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	int   count;
	int   i;
	PyObject* result;
	void*     buf;
	int    size;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "si", &signature, &count)) {
		return NULL;
	}

	if (count < 0) {
		PyErr_SetString(PyExc_ValueError, "negative count");
		return NULL;
	}

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,int, void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					signature, count, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method), 
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				signature, count, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	result = PyTuple_New(count);
	if (result == NULL) {
		return NULL;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(result, i,  PyObjC_ObjCToPython(signature, 
				((char*)buf) + (size * i)));
		if (PyTuple_GET_ITEM(result, i) == NULL) {
			Py_DECREF(result);
			return NULL;
		}
	}

	return result;
}

static void 
imp_NSCoder_decodeArrayOfObjCType_count_at_(
	void* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* signature = *(char**)args[2];
	unsigned count = *(unsigned*)args[3];
	void* buf = *(void**)args[4];

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	PyObject* seq = NULL;
	int       size;
	int       i;
	int res;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyString_FromString(signature);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	seq = PySequence_Fast(result, "Return-value must be a sequence");
	Py_DECREF(result);
	if (seq == NULL) goto error;

	if ((unsigned)PySequence_Fast_GET_SIZE(seq) != count) {
		PyErr_SetString(PyExc_TypeError,
			"return value must be a of correct size");
		goto error;
	}

	for (i = 0; (unsigned)i < count; i++) {
		res = PyObjC_PythonToObjC(signature, 
			PySequence_Fast_GET_ITEM(seq, i),
			((char*)buf)+(i*size));
		if (res == -1) goto error;
	}
	Py_DECREF(seq);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	Py_XDECREF(seq);
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSCoder_encodeBytes_length_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* bytes;
	int    size;
	int    length;

	PyObject* result;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "t#i", &bytes, &size, &length)) {
		return NULL;
	}

	if (length > size) {
		PyErr_SetString(PyExc_ValueError, "length > len(buf)");
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL,void*,int))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					bytes, length);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				bytes, length);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	if (!PyErr_Occurred()){
		result = Py_None;
		Py_INCREF(result);
	}

	return result;
}

static void 
imp_NSCoder_encodeBytes_length_(
	void* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* bytes = *(char**)args[2];
	int length = *(int*)args[3];

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyString_FromStringAndSize(bytes, length);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(length);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		goto error;
	}
	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSCoder_decodeBytesWithReturnedLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* 		bytes;
	unsigned int    size = 0;
	PyObject* v;
	PyObject* result;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			bytes = ((void*(*)(id,SEL,int*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					&size);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			bytes = (void*)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				&size);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		bytes = NULL;
	PyObjC_ENDHANDLER

	if (bytes == NULL) {
		if (PyErr_Occurred()) {
			return NULL;
		}

		result = PyTuple_New(2);
		if (result == NULL) {
			return NULL;
		}

		PyTuple_SET_ITEM(result, 0, Py_None);
		Py_INCREF(Py_None);

		v = PyObjC_ObjCToPython(@encode(unsigned), &size);
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SET_ITEM(result, 1, v);
		return result;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	v = PyString_FromStringAndSize((char*)bytes, size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 0, v);

	v = PyObjC_ObjCToPython(@encode(unsigned), &size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 1, v);

	return result;
}

static void 
imp_NSCoder_decodeBytesWithReturnedLength_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	unsigned* length = *(unsigned**)args[2];
	const void** pretval = (const void**)resp;

	PyObject* result;
	PyObject* v;
	PyObject* arglist = NULL;
	int buflen;
	int len;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (!PyTuple_Check(result)) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		goto error;
	}

	if (PyObject_AsReadBuffer(
			PyTuple_GET_ITEM(result, 0), 
			pretval, &buflen) < 0) {
		
		Py_DECREF(result);
		goto error;
	}
	
	if (PyObjC_PythonToObjC(@encode(int), 
			PyTuple_GET_ITEM(result, 1), &len) < 0) {
		Py_DECREF(result);
		goto error;
	}

	if (len < buflen) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		goto error;
	}

	*length = len;

	/* Should return an autoreleased buffer, do this by createing an 
	 * NSData that will release the buffer
	 */
	*pretval =  (const void*)[[[[NSData alloc] initWithBytes:*pretval length:len] 
		  autorelease] bytes];

	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
}

static PyObject* 
call_NSCoder_decodeBytesForKey_returnedLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* 		bytes;
	unsigned int    size = 0;
	PyObject* v;
	PyObject* result;
	id key;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "O&", PyObjCObject_Convert, &key)) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			bytes = ((void*(*)(id,SEL,id, int*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					key, &size);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			bytes = (void*)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				key,
				&size);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		bytes = NULL;
	PyObjC_ENDHANDLER

	if (bytes == NULL) {
		if (PyErr_Occurred()) {
			return NULL;
		}

		result = PyTuple_New(2);
		if (result == NULL) {
			return NULL;
		}

		PyTuple_SET_ITEM(result, 0, Py_None);
		Py_INCREF(Py_None);

		v = PyObjC_ObjCToPython(@encode(unsigned), &size);
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SET_ITEM(result, 1, v);
		return result;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	v = PyString_FromStringAndSize(bytes, size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 0, v);

	v = PyObjC_ObjCToPython(@encode(unsigned), &size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 1, v);

	return result;
}

static void 
imp_NSCoder_decodeBytesForKey_returnedLength_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	id key = *(id*)args[2];
	unsigned* length = *(unsigned**)args[3];
	const void** pretval = (const void**)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	int buflen;
	int len;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyObjC_IdToPython(key);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (!PyTuple_Check(result)) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		goto error;
	}

	if (PyObject_AsReadBuffer(
			PyTuple_GET_ITEM(result, 0), 
			pretval, &buflen) < 0) {
		
		Py_DECREF(result);
		goto error;
	}
	
	if (PyObjC_PythonToObjC(@encode(int), 
			PyTuple_GET_ITEM(result, 1), &len) < 0) {
		Py_DECREF(result);
		goto error;
	}

	if (len < buflen) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		goto error;
	}

	*length = len;

	/* Should return an autoreleased buffer, do this by createing an 
	 * NSData that will release the buffer
	 */
	*pretval =  (const void*)[[[[NSData alloc] initWithBytes:*pretval length:len] 
		  autorelease] bytes];

	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
}

static PyObject* 
call_NSCoder_encodeBytes_length_forKey_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* bytes;
	int    size;
	id     key;
	PyObject* result;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "t#O&", &bytes, &size, 
			PyObjCObject_Convert, &key)) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL,void*, int, id))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					bytes, size, key);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				bytes, size, key);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	if (!PyErr_Occurred()) {
		result = Py_None;
		Py_INCREF(result);
	}

	return result;
}

static void 
imp_NSCoder_encodeBytes_length_forKey_(
	void* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)), 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* bytes = *(char**)args[2];
	int length = *(int*)args[3];
	id key = *(id*)args[4];

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyString_FromStringAndSize(bytes, length);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(length);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 

	v = PyObjC_IdToPython(key);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 3, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (result != Py_None) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_TypeError, "Must return None");
		goto error;
	}
	Py_DECREF(result);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
}

static int 
_pyobjc_install_NSCoder(void)
{
	Class classNSCoder = objc_lookUpClass("NSCoder");
	if (classNSCoder == NULL) return 0;
  
	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeArrayOfObjCType:count:at:),
			call_NSCoder_encodeArrayOfObjCType_count_at_,
			imp_NSCoder_encodeArrayOfObjCType_count_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeValueOfObjCType:at:),
			call_NSCoder_encodeValueOfObjCType_at_,
			imp_NSCoder_encodeValueOfObjCType_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeArrayOfObjCType:count:at:),
			call_NSCoder_decodeArrayOfObjCType_count_at_,
			imp_NSCoder_decodeArrayOfObjCType_count_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeValueOfObjCType:at:),
			call_NSCoder_decodeValueOfObjCType_at_,
			imp_NSCoder_decodeValueOfObjCType_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeBytes:length:),
			call_NSCoder_encodeBytes_length_,
			imp_NSCoder_encodeBytes_length_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeBytes:length:forKey:),
			call_NSCoder_encodeBytes_length_forKey_,
			imp_NSCoder_encodeBytes_length_forKey_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeBytesWithReturnedLength:),
			call_NSCoder_decodeBytesWithReturnedLength_,
			imp_NSCoder_decodeBytesWithReturnedLength_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeBytesForKey:returnedLength::),
			call_NSCoder_decodeBytesForKey_returnedLength_,
			imp_NSCoder_decodeBytesForKey_returnedLength_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeBytesWithoutReturnedLength),
			PyObjCUnsupportedMethod_Caller,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeValuesOfObjCTypes:),
			PyObjCUnsupportedMethod_Caller,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeValuesOfObjCTypes:),
			PyObjCUnsupportedMethod_Caller,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;
	}

	return 0;
}
