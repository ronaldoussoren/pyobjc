#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface PyObjCTest_Protected : NSObject
{}
-publicMethod;
-_protectedMethod;
@end

@implementation PyObjCTest_Protected 
-publicMethod
{
	return nil;
}

-_protectedMethod
{
	return nil;
}
@end

static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initprotected(void);
void initprotected(void)
{
	PyObject* m;

	m = Py_InitModule4("protected", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "PyObjCTest_Protected", 
		PyObjCClass_New([PyObjCTest_Protected class]));
}

