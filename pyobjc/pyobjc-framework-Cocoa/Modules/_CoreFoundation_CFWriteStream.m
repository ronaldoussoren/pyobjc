#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

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


static CFStreamClientContext mod_CFStreamClientContext = {
	0,		
	NULL,
	mod_retain,
	mod_release,
	NULL
};

static void
mod_CFWriteStreamClientCallBack(	
	CFWriteStreamRef f,
	CFStreamEventType eventType,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFWriteStreamRef), &f);
	PyObject* py_eventType = PyObjC_ObjCToPython(
		@encode(CFStreamEventType), &eventType);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 0),
		"NNO", py_f, py_eventType, PyTuple_GET_ITEM(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
mod_CFWriteStreamSetClient(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_stream;
	PyObject* py_streamEvents;
	PyObject* callout;
	PyObject* info;
	CFWriteStreamRef stream;
	CFOptionFlags streamEvents;

	if (!PyArg_ParseTuple(args, "OOOO", &py_stream, &py_streamEvents, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFWriteStreamRef), py_stream, &stream) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_streamEvents, &streamEvents) < 0) {
		return NULL;
	}

	CFStreamClientContext context = mod_CFStreamClientContext;
	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	Boolean rv = FALSE;
	PyObjC_DURING
		if (callout == Py_None) {
			rv = CFWriteStreamSetClient(
				stream, streamEvents, 
				NULL, &context);
		} else {
			rv = CFWriteStreamSetClient(
				stream, streamEvents, 
				mod_CFWriteStreamClientCallBack, &context);
		}

		
	PyObjC_HANDLER
		rv = FALSE;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	return PyBool_FromLong(rv);
}

static PyMethodDef mod_methods[] = {
        {
		"CFWriteStreamSetClient",
		(PyCFunction)mod_CFWriteStreamSetClient,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFWriteStream(void);
void init_CFWriteStream(void)
{
	PyObject* m = Py_InitModule4("_CFWriteStream", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
