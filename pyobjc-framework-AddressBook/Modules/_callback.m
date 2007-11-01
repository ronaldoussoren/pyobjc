/*
 * Support for a callback function.
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <AddressBook/AddressBook.h>
#import <AddressBook/ABAddressBookC.h>

static PyObject* callback_info = NULL;


static void
m_clientcallback(CFDataRef data, CFIndex tag, void* _refcon)
{
	PyObject* refcon = (PyObject*)_refcon;

	PyGILState_STATE   state = PyGILState_Ensure();

	PyObject* callable = PyTuple_GET_ITEM(refcon, 0);
	PyObject* info     = PyTuple_GET_ITEM(refcon, 1);
	PyObject* result;

	PyObject* py_tag = PyInt_FromLong((long)tag);
	if (py_tag == NULL) {
		/* NOTE: this is unlikely to fail, but if
		 * this ever happens we leak some memory.
		 */
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* py_data = PyObjC_ObjCToPython(@encode(CFDataRef), &data);

	if (py_data == NULL) {
		if (callback_info) {
			(void)PyDict_DelItem(callback_info, py_tag);
		}
		PyObjCErr_ToObjCWithGILState(&state);
	}

	result = PyObject_CallFunction(callable, "O&lO",
		py_data, data, tag, info);
	Py_DECREF(refcon);
	if (callback_info) {
		(void)PyDict_DelItem(callback_info, py_tag);
	}
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
m_ABCancelLoadingImageDataForTag(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	long tag;

	if (!PyArg_ParseTuple(args, "l", &tag)) {
		return NULL;
	}

	PyObjC_DURING
		ABCancelLoadingImageDataForTag(tag);
	
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (callback_info) {
		PyObject* p = PyInt_FromLong(tag);
		if (p) {
			PyDict_DelItem(callback_info, p);
		}
	}

	if (PyErr_Occurred()) {
		return NULL;
	}
	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* 
m_ABBeginLoadingImageDataForClient(PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	ABPersonRef person;
	PyObject* callback;
	PyObject* info;
	PyObject* refcon;
	CFIndex tag = 0;

	if (!PyArg_ParseTuple(args, "O&OO", PyObjCObject_Convert, &person,
		&callback, &info)) {

		return NULL;
	}

	if (!PyCallable_Check(callback)) {
		PyErr_SetString(PyExc_TypeError, "callback not callable");
		return NULL;
	}

	refcon = Py_BuildValue("OO", callback, info);
	if (refcon == NULL) {
		return NULL;
	}

	PyObjC_DURING
		tag = ABBeginLoadingImageDataForClient(
				person, m_clientcallback, refcon);
	
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		Py_DECREF(refcon);
		return NULL;
	}

	if (tag == 0) {
		Py_DECREF(refcon);
	}


	PyObject* py_tag =  Py_BuildValue("l", tag);
	if (py_tag == NULL) {
		ABCancelLoadingImageDataForTag(tag);
		Py_DECREF(refcon);
		return NULL;
	}


	if (callback_info == NULL) {
		callback_info = PyDict_New();
		if (callback_info == NULL) {
			ABCancelLoadingImageDataForTag(tag);
			Py_DECREF(refcon);
			Py_DECREF(py_tag);
			return NULL;

		}
	}

	if (PyDict_SetItem(callback_info, py_tag, refcon) < 0) {
		ABCancelLoadingImageDataForTag(tag);
		Py_DECREF(refcon);
		Py_DECREF(py_tag);
		return NULL;
	}

	Py_DECREF(refcon);
	return py_tag;
}

static PyMethodDef m_methods[] = {
	{
		"ABBeginLoadingImageDataForClient",
		(PyCFunction)m_ABBeginLoadingImageDataForClient,
		METH_VARARGS, NULL
	},
	{
		"ABCancelLoadingImageDataForTag",
		(PyCFunction)m_ABCancelLoadingImageDataForTag,
		METH_VARARGS, NULL
	},
	{
		0, 0, 0, 0
	}
};



void init_callback(void);
void init_callback(void)
{
	PyObject* m = Py_InitModule4("_callback", m_methods,
			NULL, NULL, PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) { return; }
}
