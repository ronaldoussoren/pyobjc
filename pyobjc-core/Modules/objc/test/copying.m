/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface NSObject (OC_CopyHelper)
-(void)modify;
@end

@interface OC_CopyHelper : NSObject
{ }
+(NSObject*)doCopySetup:(Class)aClass;
@end

@implementation OC_CopyHelper
+(NSObject*)doCopySetup:(Class)aClass
{
	NSObject<NSCopying>* tmp;
	NSObject* retval;

	tmp = (NSObject*)[[aClass alloc] init];
	[tmp modify];

	retval = [tmp copyWithZone:nil];
	[tmp release];
	return retval;
}
@end

@interface OC_CopyBase : NSObject <NSCopying>
{
	int intVal;
}
-init;
-initWithInt:(int)intVal;
-(int)intVal;
-(void)setIntVal:(int)val;
-copyWithZone:(NSZone*)zone;
@end

@implementation OC_CopyBase
-init
{
	return [self initWithInt:0];
}

-initWithInt:(int)value
{
	self = [super init];
	if (self == nil) return nil;

	intVal = value;
	return self;
}

-(int)intVal
{
	return intVal;
}

-(void)setIntVal:(int)val
{
	intVal = val;
}

-copyWithZone:(NSZone*)zone
{
	return NSCopyObject(self, 0, zone);
	
}
@end


static PyMethodDef copying_methods[] = {
	{ 0, 0, 0, 0 }
};

void initcopying(void);
void initcopying(void)
{
	PyObject* m;

	m = Py_InitModule4("copying", copying_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	PyModule_AddObject(m, "OC_CopyHelper",
		PyObjCClass_New([OC_CopyHelper class]));
	PyModule_AddObject(m, "OC_CopyBase",
		PyObjCClass_New([OC_CopyBase class]));
}
