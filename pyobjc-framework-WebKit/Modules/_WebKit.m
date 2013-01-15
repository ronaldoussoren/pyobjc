#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <WebKit/WebKit.h>

/* We include the source code here instead of 
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_WebKit_protocols.m"


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_WebKit)
{
	PyObject* m;
	m = PyObjC_MODULE_CREATE(_WebKit)
	if (!m) { 
		PyObjC_INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
