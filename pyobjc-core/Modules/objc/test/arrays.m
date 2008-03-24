#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

struct ArrayStruct {
	int first;
	int second;
};

typedef int int_array_t[4];
typedef struct ArrayStruct struct_array_t[4];

@interface OC_ArrayTest : NSObject
{
}
#if 0
	/* It seems to be impossible to return C arrays */
+(int_array_t)arrayOf4Integers;
+(struct_array_t)arrayOf4Structs;
#endif

-(NSObject*)arrayOf4Ints:(int_array_t)array;
-(NSObject*)arrayOf4IntsIn:(in int_array_t)array;
-(NSObject*)arrayOf4IntsInOut:(inout int_array_t)array;
-(void)arrayOf4IntsOut:(out int_array_t)array;

-(NSObject*)arrayOf4Structs:(struct_array_t)array;
-(NSObject*)arrayOf4StructsIn:(in struct_array_t)array;
-(NSObject*)arrayOf4StructsInOut:(inout struct_array_t)array;
-(void)arrayOf4StructsOut:(out struct_array_t)array;

+(NSObject*)callArrayOf4Ints:(OC_ArrayTest*)object;
+(NSObject*)callArrayOf4IntsOut:(OC_ArrayTest*)object;
+(NSObject*)callArrayOf4Structs:(OC_ArrayTest*)object;
+(NSObject*)callArrayOf4StructsOut:(OC_ArrayTest*)object;
@end

@implementation OC_ArrayTest

#if 0 
	/* These don't compile for some reason */
+(int_array_t)arrayOf4Integers;
{
static int_array_t gValue = { 4, 5, 6, 7 };
	return gValue;
}
+(struct_array_t)arrayOf4Structs
{
static struct_array_t gValue = {
		{ 9, 10 },
		{ 12, 13 },
		{ 21, 24 },
		{ -1, -2 },
	};
	return gValue;
}
#endif

-(NSObject*)arrayOf4Ints:(int_array_t)array
{
	return [NSArray arrayWithObjects:
		[NSNumber numberWithInt:array[0]],
		[NSNumber numberWithInt:array[1]],
		[NSNumber numberWithInt:array[2]],
		[NSNumber numberWithInt:array[3]],
		nil];
}
-(NSObject*)arrayOf4IntsIn:(in int_array_t)array
{
	return [NSArray arrayWithObjects:
		[NSNumber numberWithInt:array[0]],
		[NSNumber numberWithInt:array[1]],
		[NSNumber numberWithInt:array[2]],
		[NSNumber numberWithInt:array[3]],
		nil];
}
-(NSObject*)arrayOf4IntsInOut:(inout int_array_t)array
{
	NSObject* result = [NSArray arrayWithObjects:
		[NSNumber numberWithInt:array[0]],
		[NSNumber numberWithInt:array[1]],
		[NSNumber numberWithInt:array[2]],
		[NSNumber numberWithInt:array[3]],
		nil];

	array[0] += 42;
	array[1] += 42;
	array[2] += 42;
	array[3] += 42;

	return result;
}
-(void)arrayOf4IntsOut:(out int_array_t)array
{
	array[0] = 99;
	array[1] = 100;
	array[2] = 102;
	array[3] = 110;
}

-(NSObject*)arrayOf4Structs:(struct_array_t)array
{
	return [NSArray arrayWithObjects:
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[0].first],
				[NSNumber numberWithInt:array[0].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[1].first],
				[NSNumber numberWithInt:array[1].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[2].first],
				[NSNumber numberWithInt:array[2].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[3].first],
				[NSNumber numberWithInt:array[3].second],
				nil],
			nil
		];
}
-(NSObject*)arrayOf4StructsIn:(in struct_array_t)array
{
	return [NSArray arrayWithObjects:
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[0].first],
				[NSNumber numberWithInt:array[0].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[1].first],
				[NSNumber numberWithInt:array[1].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[2].first],
				[NSNumber numberWithInt:array[2].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[3].first],
				[NSNumber numberWithInt:array[3].second],
				nil],
			nil
		];
}
-(NSObject*)arrayOf4StructsInOut:(inout struct_array_t)array
{
	NSObject* result = [NSArray arrayWithObjects:
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[0].first],
				[NSNumber numberWithInt:array[0].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[1].first],
				[NSNumber numberWithInt:array[1].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[2].first],
				[NSNumber numberWithInt:array[2].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[3].first],
				[NSNumber numberWithInt:array[3].second],
				nil],
			nil
		];

	int i;
	for (i = 0; i < 4; i++) {
		array[i].first += 42;
		array[i].second -= 42;
	}

	return result;
}
-(void)arrayOf4StructsOut:(out struct_array_t)array
{
	int i;
	for (i = 0; i < 4; i++) {
		array[i].first = 1 + i * i;
		array[i].second = -4 - i * i * i;
	}
}

+(NSObject*)callArrayOf4Ints:(OC_ArrayTest*)object
{
	int_array_t array = { 1, 2, 3, 4 };
	return [object arrayOf4Ints:array];
}

+(NSObject*)callArrayOf4IntsOut:(OC_ArrayTest*)object
{
	int_array_t array;
	[object arrayOf4IntsOut:array];
	return [NSArray arrayWithObjects:
			[NSNumber numberWithInt: array[0]],
			[NSNumber numberWithInt: array[1]],
			[NSNumber numberWithInt: array[2]],
			[NSNumber numberWithInt: array[3]],
			nil];
}

+(NSObject*)callArrayOf4Structs:(OC_ArrayTest*)object
{
	struct_array_t array = {
		{ 1, 2 },
		{ 3, 4 },
		{ 5, 6 },
		{ 7, 8 }
	};
	return [object arrayOf4Structs:array];
}

+(NSObject*)callArrayOf4StructsOut:(OC_ArrayTest*)object
{
	struct_array_t array;
	[object arrayOf4StructsOut:array];
	
	return [NSArray arrayWithObjects:
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[0].first],
				[NSNumber numberWithInt:array[0].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[1].first],
				[NSNumber numberWithInt:array[1].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[2].first],
				[NSNumber numberWithInt:array[2].second],
				nil],
			[NSArray arrayWithObjects:
				[NSNumber numberWithInt:array[3].first],
				[NSNumber numberWithInt:array[3].second],
				nil],
			nil
		];
}
@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initarrays(void);
void initarrays(void)
{
	PyObject* m;

	m = Py_InitModule4("arrays", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_ArrayTest", 
		PyObjCClass_New([OC_ArrayTest class]));
}
