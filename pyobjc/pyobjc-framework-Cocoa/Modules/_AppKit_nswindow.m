#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

#ifndef __LP64__

#include "pymactoolbox.h"

#else
	/* FIXME: these are inline definitions of the bits
	 * of pymactoolbox.h that we need because that header
	 * doesn't work in 64-bit mode.
	 */
#	include <Carbon/Carbon.h>
extern PyObject *WinObj_New(WindowPtr);
extern int WinObj_Convert(PyObject *, WindowPtr *);
extern PyObject *WinObj_WhichWindow(WindowPtr);

#endif

static PyObject* 
call_NSWindow_windowRef(
	PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     windowRef;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));


		windowRef = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method));

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		windowRef = NULL;
	PyObjC_ENDHANDLER

	if (windowRef == NULL) {
		if (PyErr_Occurred()) return NULL;
		result = Py_None;
		Py_INCREF(result);
	} else {
		result = WinObj_New((WindowPtr)windowRef);
	}

	return result;
}

static void 
imp_NSWindow_windowRef(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	WindowPtr* pretval = (WindowPtr*)resp;

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

	WinObj_Convert(result, pretval);
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


static PyObject* 
call_NSWindow_initWithWindowRef_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     windowRef;
	id        objc_result;

	if  (!PyArg_ParseTuple(arguments, "O&", WinObj_Convert, &windowRef)) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		objc_result = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method), windowRef);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		objc_result = nil;
		
	PyObjC_ENDHANDLER

	if (objc_result == nil && PyErr_Occurred()) return nil;

	result = PyObjC_IdToPython(objc_result);

	return result;
}

static void 
imp_NSWindow_initWithWindowRef_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	WindowPtr windowRef = *(WindowPtr*)args[2];
	id* pretval = (id*)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;
	
	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);
	
	v = WinObj_New(windowRef);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	*pretval = PyObjC_PythonToId(result);
	if (*pretval == nil && PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	*pretval = nil;
	PyObjCErr_ToObjCWithGILState(&state);
}



static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};

/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_nswindow",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__nswindow(void);

PyObject*
PyInit__nswindow(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_nswindow(void);

void
init_nswindow(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_nswindow", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	Class classNSWindow = objc_lookUpClass("NSWindow");
	if (classNSWindow == NULL) {
		INITDONE();
	}

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(initWithWindowRef:),
		call_NSWindow_initWithWindowRef_,
		imp_NSWindow_initWithWindowRef_) < 0) {

		INITERROR();
	}

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(windowRef),
		call_NSWindow_windowRef,
		imp_NSWindow_windowRef) < 0) {

		INITERROR();
	}

	INITDONE();
}
