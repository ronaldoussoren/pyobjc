/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestIdentity : NSObject
{
	NSObject* storedObject;
}

-(NSObject*)storedObject;
-(void)setStoredObject:(NSObject*)object;
-(void)dealloc;

-(void)setStoredObjectToResultOf:(SEL)aSelector on:(NSObject*)object;
-(void)setStoredObjectToInteger:(int)value;
-(void)setStoredObjectToUnsignedInteger:(unsigned int)value;
-(void)setStoredObjectToLongLong:(long long)value;
-(void)setStoredObjectToUnsignedLongLong:(unsigned long long)value;
-(void)setStoredObjectToDouble:(double)value;
-(void)setStoredObjectToFloat:(float)value;

-(int)isSameObjectAsStored:(NSObject*)value;
-(void)setStoredObjectToAProtocol;
-(void)setStoredObjectAnInstanceOf:(Class) cls;

-(void)writeStoredObjecToFile:(NSString*)fname;

@end

@implementation OC_TestIdentity
-(void)dealloc
{
	[storedObject release];
}

-(NSObject*)storedObject
{
	return [[storedObject retain] autorelease];
}

-(void)setStoredObject:(NSObject*)object
{
	[object retain];
	[storedObject release];
	storedObject = object;
}

-(void)setStoredObjectToResultOf:(SEL)aSelector on:(NSObject*)object
{
	[self setStoredObject: [object performSelector: aSelector]];
}

-(void)setStoredObjectToInteger:(int)value
{
	[self setStoredObject: [NSNumber numberWithInt: value]];
}

-(void)setStoredObjectToUnsignedInteger:(unsigned int)value
{
	[self setStoredObject: [NSNumber numberWithUnsignedInt: value]];
}

-(void)setStoredObjectToLongLong:(long long)value
{
	[self setStoredObject: [NSNumber numberWithLongLong: value]];
}

-(void)setStoredObjectToUnsignedLongLong:(unsigned long long)value
{
	[self setStoredObject: [NSNumber numberWithUnsignedLongLong: value]];
}

-(void)setStoredObjectToDouble:(double)value
{
	[self setStoredObject: [NSNumber numberWithDouble: value]];
}

-(void)setStoredObjectToFloat:(float)value
{
	[self setStoredObject: [NSNumber numberWithFloat: value]];
}

-(int)isSameObjectAsStored:(NSObject*)value
{
	return value == storedObject;
}

-(void)setStoredObjectToAProtocol
{
	[self setStoredObject: (NSObject*)@protocol(NSObject) ];
}

-(void)setStoredObjectAnInstanceOf:(Class) cls
{
	[self setStoredObject: [[cls alloc] init]];
}

-(void)writeStoredObjecToFile:(NSString*)fname
{
	[(NSArray*)storedObject writeToFile:fname atomically:YES];
}

@end

static PyMethodDef identity_methods[] = {
	{ NULL, NULL, NULL, NULL }
};

void initidentity(void);
void initidentity(void)
{
	PyObject* m;

	m = Py_InitModule4("identity", identity_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	PyModule_AddObject(m, "OC_TestIdentity", 
		PyObjCClass_New([OC_TestIdentity class]));

}
