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
-(NSRect)someRect;
-(NSRect)someRectWithRect:(NSRect)rect;
-(NSRect)someRectWithX:(int)x Y:(int)y H:(int)h W:(int)w;
-(NSRect)someRectWithObject:(StructArgClass*)o X:(int)x Y:(int)y H:(int)h W:(int)w;
@end

@implementation StructArgClass
-(NSRect)someRectWithRect:(NSRect)rect
{
	return rect;
}

-(NSRect)someRectWithX:(int)x Y:(int)y H:(int)h W:(int)w
{
	return NSMakeRect(x, y, h, w);
}

-(NSRect)someRectWithObject:(StructArgClass*)o X:(int)x Y:(int)y H:(int)h W:(int)w
{
	return [o someRectWithRect:NSMakeRect(x, y, h, w)];
}

-(NSRect)someRect
{
	NSRect retval = NSMakeRect(1,2,3,4);
	return retval;
}


-(NSString*)compP:(NSPoint)aPoint aRect:(NSRect)aRect anOp:(int)op
{
	return [NSString stringWithFormat:@"aP:%@ aR:%@ anO:%d",
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



