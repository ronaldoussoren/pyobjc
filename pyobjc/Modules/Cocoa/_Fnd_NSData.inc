/*
 * NSData mappings for special methods:
 * - initWithBytes_length_
 *
 * Should add:
 * -initWithBytesNoCopy:length:
 * -initWithBytesNoCopy:length:freeWhenDone
 * +allocWith... version of above
 * -getBytes...
 * 
 */

static PyObject* call_NSData_initWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	id        objc_result;

	if  (PyArg_ParseTuple(arguments, "s#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		objc_result = objc_msgSend(ObjCObject_GetObject(self),
				@selector(initWithBytes:length:),
				bytes, len);
		result = ObjC_IdToPython(objc_result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* supercall_NSData_initWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;

	if  (PyArg_ParseTuple(arguments, "s#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		super.receiver = ObjCObject_GetObject(self);
		super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

		objc_result = objc_msgSendSuper(&super,
				@selector(initWithBytes:length:),
				bytes, len);
		result = ObjC_IdToPython(objc_result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}


static id imp_NSData_initWithBytes_length_(id self, SEL sel,
		char* data, unsigned len)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return nil;
	}

	result = ObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	objc_result = ObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		ObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}
