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
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_Foundation",
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

PyObject* PyInit__Foundation(void);

PyObject*
PyInit__Foundation(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_Foundation(void);

void
init_Foundation(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_Foundation", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	if (setup_nsdecimal(m) == -1) INITERROR();
	if (setup_nsinvocation(m) == -1) INITERROR();
	if (setup_nsdata(m) == -1) INITERROR();
	if (setup_nsnetservice(m) == -1) INITERROR();
	if (setup_nscoder(m) == -1) INITERROR();
	if (setup_nssstring(m) == -1) INITERROR();

	INITDONE();
}
