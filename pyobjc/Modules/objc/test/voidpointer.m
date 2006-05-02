/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestVoidPointer : NSObject
{
	void* value;
}

-(void*)getvalue;
-(void)setvalue:(void*)v;
@end

@implementation OC_TestVoidPointer
-init 
{
	self = [super init];
	if (self) {
		value = NULL;
	}
	return self;
}
-(void*)getvalue
{
	return value;
}
-(void)setvalue:(void*)v
{
	value = v;
}
@end

static PyMethodDef voidpointer_methods[] = {
	{ 0, 0, 0, 0 }
};

void initvoidpointer(void);
void initvoidpointer(void)
{
	PyObject* m;

	m = Py_InitModule4("voidpointer", voidpointer_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_TestVoidPointer", 
			PyObjCClass_New([OC_TestVoidPointer class]));
}
