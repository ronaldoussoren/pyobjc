/*
 * Manual wrappers for CFBitVector
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>


static PyObject* 
mod_CFBitVectorCreate(PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_bytes;
	Py_ssize_t count;
	CFAllocatorRef allocator;
	CFBitVectorRef vector;


	if (!PyArg_ParseTuple(args, "OO" Py_ARG_SIZE_T, &py_allocator, &py_bytes, &count)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	PyObject* buf;
	void* bytes;
	int r;
	Py_ssize_t byteCount;
	
	if (count == -1) {
		byteCount = -1;
	} else {
		byteCount = count / 8;
	}

        r = PyObjC_PythonToCArray(NO, NO, "z", py_bytes, &bytes, &byteCount, &buf);
	if (r == -1) {
		return NULL;
	}

	if (count == -1) {
		count = byteCount * 8;
	}

	vector = CFBitVectorCreate(allocator, bytes, count);

	PyObjC_FreeCArray(r, bytes);
	Py_XDECREF(buf);

	PyObject* result = PyObjC_ObjCToPython(@encode(CFBitVectorRef), &vector);
	if (vector) {
		CFRelease(vector);
	}
	return result;
}

static PyObject*
mod_CFBitVectorGetBits(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_vector;
	PyObject* py_range;
	PyObject* py_bytes;
	CFBitVectorRef vector;
	CFRange range;

	if (!PyArg_ParseTuple(args, "OOO", &py_vector, &py_range, &py_bytes)) {
		return NULL;
	}


	if (PyObjC_PythonToObjC(@encode(CFBitVectorRef), py_vector, &vector) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFRange), py_range, &range) < 0) {
		return NULL;
	}
	if (py_bytes != Py_None) {
		PyErr_Format(PyExc_ValueError, "argument 3: expecting None, got instance of %s",
			py_bytes->ob_type->tp_name);
		return NULL;
	}

	PyObject* buffer = PyString_FromStringAndSize(NULL, (range.length+7)/8);
	if (buffer == NULL) {
		return NULL;
	}
	memset(PyString_AsString(buffer), 0, (range.length+7)/8);

	CFBitVectorGetBits(vector, range, (unsigned char*)PyString_AsString(buffer));
	return buffer;
}





static PyMethodDef mod_methods[] = {
        {
		"CFBitVectorCreate",
		(PyCFunction)mod_CFBitVectorCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFBitVectorGetBits",
		(PyCFunction)mod_CFBitVectorGetBits,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFBitVector(void);
void init_CFBitVector(void)
{
	PyObject* m = Py_InitModule4("_CFBitVector", mod_methods, "", NULL,
		PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
