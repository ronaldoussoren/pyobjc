/*
 * Manual wrappers for CFBag
 */
static PyObject*
mod_CFBagGetValues(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args)
{
	PyObject* py_bag;
	CFBagRef bag;


	if (!PyArg_ParseTuple(args, "O", &py_bag)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFBagRef), py_bag, &bag) < 0) {
		return NULL;
	}

	CFIndex count = CFBagGetCount(bag);
	NSObject** members = malloc(sizeof(NSObject*) * count);
	if (members == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
	memset(members, 0, sizeof(NSObject*) * count);

	CFBagGetValues(bag, (const void**)members);
	PyObject* result = PyObjC_CArrayToPython(@encode(NSObject*), members, (Py_ssize_t)count);
	free(members);
	return result;
}


static PyObject* 
mod_CFBagCreate(PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_members;
	Py_ssize_t count;
	CFAllocatorRef allocator;
	void** members;
	int r;
	PyObject* buf = NULL;
	CFBagRef bag;


	if (!PyArg_ParseTuple(args, "OO" Py_ARG_SIZE_T, &py_allocator, &py_members, &count)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	r = PyObjC_PythonToCArray(NO, NO, @encode(NSObject*), py_members, (void**)&members, &count, &buf);
	if (r == -1) {
		return NULL;
	}

	bag = CFBagCreate(allocator, (const void**)members, (CFIndex)count, &kCFTypeBagCallBacks);

	PyObjC_FreeCArray(r, members);
	Py_XDECREF(buf);

	PyObject* result = PyObjC_ObjCToPython(@encode(CFBagRef), &bag);
	if (bag) {
		CFRelease(bag);
	}
	return result;
}

static PyObject* 
mod_CFBagCreateMutable(PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	Py_ssize_t count;
	CFAllocatorRef allocator;
	CFBagRef bag;


	if (!PyArg_ParseTuple(args, "O" Py_ARG_SIZE_T, &py_allocator, &count)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	bag = CFBagCreateMutable(allocator, count, &kCFTypeBagCallBacks);

	PyObject* result = PyObjC_ObjCToPython(@encode(CFBagRef), &bag);
	if (bag) {
		CFRelease(bag);
	}
	return result;
}

#define COREFOUNDATION_CFBAG_METHODS \
        {						\
		"CFBagCreate",				\
		(PyCFunction)mod_CFBagCreate,		\
		METH_VARARGS,				\
		NULL					\
	},						\
        {						\
		"CFBagCreateMutable",			\
		(PyCFunction)mod_CFBagCreateMutable,	\
		METH_VARARGS,				\
		NULL					\
	},						\
        {						\
		"CFBagGetValues",			\
		(PyCFunction)mod_CFBagGetValues,	\
		METH_VARARGS,				\
		NULL					\
	},
