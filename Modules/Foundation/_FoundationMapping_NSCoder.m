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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				signature, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void 
imp_NSCoder_encodeValueOfObjCType_at_(id self, SEL sel,
	char* signature, void* buf)	
{
	PyObject* result;
	PyObject* arglist;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	
	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 2, PyObjC_ObjCToPython(signature, buf));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	Py_DECREF(result);
	PyGILState_Release(state);
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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				signature, count, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void 
imp_NSCoder_encodeArrayOfObjCType_count_at_(id self, SEL sel,
	char* signature, unsigned count, void* buf)	
{
	PyObject* result;
	PyObject* arglist;
	PyObject* values;
	int       size;
	int       i;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 2, PyInt_FromLong(count));

	values = PyTuple_New(count);
	if (values == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	for (i = 0; (unsigned)i < count; i++) {
		PyTuple_SetItem(values, i, PyObjC_ObjCToPython(signature, 
			((char*)buf)+(i*size)));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		Py_DECREF(values);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	PyTuple_SetItem(arglist, 3, values);

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(result);
	PyGILState_Release(state);
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


	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				signature, buf);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

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
imp_NSCoder_decodeValueOfObjCType_at_(id self, SEL sel,
	char* signature, void* buf)	
{
	PyObject* result;
	PyObject* arglist;
	int err;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyString_FromString(signature));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	err = PyObjC_PythonToObjC(signature, result, buf);
	Py_DECREF(result);

	if (err == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyGILState_Release(state);
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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method), 
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				signature, count, buf);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

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
imp_NSCoder_decodeArrayOfObjCType_count_at_(id self, SEL sel,
	char* signature, unsigned count, void* buf)	
{
	PyObject* result;
	PyObject* arglist;
	PyObject* values;
	PyObject* seq;
	int       size;
	int       i;
	int res;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	size = PyObjCRT_SizeOfType(signature);
	if (size == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 2, PyInt_FromLong(count));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	seq = PySequence_Fast(result, "Must return a sequence of length 2");
	if (seq == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (PySequence_Fast_GET_SIZE(seq) != 2) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_TypeError,
			"Must return a sequence of length 2");
		Py_DECREF(seq);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (PySequence_Fast_GET_ITEM(seq, 0) != Py_None) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[0] must be Py_None");
		Py_DECREF(seq);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	values = PySequence_Fast_GET_ITEM(seq, 1);
	if (values == NULL) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[1] must be a sequence");
		Py_DECREF(seq);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(seq);

	if ((unsigned)PySequence_Fast_GET_SIZE(values) != count) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[1] must be a of correct size");
		Py_DECREF(values);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}


	for (i = 0; (unsigned)i < count; i++) {
		res = PyObjC_PythonToObjC(signature, 
			PySequence_Fast_GET_ITEM(values, i),
			((char*)buf)+(i*size));
		if (res == -1) {
			Py_DECREF(values);
			PyObjCErr_ToObjCWithGILState(&state);
		}
	}
	Py_DECREF(values);
	PyGILState_Release(state);
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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				bytes, length);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void 
imp_NSCoder_encodeBytes_length_(id self, SEL sel, char* bytes, int length)	
{
	PyObject* result;
	PyObject* arglist;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyString_FromStringAndSize(bytes, length));
	PyTuple_SetItem(arglist, 2, PyInt_FromLong(length));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(result);
	PyGILState_Release(state);
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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes = (void*)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				&size);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		bytes = NULL;
	NS_ENDHANDLER

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

static void* 
imp_NSCoder_decodeBytesWithReturnedLength_(id self, SEL sel, unsigned* length)
{
	PyObject* result;
	PyObject* arglist;
	void* bufptr;
	int buflen;
	int len;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	if (!PyTuple_Check(result)) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	if (PyObject_AsReadBuffer(
			PyTuple_GET_ITEM(result, 0), 
			(const void**)&bufptr, &buflen) < 0) {
		
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}
	
	if (PyObjC_PythonToObjC(@encode(int), 
			PyTuple_GET_ITEM(result, 1), &len) < 0) {
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	if (len < buflen) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	*length = len;

	/* Should return an autoreleased buffer, do this by createing an 
	 * NSData that will release the buffer
	 */
	bufptr =  (void*)[[[[NSData alloc] initWithBytes:bufptr length:len] 
		  autorelease] bytes];

	Py_DECREF(result);
	PyGILState_Release(state);
	return bufptr;
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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes = (void*)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				key,
				&size);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		bytes = NULL;
	NS_ENDHANDLER

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

static void* 
imp_NSCoder_decodeBytesForKey_returnedLength_(id self, SEL sel, id key, unsigned* length)
{
	PyObject* result;
	PyObject* arglist;
	void* bufptr;
	int buflen;
	int len;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyObjC_IdToPython(key));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	if (!PyTuple_Check(result)) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	if (PyObject_AsReadBuffer(
			PyTuple_GET_ITEM(result, 0), 
			(const void**)&bufptr, &buflen) < 0) {
		
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}
	
	if (PyObjC_PythonToObjC(@encode(int), 
			PyTuple_GET_ITEM(result, 1), &len) < 0) {
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	if (len < buflen) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	*length = len;

	/* Should return an autoreleased buffer, do this by createing an 
	 * NSData that will release the buffer
	 */
	bufptr =  (void*)[[[[NSData alloc] initWithBytes:bufptr length:len] 
		  autorelease] bytes];

	Py_DECREF(result);
	PyGILState_Release(state);
	return bufptr;
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

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				bytes, size, key);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void 
imp_NSCoder_encodeBytes_length_forKey_(
	id self, SEL sel, char* bytes, int length, id key)	
{
	PyObject* result;
	PyObject* arglist;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	PyTuple_SetItem(arglist, 0, PyObjC_IdToPython(self));
	PyTuple_SetItem(arglist, 1, PyString_FromStringAndSize(bytes, length));
	PyTuple_SetItem(arglist, 2, PyInt_FromLong(length));
	PyTuple_SetItem(arglist, 3, PyObjC_IdToPython(key));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(result);
	PyGILState_Release(state);
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
			(IMP)imp_NSCoder_encodeArrayOfObjCType_count_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeValueOfObjCType:at:),
			call_NSCoder_encodeValueOfObjCType_at_,
			(IMP)imp_NSCoder_encodeValueOfObjCType_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeArrayOfObjCType:count:at:),
			call_NSCoder_decodeArrayOfObjCType_count_at_,
			(IMP)imp_NSCoder_decodeArrayOfObjCType_count_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeValueOfObjCType:at:),
			call_NSCoder_decodeValueOfObjCType_at_,
			(IMP)imp_NSCoder_decodeValueOfObjCType_at_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeBytes:length:),
			call_NSCoder_encodeBytes_length_,
			(IMP)imp_NSCoder_encodeBytes_length_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(encodeBytes:length:forKey:),
			call_NSCoder_encodeBytes_length_forKey_,
			(IMP)imp_NSCoder_encodeBytes_length_forKey_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeBytesWithReturnedLength:),
			call_NSCoder_decodeBytesWithReturnedLength_,
			(IMP)imp_NSCoder_decodeBytesWithReturnedLength_) < 0) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSCoder,
			@selector(decodeBytesForKey:returnedLength::),
			call_NSCoder_decodeBytesForKey_returnedLength_,
			(IMP)imp_NSCoder_decodeBytesForKey_returnedLength_) < 0) {
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
