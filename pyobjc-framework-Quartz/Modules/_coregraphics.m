/*
 * Manual wrappers for CoreGraphics
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

#if PyObjC_BUILD_RELEASE >= 1005
static PyObject*
m_CGFontCopyTableTags(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_font;
	CGFontRef font;
	CFArrayRef tags;

	if (!PyArg_ParseTuple(args, "O", &py_font)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CGFontRef), py_font, &font) == -1) {
		return NULL;
	}

	tags = NULL;
	PyObjC_DURING
		tags = CGFontCopyTableTags(font);

	PyObjC_HANDLER
		tags = NULL;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (tags == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (tags == NULL)  {
		Py_INCREF(Py_None);
		return Py_None;
	}

	Py_ssize_t len = CFArrayGetCount(tags);
	Py_ssize_t i;
	PyObject* result = PyTuple_New(len);
	if (result == NULL) {
		CFRelease(tags);
		return NULL;
	}

	for (i = 0; i < len; i++) {
		uint32_t cur = (uint32_t)(uintptr_t)CFArrayGetValueAtIndex(tags, i);
		PyObject* v = PyObjC_ObjCToPython(@encode(uint32_t), &cur);
		if (v == NULL) {
			CFRelease(tags);
			return NULL;
		}
		PyTuple_SET_ITEM(result, i, v);
	}
	CFRelease(tags);
	return result;
}

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
		CGWindowID cur = (CGWindowID)(NSInteger)CFArrayGetValueAtIndex(windowList, i);
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
		CFArrayAppendValue(array, (const void*)(NSInteger)windowID);
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
#endif /* PyObjC_BUILD_RELEASE >= 1005*/

static PyObject*
m_CGBitmapContextCreate(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_data;
	PyObject* py_width;
	PyObject* py_height;
	PyObject* py_bitsPerComponent;
	PyObject* py_bytesPerRow;
	PyObject* py_colorSpace;
	PyObject* py_bitmapInfo;

	void*	data;
	size_t  width;
	size_t  height;
	size_t  bitsPerComponent;
	size_t  bytesPerRow;
	CGColorSpaceRef colorSpace;
	CGBitmapInfo bitmapInfo;

	if (!PyArg_ParseTuple(args, "OOOOOOO", &py_data, &py_width, &py_height, &py_bitsPerComponent, &py_bytesPerRow, &py_colorSpace, &py_bitmapInfo)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(size_t), py_width, &width) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(size_t), py_height, &height) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(size_t), py_bitsPerComponent, &bitsPerComponent) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(size_t), py_bytesPerRow, &bytesPerRow) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CGColorSpaceRef), py_colorSpace, &colorSpace) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CGBitmapInfo), py_bitmapInfo, &bitmapInfo) == -1) {
		return NULL;
	}

	if (py_data == Py_None) {
		data = NULL;

	} else if (PyUnicode_Check(py_data)) {
		PyErr_SetString(PyExc_TypeError, "Cannot use Unicode as backing store");
		return NULL;

	} else {
		Py_ssize_t size;

		if (PyObject_AsWriteBuffer(py_data, &data, &size) == -1) {
			return NULL;
		}
	}


	CGContextRef ctx = NULL;
	PyObjC_DURING
		ctx = CGBitmapContextCreate(data, width, height, bitsPerComponent, bytesPerRow, colorSpace, bitmapInfo);

	PyObjC_HANDLER
		ctx = NULL;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (ctx == NULL && PyErr_Occurred()) {
		return NULL;
	}

	if (ctx == NULL)  {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* rv = PyObjC_ObjCToPython(@encode(CGContextRef), &ctx);
	CFRelease(ctx);
	return rv;
}

#if PyObjC_BUILD_RELEASE >= 1006
static void
m_releasecallback(void* releaseInfo, void* data)
{
	PyObject* py_data = (PyObject*)releaseInfo;

	PyGILState_STATE   state = PyGILState_Ensure();

	if (PyTuple_GET_ITEM(releaseInfo, 0) != Py_None) {
		PyObject* r = PyObject_CallFunction(
			PyTuple_GET_ITEM(py_data, 0), "OO",
			PyTuple_GET_ITEM(py_data, 1),
			PyTuple_GET_ITEM(py_data, 2));
		Py_XDECREF(r);
	}

	Py_DECREF(py_data);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyGILState_Release(state);

}

static PyObject*
m_CGBitmapContextCreateWithData(PyObject* self __attribute__((__unused__)), 
		PyObject* args)
{
	PyObject* py_data;
	PyObject* py_width;
	PyObject* py_height;
	PyObject* py_bitsPerComponent;
	PyObject* py_bytesPerRow;
	PyObject* py_colorSpace;
	PyObject* py_bitmapInfo;
	PyObject* py_releaseCallback;
	PyObject* py_releaseInfo;

	void*	data;
	size_t  width;
	size_t  height;
	size_t  bitsPerComponent;
	size_t  bytesPerRow;
	CGColorSpaceRef colorSpace;
	CGBitmapInfo bitmapInfo;

	if (!PyArg_ParseTuple(args, "OOOOOOOOO", 
		&py_data, &py_width, &py_height, &py_bitsPerComponent, 
		&py_bytesPerRow, &py_colorSpace, &py_bitmapInfo,
		&py_releaseCallback, &py_releaseInfo
		)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(size_t), py_width, &width) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(size_t), py_height, &height) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(size_t), py_bitsPerComponent, &bitsPerComponent) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(size_t), py_bytesPerRow, &bytesPerRow) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CGColorSpaceRef), py_colorSpace, &colorSpace) == -1) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CGBitmapInfo), py_bitmapInfo, &bitmapInfo) == -1) {
		return NULL;
	}

	if (py_data == Py_None) {
		data = NULL;

	} else if (PyUnicode_Check(py_data)) {
		PyErr_SetString(PyExc_TypeError, "Cannot use Unicode as backing store");
		return NULL;

	} else {
		Py_ssize_t size;

		if (PyObject_AsWriteBuffer(py_data, &data, &size) == -1) {
			return NULL;
		}
	}

	PyObject* releaseInfo = PyTuple_New(3);
	if (releaseInfo == NULL) {
		return NULL;
	}
	PyTuple_SET_ITEM(releaseInfo, 0, py_releaseCallback);
	Py_INCREF(py_releaseCallback);
	PyTuple_SET_ITEM(releaseInfo, 1, py_releaseInfo);
	Py_INCREF(py_releaseInfo);
	PyTuple_SET_ITEM(releaseInfo, 2, py_data);
	Py_INCREF(py_data);


	CGContextRef ctx = NULL;
	PyObjC_DURING
		ctx = CGBitmapContextCreateWithData(data, width, height, bitsPerComponent, bytesPerRow, colorSpace, bitmapInfo, m_releasecallback, releaseInfo);

	PyObjC_HANDLER
		ctx = NULL;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (ctx == NULL && PyErr_Occurred()) {
		Py_DECREF(releaseInfo);
		return NULL;
	}

	if (ctx == NULL)  {
		Py_DECREF(releaseInfo);
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* rv = PyObjC_ObjCToPython(@encode(CGContextRef), &ctx);
	CFRelease(ctx);
	return rv;
}
#endif


static PyMethodDef mod_methods[] = {
#if PyObjC_BUILD_RELEASE >= 1005
	{
		"CGFontCopyTableTags",
		(PyCFunction)m_CGFontCopyTableTags,
		METH_VARARGS,
		NULL
	},
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
#endif /* PyObjC_BUILD_RELEASE >= 1005 */
	{
		"CGBitmapContextCreate",
		(PyCFunction)m_CGBitmapContextCreate,
		METH_VARARGS,
		NULL
	},
#if PyObjC_BUILD_RELEASE >= 1006
	{
		"CGBitmapContextCreateWithData",
		(PyCFunction)m_CGBitmapContextCreateWithData,
		METH_VARARGS,
		NULL
	},
#endif


	{ 0, 0, 0, }
};

PyObjC_MODULE_INIT(_coregraphics)
{
	PyObject* m = PyObjC_MODULE_CREATE(_coregraphics);
	if (!m) PyObjC_INITERROR();

#if PyObjC_BUILD_RELEASE >= 1005
	PyObject* d = PyModule_GetDict(m);
	if (!d) PyObjC_INITERROR();
#endif

        if (PyObjC_ImportAPI(m) < 0) PyObjC_INITERROR();

#if PyObjC_BUILD_RELEASE >= 1005
	if (CGFontCopyTableTags == NULL) {
		if (PyDict_DelItemString(d, "CGFontCopyTableTags") < 0) {
			PyObjC_INITERROR();
		}
	}

	if (CGWindowListCreate == NULL) {
		if (PyDict_DelItemString(d, "CGWindowListCreate") < 0) {
			PyObjC_INITERROR();
		}
	}

	if (CGWindowListCreateDescriptionFromArray == NULL) {
		if (PyDict_DelItemString(d, "CGWindowListCreateDescriptionFromArray") < 0) {
			PyObjC_INITERROR();
		}
	}

	if (CGWindowListCreateImageFromArray == NULL) {
		if (PyDict_DelItemString(d, "CGWindowListCreateImageFromArray") < 0) {
			PyObjC_INITERROR();
		}
	}
#endif 

	PyObjC_INITDONE();
}
