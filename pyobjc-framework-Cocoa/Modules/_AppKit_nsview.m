#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static PyObject* 
call_NSView_getRectsBeingDrawn_count_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* v;
	NSRect* rects;
	PyObject* arg1, *arg2;
	int count;

	if  (!PyArg_ParseTuple(arguments, "OO", &arg1, &arg2)) {
		return NULL;
	}

	if (arg1 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}
	if (arg2 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "count must be None");
		return NULL;
	}


	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				&rects, &count);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	v = PyObjC_CArrayToPython(@encode(NSRect), rects, count);
	if (v == NULL) return NULL;

	result = Py_BuildValue("Oi", v, count);
	Py_XDECREF(v);

	return result;
}



static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_nsview",
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

PyObject* PyInit__nsview(void);

PyObject*
PyInit__nsview(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_nsview(void);

void
init_nsview(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_nsview", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	Class classNSView = objc_lookUpClass("NSView");
	if (classNSView == NULL) {
		INITDONE();
	}

	if (PyObjC_RegisterMethodMapping(
		classNSView,
		@selector(getRectsBeingDrawn:count:),
		call_NSView_getRectsBeingDrawn_count_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		INITERROR();
	}

	INITDONE();
}
