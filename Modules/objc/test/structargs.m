/*
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Cocoa/Cocoa.h>

@interface StructArgClass : NSObject 
{
}
-(NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op;
-(unsigned)stackPtr;
@end

@implementation StructArgClass
-(NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op
{
	return [NSString stringWithFormat:@"aP:%@ aR:%@ %anO:%d",
			NSStringFromPoint(aPoint),
			NSStringFromRect(aRect),
			op];
}
-(unsigned)stackPtr
{
	char c;

	return ((unsigned)&c)+1;
}
@end

static PyMethodDef NULL_methods[] = {
	                { 0, 0, 0, 0 }
};

void initstructargs(void);
void initstructargs(void)
{
	PyObject* m;

	m = Py_InitModule4("structargs", NULL_methods,
		NULL, NULL, PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) return;

	PyModule_AddObject(m, "StructArgClass",
		PyObjCClass_New([StructArgClass class]));
}



