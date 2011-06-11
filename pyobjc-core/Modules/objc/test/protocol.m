/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@protocol OC_TestProtocol
-(int)method1;
-(void)method2:(int)v;
@end

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wprotocol"
#pragma clang diagnostic ignored "-Wincomplete-implementation"
@interface OC_TestProtocolClass : NSObject <OC_TestProtocol>
{}
@end

@implementation OC_TestProtocolClass
@end
#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"protocols",
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

PyObject* PyInit_protocol(void);

PyObject*
PyInit_protocol(void)

#else

#define INITERROR() return
#define INITDONE() return

void initprotocol(void);

void
initprotocol(void)
#endif
{
	PyObject* m;
	Protocol* p;


#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("protocol", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}
	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	p = @protocol(OC_TestProtocol);
	PyObject* prot = PyObjC_ObjCToPython("@", &p);
	if (!prot) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "OC_TestProtocol", prot) < 0) {
		INITERROR();
	}

	INITDONE();
}
