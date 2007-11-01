/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>


static PyMethodDef initialize_methods[] = {
	{ 0, 0, 0, 0 }
};

typedef struct TestStructPointerStruct* Foo;

void initstructpointer2(void);
void initstructpointer2(void)
{
	PyObject* m;
	PyObject* v;

	m = Py_InitModule4("structpointer2", initialize_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	v = PyObjCCreateOpaquePointerType("TestStructPointerStructPtr",
			@encode(Foo), NULL);
	if (v == NULL) return;
	PyDict_SetItemString(PyModule_GetDict(m), "TestStructPointerStructPtr",
			v);
}
