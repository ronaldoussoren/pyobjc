/*
 * This module contains custom mapping functions for problematic methods
 *
 * TODO: I (Ronald) have now written mappings for two methods, and I'd say
 *       that we can do better...
 */

#include <Python.h>
#include <Foundation/Foundation.h>
#include <objc/objc-runtime.h>
#include "pyobjc-api.h"

PyDoc_STRVAR(mapping_doc,
	"This module registers some utility functions with the PyObjC core \n"
	"and is not used by 'normal' python code"
);

static PyMethodDef mapping_methods[] = {
	{ 0, 0, 0, 0 }
};

#include "_FoundationMapping_NSData.m"
#include "_FoundationMapping_NSCoder.m"

void init_FoundationMapping(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_FoundationMapping", mapping_methods, mapping_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;
	
	if (ObjC_ImportModule(m) < 0) {
		return;
	}

	if (__pyobjc_install_NSCoder()) return;
	if (__pyobjc_install_NSData()) return;
	
	if (PyErr_Occurred()) {
		printf("Python error\n");
		PyErr_Print();
	}
}
