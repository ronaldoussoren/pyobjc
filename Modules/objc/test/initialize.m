/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static int numUninitialized = 0;

@interface OC_TestInitialize : NSObject
{
	int       isInitialized;
}
-init;
-retain;
-(void)release;
-autorelease;
-(int)isInitialized;
+(int)numUninitialized;
-(id)dummy;
+(id)makeInstance;

/* completely unrelated ... */
-(oneway void)onewayVoidMethod;

@end

@implementation OC_TestInitialize 

-init
{
	self = [super init];
	if (!self) return self;

	isInitialized = 1;
	return self;
}

-retain
{
	if (!isInitialized) {
		numUninitialized ++;
	}
	return [super retain];
}

-(void)release
{
	if (!isInitialized) {
		numUninitialized ++;
	}
	[super release];
}

-(id)autorelease
{
	if (!isInitialized) {
		numUninitialized ++;
	}
	return [super autorelease];
}

-(int)isInitialized
{
	return isInitialized;
}

+(int)numUninitialized
{
	return numUninitialized;
}

-(id)dummy
{
	return @"hello";
}

+(id)makeInstance
{
	return [[[self alloc] init] autorelease];
}

-(oneway void)onewayVoidMethod
{
	isInitialized=-1;
}

@end


static PyMethodDef initialize_methods[] = {
	{ 0, 0, 0, 0 }
};

void initinitialize(void);
void initinitialize(void)
{
	PyObject* m;

	m = Py_InitModule4("initialize", initialize_methods, 
			NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	PyModule_AddObject(m, "OC_TestInitialize", 
		PyObjCClass_New([OC_TestInitialize class]));
}
