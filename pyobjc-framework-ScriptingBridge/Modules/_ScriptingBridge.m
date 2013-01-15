#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <ScriptingBridge/ScriptingBridge.h>

/* We include the source code here instead of 
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_ScriptingBridge_protocols.m"


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_ScriptingBridge)
{
	PyObject* m;
	m = PyObjC_MODULE_CREATE(_ScriptingBridge)
	if (!m) { 
		PyObjC_INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
