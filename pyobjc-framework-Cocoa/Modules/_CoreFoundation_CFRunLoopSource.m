#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static const void* 
mod_retain(const void* info) 
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_INCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_release(const void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_DECREF((PyObject*)info);
	PyGILState_Release(state);
}

static void 
mod_schedule(void* info, CFRunLoopRef rl, CFStringRef mode)
{
	if (info == NULL) return;

	PyGILState_STATE state = PyGILState_Ensure();
	if (PyTuple_GET_ITEM(info, 1) != Py_None)  {
		PyObject* py_info = PyTuple_GET_ITEM(info, 4);
		PyObject* py_rl = PyObjC_ObjCToPython(@encode(CFRunLoopRef), &rl);
		if (py_rl == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
		PyObject* py_mode = PyObjC_ObjCToPython(@encode(CFStringRef), &mode);
		if (py_rl == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}

		PyObject* result = PyObject_CallFunction(
			PyTuple_GET_ITEM(info, 1),
			"ONN", py_info, py_rl, py_mode);
		if (result == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
		Py_DECREF(result);
	}
	PyGILState_Release(state);
}

static void 
mod_cancel(void* info, CFRunLoopRef rl, CFStringRef mode)
{
	if (info == NULL) return;

	PyGILState_STATE state = PyGILState_Ensure();
	if (PyTuple_GET_ITEM(info, 2) != Py_None)  {
		PyObject* py_info = PyTuple_GET_ITEM(info, 4);
		PyObject* py_rl = PyObjC_ObjCToPython(@encode(CFRunLoopRef), &rl);
		if (py_rl == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
		PyObject* py_mode = PyObjC_ObjCToPython(@encode(CFStringRef), &mode);
		if (py_rl == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}

		PyObject* result = PyObject_CallFunction(
			PyTuple_GET_ITEM(info, 2),
			"ONN", py_info, py_rl, py_mode);
		if (result == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
		Py_DECREF(result);
	}
	PyGILState_Release(state);
}

static void 
mod_perform(void* info)
{
	if (info == NULL) return;

	PyGILState_STATE state = PyGILState_Ensure();
	if (PyTuple_GET_ITEM(info, 3) != Py_None)  {
		PyObject* py_info = PyTuple_GET_ITEM(info, 4);

		PyObject* result = PyObject_CallFunction(
			PyTuple_GET_ITEM(info, 3),
			"O", py_info);
		if (result == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
		Py_DECREF(result);
	}
	PyGILState_Release(state);
}

static CFRunLoopSourceContext mod_CFRunLoopSourceContext = {
	0,		
	NULL,
	mod_retain,
	mod_release,
	NULL,
	NULL,
	NULL,
	mod_schedule,
	mod_cancel,
	mod_perform
};

static PyObject*
mod_CFRunLoopSourceCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_order;
	PyObject* py_context;
	CFAllocatorRef allocator;
	CFIndex order;
	CFRunLoopSourceContext context = mod_CFRunLoopSourceContext;

	if (!PyArg_ParseTuple(args, "OOO", &py_allocator, &py_order, &py_context)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFIndex), py_order, &order) < 0) {
		return NULL;
	}

	if (!PyTuple_Check(py_context) || PyTuple_GET_SIZE(py_context) != 5) {
		PyErr_SetString(PyExc_ValueError, "context must be tuple of length 5");
		return NULL;
	}

	PyObject* v = PyTuple_GetItem(py_context, 0);
	if (!PyInt_Check(v) || PyInt_AsLong(v) != 0) {
		PyErr_SetString(PyExc_ValueError, "Version field must be 0");
		return NULL;
	}


	context.info = py_context;
	Py_INCREF(py_context);

	CFRunLoopSourceRef rv = NULL;
	PyObjC_DURING
		rv = CFRunLoopSourceCreate(
			allocator, order, &context);
		

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFRunLoopSourceRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}


static PyObject*
mod_CFRunLoopSourceGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_f;
	PyObject* py_context = NULL;
	CFRunLoopSourceRef f;
	CFRunLoopSourceContext context;

	if (!PyArg_ParseTuple(args, "O|O", &py_f, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFRunLoopSourceRef), py_f, &f) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFRunLoopSourceGetContext(f, &context);

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

	if (context.info == NULL) {
		Py_INCREF(PyObjC_NULL);
		return PyObjC_NULL;
	}

	Py_INCREF((PyObject*)(context.info));
	return (PyObject*)(context.info);
}

static PyMethodDef mod_methods[] = {
        {
		"CFRunLoopSourceCreate",
		(PyCFunction)mod_CFRunLoopSourceCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFRunLoopSourceGetContext",
		(PyCFunction)mod_CFRunLoopSourceGetContext,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFRunLoopSource(void);
void init_CFRunLoopSource(void)
{
	PyObject* m = Py_InitModule4("_CFRunLoopSource", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
