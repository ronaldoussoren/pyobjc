/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

struct TestStructPointerStruct {
	int i1;
};

static struct TestStructPointerStruct myGlobal = { 1 };

@interface OC_TestStructPointer : NSObject
{
}
+(struct TestStructPointerStruct*)returnPointerToStruct;
@end

@implementation OC_TestStructPointer
+(struct TestStructPointerStruct*)returnPointerToStruct
{
	return &myGlobal;
}
@end


static PyMethodDef initialize_methods[] = {
	{ 0, 0, 0, 0 }
};

void initstructpointer1(void);
void initstructpointer1(void)
{
	PyObject* m;

	m = Py_InitModule4("structpointer1", initialize_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	PyModule_AddObject(m, "OC_TestStructPointer", 
		PyObjCClass_New([OC_TestStructPointer class]));
}
