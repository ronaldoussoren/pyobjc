/*
 * Helper methods for the XML metadata testcases.
 *
 * - add global functions
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

static void use_int(int x __attribute__((__unused__))) { };
static void use_charpp(char** x __attribute__((__unused__))) { };
static void use_id(id x __attribute__((__unused__))) { };

@interface OC_MetaDataTest : NSObject
{
}
/* Return value arrays: */
-(int*)   makeIntArrayOf5;
-(char**) makeStringArray;
-(int*)   makeIntArrayOf:(int)count;
-(const int*)   nullIntArrayOf5;
-(char**) nullStringArray;
-(int*)   nullIntArrayOf:(int)count;
-(int*)   unknownLengthArray;

/* In arrays: */
-(NSArray*)makeIntArray:(int*) data count:(unsigned)count;
-(NSArray*)makeIntArray:(int*) data halfCount:(unsigned)count;
-(NSArray*)makeIntArray:(int*) data countPtr:(unsigned*)countPtr;
-(NSArray*)nullIntArray:(int*) data count:(unsigned)count;
-(NSArray*)makeStringArray:(char**)data;
-(NSArray*)makeObjectArray:(id*)data;
-(NSArray*)nullStringArray:(char**)data;
-(NSArray*)make4Tuple:(double*)data;
-(NSArray*)null4Tuple:(double*)data;
-(NSArray*) makeVariableLengthArray:(int*)array halfCount:(int)cnt;

/* Out arrays: */
-(void)fillArray:(int*)data count:(int)count;
-(int)nullfillArray:(int*)data count:(int)count;
-(void)fill4Tuple:(int*)data;
-(int)nullfill4Tuple:(int*)data;
-(int)fillArray:(int*)data uptoCount:(int)count;
-(int)maybeFillArray:(int*)data;

/* NULL-terminated output arrays can't work, these are just here to check that the
 * bridge knows this too.
 */
-(void)fillStringArray:(char**)data;
-(int)nullfillStringArray:(char**)data;

/* In/out arrays: */
-(void)reverseArray:(float*)data count:(int)count;
-(int)nullreverseArray:(float*)data count:(int)count;
-(void)reverseStrings:(char**)data;
-(int)nullreverseStrings:(char**)data;
-(void)reverse4Tuple:(short*)data;
-(int)nullreverse4Tuple:(short*)data;
-(int)reverseArray:(float*)data uptoCount:(int)count;
-(int)maybeReverseArray:(short*)data;


/* pass-by-reference */
-(int)sumX:(int*)x andY:(int*)y;		/* in */
-(int)divBy5:(int)x remainder:(int*)r;		/* out */
-(void)swapX:(double*)x andY:(double*)y; 	/* inout */
-(NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z;

-(NSArray*)makeArrayWithFormat:(NSString*)fmt, ...;
-(NSArray*)makeArrayWithCFormat:(char*)fmt, ...;
-(NSArray*)makeArrayWithArguments:(id)arg, ...;

/* Helpers for calling back into python: */

+(int*)   makeIntArrayOf5On:(OC_MetaDataTest*)obj;
+(char**) makeStringArrayOn:(OC_MetaDataTest*)obj;
+(int*)   makeIntArrayOf:(int)count on:(OC_MetaDataTest*)obj;
+(const int*)   nullIntArrayOf5On:(OC_MetaDataTest*)obj;
+(char**) nullStringArrayOn:(OC_MetaDataTest*)obj;
+(int*)   nullIntArrayOf:(int)count on:(OC_MetaDataTest*)obj;
+(NSArray*)makeIntArray:(int*) data count:(unsigned)count on:(OC_MetaDataTest*)obj;
+(NSArray*)makeIntArray:(int*) data countPtr:(unsigned*)countPtr on:(OC_MetaDataTest*)obj;
+(NSArray*)nullIntArray:(int*) data count:(unsigned)count on:(OC_MetaDataTest*)obj;
+(NSArray*)makeStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+(NSArray*)makeObjectArray:(id*)data on:(OC_MetaDataTest*)obj;
+(NSArray*)nullStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+(NSArray*)make4Tuple:(double*)data on:(OC_MetaDataTest*)obj;
+(NSArray*)null4Tuple:(double*)data on:(OC_MetaDataTest*)obj;
+(void)fillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj;
+(int)nullfillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj;
+(void)fill4Tuple:(int*)data on:(OC_MetaDataTest*)obj;
+(int)nullfill4Tuple:(int*)data on:(OC_MetaDataTest*)obj;
+(int)fillArray:(int*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj;
+(int)maybeFillArray:(int*)data on:(OC_MetaDataTest*)obj;
+(void)fillStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+(int)nullfillStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+(void)reverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj;
+(int)nullreverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj;
+(void)reverseStrings:(char**)data on:(OC_MetaDataTest*)obj;
+(int)nullreverseStrings:(char**)data on:(OC_MetaDataTest*)obj;
+(void)reverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj;
+(int)nullreverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj;
+(int)reverseArray:(float*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj;
+(int)maybeReverseArray:(short*)data on:(OC_MetaDataTest*)obj;
+(int)sumX:(int*)x andY:(int*)y on:(OC_MetaDataTest*)obj;
+(int)divBy5:(int)x remainder:(int*)r on:(OC_MetaDataTest*)obj;
+(void)swapX:(double*)x andY:(double*)y on:(OC_MetaDataTest*)obj;
+(NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z on:(OC_MetaDataTest*)obj;

/* Various */
-(void)varargsMethodWithObjects:(id)first, ...;
-(int)ignoreMethod;

/* Byte arrays and C-strings */
-(NSData*)makeDataForBytes:(char*)data count:(int)count;
-(NSData*)makeDataForVoids:(void*)data count:(int)count;
-(void)addOneToBytes:(char*)data count:(int)count;
-(void)addOneToVoids:(void*)data count:(int)count;
-(void)fillBuffer:(char*)data count:(int)count;
-(void)fillVoids:(void*)data count:(int)count;

@end

@implementation OC_MetaDataTest


-(int*)   makeIntArrayOf5
{
	static int result[5];
	int i;
	for (i = 0; i < 5; i++) {
		result[i] = i*i;
	}
	return result;
}

-(char**) makeStringArray
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


-(int*)   makeIntArrayOf:(int)count
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
-(int*)   nullIntArrayOf5
{
	return NULL;
}

-(char**) nullStringArray
{
	return NULL;
}

-(int*)   nullIntArrayOf:(int)count
{
	use_int(count);
	return NULL;
}


-(NSArray*)nullIntArray:(int*) data count:(unsigned)count
{
	if (data) {
		return [self makeIntArray:data count:count];
	} else {
		return nil;
	}
}

-(NSArray*)makeIntArray:(int*) data countPtr:(unsigned*)countPtr
{
	return [self makeIntArray:data count:*countPtr];
}

-(NSArray*)makeIntArray:(int*) data halfCount:(unsigned)count
{
	return [self makeIntArray:data count:count*2];
}

-(NSArray*)makeIntArray:(int*) data count:(unsigned)count
{
	NSMutableArray* array;
	unsigned i;

	array = [NSMutableArray arrayWithCapacity:count];

	for (i = 0; i < count; i++) {
		[array addObject: [NSNumber numberWithInt:data[i]]];
	}
	return array;
}

-(NSArray*)make4Tuple:(double*)data
{
	NSMutableArray* array;
	unsigned i;

	array = [NSMutableArray array];

	for (i = 0; i < 4; i++) {
		[array addObject: [NSNumber numberWithDouble:data[i]]];
	}
	return array;
}

-(NSArray*)null4Tuple:(double*)data
{
	if (data)  {
		return [self make4Tuple:data];
	} else {
		return nil;
	}
}


-(NSArray*)nullStringArray:(char**)data
{
	if (data) {
		return [self makeStringArray:data];
	} else {
		return nil;
	}
}

-(NSArray*)makeStringArray:(char**)data
{
	NSMutableArray* array;

	array = [NSMutableArray array];

	while (*data != NULL) {
		[array addObject: [NSString stringWithCString: *data]];
		data ++;
	}
	return array;
}

-(NSArray*)makeObjectArray:(id*)data;
{
	NSMutableArray* array;

	array = [NSMutableArray array];

	while (*data != NULL) {
		[array addObject: *data];
		data ++;
	}
	return array;
}

-(void)fillArray:(int*)data count:(int)count
{
	int i;
	for (i = 0; i < count; i++) {
		data[i] = i*i;
	}
}

-(int)nullfillArray:(int*)data count:(int)count
{
	if (data == NULL) {
		return 0;
	} else {
		[self fillArray:data count:count];
		return 1;
	}
}

-(void)fill4Tuple:(int*)data;
{
	int i;
	for (i = 0; i < 4; i++) {
		data[i] = - i * i * i;
	}
}

-(int)nullfill4Tuple:(int*)data;
{
	if (data == NULL) {
		return 0;
	} else {
		[self fill4Tuple:data];
		return 1;
	}
}

-(void)fillStringArray:(char**)data
{
	use_charpp(data);
	/* NULL-terminated output arrays can't work */
}

-(int)nullfillStringArray:(char**)data
{
	if (data == NULL) return 0;
	[self fillStringArray:data];
	return 1;
}

-(void)reverseArray:(float*)data count:(int)count;
{
	float t;
	int i;
	for (i = 0; i < count / 2; i++) {
		t = data[i];
		data[i] = data[count - 1 - i];
		data[count - 1 -i] = t;
	}
}

-(int)nullreverseArray:(float*)data count:(int)count;
{
	if (data == NULL) return 0;
	[self reverseArray:data count:count];
	return 1;
}

-(void)reverseStrings:(char**)data;
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

-(int)nullreverseStrings:(char**)data;
{
	if (data == NULL) return 0;
	[self reverseStrings:data];
	return 1;
}

-(void)reverse4Tuple:(short*)data
{
	short t;

	t = data[0];
	data[0] = data[3];
	data[3] = t;

	t = data[1];
	data[1] = data[2];
	data[2] = t;
}

-(int)nullreverse4Tuple:(short*)data
{
	if (data == NULL) return 0;
	[self reverse4Tuple:data];
	return 1;
}

-(int)sumX:(int*)x andY:(int*)y		/* in */
{
	return *x + *y;
}

-(int)divBy5:(int)x remainder:(int*)r	/* out */
{
	*r = x % 5;
	return x / 5;
}

-(void)swapX:(double*)x andY:(double*)y /* inout */
{
	int t = *x;
	*x = *y;
	*y = t;
}

-(NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z
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
	
-(int)fillArray:(int*)data uptoCount:(int)count
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

-(int)maybeFillArray:(int*)data
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

-(int)reverseArray:(float*)data uptoCount:(int)count
{
	[self reverseArray:data count:count];
	return count/2;
}

-(int)maybeReverseArray:(short*)data;
{
	[self reverse4Tuple:data];
	return 2;
}


+(int*)   makeIntArrayOf5On:(OC_MetaDataTest*)obj
{
	return [obj makeIntArrayOf5];
}

+(char**) makeStringArrayOn:(OC_MetaDataTest*)obj
{
	return [obj makeStringArray];
}

+(int*)   makeIntArrayOf:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj makeIntArrayOf:count];
}

+(const int*)   nullIntArrayOf5On:(OC_MetaDataTest*)obj
{
	return [obj nullIntArrayOf5];
}

+(char**) nullStringArrayOn:(OC_MetaDataTest*)obj
{
	return [obj nullStringArray];
}

+(int*)   nullIntArrayOf:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj nullIntArrayOf:count];
}

+(NSArray*)makeIntArray:(int*) data count:(unsigned)count on:(OC_MetaDataTest*)obj
{
	return [obj makeIntArray:data count:count];
}

+(NSArray*)makeIntArray:(int*) data countPtr:(unsigned*)countPtr on:(OC_MetaDataTest*)obj
{
	return [obj makeIntArray:data countPtr:countPtr];
}

+(NSArray*)nullIntArray:(int*) data count:(unsigned)count on:(OC_MetaDataTest*)obj
{
	return [obj nullIntArray:data count:count];
}

+(NSArray*)makeStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
	return [obj makeStringArray:data];
}

+(NSArray*)makeObjectArray:(id*)data on:(OC_MetaDataTest*)obj
{
	return [obj makeObjectArray:data];
}

+(NSArray*)nullStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
	return [obj nullStringArray:data];
}

+(NSArray*)make4Tuple:(double*)data on:(OC_MetaDataTest*)obj
{
	return [obj make4Tuple:data];
}

+(NSArray*)null4Tuple:(double*)data on:(OC_MetaDataTest*)obj
{
	return [obj null4Tuple:data];
}

+(void)fillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj fillArray:data count:count];
}

+(int)nullfillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj nullfillArray:data count:count];
}

+(void)fill4Tuple:(int*)data on:(OC_MetaDataTest*)obj
{
	return [obj fill4Tuple:data];
}

+(int)nullfill4Tuple:(int*)data on:(OC_MetaDataTest*)obj
{
	return [obj nullfill4Tuple:data];
}

+(int)fillArray:(int*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj fillArray:data uptoCount:count];
}

+(int)maybeFillArray:(int*)data on:(OC_MetaDataTest*)obj
{
	return [obj maybeFillArray:data];
}

+(void)fillStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
	[obj fillStringArray:data];
}

+(int)nullfillStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
	return [obj nullfillStringArray:data];
}

+(void)reverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj
{
	[obj reverseArray:data count:count];
}

+(int)nullreverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj nullreverseArray:data count:count];
}

+(void)reverseStrings:(char**)data on:(OC_MetaDataTest*)obj
{
	[obj reverseStrings:data];
}

+(int)nullreverseStrings:(char**)data on:(OC_MetaDataTest*)obj
{
	return [obj nullreverseStrings:data];
}

+(void)reverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj
{
	[obj reverse4Tuple:data];
}

+(int)nullreverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj
{
	return [obj nullreverse4Tuple:data];
}

+(int)reverseArray:(float*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj
{
	return [obj reverseArray:data uptoCount:count];
}

+(int)maybeReverseArray:(short*)data on:(OC_MetaDataTest*)obj
{
	return [obj maybeReverseArray:data];
}

+(int)sumX:(int*)x andY:(int*)y on:(OC_MetaDataTest*)obj
{
	return [obj sumX:x andY:y];
}

+(int)divBy5:(int)x remainder:(int*)r on:(OC_MetaDataTest*)obj
{
	return [obj divBy5:x remainder:r];
}

+(void)swapX:(double*)x andY:(double*)y on:(OC_MetaDataTest*)obj
{
	return [obj swapX:x andY:y];
}

+(NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z on:(OC_MetaDataTest*)obj
{
	return [obj input:x output:y inputAndOutput:z];
}

-(NSArray*)makeArrayWithFormat:(NSString*)fmt, ...
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

-(NSArray*)makeArrayWithCFormat:(char*)fmt, ...
{
	va_list ap;
	char  buffer[2048];
	
	va_start(ap, fmt);
	vsnprintf(buffer, sizeof(buffer), fmt, ap);
	va_end(ap);

	return [NSArray arrayWithObjects: 
			[NSString stringWithUTF8String:fmt], 
			[NSString stringWithUTF8String:buffer], 
			NULL];
}

-(NSArray*)makeArrayWithArguments:(id)arg, ...;
{
	va_list ap;
	NSMutableArray* array = [[NSMutableArray alloc] init];
	if (arg == NULL) {
		return array;
	}


	va_start(ap, arg);
	do {
		[array addObject:arg];
		arg = va_arg(ap, id);
	} while (arg != NULL);

	va_end(ap);
	return array;
}

-(void)varargsMethodWithObjects:(id)first, ...
{
	use_id(first);
}

-(int)ignoreMethod
{
	return 42;
}

-(NSData*)makeDataForBytes:(char*)data count:(int)count
{
	return [NSData dataWithBytes:data length:count];
}

-(NSData*)makeDataForVoids:(void*)data count:(int)count
{
	return [NSData dataWithBytes:data length:count];
}

-(void)addOneToBytes:(char*)data count:(int)count
{
	int i;
	for (i = 0;i < count; i++) {
		data[i] += 1;
	}
}

-(void)addOneToVoids:(void*)data count:(int)count
{
	int i;
	for (i = 0; i < count; i++) {
		((char*)data)[i] += 2;
	}
}

-(void)fillBuffer:(char*)data count:(int)count
{
	memset(data, '\xfe', count);
}

-(void)fillVoids:(void*)data count:(int)count
{
	memset(data, '\xab', count);
}

-(int*)   unknownLengthArray
{
static  int theValue[] = { 1, 3, 5, 7, 11, 13, 17, 19 };
	return theValue;
}

-(int*)  unknownLengthMutable
{
static  int theValue[20];
	return theValue;
}

-(NSArray*) makeVariableLengthArray:(int*)array halfCount:(int)cnt
{
	cnt *= 2;

	NSMutableArray* result;
	int i;

	result = [NSMutableArray arrayWithCapacity:cnt];

	for (i = 0; i < cnt; i++) {
		[result addObject: [NSNumber numberWithFloat:array[i]]];
	}
	return result;
}


@end


static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 }
};

void initmetadata(void);
void initmetadata(void)
{
	PyObject* m;

	m = Py_InitModule4("metadata", mod_methods, NULL, NULL, PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	PyModule_AddObject(m, "OC_MetaDataTest", 
		PyObjCClass_New([OC_MetaDataTest class]));
}
