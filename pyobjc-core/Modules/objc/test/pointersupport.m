/*
 * Helper methods opaque-pointer tests (objc.test.test_opaque)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

static PyObject*
make_opaque_capsule(PyObject* mod __attribute__((__unused__)))
{
	return PyCapsule_New((void*)1234, "objc.__opaque__", NULL);
}

static PyObject*
make_object_capsule(PyObject* mod __attribute__((__unused__)))
{
	NSObject* object = [[[NSObject alloc] init] autorelease];
	return PyCapsule_New(object, "objc.__object__", NULL);
}


static PyMethodDef mod_methods[] = {
	{
		"opaque_capsule",
		(PyCFunction)make_opaque_capsule,
		METH_NOARGS,
		0,
	},
	{
		"object_capsule",
		(PyCFunction)make_object_capsule,
		METH_NOARGS,
		0,
	},
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"pointersupport",
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

PyObject* PyInit_pointersupport(void);

PyObject*
PyInit_pointersupport(void)

#else

#define INITERROR() return
#define INITDONE() return

void initpointersupport(void);

void
initpointersupport(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("pointersupport", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	INITDONE();
}
