/*
 * Several methods of NSBezierPath cannot be handled automaticly because the 
 * size of a C-style array depends on the value of another argument.
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <AppKit/AppKit.h>

static PyObject* 
call_NSBezierPath_elementAtIndex_associatedPoints_(
	PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	PyObject* result;
	PyObject* v;
	struct objc_super super;
	int    idx;
	int    pointCount;
	NSPoint points[3];
	NSBezierPathElement res;
	
	if  (!PyArg_ParseTuple(arguments, "i", &idx)) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			res = ((NSBezierPathElement(*)(id,SEL,int,NSPoint*))
			   PyObjCIMP_GetIMP(method))(
			   	PyObjCObject_GetObject(self),
				PyObjCIMP_GetSelector(method),
				idx,
				points
			   );
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method), 
				PyObjCObject_GetObject(self));


			res = (NSBezierPathElement)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method), 
				idx,
				points);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	switch (res) {
	case NSMoveToBezierPathElement: pointCount = 1; break;
	case NSLineToBezierPathElement: pointCount = 1; break;
	case NSCurveToBezierPathElement: pointCount = 3; break;
	case NSClosePathBezierPathElement: pointCount = 0; break;
	default:
		PyErr_SetString(PyExc_ValueError, 
			"ObjC returned illegal value");
		return NULL;
	}

	result = PyTuple_New(2);
	if (result == NULL) return NULL;

	v = PyObjC_ObjCToPython(@encode(NSBezierPathElement), &res);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 0, v);

	v = PyObjC_CArrayToPython(@encode(NSPoint), points, pointCount);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 1, v);

	return result;
}

static PyObject* 
call_NSBezierPath_setAssociatedPoints_atIndex_(
	PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	int    idx;
	NSPoint points[3];
	PyObject* pointList;
	PyObject* seq;
	int i, len;
	
	if  (!PyArg_ParseTuple(arguments, "Oi", &pointList, &idx)) {
		return NULL;
	}

	memset(points, 0, sizeof(points));

	seq = PySequence_Fast(pointList, "points is not a sequence");
	if (seq == NULL) {
		return NULL;
	}

	len = PySequence_Fast_GET_SIZE(seq);
	if (len > 3) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_ValueError, "Need at most 3 elements");
		return NULL;
	}

	for (i = 0; i < len; i++) {
		int err = PyObjC_PythonToObjC(@encode(NSPoint), 
			PySequence_Fast_GET_ITEM(seq, i), points + i);
		if (err == -1) {
			return NULL;
		}
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL,NSPoint*,int))
			   PyObjCIMP_GetIMP(method))(
			   	PyObjCObject_GetObject(self),
				PyObjCIMP_GetSelector(method),
				points,
				idx);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));


			(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				points,
				idx);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	result = Py_None;
	Py_INCREF(result);

	return result;
}

static void 
imp_NSBezierPath_elementAtIndex_associatedPoints_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	int idx = *(int*)args[2];
	NSPoint* points = *(NSPoint**)args[3];

	PyObject* result;
	PyObject* seq = NULL;
	PyObject* arglist = NULL;
	PyObject* v;
	int err;
	int pointCount;
	int i;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	v = PyInt_FromLong(idx);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	seq = PySequence_Fast(result, "should return tuple of lenght 2");
	Py_DECREF(result);
	if (seq == NULL) goto error;

	if (PySequence_Fast_GET_SIZE(seq) != 2) {
		PyErr_SetString(PyExc_ValueError, 
			"should return tuple of lenght 2");
		goto error;
	}

	v = PySequence_Fast_GET_ITEM(seq, 0);

	err = PyObjC_PythonToObjC(@encode(NSBezierPathElement), v, resp);
	if (err == -1) goto error;

	v = PySequence_Fast(PySequence_Fast_GET_ITEM(seq, 1),
		"result[1] should be a sequence");
	if (v == NULL) goto error;

	switch (*(NSBezierPathElement*)resp) {
	case NSMoveToBezierPathElement: pointCount = 1; break;
	case NSLineToBezierPathElement: pointCount = 1; break;
	case NSCurveToBezierPathElement: pointCount = 3; break;
	case NSClosePathBezierPathElement: pointCount = 0; break;
	default:
		PyErr_SetString(PyExc_ValueError, 
			"Return[0] should be NS{*}PathElement");
		Py_DECREF(v);
		goto error;
	}

	if (PySequence_Fast_GET_SIZE(v) != pointCount) {
		PyErr_SetString(PyExc_ValueError,
			"wrong number of points");
		Py_DECREF(v);
		goto error;
	}

	for (i = 0; i < pointCount; i++) {
		err = PyObjC_PythonToObjC(@encode(NSPoint),
			PySequence_Fast_GET_ITEM(v, i),
			points + i);
		if (err == -1) {
			Py_DECREF(v);
			goto error;
		}
	}

	Py_DECREF(v);
	Py_DECREF(seq);
	PyGILState_Release(state);
	return;

error:
	*(NSBezierPathElement*)resp = 0;
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	Py_XDECREF(seq);
	PyObjCErr_ToObjCWithGILState(&state);
}


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_nsbezierpath(void);
void init_nsbezierpath(void)
{
	PyObject* m = Py_InitModule4("_nsbezierpath", mod_methods, "", NULL,
			PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	Class cls = objc_lookUpClass("NSBezierPath");
	if (!cls) return;

	if (PyObjC_RegisterMethodMapping(cls,
		@selector(elementAtIndex:associatedPoints:),
		call_NSBezierPath_elementAtIndex_associatedPoints_,
		imp_NSBezierPath_elementAtIndex_associatedPoints_) < 0 ) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(cls,
		@selector(setAssociatedPoints:atIndex:),
		call_NSBezierPath_setAssociatedPoints_atIndex_,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return;
	}

	return;
}
