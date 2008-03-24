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
-(NSObject*)arrayOf4Structs:(struct FooStruct[4])argument;
{
	return [NSData dataWithBytes:(void*)argument length:sizeof(argument)];
}

@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initstructs(void);
void initstructs(void)
{
	PyObject* m;

	m = Py_InitModule4("structs", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_StructTest", 
		PyObjCClass_New([OC_StructTest class]));
}

