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


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"initialize",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit_initialize(void);

PyObject*
PyInit_initialize(void)

#else

#define INITERROR() return
#define INITDONE() return

void initinitialize(void);

void
initinitialize(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("initialize", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "OC_TestInitialize", 
		PyObjCClass_New([OC_TestInitialize class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
