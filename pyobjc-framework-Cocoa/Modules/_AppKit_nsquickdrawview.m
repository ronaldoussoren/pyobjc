
#if !defined(__LP64__) && PY_MAJOR_VERSION == 2
	/* Quickdraw only exists in 32-bit mode. We do define a dummy 
	 * init function to avoid breaking the Python module.
	 */

#include "pymactoolbox.h"

static PyObject* 
call_NSQuickDrawView_qdport(
		PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     port;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));


		port = ((void*(*)(struct objc_super*, SEL))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method));

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		port = NULL;
	
	PyObjC_ENDHANDLER

	if (port == NULL) {
		if (PyErr_Occurred()) return NULL;
		result = Py_None;
		Py_INCREF(result);
	} else {
		result = GrafObj_New((GrafPtr)port);
	}

	return result;
}

static void 
imp_NSQuickDrawView_qdport(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	GrafPtr* pretval = (GrafPtr*)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	GrafObj_Convert(result, pretval);
	Py_DECREF(result);

	if (PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	*pretval = NULL;
	PyObjCErr_ToObjCWithGILState(&state);
}

#endif


static int setup_nsquickdrawview(PyObject* m __attribute__((__unused__)))
{
#if !defined(__LP64__) && PY_MAJOR_VERSION == 2
	Class classNSQuickDrawView = objc_lookUpClass("NSQuickDrawView");
	if (classNSQuickDrawView == NULL) {
		return 0;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSQuickDrawView,
		@selector(qdport),
		call_NSQuickDrawView_qdport,
		imp_NSQuickDrawView_qdport) < 0) {

		return -1;
	}
#endif

	return 0;
}
