
#if PY_MAJOR_VERSION == 2
#  define BYTES_ARG "s"

#else
#  define BYTES_ARG "y"

#endif

static PyObject* 
call_NSCoder_encodeValueOfObjCType_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* typestr;
	PyObject* value;
	void*     buf;
	int    size;
	int err;
	struct objc_super super;
	Py_ssize_t typestr_len;

	if  (
		!PyArg_ParseTuple(arguments, BYTES_ARG "#O", &typestr, &typestr_len, &value)) {
		return NULL;
	}

	size = PyObjCRT_SizeOfType(typestr);
	if (size == -1) {
		return NULL;
	}
	buf = PyMem_Malloc(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	err = PyObjC_PythonToObjC(typestr, value, buf);
	if (err == -1) {
		PyMem_Free(buf);
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					typestr, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			((void(*)(struct objc_super*,SEL,char*,void*))objc_msgSendSuper)(&super,
					PyObjCSelector_GetSelector(method),
					typestr, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	PyMem_Free(buf);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
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
	char* typestr = *(char**)args[2];
	void* buf = *(void**)args[3];

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;
	
	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0,  pyself);
	Py_INCREF(pyself);

	v = PyBytes_FromString(typestr);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v);

	v = PyObjC_ObjCToPython(typestr, buf);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;

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
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
}


static PyObject* 
call_NSCoder_encodeArrayOfObjCType_count_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* typestr;
	NSUInteger   count;
	NSUInteger   i;
	int   value_len;
	PyObject* value;
	void*     buf;
	int    size;
	int err;
	struct objc_super super;
	Py_ssize_t typestr_len;

	if  (!PyArg_ParseTuple(arguments, BYTES_ARG "#" Py_ARG_NSUInteger "O", &typestr, &typestr_len, &count, &value)) {
		return NULL;
	}

	size = PyObjCRT_SizeOfType(typestr);
	if (size == -1) {
		return NULL;
	}
	buf = PyMem_Malloc(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (!PySequence_Check(value)) {
		PyMem_Free(buf);
		PyErr_SetString(PyExc_TypeError, "Need sequence of objects");
		return NULL;
	}

	value_len = PySequence_Size(value);
	if (value_len > count) {
		PyMem_Free(buf);
		PyErr_SetString(PyExc_ValueError, "Inconsistent arguments");
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(typestr, 
				PySequence_GetItem(value, i), 
				((char*)buf) + (size * i));
		if (err == -1) {
			PyMem_Free(buf);
			return NULL;
		}
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,NSUInteger, void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					typestr, count, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			((void(*)(struct objc_super*,SEL, char*, NSUInteger, void*))objc_msgSendSuper)(&super,
					PyObjCSelector_GetSelector(method),
					typestr, count, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	PyMem_Free(buf);
	if (PyErr_Occurred()) return NULL;

	Py_INCREF(Py_None);
	return Py_None;
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
	char* typestr = *(char**)args[2];
	NSUInteger count = *(NSUInteger*)args[3];
	void* buf = *(void**)args[4];

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyObject* values = NULL;
	Py_ssize_t    size;
	NSUInteger     i;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) goto error;

	size = PyObjCRT_SizeOfType(typestr);
	if (size == -1) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself);
	Py_INCREF(pyself);

	v = PyBytes_FromString(typestr);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v);

	values = PyTuple_New(count);
	if (values == NULL) goto error;

	for (i = 0; i < count; i++) {
		v = PyObjC_ObjCToPython(typestr, ((char*)buf)+(i*size));
		if (v == NULL) goto error;
		PyTuple_SetItem(values, i, v);
	}
	PyTuple_SetItem(arglist, 3, values);
	values = NULL;

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;

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
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie);
	}
	Py_XDECREF(values);
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSCoder_decodeValueOfObjCType_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* typestr;
	PyObject* value;
	void*     buf;
	Py_ssize_t    size, typestr_len;
	struct objc_super super;
	PyObject* py_buf;

	if  (!PyArg_ParseTuple(arguments, BYTES_ARG "#O", &typestr, &typestr_len, &py_buf)) {
		return NULL;
	}

	if (py_buf != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	size = PyObjCRT_SizeOfType(typestr);
	if (size == -1) {
		return NULL;
	}
	buf = PyMem_Malloc(size);
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
					typestr, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					typestr, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		PyMem_Free(buf);
		return NULL;
	}

	value = PyObjC_ObjCToPython(typestr, buf);
	PyMem_Free(buf);
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
	char* typestr = *(char**)args[2];
	void* buf = *(void**)args[3];

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v;
	int err;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	v = PyBytes_FromString(typestr);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	err = PyObjC_PythonToObjC(typestr, result, buf);
	Py_DECREF(result);
	if (err == -1) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
	return;
}

static PyObject* 
call_NSCoder_decodeArrayOfObjCType_count_at_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* typestr;
	NSUInteger   count;
	int   i;
	PyObject* result;
	PyObject* py_buf;
	void*     buf;
	int    size;
	struct objc_super super;
	Py_ssize_t typestr_len;

	if  (!PyArg_ParseTuple(arguments, BYTES_ARG "#" Py_ARG_NSUInteger "O", &typestr, &typestr_len, &count, &py_buf)) {
		return NULL;
	}

	if (py_buf != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	size = PyObjCRT_SizeOfType(typestr);
	if (size == -1) {
		return NULL;
	}
	buf = PyMem_Malloc(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, char*,NSUInteger, void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					typestr, count, buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method), 
				PyObjCObject_GetObject(self));

			((void(*)(struct objc_super*,SEL,char*,NSUInteger,void*))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				typestr, (NSUInteger)count, buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		PyMem_Free(buf);
		return NULL;
	}

	result = PyTuple_New(count);
	if (result == NULL) {
		PyMem_Free(buf);
		return NULL;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SetItem(result, i,  PyObjC_ObjCToPython(typestr, 
				((char*)buf) + (size * i)));
		if (PyTuple_GetItem(result, i) == NULL) {
			Py_DECREF(result);
			PyMem_Free(buf);
			return NULL;
		}
	}

	PyMem_Free(buf);
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
	char* typestr = *(char**)args[2];
	NSUInteger count = *(unsigned*)args[3];
	void* buf = *(void**)args[4];

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	PyObject* seq = NULL;
	Py_ssize_t       size;
	NSUInteger       i;
	int res;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	size = PyObjCRT_SizeOfType(typestr);
	if (size == -1) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	v = PyBytes_FromString(typestr);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	seq = PySequence_Fast(result, "Return-value must be a sequence");
	Py_DECREF(result);
	if (seq == NULL) goto error;

	if ((NSUInteger)PySequence_Fast_GET_SIZE(seq) != count) {
		PyErr_SetString(PyExc_TypeError,
			"return value must be a of correct size");
		goto error;
	}

	for (i = 0; i < count; i++) {
		res = PyObjC_PythonToObjC(typestr, 
			PySequence_Fast_GET_ITEM(seq, i),
			((char*)buf)+(i*size));
		if (res == -1) goto error;
	}
	Py_DECREF(seq);
	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	Py_XDECREF(seq);
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSCoder_encodeBytes_length_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* bytes;
	Py_ssize_t    size;
	Py_ssize_t    length;

	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, BYTES_ARG"#"Py_ARG_SIZE_T, &bytes, &size, &length)) {
		return NULL;
	}

	if (length > size) {
		PyErr_Format(PyExc_ValueError, "length %" PY_FORMAT_SIZE_T "d > len(buf) %" PY_FORMAT_SIZE_T "d",
			length, size);
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL,void*,NSUInteger))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					bytes, length);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			((void(*)(struct objc_super*,SEL,void*,NSUInteger))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				bytes, length);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	Py_INCREF(Py_None);
	return Py_None;
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
	NSUInteger length = *(int*)args[3];

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	v = PyBytes_FromStringAndSize(bytes, length);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(length);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
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
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSCoder_decodeBytesWithReturnedLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* 		bytes;
	NSUInteger    size = 0;
	PyObject* v;
	PyObject* result;
	PyObject* py_buf;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "O", &py_buf)) {
		return NULL;
	}
	if (py_buf != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			bytes = ((void*(*)(id,SEL,NSUInteger*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					&size);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			bytes = ((void*(*)(struct objc_super*,SEL,NSUInteger*))objc_msgSendSuper)(&super,
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

		PyTuple_SetItem(result, 0, Py_None);
		Py_INCREF(Py_None);

		v = PyObjC_ObjCToPython(@encode(unsigned), &size);
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SetItem(result, 1, v);
		return result;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	v = PyBytes_FromStringAndSize((char*)bytes, size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SetItem(result, 0, v);

	v = PyObjC_ObjCToPython(@encode(unsigned), &size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SetItem(result, 1, v);

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
	NSUInteger* length = *(NSUInteger**)args[2];
	const void** pretval = (const void**)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	Py_ssize_t buflen;
	NSUInteger len;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	if (!PyTuple_Check(result)) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		goto error;
	}

	if (PyObject_AsReadBuffer(
			PyTuple_GetItem(result, 0), 
			pretval, &buflen) < 0) {
		
		Py_DECREF(result);
		goto error;
	}
	
	if (PyObjC_PythonToObjC(@encode(NSUInteger), 
			PyTuple_GetItem(result, 1), &len) < 0) {
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
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
}

static PyObject* 
call_NSCoder_decodeBytesForKey_returnedLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* 		bytes;
	NSUInteger    size = 0;
	PyObject* v;
	PyObject* result;
	PyObject* py_buf;
	id key;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, "O&O", PyObjCObject_Convert, &key, &py_buf)) {
		return NULL;
	}
	if (py_buf != NULL) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			bytes = ((void*(*)(id,SEL,id, NSUInteger*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					key, (NSUInteger *)&size);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			bytes = ((void*(*)(struct objc_super*,SEL,id,NSUInteger*))objc_msgSendSuper)(&super,
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

		PyTuple_SetItem(result, 0, Py_None);
		Py_INCREF(Py_None);

		v = PyObjC_ObjCToPython(@encode(unsigned), &size);
		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}
		PyTuple_SetItem(result, 1, v);
		return result;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	v = PyBytes_FromStringAndSize(bytes, size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SetItem(result, 0, v);

	v = PyObjC_ObjCToPython(@encode(NSUInteger), &size);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SetItem(result, 1, v);

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
	NSUInteger* length = *(NSUInteger**)args[3];
	const void** pretval = (const void**)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	Py_ssize_t buflen;
	NSUInteger len;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

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
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	if (!PyTuple_Check(result)) {
		Py_DECREF(result);
		PyErr_SetString(PyExc_ValueError, 
			"Should return (bytes, length)");
		goto error;
	}

	if (PyObject_AsReadBuffer(
			PyTuple_GetItem(result, 0), 
			pretval, &buflen) < 0) {
		
		Py_DECREF(result);
		goto error;
	}
	
	if (PyObjC_PythonToObjC(@encode(NSUInteger), 
			PyTuple_GetItem(result, 1), &len) < 0) {
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
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
}

static PyObject* 
call_NSCoder_encodeBytes_length_forKey_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* 		bytes;
	Py_ssize_t  	size;
	id     		key;
	struct objc_super super;

	if  (!PyArg_ParseTuple(arguments, BYTES_ARG "#O&", &bytes, &size, 
			PyObjCObject_Convert, &key)) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL,void*, NSUInteger, id))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					bytes, size, key);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			((void(*)(struct objc_super*, SEL, void*, NSUInteger, id))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				bytes, (NSUInteger)size, key);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	Py_INCREF(Py_None);
	return Py_None;
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
	NSUInteger length = *(int*)args[3];
	id key = *(id*)args[4];

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	v = PyBytes_FromStringAndSize(bytes, length);
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
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
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
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
}

static int setup_nscoder(PyObject* m __attribute__((__unused__)))
{
	Class classNSCoder = objc_lookUpClass("NSCoder");
  
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
