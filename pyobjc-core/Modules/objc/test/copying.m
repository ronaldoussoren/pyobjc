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
{}
+(NSObject<NSCopying>*)doCopySetup:(Class)aClass;
+(NSObject*)newObjectOfClass:(Class)aClass;
@end

@implementation OC_CopyHelper
+(NSObject<NSCopying>*)doCopySetup:(Class)aClass
{
	NSObject<NSCopying>* tmp;
	NSObject<NSCopying>* retval;

	tmp = (NSObject<NSCopying>*)[[aClass alloc] init];
	[tmp modify];

	retval = [tmp copyWithZone:nil];
	[tmp release];
	return [retval autorelease];
}

+(NSObject*)newObjectOfClass:(Class)aClass
{
	return [[aClass alloc] init];
}
@end

@interface OC_CopyBase : NSObject <NSCopying>
{
	int intVal;
}
-(instancetype)init;
-(instancetype)initWithInt:(int)intVal;
-(int)intVal;
-(void)setIntVal:(int)val;
-(instancetype)copyWithZone:(NSZone*)zone;
@end

@implementation OC_CopyBase
-(instancetype)init
{
	return [self initWithInt:0];
}

-(instancetype)initWithInt:(int)value
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

#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

-(instancetype)copyWithZone:(NSZone*)zone
{
	return NSCopyObject(self, 0, zone);
	
}
@end


static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"copying",
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

PyObject* PyInit_copying(void);

PyObject*
PyInit_copying(void)

#else

#define INITERROR() return
#define INITDONE() return

void initcopying(void);

void
initcopying(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("copying", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "OC_CopyHelper",
		PyObjCClass_New([OC_CopyHelper class])) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "OC_CopyBase",
		PyObjCClass_New([OC_CopyBase class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
