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
void inittestclassandinst(void);
static PyMethodDef no_methods[] = {
	{ 0, 0, 0, 0 }
};

void inittestclassandinst(void)
{
	PyObject* m;

	m = Py_InitModule4("testclassandinst", no_methods, 
		NULL, NULL, PYTHON_API_VERSION);
	if (!m) return;

	if (PyObjC_ImportAPI(m) < 0) return;

	PyModule_AddObject(m, "PyObjC_TestClassAndInstance", 
		PyObjCClass_New([PyObjC_TestClassAndInstance class]));

	PyModule_AddObject(m, "PyObjC_TestUnallocatable", 
		PyObjCClass_New([PyObjC_TestUnallocatable class]));
}
