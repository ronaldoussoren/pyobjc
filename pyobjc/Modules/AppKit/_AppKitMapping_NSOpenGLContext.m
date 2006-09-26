/*
 * Special wrappers for NSOpenGLContext methods with 'difficult' arguments.
 *
 * TODO:
 * -setOffScreen:width:height:rowbytes:
 * -CGLContextObj
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

static PyObject*
call_NSOpenGLContext_setValues_forParameter_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	long* values;
	PyObject* pyValues;
	PyObject* pyParam;
	PyObject* seq;
	NSOpenGLContextParameter param;
	Py_ssize_t count, i;


	if (!PyArg_ParseTuple(arguments, "OO", &pyValues, &pyParam)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSOpenGLContextParameter),
			pyParam, &param) == -1) {
		return NULL;
	}

	seq = PySequence_Fast(pyValues, "attributes must be a sequence");
	if (seq == NULL) {
		return NULL;
	}

	count = PySequence_Fast_GET_SIZE(seq);
#if 1
	if (param == NSOpenGLCPSwapRectangle) {
		if (count != 4) {
			Py_DECREF(seq);
			PyErr_Format(PyExc_ValueError,
				"param needs 4 integers, "
				"not %d", count);
			return NULL;
		}
	} else if (
			(param == NSOpenGLCPSwapRectangleEnable)
		||	(param == NSOpenGLCPRasterizationEnable)
		||	(param == NSOpenGLCPSwapInterval)
		||	(param == NSOpenGLCPSurfaceOrder)
		||	(param == NSOpenGLCPSurfaceOpacity)
		||	(param == NSOpenGLCPStateValidation)
	) {
		if (count != 1)  {
			Py_DECREF(seq);
			PyErr_Format(PyExc_ValueError,
				"param needs 1 integer, "
				"not %d", count);
			return NULL;
		}
	}
	/* else: lets hope the user knows what he's doing... */
#endif

	values = malloc(sizeof(long) * count);
	if (values == NULL) {
		Py_DECREF(seq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		if (PyObjC_PythonToObjC(
			@encode(long),
			PySequence_Fast_GET_ITEM(seq, i),
			values + i) == -1) {

			PyErr_SetString(PyExc_ValueError,
					"attribute values must be integers");

			Py_DECREF(seq);
			free(values);
			return NULL;
		}
	}
	Py_DECREF(seq);

	PyObjC_DURING
                if (PyObjCIMP_Check(method)) {
			((void(*)(id, SEL, long*, NSOpenGLContextParameter))
			 PyObjCIMP_GetIMP(method))(
				 PyObjCObject_GetObject(self),
				 PyObjCIMP_GetSelector(method),
				 values,
				 param);
		} else {
			PyObjC_InitSuper(
				&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));
		
			objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				values, param);
		}

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	free(values);
	if (PyErr_Occurred()) {
		return NULL;
	}
	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject*
call_NSOpenGLContext_getValues_forParameter_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	long* values;
	PyObject* pyParam;
	PyObject* seq;
	NSOpenGLContextParameter param;
	Py_ssize_t count, i;


	if (!PyArg_ParseTuple(arguments, "O", &pyParam)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSOpenGLContextParameter),
			pyParam, &param) == -1) {
		return NULL;
	}

	if (param == NSOpenGLCPSwapRectangle) {
		count = 4;
		
	} else if (
			(param == NSOpenGLCPSwapRectangleEnable)
		||	(param == NSOpenGLCPRasterizationEnable)
		||	(param == NSOpenGLCPSwapInterval)
		||	(param == NSOpenGLCPSurfaceOrder)
		||	(param == NSOpenGLCPSurfaceOpacity)
		||	(param == NSOpenGLCPStateValidation)
	) {
		count = 1;
	} else {
		PyErr_SetString(PyExc_ValueError, "Don't know how many values to allocate");
		return NULL;
	}

	values = malloc(sizeof(long) * count);
	if (values == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
                if (PyObjCIMP_Check(method)) {
			((void(*)(id, SEL, long*, NSOpenGLContextParameter))
			 PyObjCIMP_GetIMP(method))(
				 PyObjCObject_GetObject(self),
				 PyObjCIMP_GetSelector(method),
				 values,
				 param);
		} else {
			PyObjC_InitSuper(
				&super,
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));
		
			objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				values, param);
		}

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	seq = PyTuple_New(count);
	for (i = 0; i < count; i++) {
		PyObject* v = PyObjC_ObjCToPython(@encode(long), values+i);
		if (v == NULL) {
			free(values);
			Py_DECREF(seq);
			return NULL;
		}
	}

	free(values);
	return seq;
}

static int 
_pyobjc_install_NSOpenGLContext(void)
{
	Class classNSOpenGLContext = objc_lookUpClass("NSOpenGLContext");

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(CGLContextObj),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(getValues:forParameter:),
		call_NSOpenGLContext_getValues_forParameter_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(setValues:forParameter:),
		call_NSOpenGLContext_setValues_forParameter_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLContext,
		@selector(setOffScreen:width:height:rowbytes:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
