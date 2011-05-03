#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

/* We include the source code here instead of 
 * using the linker due to limitations in pyobjc-api.h
 */

#include "_Foundation_NSDecimal.m"
#include "_Foundation_NSInvocation.m"
#include "_Foundation_data.m"
#include "_Foundation_netservice.m"
#include "_Foundation_nscoder.m"
#include "_Foundation_string.m"
#include "_Foundation_typecode.m"

static PyMethodDef mod_methods[] = {
	FOUNDATION_TYPECODE_METHODS
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_Foundation)
{
	PyObject* m;
	m = PyObjC_MODULE_CREATE(_Foundation)
	if (!m) { 
		PyObjC_INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

	if (setup_nsdecimal(m) == -1) PyObjC_INITERROR();
	if (setup_nsinvocation(m) == -1) PyObjC_INITERROR();
	if (setup_nsdata(m) == -1) PyObjC_INITERROR();
	if (setup_nsnetservice(m) == -1) PyObjC_INITERROR();
	if (setup_nscoder(m) == -1) PyObjC_INITERROR();
	if (setup_nssstring(m) == -1) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
