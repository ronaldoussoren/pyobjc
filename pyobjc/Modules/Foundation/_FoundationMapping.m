/*
 * This module contains custom mapping functions for problematic methods
 *
 * NOTE: all interesting code is in _FoundationMapping_*.m
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


#include "_FoundationMapping_NSArray.m"
#include "_FoundationMapping_NSCoder.m"
#include "_FoundationMapping_NSData.m"
#include "_FoundationMapping_NSDictionary.m"
#include "_FoundationMapping_NSMutableArray.m"
#include "_FoundationMapping_NSNetService.m"
#include "_FoundationMapping_NSScriptObjectSpecifier.m"
#include "_FoundationMapping_NSSet.m"
#include "_FoundationMapping_NSString.m"

/* This prototype is needed to silence a GCC warning */
void init_FoundationMapping(void);

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

	if (_pyobjc_install_NSArray() != 0) return;
	if (_pyobjc_install_NSCoder() != 0) return;
	if (_pyobjc_install_NSData() != 0) return;
	if (_pyobjc_install_NSDictionary() != 0) return;
	if (_pyobjc_install_NSMutableArray() != 0) return;
	if (_pyobjc_install_NSNetService() != 0) return;
	if (_pyobjc_install_NSScriptObjectSpecifier() != 0) return;
	if (_pyobjc_install_NSSet() != 0) return;
	if (_pyobjc_install_NSString() != 0) return;
}
