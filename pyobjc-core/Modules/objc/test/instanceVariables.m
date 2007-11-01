/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface ClassWithVariables : NSObject
{ 
	int	intValue;
	double	floatValue;
	char	charValue;
	char*	strValue;
	NSRect  rectValue;
	NSObject* nilValue;
	PyObject* pyValue;
	NSString* objValue;
}
-init;
-(void)dealloc;
@end

@implementation ClassWithVariables
-init
{
	self = [super init];
	if (self == nil) return nil;

	intValue = 42;
	floatValue = -10.055;
	charValue = 'a';
	strValue = "hello world";
	rectValue = NSMakeRect(1,2,3,4);
	nilValue = nil;
	pyValue = PySlice_New(
			PyInt_FromLong(1), 
			PyInt_FromLong(10), 
			PyInt_FromLong(4));
	objValue = [[NSObject alloc] init];
	return self;
}

-(void)dealloc
{
	Py_XDECREF(pyValue);
	[objValue release];
	[nilValue release];
	[super dealloc];
}

@end


static PyMethodDef ivar_methods[] = {
	{ 0, 0, 0, 0 }
};

void initinstanceVariables(void);
void initinstanceVariables(void)
{
	PyObject* m;

	m = Py_InitModule4("instanceVariables", ivar_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	PyModule_AddObject(m, "ClassWithVariables",
		PyObjCClass_New([ClassWithVariables class]));
}
