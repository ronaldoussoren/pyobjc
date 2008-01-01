/*
 * Helper methods for the XML metadata testcases - global function edition
 *
 * This file has the same structure as generated for inline function by 
 * the metadata tool.
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

static int* makeIntArrayOf5(void)
{
	static int result[5];
	int i;
	for (i = 0; i < 5; i++) {
		result[i] = i*i;
	}
	return result;
}

static char** makeStringArray(void)
{
	static char* result[] = {
		"hello",
		"world",
		"out",
		"there",
		NULL
	};
	return result;
}


static int* makeIntArrayOf_(int count)
{
	static int* result = NULL;
	int i;

	if (result) {
		free(result);
	}
	result = malloc(sizeof(int) * count);
	if (result == NULL) {
		return NULL;
	}
	for (i = 0; i < count; i++) {
		result[i] = i * i * i;
	}
	return result;
}

static int* nullIntArrayOf5(void)
{
	return NULL;
}

static char** nullStringArray(void)
{
	return NULL;
}

static int* nullIntArrayOf_(int count __attribute__((__unused__)))
{
	return NULL;
}

static NSArray* makeIntArray_count_(int* data, unsigned count)
{
	NSMutableArray* array;
	unsigned i;

	array = [NSMutableArray arrayWithCapacity:count];

	for (i = 0; i < count; i++) {
		[array addObject: [NSNumber numberWithInt:data[i]]];
	}
	return array;
}

static NSArray* nullIntArray_count_(int* data, unsigned count)
{
	if (data) {
		return makeIntArray_count_(data, count);
	} else {
		return nil;
	}
}

static NSArray* makeIntArray_countPtr_(int* data, unsigned* countPtr)
{
	return makeIntArray_count_(data, *countPtr);
}


static NSArray* make4Tuple_(double* data)
{
	NSMutableArray* array;
	unsigned i;

	array = [NSMutableArray array];

	for (i = 0; i < 4; i++) {
		[array addObject: [NSNumber numberWithDouble:data[i]]];
	}
	return array;
}

static NSArray* null4Tuple_(double* data)
{
	if (data)  {
		return make4Tuple_(data);
	} else {
		return nil;
	}
}



static NSArray* makeStringArray_(char** data)
{
	NSMutableArray* array;

	array = [NSMutableArray array];

	while (*data != NULL) {
		[array addObject: [NSString stringWithCString: *data]];
		data ++;
	}
	return array;
}

static NSArray* nullStringArray_(char** data)
{
	if (data) {
		return makeStringArray_(data);
	} else {
		return nil;
	}
}

static NSArray* makeObjectArray_(id* data)
{
	NSMutableArray* array;

	array = [NSMutableArray array];

	while (*data != NULL) {
		[array addObject: *data];
		data ++;
	}
	return array;
}

static void fillArray_count_(int* data, int count)
{
	int i;
	for (i = 0; i < count; i++) {
		data[i] = i*i;
	}
}

static int nullfillArray_count_(int* data, int count)
{
	if (data == NULL) {
		return 0;
	} else {
		fillArray_count_(data, count);
		return 1;
	}
}

static void fill4Tuple_(int* data)
{
	int i;
	for (i = 0; i < 4; i++) {
		data[i] = - i * i * i;
	}
}

static int nullfill4Tuple_(int* data)
{
	if (data == NULL) {
		return 0;
	} else {
		fill4Tuple_(data);
		return 1;
	}
}

static int fillStringArray_(char** data __attribute__((__unused__)))
{
	return -1;
}

static int nullfillStringArray_(char** data)
{
	if (data == NULL) return 0;
	fillStringArray_(data);
	return 1;
}

static void reverseArray_count_(float* data, int count)
{
	float t;
	int i;
	for (i = 0; i < count / 2; i++) {
		t = data[i];
		data[i] = data[count - 1 - i];
		data[count - 1 -i] = t;
	}
}

static int nullreverseArray_count_(float* data, int count)
{
	if (data == NULL) return 0;
	reverseArray_count_(data, count);
	return 1;
}

static void reverseStrings_(char** data)
{
	int count, i;
	char* t;

	for (count = 0; data[count] != NULL; count++) {
		;
	}

	for (i = 0; i < count / 2 ; i++) {
		t = data[i];
		data[i] = data[count-1-i];
		data[count-1-i] = t;
	}
}

static int nullreverseStrings_(char** data)
{
	if (data == NULL) return 0;
	reverseStrings_(data);
	return 1;
}

static void reverse4Tuple_(short* data) 
{
	short t;

	t = data[0];
	data[0] = data[3];
	data[3] = t;

	t = data[1];
	data[1] = data[2];
	data[2] = t;
}

static int nullreverse4Tuple_(short* data)
{
	if (data == NULL) return 0;
	reverse4Tuple_(data);
	return 1;
}


static int sumX_andY_(int* x, int* y)
{
	return *x + *y;
}

static int divBy5_remainder_(int x, int* r)
{
	*r = x % 5;
	return x / 5;
}

static void swapX_andY_(double* x, double* y)
{
	int t = *x;
	*x = *y;
	*y = t;
}

static NSArray* input_output_inputAndOutput_(int* x, int* y, int* z)
{
	char buf[64];
	NSMutableArray* result = [NSMutableArray array];

	snprintf(buf, sizeof(buf), "%p", x);
	[result addObject: [NSString stringWithCString:buf]];

	snprintf(buf, sizeof(buf), "%p", y);
	[result addObject: [NSString stringWithCString:buf]];

	snprintf(buf, sizeof(buf), "%p", z);
	[result addObject: [NSString stringWithCString:buf]];

	if (y) {
		if (x) {
			if (z) {
				*y = *x + *z;
			} else {
				*y = *x + 42;
			}
		} else if (z) {
			*y = 42 - *z;
		} else {
			*y = -1;
		}
	}

	if (z) {
		if (x) {
			*z = *x - *z;
		} else {
			*z = -*z;
		}
	}

	return result;
}
	
static int fillArray_uptoCount_(int* data, int count)
{
	int i;
	for (i = 0; i < count / 2; i++) {
		data[i] = i + 2;
	}
	for (i = count/2; i < count; i++) {
		data[i] = -42;
	}
	return count/2;
}

static int maybyFillArray_(int *data)
{
	int i;
	for (i = 0; i < 2; i++) {
		data[i] = i + 10;
	}
	for (i = 2; i < 4; i++) {
		data[i] = -42;
	}
	return 2;
}

static int reverseArray_uptoCount_(float* data, int count)
{
	reverseArray_count_(data, count);
	return count/2;
}

static int maybeReverseArray_(short* data)
{
	reverse4Tuple_(data);
	return 2;
}


static NSArray* makeArrayWithFormat_(NSString* fmt, ...)
{
	va_list ap;
	char buffer[2048];

	va_start(ap, fmt);
	vsnprintf(buffer, sizeof(buffer), [fmt UTF8String], ap);
	va_end(ap);

	return [NSArray arrayWithObjects: 
			fmt, 
			[NSString stringWithUTF8String:buffer],
			NULL];
}

static NSArray* makeArrayWithCFormat_(char* fmt, ...)
{
	va_list ap;
	char buffer[2048];

	va_start(ap, fmt);
	vsnprintf(buffer, sizeof(buffer), fmt, ap);
	va_end(ap);

	return [NSArray arrayWithObjects: 
			[NSString stringWithUTF8String:fmt], 
			[NSString stringWithUTF8String:buffer], 
			NULL];
}

static int maybeFillArray_(int* data)
{       
	int i;  
	for (i = 0; i < 2; i++) {
		data[i] = i + 10;
	}
	for (i = 2; i < 4; i++) {
		data[i] = -42;
	}
	return 2;
}


typedef void (*F)(void);
static struct function {
	char* name;
	F	function;
} gFunctionMap[] = {
	{ "makeIntArrayOf5", (F)makeIntArrayOf5 },
	{ "makeStringArray", (F)makeStringArray },
	{ "makeIntArrayOf_", (F)makeIntArrayOf_ },
	{ "nullIntArrayOf5", (F)nullIntArrayOf5 },
	{ "nullStringArray", (F)nullStringArray },
	{ "nullIntArrayOf_", (F)nullIntArrayOf_ },
	{ "nullIntArray_count_", (F)nullIntArray_count_ },
	{ "makeIntArray_countPtr_", (F)makeIntArray_countPtr_ },
	{ "makeIntArray_count_", (F)makeIntArray_count_ },
	{ "make4Tuple_", (F)make4Tuple_ },
	{ "null4Tuple_", (F)null4Tuple_ },
	{ "nullStringArray_", (F)nullStringArray_ },
	{ "makeStringArray_", (F)makeStringArray_ },
	{ "makeObjectArray_", (F)makeObjectArray_ },
	{ "fillArray_count_", (F)fillArray_count_ },
	{ "nullfillArray_count_", (F)nullfillArray_count_ },
	{ "fill4Tuple_", (F)fill4Tuple_ },
	{ "nullfill4Tuple_", (F)nullfill4Tuple_ },
	{ "fillStringArray_", (F)fillStringArray_ },
	{ "nullfillStringArray_", (F)nullfillStringArray_ },
	{ "reverseArray_count_", (F)reverseArray_count_ },
	{ "nullreverseArray_count_", (F)nullreverseArray_count_ },
	{ "reverseStrings_", (F)reverseStrings_ },
	{ "nullreverseStrings_", (F)nullreverseStrings_ },
	{ "reverse4Tuple_", (F)reverse4Tuple_ },
	{ "nullreverse4Tuple_", (F)nullreverse4Tuple_ },
	{ "sumX_andY_", (F)sumX_andY_ },
	{ "divBy5_remainder_", (F)divBy5_remainder_ },
	{ "swapX_andY_", (F)swapX_andY_ },
	{ "input_output_inputAndOutput_", (F)input_output_inputAndOutput_ },
	{ "fillArray_uptoCount_", (F)fillArray_uptoCount_ },
	{ "maybyFillArray_", (F)maybyFillArray_ },
	{ "reverseArray_uptoCount_", (F)reverseArray_uptoCount_ },
	{ "maybeReverseArray_", (F)maybeReverseArray_ },
	{ "makeArrayWithFormat_", (F)makeArrayWithFormat_ },
	{ "makeArrayWithCFormat_", (F)makeArrayWithCFormat_ },
	{ "maybeFillArray_", (F)maybeFillArray_ },

	{ NULL, NULL }
};


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initmetadatafunction(void);
void initmetadatafunction(void)
{
	PyObject* m;
	PyObject* v;

	m = Py_InitModule4("metadatafunction", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
	
	v = PyCObject_FromVoidPtr(gFunctionMap, NULL);
	PyModule_AddObject(m, "function_list", v);
}
