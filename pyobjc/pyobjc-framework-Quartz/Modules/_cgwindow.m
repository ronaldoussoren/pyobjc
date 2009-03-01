/*
 * Manual wrappers for CoreGraphics
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static PyObject*
m_CGWindowListCreate(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_option;
	PyObject* py_relativeToWindow;
	CGWindowListOption option;
	CGWindowID relativeToWindow;
	CFArrayRef windowList;

	if (!PyArg_ParseTuple(args, "OO", &py_option, &py_relativeToWindow)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CGWindowListOption), py_option, &option) == -1) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CGWindowID), py_relativeToWindow, &relativeToWindow) == -1) {
		return NULL;
	}

	windowList = NULL;
	PyObjC_DURING
		windowList = CGWindowListCreate(option, relativeToWindow);

	PyObjC_HANDLER
		windowList = NULL;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (windowList == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (windowList == NULL)  {
		Py_INCREF(Py_None);
		return Py_None;
	}

	Py_ssize_t len = CFArrayGetCount(windowList);
	Py_ssize_t i;
	PyObject* result = PyTuple_New(len);
	if (result == NULL) {
		CFRelease(windowList);
		return NULL;
	}

	for (i = 0; i < len; i++) {
		CGWindowID cur = (CGWindowID)CFArrayGetValueAtIndex(windowList, i);
		PyObject* v = PyObjC_ObjCToPython(@encode(CGWindowID), &cur);
		if (v == NULL) {
			CFRelease(windowList);
			return NULL;
		}
		PyTuple_SET_ITEM(result, i, v);
	}
	CFRelease(windowList);
	return result;
}


static CFArrayRef
createWindowList(PyObject* items)
{
	PyObject* seq = PySequence_Fast(items, "list of windowIDs");
	if (seq == NULL) {
		return NULL;
	}

	CFMutableArrayRef array = CFArrayCreateMutable(NULL, PySequence_Fast_GET_SIZE(seq), NULL);
	if (array == NULL) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "Cannot create CFArray");
		return NULL;
	}

	Py_ssize_t len = PySequence_Fast_GET_SIZE(seq);
	Py_ssize_t i;
	for (i = 0; i < len; i++) {
		CGWindowID windowID;

		if (PyObjC_PythonToObjC(@encode(CGWindowID), PySequence_Fast_GET_ITEM(seq, i), &windowID) == -1) {
			Py_DECREF(seq);
			CFRelease(array);
			return NULL;
		}
		CFArrayAppendValue(array, (const void*)windowID);
	}
	Py_DECREF(seq);
	return (CFArrayRef)array;
}

static PyObject*
m_CGWindowListCreateDescriptionFromArray(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_windowArray;
	CFArrayRef windowArray;

	if (!PyArg_ParseTuple(args, "O", &py_windowArray)) {
		return NULL;
	}

	windowArray = createWindowList(py_windowArray);
	if (windowArray == NULL) {
		return NULL;
	}

	CFArrayRef descriptions = NULL;
	PyObjC_DURING
		descriptions = CGWindowListCreateDescriptionFromArray(windowArray);

	PyObjC_HANDLER
		descriptions = NULL;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	CFRelease(windowArray);

	if (descriptions == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (descriptions == NULL)  {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* rv = PyObjC_ObjCToPython(@encode(CFArrayRef), &descriptions);
	CFRelease(descriptions);
	return rv;
}

static PyObject*
m_CGWindowListCreateImageFromArray(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_screenBounds;
	PyObject* py_windowArray;
	PyObject* py_imageOption;
	CGRect screenBounds;
	CFArrayRef windowArray;
	CGWindowImageOption imageOption;

	if (!PyArg_ParseTuple(args, "OOO", &py_screenBounds, &py_windowArray, &py_imageOption)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CGRect), py_screenBounds, &screenBounds) == -1) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CGWindowImageOption), py_imageOption, &imageOption) == -1) {
		return NULL;
	}


	windowArray = createWindowList(py_windowArray);
	if (windowArray == NULL) {
		return NULL;
	}

	CGImageRef image = NULL;
	PyObjC_DURING
		image = CGWindowListCreateImageFromArray(screenBounds, windowArray, imageOption);

	PyObjC_HANDLER
		image = NULL;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	CFRelease(windowArray);

	if (image == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (image == NULL)  {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* rv = PyObjC_ObjCToPython(@encode(CGImageRef), &image);
	CFRelease(image);
	return rv;
}


static PyMethodDef m_methods[] = {
	{
		"CGWindowListCreate",
		(PyCFunction)m_CGWindowListCreate,
		METH_VARARGS,
		NULL
	},
	{
		"CGWindowListCreateDescriptionFromArray",
		(PyCFunction)m_CGWindowListCreateDescriptionFromArray,
		METH_VARARGS,
		NULL
	},
	{
		"CGWindowListCreateImageFromArray",
		(PyCFunction)m_CGWindowListCreateImageFromArray,
		METH_VARARGS,
		NULL
	},


	{ 0, 0, 0, }
};

void init_cgwindow(void);
void init_cgwindow(void)
{
	PyObject* m = Py_InitModule4("_cgwindow", m_methods,
		NULL, NULL, PYTHON_API_VERSION);

        if (PyObjC_ImportAPI(m) < 0) { return; }
}
