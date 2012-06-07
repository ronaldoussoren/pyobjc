/*
 * Helper methods struct tests (objc.test.test_struct)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

struct FooStruct {
	int first;
	int second;
};

@interface OC_StructTest : NSObject
{
}
+(struct FooStruct)createWithFirst:(int)first andSecond:(int)second;
+(int)sumFields:(struct FooStruct)foo;
-(NSObject*)arrayOf4Structs:(struct FooStruct[4])argument;

+(NSObject*)callArrayOf4Structs:(OC_StructTest*)object;
@end

@implementation OC_StructTest
+(struct FooStruct)createWithFirst:(int)first andSecond:(int)second
{
	struct FooStruct f;
	f.first = first;
	f.second = second;
	return f;
}

+(int)sumFields:(struct FooStruct)foo
{
	return foo.first + foo.second;
}

+(NSObject*)callArrayOf4Structs:(OC_StructTest*)object
{
static	struct FooStruct structs[4] = {
		{ 1, 2 },
		{ 3, 4 },
		{ 5, 6 },
		{ 7, 8 },
	};

	return [object arrayOf4Structs:structs];
}
-(NSObject*)arrayOf4Structs:(struct FooStruct[4])argument
{
	return [NSData dataWithBytes:(void*)argument length:4*sizeof(*argument)];
}

@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
	PyModuleDef_HEAD_INIT,
	"structs",
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

PyObject* PyInit_structs(void);

PyObject*
PyInit_structs(void)

#else

#define INITERROR() return
#define INITDONE() return

void initstructs(void);

void
initstructs(void)
#endif
{
	PyObject* m;


#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("structs", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) < 0) {
		INITERROR();
	}

	if (PyModule_AddObject(m, "OC_StructTest", 
		PyObjCClass_New([OC_StructTest class])) < 0) {
		INITERROR();
	}

	INITDONE();
}
