/*
 * This module contains custom mapping functions for problematic methods
 */

#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

PyDoc_STRVAR(mapping_doc,
	"This module registers some utility functions with the PyObjC core \n"
	"and is not used by 'normal' python code"
);

static PyMethodDef mapping_methods[] = {
	{ 0, 0, 0, 0 }
};

/* These are needed to silence GCC */
void init_FoundationMapping(void);
int _pyobjc_install_NSCoder(void);
int _pyobjc_install_NSDictionary(void);
int _pyobjc_install_NSData(void);

#include "_FoundationMapping_NSCoder.m"
#include "_FoundationMapping_NSData.m"
#include "_FoundationMapping_NSDictionary.m"


void init_FoundationMapping(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_FoundationMapping", mapping_methods, mapping_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;
	
	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	if (_pyobjc_install_NSCoder()) return;
	if (_pyobjc_install_NSData()) return;
	if (_pyobjc_install_NSDictionary()) return;
}
