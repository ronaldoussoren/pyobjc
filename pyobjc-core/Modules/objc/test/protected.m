#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface PyObjCTest_Protected : NSObject
{}
-(id)publicMethod;
-(id)_protectedMethod;
@end

@implementation PyObjCTest_Protected 
-(id)publicMethod
{
	return nil;
}

-(id)_protectedMethod
{
	return nil;
}
@end

static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"protected",
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

PyObject* PyInit_protected(void);

PyObject*
PyInit_protected(void)

#else

#define INITERROR() return
#define INITDONE() return

void initprotected(void);

void
initprotected(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("protected", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjCTest_Protected", 
		PyObjCClass_New([PyObjCTest_Protected class])) < 0){
		INITERROR();
	}
	INITDONE();
}
