/*
 * This module contains custom mapping functions for problematic methods
 */

#include <Python.h>
#include <Foundation/Foundation.h>
#include <objc/objc-runtime.h>
#include "pyobjc-api.h"

/* mapping for NSMatrix.getNumberOfRows:columns: 
 *
 * -(void)getNumberOfRows:(int *)rowCount columns:(int *)columnCount 
 * 
 * mapped onto func() -> (int, int)
 *
 * TODO: call_* and supercall_* are almost the same, could generate these!
 */
static PyObject*
call_NSMatrix_getNumerOfRows_columns_(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	int       rowCount, columnCount;
	PyObject* result;

	if (PyArg_ParseTuple(arguments, "") < 0) {
		return NULL;
	}

	NS_DURING
		(void)objc_msgSend(ObjCObject_GetObject(self), 
					@selector(getNumberOfRows:columns:),
					&rowCount, &columnCount);

		result = PyTuple_New(2);
		if (result != NULL) {
			PyTuple_SET_ITEM(result,0,PyInt_FromLong(rowCount));
			PyTuple_SET_ITEM(result,1,PyInt_FromLong(columnCount));

			if (PyErr_Occurred()) {
				Py_DECREF(result);
				result = NULL;
			}
		}

	NS_HANDLER
		ObjCErr_FromObjC(localException);
		PyErr_Print();
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject*
supercall_NSMatrix_getNumerOfRows_columns_(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	int       rowCount, columnCount;
	PyObject* result;
	struct objc_super super;

	if (PyArg_ParseTuple(arguments, "") < 0) {
		return NULL;
	}

	NS_DURING
		super.receiver = ObjCObject_GetObject(self);
		super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

		(void)objc_msgSendSuper(&super, 
					@selector(getNumerOfRows:columns:),
					&rowCount, &columnCount);

		result = PyTuple_New(2);
		if (result != NULL) {
			PyTuple_SET_ITEM(result,0,PyInt_FromLong(rowCount));
			PyTuple_SET_ITEM(result,1,PyInt_FromLong(columnCount));

			if (PyErr_Occurred()) {
				Py_DECREF(result);
				result = NULL;
			}
		}

	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void
imp_NSMatrix_getNumerOfRows_columns_(id self, SEL sel, 
			int* rowCount, int* columnCount)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;

	arglist = PyTuple_New(0);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	result = ObjC_CallPython(self, sel, arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	if (!PySequence_Check(result)) {
		PyErr_SetString(PyExc_TypeError, 
			"Must return (int, int)");
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}

	v = PySequence_GetItem(result, 0);
	if (v == NULL) {
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}

	if (!PyInt_Check(v)) {
		PyErr_SetString(PyExc_TypeError, 
			"Must return (int, int)");
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}

	*rowCount = PyInt_AsLong(v);

	v = PySequence_GetItem(result, 1);
	if (v == NULL) {
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}

	if (!PyInt_Check(v)) {
		PyErr_SetString(PyExc_TypeError, 
			"Must return (int, int)");
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}

	*columnCount = PyInt_AsLong(v);

	Py_DECREF(result);
}

/* end custom mapping for NSMatrix.getNumerOfRows:columns: */

/*
 * TODO: (NSMatrix only)
 * - (BOOL)getRow:(int *)row column:(int *)column forPoint:(NSPoint)aPoint
 * - (BOOL)getRow:(int *)row column:(int *)column ofCell:(NSCell *)aCell
 *
 * TODO2: Write python script that prints all problematic selectors
 */

PyDoc_STRVAR(mapping_doc,
	"This module registers some utility functions with the PyObjC core \n"
	"and is not used by 'normal' python code"
);

static PyMethodDef mapping_methods[] = {
	{ 0, 0, 0, 0 }
};

void init_AppKitMapping(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_AppKitMapping", mapping_methods, mapping_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;
	

	if (ObjC_ImportModule(m) < 0) {
		return;
	}

	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSMatrix"), 
			@selector(getNumberOfRows:columns:),
			call_NSMatrix_getNumerOfRows_columns_,
			supercall_NSMatrix_getNumerOfRows_columns_,
			(IMP)imp_NSMatrix_getNumerOfRows_columns_) < 0) {

		PyErr_Print();
		return;
	}

	/* register other specials */
}
