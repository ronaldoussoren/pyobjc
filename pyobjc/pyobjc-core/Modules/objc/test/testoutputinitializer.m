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
void inittestoutputinitializer(void);
static PyMethodDef no_methods[] = {
	{ 0, 0, 0, 0 }
};

void inittestoutputinitializer(void)
{
	PyObject* m;

	m = Py_InitModule4("testoutputinitializer", no_methods, 
		NULL, NULL, PYTHON_API_VERSION);
	if (!m) return;

	if (PyObjC_ImportAPI(m) < 0) return;

	PyModule_AddObject(m, "PyObjC_TestOutputInitializer", 
		PyObjCClass_New([PyObjC_TestOutputInitializer class]));
}
