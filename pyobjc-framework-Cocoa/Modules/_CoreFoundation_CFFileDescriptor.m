#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

#if MAC_OS_X_VERSION_10_5 <= MAC_OS_X_VERSION_MAX_ALLOWED

static void* 
mod_retain(void* info) 
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_INCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_release(void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_DECREF((PyObject*)info);
	PyGILState_Release(state);
}


static CFFileDescriptorContext mod_CFFileDescriptorContext = {
	0,		
	NULL,
	mod_retain,
	mod_release,
	NULL
};

static void
mod_CFFileDescriptorCallBack(	
	CFFileDescriptorRef f,
	CFOptionFlags callBackType,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFFileDescriptorRef), &f);
	PyObject* py_callBackType = PyObjC_ObjCToPython(
		@encode(CFOptionFlags), &callBackType);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 0),
		"NNO", py_f, py_callBackType, PyTuple_GET_ITEM(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
mod_CFFileDescriptorCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_descriptor;
	PyObject* py_closeOnInvalidate;
	PyObject* callout;
	PyObject* info;
	CFAllocatorRef allocator;
	CFFileDescriptorNativeDescriptor descriptor;
	Boolean closeOnInvalidate;

	if (!PyArg_ParseTuple(args, "OOOOO", &py_allocator, &py_descriptor, &py_closeOnInvalidate, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFFileDescriptorNativeDescriptor), py_descriptor, &descriptor) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(bool), py_closeOnInvalidate, &closeOnInvalidate) < 0) {
		return NULL;
	}

	CFFileDescriptorContext context = mod_CFFileDescriptorContext;
	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFFileDescriptorRef rv = NULL;
	PyObjC_DURING
		rv = CFFileDescriptorCreate(
			allocator, descriptor, closeOnInvalidate,
			mod_CFFileDescriptorCallBack, &context);
		

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFFileDescriptorRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}


static PyObject*
mod_CFFileDescriptorGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_f;
	PyObject* py_context = NULL;
	CFFileDescriptorRef f;
	CFFileDescriptorContext context;

	if (!PyArg_ParseTuple(args, "O|O", &py_f, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFFileDescriptorRef), py_f, &f) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFFileDescriptorGetContext(f, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
		return NULL;
	}

	if (context.retain != mod_retain) {
		PyErr_SetString(PyExc_ValueError, 
			"retrieved context is not supported");
		return NULL;
	}

	Py_INCREF(PyTuple_GET_ITEM((PyObject*)context.info, 1));
	return PyTuple_GET_ITEM((PyObject*)context.info, 1);
}
#endif

static PyMethodDef mod_methods[] = {
#if MAC_OS_X_VERSION_10_5 <= MAC_OS_X_VERSION_MAX_ALLOWED
        {
		"CFFileDescriptorCreate",
		(PyCFunction)mod_CFFileDescriptorCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFFileDescriptorGetContext",
		(PyCFunction)mod_CFFileDescriptorGetContext,
		METH_VARARGS,
		NULL
	},
#endif
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFFileDescriptor(void);
void init_CFFileDescriptor(void)
{
	PyObject* m = Py_InitModule4("_CFFileDescriptor", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
