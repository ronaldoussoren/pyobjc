/*
 * NSMovie mappings for special methods:
 * - QTMovie
 * - initWithMovie:
 *
 * Note: Python 2.3 is needed to make use of this functionality
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

#include "pymactoolbox.h"

static PyObject* call_NSMovie_QTMovie(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     movie;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));


		movie = objc_msgSendSuper(&super,
				@selector(QTMovie));
		if (movie == NULL) {
			result = Py_None;
			Py_INCREF(result);
		} else {
			result = MovieObj_New((Movie)movie);
		}
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void* imp_NSMovie_QTMovie(id self, SEL sel)
{
	PyObject* result;
	PyObject* arglist;
	Movie    objc_result;

	arglist = PyTuple_New(0);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	MovieObj_Convert(result, &objc_result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}


static PyObject* call_NSMovie_initWithMovie_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     movie;
	id        objc_result;

	if  (!PyArg_ParseTuple(arguments, "O&", MovieObj_Convert, &movie)) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		objc_result = objc_msgSendSuper(&super,
				@selector(initWithMovie:), movie);
		result = PyObjC_IdToPython(objc_result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static id imp_NSMovie_initWithMovie_(id self, SEL sel, void* movie)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	arglist = PyTuple_New(1);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}
	
	PyTuple_SET_ITEM(arglist, 0, MovieObj_New(movie));
	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	objc_result = PyObjC_PythonToId(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}


static int 
_pyobjc_install_NSMovie(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSMovie"), 
		@selector(QTMovie),
		call_NSMovie_QTMovie,
		(IMP)imp_NSMovie_QTMovie) < 0 ) {

		NSLog(@"Error occurred while installing NSMovie method bridge (QTMovie).");
		PyErr_Print();
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSMovie"), 
		@selector(initWithMovie:),
		call_NSMovie_initWithMovie_,
		(IMP)imp_NSMovie_initWithMovie_) < 0 ) {

		NSLog(@"Error occurred while installing NSMovie method bridge (initWithMovie_).");
		PyErr_Print();
		return -1;
	}

	return 0;
}
