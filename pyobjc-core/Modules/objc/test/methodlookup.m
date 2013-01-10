/*
 * Helper classes for test_methodlookup
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface PyObjC_MethodLookup1 : NSObject
{
}
-(int)instance;
-(int)instance2;
-(int)instance3;
-(int)instance4;
-(int)both;
+(int)both;
+(int)clsmeth;
+(int)clsmeth2;
+(int)clsmeth3;
+(int)clsmeth4;

+(id)OC_description;
-(id)OC_description;
-(int)pyobjc__instanceCount;
+(int)pyobjc__classCount;
-(id)pyobjc_setObject:(id)o forKey:(id)k;
+(id)pyobjc_setObject:(id)o forKey:(id)k;
@end

@implementation PyObjC_MethodLookup1

-(int)instance
{
	return 1;
}

-(int)instance2
{
	return -1;
}

-(int)instance3
{
	return -1;
}

-(int)instance4
{
	return -1;
}

-(int)both
{
	return 2;
}

+(int)both
{
	return 3;
}

+(int)clsmeth
{
	return 4;
}

+(int)clsmeth2
{
	return 4;
}
+(int)clsmeth3
{
	return 4;
}
+(int)clsmeth4
{
	return 4;
}
+(id)OC_description
{
	return @"class description";
}

-(id)OC_description
{
	return @"method description";
}

-(int)pyobjc__instanceCount
{
	return 42;
}

+(int)pyobjc__classCount
{
	return 99;
}

-(id)pyobjc_setObject:(id)o forKey:(id)k
{
	return [NSArray arrayWithObjects: o, k, nil];
}

+(id)pyobjc_setObject:(id)o forKey:(id)k
{
	return [NSArray arrayWithObjects: k, o, nil];
}


@end


@interface PyObjC_MethodLookup2 : PyObjC_MethodLookup1
{
}
-(int)instance;
-(int)instance3;
-(int)both;
+(int)both;
+(int)clsmeth;
+(int)clsmeth3;
@end

@implementation PyObjC_MethodLookup2

-(int)instance
{
	return 10;
}

-(int)instance3
{
	return -10;
}


-(int)both
{
	return 20;
}

+(int)both
{
	return 30;
}

+(int)clsmeth
{
	return 40;
}

+(int)clsmeth3
{
	return -40;
}
@end



static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"methodlookup",
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

PyObject* PyInit_methodlookup(void);

PyObject* __attribute__((__visibility__("default")))
PyInit_methodlookup(void)

#else

#define INITERROR() return
#define INITDONE() return

void initmethodlookup(void);

void __attribute__((__visibility__("default")))
initmethodlookup(void)
#endif
{
	PyObject* m;

#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("methodlookup", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "PyObjC_MethodLookup1", 
		PyObjCClass_New([PyObjC_MethodLookup1 class])) < 0) {
		INITERROR();
	}
	if (PyModule_AddObject(m, "PyObjC_MethodLookup2", 
		PyObjCClass_New([PyObjC_MethodLookup2 class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
