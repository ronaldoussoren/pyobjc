/*
 * Helper methods opaque-pointer tests (objc.test.test_opaque)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

typedef struct _Foo* FooHandle;
typedef struct _Bar* BarHandle;

@interface OC_OpaqueTest : NSObject
{
}
+(FooHandle)createFoo:(int)value;
+(FooHandle)nullFoo;
+(void)deleteFoo:(FooHandle)handle;
+(int)getValueOf:(FooHandle)foo;
+(void)setValue:(int)value forFoo:(FooHandle)handle;


+(BarHandle)createBarWithFirst:(double)first andSecond:(double)second;
+(BarHandle)nullBar;
+(void)getFirst:(double*)first andSecond:(double*)second of:(BarHandle)bar;
+(void)setFirst:(double)first andSecond:(double)second of:(BarHandle)bar;
+(void)deleteBar:(BarHandle)handle;
+(double)getFirst:(BarHandle)handle;
+(double)getSecond:(BarHandle)handle;
@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initopaque(void);
void initopaque(void)
{
	PyObject* m;

	m = Py_InitModule4("opaque", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_OpaqueTest", 
		PyObjCClass_New([OC_OpaqueTest class]));
	PyModule_AddObject(m, "FooHandle", 
		PyObjCCreateOpaquePointerType("FooHandle",
			                @encode(FooHandle), "FooHandle doc"));
	PyModule_AddObject(m, "BarEncoded",  PyString_FromString(@encode(BarHandle)));
}

/*
 * Only define the full structs here to ensure that @encode won't include
 * the field definition into the encoded value.
 */

struct _Foo {
	int index;
};

struct _Bar {
	double first;
	double second;
};

@implementation OC_OpaqueTest
+(FooHandle)createFoo:(int)value
{
	FooHandle result = malloc(sizeof(struct _Foo));
	if (result == NULL) {
		return NULL;
	}
	result->index = value;
	return result;
}

+(FooHandle)nullFoo
{
	return NULL;
}

+(void)deleteFoo:(FooHandle)handle
{
	if (handle) {
		free(handle);
	}
}

+(int)getValueOf:(FooHandle)foo
{
	return foo->index;
}

+(void)setValue:(int)value forFoo:(FooHandle)handle
{
	handle->index = value;
}

+(BarHandle)createBarWithFirst:(double)first andSecond:(double)second
{
	BarHandle result = malloc(sizeof(struct _Bar));
	if (result == NULL) return NULL;

	result->first = first;
	result->second = second;
	return result;
}

+(BarHandle)nullBar
{
	return NULL;
}


+(void)getFirst:(double*)first andSecond:(double*)second of:(BarHandle)bar
{
	*first = bar->first;
	*second = bar->second;
}

+(void)setFirst:(double)first andSecond:(double)second of:(BarHandle)bar
{
	bar->first = first;
	bar->second = second;
}

+(void)deleteBar:(BarHandle)handle
{
	if (handle) {
		free(handle);
	}
}

+(double)getFirst:(BarHandle)handle
{
	return handle->first;
}

+(double)getSecond:(BarHandle)handle
{
	return handle->second;
}

@end
