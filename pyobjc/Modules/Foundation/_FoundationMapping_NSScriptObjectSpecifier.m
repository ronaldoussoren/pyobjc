/*
 * Special wrappers for NSScriptObjectSpecifier methods with 'difficult' 
 * arguments.
 *
 * indicesOfObjectsByEvaluatingWithContainer:count:	[call]
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject*
call_NSScriptObjectSpecifier_indicesOfObjectsByEvaluatingWithContainer_count_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	id container;
	int* res;
	int  numrefs;
	struct objc_super super;
	PyObject* retVal;
	PyObject* v;
	int i;

	if  (!PyArg_ParseTuple(arguments, "O&", 
			PyObjCObject_Convert, &container)) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = (int*)objc_msgSendSuper(&super,
		    @selector(indicesOfObjectsByEvaluatingWithContainer:count:),
		    container, &numrefs);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = NULL;
		numrefs = -2;
	NS_ENDHANDLER

	if (res == NULL && PyErr_Occurred()) {
		return NULL;
	}

	retVal = PyTuple_New(2);
	if (retVal == NULL) {
		return NULL;
	}

	PyTuple_SET_ITEM(retVal, 1, PyInt_FromLong(numrefs));
	if (PyErr_Occurred()) {
		Py_DECREF(retVal);
		return NULL;
	}

	if (res == NULL) {
		PyTuple_SET_ITEM(retVal, 0, Py_None);
		Py_INCREF(Py_None);

	} else {
		v = PyTuple_New(numrefs);
		if (v == NULL) {
			Py_DECREF(retVal);
			return NULL;
		}

		for (i = 0; i < numrefs; i++) {
			PyTuple_SET_ITEM(v, i, PyInt_FromLong(res[i]));
			if (PyErr_Occurred()) {
				Py_DECREF(v);
				Py_DECREF(retVal);
			}
		}

		PyTuple_SET_ITEM(retVal, 0, v);
	}
	return retVal;
}

#if 0
/* How to avoid leaking the result? */
static int*
imp_NSScriptObjectSpecifier_indicesOfObjectsByEvaluatingWithContainer_count_(
	id self, id _meth, id container, int* numrefs)
{
}
#endif
		

static int 
_pyobjc_install_NSScriptObjectSpecifier(void)
{
	Class classNSScriptObjectSpecifier = objc_lookUpClass("NSScriptObjectSpecifier");
	if (classNSScriptObjectSpecifier == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSScriptObjectSpecifier,
		@selector(indicesOfObjectsByEvaluatingWithContainer:count:),
		call_NSScriptObjectSpecifier_indicesOfObjectsByEvaluatingWithContainer_count_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}


	return 0;
}
