/*
 * XXX: PyObjC_TestOutputInitializer is a class that can't be created
 *      from Python but ends up in some fun places like NSAttributedString
 */

#include <Python.h>
#include <pyobjc-api.h>

#import <Foundation/Foundation.h>

#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif

@interface PyObjC_TestOutputInitializer: NSObject
{
    int _priv;
}

-initWithBooleanOutput:(BOOL *)outBool;
-(BOOL)isInitialized;
@end

@implementation PyObjC_TestOutputInitializer
-initWithBooleanOutput:(BOOL *)outBool
{
    self = [self init];
    *outBool = YES;
    _priv = YES;
    return self;
}

-(BOOL)isInitialized
{
    return _priv;
}
@end

/* Python glue */
static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"testoutputinitializer",
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

PyObject* PyInit_testoutputinitializer(void);

PyObject*
PyInit_testoutputinitializer(void)

#else

#define INITERROR() return
#define INITDONE() return

void inittestoutputinitializer(void);

void
inittestoutputinitializer(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("testoutputinitializer", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjC_TestOutputInitializer", 
		PyObjCClass_New([PyObjC_TestOutputInitializer class])) < 0) {
		INITERROR();
	}
	INITDONE();
}
