/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestIdentity : NSObject
{
	NSObject* storedObject;
	int       isClassic;
}

-(NSObject*)storedObject;
-(void)setStoredClassicObject:(NSObject*)object;
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
-(void)setStoredObjectAnInstanceOfClassic:(Class) cls;

-(void)writeStoredObjectToFile:(NSString*)fname;

@end

@implementation OC_TestIdentity
-(void)dealloc
{
	if (isClassic) {
		/* pass, we could call free but why bother? */
	} else {
		[storedObject release];
	}
    [super dealloc];
}

-(NSObject*)storedObject
{
	if (isClassic) {
		return storedObject;
	} else {
		return [[storedObject retain] autorelease];
	}
}

-(void)setStoredObject:(NSObject*)object
{
	if (!isClassic) {
		[storedObject release];
	}
	[object retain];
	storedObject = object;
	isClassic = 0;
}

-(void)setStoredClassicObject:(NSObject*)object
{
	if (!isClassic) {
		[storedObject release];
	}
	storedObject = object;
	isClassic = 1;
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
	[self setStoredClassicObject: (NSObject*)@protocol(NSObject) ];
}

-(void)setStoredObjectAnInstanceOf:(Class) cls
{
	[self setStoredObject: [[[cls alloc] init] autorelease]];
}
-(void)setStoredObjectAnInstanceOfClassic:(Class)cls
{
	[self setStoredClassicObject:[[cls alloc] init]];
}

-(void)writeStoredObjectToFile:(NSString*)fname
{
	[(NSArray*)storedObject writeToFile:fname atomically:YES];
}

@end

static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"identity",
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

PyObject* PyInit_identity(void);

PyObject*
PyInit_identity(void)

#else

#define INITERROR() return
#define INITDONE() return

void initidentity(void);

void
initidentity(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("identity", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "OC_TestIdentity", 
		PyObjCClass_New([OC_TestIdentity class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
