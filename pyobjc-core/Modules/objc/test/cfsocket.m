/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#include <CoreFoundation/CoreFoundation.h>

@interface OC_TestCFSocket : NSObject
-(id)newSocket;
@end

@implementation OC_TestCFSocket
-(id)newSocket
{
	CFSocketRef sock;

	sock = CFSocketCreate(NULL, 0, 0, 0, 0, 0, 0);
	return (id)sock;
}
@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"cfsocket",
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

PyObject* PyInit_cfsocket(void);

PyObject*
PyInit_cfsocket(void)

#else

#define INITERROR() return
#define INITDONE() return

void initcfsocket(void);

void
initcfsocket(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("cfsocket", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_TestCFSocket", 
			PyObjCClass_New([OC_TestCFSocket class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
