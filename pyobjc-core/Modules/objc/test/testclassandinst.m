/*
 * XXX: PyObjC_TestClassAndInstance is a class that can't be created
 *      from Python but ends up in some fun places like NSWindow
 */

#include <Python.h>
#include <pyobjc-api.h>

#import <Foundation/Foundation.h>

#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif

@interface PyObjC_TestUnallocatable : NSObject
{
}
@end

@implementation PyObjC_TestUnallocatable
+ allocWithZone:(NSZone *)zone 
{
    return nil;
}
@end

@interface PyObjC_TestClassAndInstance: NSObject
{
}

+ (BOOL)isInstance;
- (BOOL)isInstance;
@end

@implementation PyObjC_TestClassAndInstance
+(BOOL)isInstance
{
	return NO;
}
-(BOOL)isInstance
{
	return YES;
}
@end

/* Python glue */
static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"testclassandinst",
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

PyObject* PyInit_testclassandinst(void);

PyObject*
PyInit_testclassandinst(void)

#else

#define INITERROR() return
#define INITDONE() return

void inittestclassandinst(void);

void
inittestclassandinst(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("testclassandinst", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjC_TestClassAndInstance", 
		PyObjCClass_New([PyObjC_TestClassAndInstance class])) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjC_TestUnallocatable", 
		PyObjCClass_New([PyObjC_TestUnallocatable class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
