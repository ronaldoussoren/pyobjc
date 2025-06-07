/*
 * Helper methods for the XML metadata testcases.
 *
 * - add global functions
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

static void use_int(int x __attribute__((__unused__))){}
static void use_charpp(char** x __attribute__((__unused__))){}
static void use_id(id x __attribute__((__unused__))){}

@interface OC_MetaDataTest : NSObject {
}

-(id _Nullable)makeBuffer:(void*)buffer len:(size_t)bufsize;


+ (BOOL)boolClassMethod;
/* Return value arrays: */
- (int*)makeIntArrayOf5;
- (char**)makeStringArray;
- (int*)makeIntArrayOf:(int)count;
- (const int*)nullIntArrayOf5;
- (char**)nullStringArray;
- (int*)nullIntArrayOf:(int)count;
- (int*)unknownLengthArray;




/* In arrays: */
- (NSArray* _Nullable)makeIntArray:(int*)data count:(unsigned char)count;
- (NSArray* _Nullable)makeIntArray:(int*)data floatcount:(float)count;
- (NSArray* _Nullable)makeIntArray:(int*)data halfCount:(unsigned)count;
- (NSArray* _Nullable)makeIntArray:(int*)data countPtr:(unsigned*)countPtr;
- (NSArray* _Nullable)nullIntArray:(int*)data count:(unsigned)count;
- (NSArray* _Nullable)makeIntArray:(int*)array sameSize:(NSArray*)cnt;
- (NSArray* _Nullable)makeStringArray:(char**)data;
- (NSArray* _Nullable)makeObjectArray:(id*)data;
- (NSArray* _Nullable)nullStringArray:(char**)data;
- (NSArray* _Nullable)make4Tuple:(double*)data;
- (NSArray* _Nullable)null4Tuple:(double*)data;
- (NSArray* _Nullable)makeVariableLengthArray:(int*)array halfCount:(int)cnt;

/* Out arrays: */
- (void)fillArray:(int*)data count:(int)count;
- (int)nullfillArray:(int*)data count:(int)count;
- (void)fill4Tuple:(int*)data;
- (int)nullfill4Tuple:(int*)data;
- (int)fillArray:(int*)data uptoCount:(int)count;
- (int)maybeFillArray:(int*)data;

/* NULL-terminated output arrays can't work, these are just here to check that the
 * bridge knows this too.
 */
- (void)fillStringArray:(char**)data;
- (int)nullfillStringArray:(char**)data;

/* In/out arrays: */
- (void)reverseArray:(float*)data count:(int)count;
- (int)nullreverseArray:(float*)data count:(int)count;
- (void)reverseStrings:(char**)data;
- (int)nullreverseStrings:(char**)data;
- (void)reverse4Tuple:(short*)data;
- (int)nullreverse4Tuple:(short*)data;
- (int)reverseArray:(float*)data uptoCount:(int)count;
- (int)maybeReverseArray:(short*)data;

/* pass-by-reference */
- (int)sumX:(int*)x andY:(int*)y;         /* in */
- (int)divBy5:(int)x remainder:(int*)r;   /* out */
- (void)swapX:(double*)x andY:(double*)y; /* inout */
- (NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z;

- (NSArray* _Nullable)makeArrayWithFormat:(NSString*)fmt, ...;
- (NSArray* _Nullable)makeArrayWithCFormat:(char*)fmt, ...;
- (NSArray* _Nullable)makeArrayWithArguments:(id)arg, ...;

/* Helpers for calling back into python: */

+ (NSArray* _Nullable)makeIntArray:(int*)array sameSizeAs:(NSArray**)value on:(OC_MetaDataTest*)obj;;
+ (int*)makeIntArrayOf5On:(OC_MetaDataTest*)obj;
+ (char**)makeStringArrayOn:(OC_MetaDataTest*)obj;
+ (int*)makeIntArrayOf:(int)count on:(OC_MetaDataTest*)obj;
+ (const int*)nullIntArrayOf5On:(OC_MetaDataTest*)obj;
+ (char**)nullStringArrayOn:(OC_MetaDataTest*)obj;
+ (int*)nullIntArrayOf:(int)count on:(OC_MetaDataTest*)obj;
+ (NSArray*)makeIntArray:(int*)data count:(unsigned char)count on:(OC_MetaDataTest*)obj;
+ (NSArray* _Nullable)makeIntArray:(int*)array sameSize:(NSArray*)cnt on:(OC_MetaDataTest*)obj;
+ (NSArray*)makeIntArray:(int*)data countPtr:(unsigned*)countPtr on:(OC_MetaDataTest*)obj;
+ (NSArray*)nullIntArray:(int*)data count:(unsigned)count on:(OC_MetaDataTest*)obj;
+ (NSArray*)makeStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+ (NSArray*)makeObjectArray:(id*)data on:(OC_MetaDataTest*)obj;
+ (NSArray*)nullStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+ (NSArray*)make4Tuple:(double*)data on:(OC_MetaDataTest*)obj;
+ (NSArray*)null4Tuple:(double*)data on:(OC_MetaDataTest*)obj;
+ (void)fillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj;
+ (int)nullfillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj;
+ (void)fill4Tuple:(int*)data on:(OC_MetaDataTest*)obj;
+ (int)nullfill4Tuple:(int*)data on:(OC_MetaDataTest*)obj;
+ (int)fillArray:(int*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj;
+ (int)maybeFillArray:(int*)data on:(OC_MetaDataTest*)obj;
+ (void)fillStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+ (int)nullfillStringArray:(char**)data on:(OC_MetaDataTest*)obj;
+ (void)reverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj;
+ (int)nullreverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj;
+ (void)reverseStrings:(char**)data on:(OC_MetaDataTest*)obj;
+ (int)nullreverseStrings:(char**)data on:(OC_MetaDataTest*)obj;
+ (void)reverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj;
+ (int)nullreverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj;
+ (int)reverseArray:(float*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj;
+ (int)maybeReverseArray:(short*)data on:(OC_MetaDataTest*)obj;
+ (int)sumX:(int*)x andY:(int*)y on:(OC_MetaDataTest*)obj;
+ (int)divBy5:(int)x remainder:(int*)r on:(OC_MetaDataTest*)obj;
+ (void)swapX:(double*)x andY:(double*)y on:(OC_MetaDataTest*)obj;
+ (NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z on:(OC_MetaDataTest*)obj;

/* Various */
- (void)varargsMethodWithObjects:(id)first, ...;
- (int)ignoreMethod;

/* Byte arrays and C-strings */
- (NSData*)makeDataForBytes:(char*)data count:(int)count;
- (NSData*)makeDataForVoids:(void*)data count:(int)count;
- (void)addOneToBytes:(char*)data count:(int)count;
- (void)addOneToVoids:(void*)data count:(int)count;
- (void)fillBuffer:(char*)data count:(int)count;
- (void)fillVoids:(void*)data count:(int)count;


@end

@implementation OC_MetaDataTest

-(id(^)(int, float))getAnonBlock
{
    return ^(int a, float b) {
        return [NSString stringWithFormat:@"%d %f", a, b];
    };
}

-(id)callBlock:(id(^)(void))block
{
    return block();
}

+(id)callBlockOn:(OC_MetaDataTest*)obj
{
    return [obj callBlock:^ { return @"hello";}];
}


-(int)intInArg:(int)a
{
    return -a;
}

-(int)intOutArg:(int)a
{
    return 2-a;
}
-(int)intInOutArg:(int)a
{
    return 2+a;
}

+(int)intInArg:(int)a on:(OC_MetaDataTest*)obj
{
    return [obj intInArg:a];
}

+(int)intOutArg:(int)a on:(OC_MetaDataTest*)obj
{
    return [obj intOutArg:a];
}

+(int)intInOutArg:(int)a on:(OC_MetaDataTest*)obj
{
    return [obj intInOutArg:a];
}

-(id)derefResultArgument:(int*)value
{
    return @"shouldn't happen";
}

+(id)derefResultArgument:(int)value on:(OC_MetaDataTest*)obj
{
    return [obj derefResultArgument:&value];
}

+ (BOOL)boolClassMethod
{
    return YES;
}

- (int*)makeIntArrayOf5
{
    static int result[5];
    int        i;
    for (i = 0; i < 5; i++) {
        result[i] = i * i;
    }
    return result;
}

- (char**)makeStringArray
{
    static char* result[] = {"hello", "world", "out", "there", NULL};
    return result;
}

- (int*)makeIntArrayOf:(int)count
{
    static int* result = NULL;
    int         i;

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
- (const int*)nullIntArrayOf5
{
    return NULL;
}

- (char**)nullStringArray
{
    return NULL;
}

- (int*)nullIntArrayOf:(int)count
{
    use_int(count);
    return NULL;
}

- (NSArray*)nullIntArray:(int*)data count:(unsigned)count
{
    if (data) {
        return [self makeIntArray:data count:count];
    } else {
        return nil;
    }
}

- (NSArray*)makeIntArray:(int*)data countPtr:(unsigned*)countPtr
{
    return [self makeIntArray:data count:*countPtr];
}

- (NSArray*)makeIntArray:(int*)data halfCount:(unsigned)count
{
    return [self makeIntArray:data count:count * 2];
}

+ (NSArray* _Nullable)makeIntArray:(int*)data floatcount:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj makeIntArray:data floatcount:(float)count];
}

- (NSArray*)makeIntArray:(int*)data floatcount:(float)count
{
    return [self makeIntArray:data count:(unsigned char)count];
}

- (NSArray*)makeIntArray:(int*)data count:(unsigned char)count
{
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray arrayWithCapacity:count];

    for (i = 0; i < count; i++) {
        [array addObject:[NSNumber numberWithInt:data[i]]];
    }
    return array;
}

- (NSArray* _Nullable)makeIntArray:(int*)data sameSize:(NSArray*)cnt
{
    NSUInteger count = [cnt count];
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray arrayWithCapacity:count];

    for (i = 0; i < count; i++) {
        [array addObject:[NSNumber numberWithInt:data[i]]];
    }
    return array;
}

- (NSArray* _Nullable)makeIntArray:(int*)data sameSizeAs:(NSArray**)cnt
{
    NSUInteger count = cnt?(*cnt?[*cnt count]:0):0;
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray arrayWithCapacity:count];

    for (i = 0; i < count; i++) {
        [array addObject:[NSNumber numberWithInt:data[i]]];
    }
    return array;
}

- (NSArray*)make4Tuple:(double*)data
{
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray array];

    for (i = 0; i < 4; i++) {
        [array addObject:[NSNumber numberWithDouble:data[i]]];
    }
    return array;
}

- (NSArray*)make8Tuple:(double*)data
{
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray array];

    for (i = 0; i < 8; i++) {
        [array addObject:[NSNumber numberWithDouble:data[i]]];
    }
    return array;
}

- (NSArray*)make8TupleB:(double*)data
{
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray array];

    for (i = 0; i < 8; i++) {
        [array addObject:[NSNumber numberWithDouble:data[i]]];
    }
    return array;
}

- (NSArray*)null4Tuple:(double*)data
{
    if (data) {
        return [self make4Tuple:data];
    } else {
        return nil;
    }
}

- (NSArray*)nullStringArray:(char**)data
{
    if (data) {
        return [self makeStringArray:data];
    } else {
        return nil;
    }
}

- (NSArray*)makeStringArray:(char**)data
{
    NSMutableArray* array;

    array = [NSMutableArray array];

    while (*data != NULL) {
        NSObject* a = [NSString stringWithUTF8String:*data];
        if (!a)
            return nil;
        [array addObject:a];
        data++;
    }
    return array;
}

- (NSArray*)makeObjectArray:(id*)data
{
    NSMutableArray* array;

    array = [NSMutableArray array];

    while (*data != NULL) {
        [array addObject:*data];
        data++;
    }
    return array;
}

- (void)fillArray:(int*)data count:(int)count
{
    int i;
    for (i = 0; i < count; i++) {
        data[i] = i * i;
    }
}

- (int)nullfillArray:(int*)data count:(int)count
{
    if (data == NULL) {
        return 0;
    } else {
        [self fillArray:data count:count];
        return 1;
    }
}

- (void)fill4Tuple:(int*)data
{
    int i;
    for (i = 0; i < 4; i++) {
        data[i] = -i * i * i;
    }
}

- (int)nullfill4Tuple:(int*)data
{
    if (data == NULL) {
        return 0;
    } else {
        [self fill4Tuple:data];
        return 1;
    }
}

- (void)fillStringArray:(char**)data
{
    use_charpp(data);
    /* NULL-terminated output arrays can't work */
}

- (int)nullfillStringArray:(char**)data
{
    if (data == NULL)
        return 0;
    [self fillStringArray:data];
    return 1;
}

- (void)reverseArray:(float*)data count:(int)count
{
    float t;
    int   i;
    for (i = 0; i < count / 2; i++) {
        t                   = data[i];
        data[i]             = data[count - 1 - i];
        data[count - 1 - i] = t;
    }
}

- (int)nullreverseArray:(float*)data count:(int)count
{
    if (data == NULL)
        return 0;
    [self reverseArray:data count:count];
    return 1;
}

- (void)reverseStrings:(char**)data
{
    int   count, i;
    char* t;

    for (count = 0; data[count] != NULL; count++) {
        ;
    }

    for (i = 0; i < count / 2; i++) {
        t                   = data[i];
        data[i]             = data[count - 1 - i];
        data[count - 1 - i] = t;
    }
}

- (int)nullreverseStrings:(char**)data
{
    if (data == NULL)
        return 0;
    [self reverseStrings:data];
    return 1;
}

- (void)reverse4Tuple:(short*)data
{
    short t;

    t       = data[0];
    data[0] = data[3];
    data[3] = t;

    t       = data[1];
    data[1] = data[2];
    data[2] = t;
}

- (int)nullreverse4Tuple:(short*)data
{
    if (data == NULL)
        return 0;
    [self reverse4Tuple:data];
    return 1;
}

- (int)sumX:(int*)x andY:(int*)y /* in */
{
    return *x + *y;
}

- (int)divBy5:(int)x remainder:(int*)r /* out */
{
    *r = x % 5;
    return x / 5;
}

- (void)swapX:(double*)x andY:(double*)y /* inout */
{
    double t = *x;
    *x       = *y;
    *y       = t;
}

- (NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z
{
    char            buf[64];
    NSMutableArray* result = [NSMutableArray array];
    NSObject*       a;

    snprintf(buf, sizeof(buf), "%p", (void*)x);
    a = [NSString stringWithUTF8String:buf];
    if (!a)
        return nil;
    [result addObject:a];

    snprintf(buf, sizeof(buf), "%p", (void*)y);
    a = [NSString stringWithUTF8String:buf];
    if (!a)
        return nil;
    [result addObject:a];

    snprintf(buf, sizeof(buf), "%p", (void*)z);
    a = [NSString stringWithUTF8String:buf];
    if (!a)
        return nil;
    [result addObject:a];

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

- (int)fillArray:(int*)data uptoCount:(int)count
{
    int i;
    for (i = 0; i < count / 2; i++) {
        data[i] = i + 2;
    }
    for (i = count / 2; i < count; i++) {
        data[i] = -42;
    }
    return count / 2;
}

- (int)maybeFillArray:(int*)data
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

- (int)reverseArray:(float*)data uptoCount:(int)count
{
    [self reverseArray:data count:count];
    return count / 2;
}

- (int)maybeReverseArray:(short*)data
{
    [self reverse4Tuple:data];
    return 2;
}

- (id _Nullable)makeBuffer:(void*)buffer len:(size_t)bufsize
{
    return [NSData dataWithBytes:buffer length:bufsize];
}


+ (id)makeBuffer:(void*)buffer len:(size_t)bufsize on:(OC_MetaDataTest*)obj
{
    id value =  [obj makeBuffer:buffer len:bufsize];
    return value;
}

+ (int*)makeIntArrayOf5On:(OC_MetaDataTest*)obj
{
    return [obj makeIntArrayOf5];
}

+ (char**)makeStringArrayOn:(OC_MetaDataTest*)obj
{
    return [obj makeStringArray];
}

+ (int*)makeIntArrayOf:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj makeIntArrayOf:count];
}

+ (const int*)nullIntArrayOf5On:(OC_MetaDataTest*)obj
{
    return [obj nullIntArrayOf5];
}

+ (char**)nullStringArrayOn:(OC_MetaDataTest*)obj
{
    return [obj nullStringArray];
}

+ (int*)nullIntArrayOf:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj nullIntArrayOf:count];
}

+ (NSArray*)makeIntArray:(int*)data count:(unsigned char)count on:(OC_MetaDataTest*)obj
{
    return [obj makeIntArray:data count:count];
}

+ (NSArray* _Nullable)makeIntArray:(int*)array sameSize:(NSArray*)cnt on:(OC_MetaDataTest*)obj
{
    return [obj makeIntArray:array sameSize:cnt];
}

+ (NSArray* _Nullable)makeIntArray:(int*)array sameSizeAs:(NSArray**)cnt on:(OC_MetaDataTest*)obj
{
    return [obj makeIntArray:array sameSizeAs:cnt];
}

+ (NSArray* _Nullable)makeIntArray:(int*)array sameSizeAsNilOn:(OC_MetaDataTest*)obj
{
    NSArray* cnt = nil;
    return [obj makeIntArray:array sameSizeAs:&cnt];
}

+ (NSArray*)makeIntArray:(int*)data countPtr:(unsigned*)countPtr on:(OC_MetaDataTest*)obj
{
    return [obj makeIntArray:data countPtr:countPtr];
}

+ (NSArray*)nullIntArray:(int*)data count:(unsigned)count on:(OC_MetaDataTest*)obj
{
    return [obj nullIntArray:data count:count];
}

+ (NSArray*)makeStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
    return [obj makeStringArray:data];
}

+ (NSArray*)makeObjectArray:(id*)data on:(OC_MetaDataTest*)obj
{
    return [obj makeObjectArray:data];
}

+ (NSArray*)nullStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
    return [obj nullStringArray:data];
}

+ (NSArray*)make4Tuple:(double*)data on:(OC_MetaDataTest*)obj
{
    return [obj make4Tuple:data];
}

+ (NSArray*)make8Tuple:(double*)data on:(OC_MetaDataTest*)obj
{
    return [obj make8Tuple:data];
}

+ (NSArray*)make8TupleB:(double*)data on:(OC_MetaDataTest*)obj
{
    return [obj make8TupleB:data];
}

+ (NSArray*)null4Tuple:(double*)data on:(OC_MetaDataTest*)obj
{
    return [obj null4Tuple:data];
}

+ (void)fillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj
{
    [obj fillArray:data count:count];
}

+ (int)nullfillArray:(int*)data count:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj nullfillArray:data count:count];
}

+ (void)fill4Tuple:(int*)data on:(OC_MetaDataTest*)obj
{
    [obj fill4Tuple:data];
}

+ (int)nullfill4Tuple:(int*)data on:(OC_MetaDataTest*)obj
{
    return [obj nullfill4Tuple:data];
}

+ (int)fillArray:(int*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj fillArray:data uptoCount:count];
}

+ (int)maybeFillArray:(int*)data on:(OC_MetaDataTest*)obj
{
    return [obj maybeFillArray:data];
}

+ (void)fillStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
    [obj fillStringArray:data];
}

+ (int)nullfillStringArray:(char**)data on:(OC_MetaDataTest*)obj
{
    return [obj nullfillStringArray:data];
}

+ (void)reverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj
{
    [obj reverseArray:data count:count];
}

+ (int)nullreverseArray:(float*)data count:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj nullreverseArray:data count:count];
}

+ (void)reverseStrings:(char**)data on:(OC_MetaDataTest*)obj
{
    [obj reverseStrings:data];
}

+ (int)nullreverseStrings:(char**)data on:(OC_MetaDataTest*)obj
{
    return [obj nullreverseStrings:data];
}

+ (void)reverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj
{
    [obj reverse4Tuple:data];
}

+ (int)nullreverse4Tuple:(short*)data on:(OC_MetaDataTest*)obj
{
    return [obj nullreverse4Tuple:data];
}

+ (int)reverseArray:(float*)data uptoCount:(int)count on:(OC_MetaDataTest*)obj
{
    return [obj reverseArray:data uptoCount:count];
}

+ (int)maybeReverseArray:(short*)data on:(OC_MetaDataTest*)obj
{
    return [obj maybeReverseArray:data];
}

+ (int)sumX:(int*)x andY:(int*)y on:(OC_MetaDataTest*)obj
{
    return [obj sumX:x andY:y];
}

+ (int)divBy5:(int)x remainder:(int*)r on:(OC_MetaDataTest*)obj
{
    return [obj divBy5:x remainder:r];
}

+ (void)swapX:(double*)x andY:(double*)y on:(OC_MetaDataTest*)obj
{
    [obj swapX:x andY:y];
}

+ (NSArray*)input:(int*)x output:(int*)y inputAndOutput:(int*)z on:(OC_MetaDataTest*)obj
{
    return [obj input:x output:y inputAndOutput:z];
}

- (NSArray*)makeArrayWithFormat:(NSString*)fmt, ...
{
    va_list ap;
    char    buffer[2048];

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"

    va_start(ap, fmt);
    vsnprintf(buffer, sizeof(buffer), [fmt UTF8String], ap);
    va_end(ap);

#pragma clang diagnostic pop

    return [NSArray arrayWithObjects:fmt, [NSString stringWithUTF8String:buffer], NULL];
}

#pragma GCC diagnostic   push
#pragma clang diagnostic push
#pragma GCC diagnostic   ignored "-Wformat-nonliteral"
#pragma clang diagnostic ignored "-Wformat-nonliteral"

- (NSArray* _Nullable)makeArrayWithCFormat:(char*)fmt, ...
{
    va_list   ap;
    char      buffer[2048];
    NSObject* a1;
    NSObject* a2;

    va_start(ap, fmt);
    vsnprintf(buffer, sizeof(buffer), fmt, ap);
    va_end(ap);

    a1 = [NSString stringWithUTF8String:fmt];
    if (!a1)
        return nil;
    a2 = [NSString stringWithUTF8String:buffer];
    if (!a2)
        return nil;

    return [NSArray arrayWithObjects:a1, a2, nil];
}
#pragma GCC diagnostic   pop
#pragma clang diagnostic pop

- (NSArray*)makeArrayWithArguments:(id)arg, ...
{
    va_list         ap;
    NSMutableArray* array = [[[NSMutableArray alloc] init] autorelease];
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

- (void)varargsMethodWithObjects:(id)first, ...
{
    use_id(first);
}

- (int)ignoreMethod
{
    return 42;
}

- (NSData*)makeDataForBytes:(char*)data count:(int)count
{
    return [NSData dataWithBytes:data length:count];
}

- (NSData*)makeDataForVoids:(void*)data count:(int)count
{
    return [NSData dataWithBytes:data length:count];
}

- (void)addOneToBytes:(char*)data count:(int)count
{
    int i;
    for (i = 0; i < count; i++) {
        data[i] += 1;
    }
}

- (void)addOneToVoids:(void*)data count:(int)count
{
    int i;
    for (i = 0; i < count; i++) {
        ((char*)data)[i] += 2;
    }
}

- (void)fillBuffer:(char*)data count:(int)count
{
    memset(data, '\xfe', count);
}

- (void)fillVoids:(void*)data count:(int)count
{
    memset(data, '\xab', count);
}

- (int*)unknownLengthArray
{
    static int theValue[] = {1, 3, 5, 7, 11, 13, 17, 19};
    return theValue;
}

- (int*)unknownLengthMutable
{
    static int theValue[20];
    return theValue;
}

- (NSArray*)makeVariableLengthArray:(int*)array halfCount:(int)cnt
{
    cnt *= 2;

    NSMutableArray* result;
    int             i;

    result = [NSMutableArray arrayWithCapacity:cnt];

    for (i = 0; i < cnt; i++) {
        [result addObject:[NSNumber numberWithFloat:array[i]]];
    }
    return result;
}

- (NSArray* _Nullable)makeNullDelimitedObjectArray:(id)value, ...
{
    va_list ap;
    NSMutableArray* result = [NSMutableArray array];
    if (!result) return nil;

    va_start(ap, value);

    while(value != nil) {
        [result addObject:value];

        value = va_arg(ap, id);
    }

    va_end(ap);
    return result;
}

- (NSArray* _Nullable)makeNullDelimitedIntArray:(int)value, ...
{
    va_list ap;
    NSMutableArray* result = [NSMutableArray array];
    if (!result) return nil;

    va_start(ap, value);

    while(value) {
        [result addObject:[NSNumber numberWithInt:value]];

        value = va_arg(ap, int);
    }

    va_end(ap);
    return result;
}

- (NSArray* _Nullable) makeCountedObjectArray:(int)count values:(id)value, ...
{
    va_list ap;
    int i;
    NSMutableArray* result = [NSMutableArray array];
    if (!result) return nil;

    va_start(ap, value);

    for (i = 0; i < count; i++) {
        [result addObject:value];
        value = va_arg(ap, id);
    }

    va_end(ap);
    return result;
}

- (NSArray* _Nullable) makeCountedIntArray:(int)count values:(int)value, ...
{
    va_list ap;
    int i;
    NSMutableArray* result = [NSMutableArray array];
    if (!result) return nil;

    va_start(ap, value);

    for (i = 0; i < count; i++) {
        [result addObject:[NSNumber numberWithInt:value]];
        value = va_arg(ap, int);
    }

    va_end(ap);
    return result;
}

+ (NSArray*)makeVariableLengthArray:(int*)array halfCount:(int)cnt on:(OC_MetaDataTest*)value
{
    return [value makeVariableLengthArray:array halfCount:cnt];
}

/* various pointer return values */
- (int* _Nullable)returnPointerPlain
{
    static int value = 42;
    return &value;
}

- (int* _Nullable)returnPointerFixedLen
{
    static int values[5] = { 2, 3, 5, 7, 11 };
    return values;
}

- (char* _Nullable)returnCharPFixedLen
{
    return "hello";
}

- (int* _Nullable)returnPointerVariadic
{
    static int values[] = { 2, 4, 8, 16, 32, 64, 128, 256, 512 };
    return values;
}

- (int* _Nullable)returnPointerNullDelimited
{
    static int values[] = { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
    return values;
}

- (char* _Nullable)returnCharPNullDelimited
{
    return "hello world\0xyz";;
}

- (int* _Nullable)returnPointerCounted:(int)count
{
    static int* cache = NULL;

    if (cache != NULL) {
        free(cache);
    }

    cache = malloc(count * sizeof(int));
    if (cache == NULL) {
        return NULL;
    }

    for(int i = 0; i < count; i++) {
        cache[i] = -i * i;
    }
    return cache;
}
- (int* _Nullable)returnPointerFloatCounted:(float)count
{
    return [self returnPointerCounted:(int)count];
}

- (int* _Nullable)returnPointerCountedIn:(int*)count
{
    return [self returnPointerCounted:*count];
}

- (int* _Nullable)returnPointerCountedOut:(int*)count
{
    *count=3;
    return [self returnPointerCounted:*count];
}

- (int* _Nullable) returnPointerCountedInOut:(int*)count
{
    int prev = *count;
    *count=3;
    int* result = [self returnPointerCounted:*count];
    if (result) {
        result[0] = prev;
    }
    return result;
}

- (int* _Nullable)returnPointerDeref
{
    static int value = 99;
    return &value;
}

-(int* _Nullable)returnPointerToFree
{
    int* result = malloc(4*sizeof(int));
    if (result == NULL) {
        return NULL;
    }
    result[0] = 0;
    result[1] = 1;
    result[2] = 2;
    result[3] = 3;
    return result;
}

-(int* _Nullable)returnPointerToFreeVariadic
{
    int* result = malloc(4*sizeof(int));
    if (result == NULL) {
        return NULL;
    }
    result[0] = 0;
    result[1] = 1;
    result[2] = 2;
    result[3] = 3;
    return result;
}

+ (int* _Nullable)returnPointerPlainOn:(OC_MetaDataTest*)value
{
    return [value returnPointerPlain];
}

+ (int* _Nullable)returnPointerFixedLenOn:(OC_MetaDataTest*)value
{
    return [value returnPointerFixedLen];
}

+ (char* _Nullable)returnCharPFixedLenOn:(OC_MetaDataTest*)value
{
    return [value returnCharPFixedLen];
}

+ (int* _Nullable)returnPointerVariadicOn:(OC_MetaDataTest*)value
{
    return [value returnPointerVariadic];
}

+ (int* _Nullable)returnPointerNullDelimitedOn:(OC_MetaDataTest*)value
{
    return [value returnPointerNullDelimited];
}

+ (char* _Nullable)returnCharPNullDelimitedOn:(OC_MetaDataTest*)value
{
    return [value returnCharPNullDelimited];
}

+ (int* _Nullable)returnPointerCounted:(int)count on:(OC_MetaDataTest*)value
{
    return [value returnPointerCounted:count];
}

+ (int* _Nullable)returnPointerFloatCounted:(int)count on:(OC_MetaDataTest*)value
{
    return [value returnPointerFloatCounted:count];
}

+ (int* _Nullable)returnPointerCountedIn:(int*)count on:(OC_MetaDataTest*)value
{
    return [value returnPointerCountedIn:count];
}

+ (int* _Nullable)returnPointerCountedOut:(int*)count on:(OC_MetaDataTest*)value
{
    return [value returnPointerCountedOut:count];
}

+ (int* _Nullable)returnPointerCountedInOut:(int*)count on:(OC_MetaDataTest*)value
{
    return [value returnPointerCountedInOut:count];
}

+ (int* _Nullable)returnPointerDerefOn:(OC_MetaDataTest*)value
{
    return [value returnPointerDeref];
}

+ (int* _Nullable)returnPointerToFreeOn:(OC_MetaDataTest*)value
{
    return [value returnPointerToFree];
}

+ (int* _Nullable)returnPointerToFreeVariadicOn:(OC_MetaDataTest*)value
{
    return [value returnPointerToFreeVariadic];
}


/* Char* input argument (_C_CHARPTR) */
- (id _Nullable)charpArgPlain:(char*)arg
{
    return nil;
}

- (id _Nullable)charpArgNullTerminated:(char*)arg
{
    return nil;
}

- (id _Nullable)charpArg5Chars:(char*)arg
{
    return nil;
}

- (id _Nullable)charpArgVariadic:(char*)arg
{
    return nil;
}

- (id _Nullable)charpArgDeref:(char*)arg
{
    return nil;
}

- (id _Nullable)charpArgCounted:(char*)arg count:(int)c
{
    return nil;
}

- (id _Nullable)charpArgCounted:(char*)arg floatcount:(float)c
{
    return nil;
}

+ (id _Nullable)charpArgPlainOn:(OC_MetaDataTest*)value
{
    return [value charpArgPlain:NULL];
}

+ (id _Nullable)charpArgPlain:(char*)arg on:(OC_MetaDataTest*)value
{
    return [value charpArgPlain:arg];
}

+ (id _Nullable)charpArgNullTerminated:(char*)arg on:(OC_MetaDataTest*)value
{
    return [value charpArgNullTerminated:arg];
}

+ (id _Nullable)charpArg5Chars:(char*)arg on:(OC_MetaDataTest*)value
{
    return [value charpArg5Chars:arg];
}

+ (id _Nullable)charpArgVariadic:(char*)arg on:(OC_MetaDataTest*)value
{
    return [value charpArgVariadic:arg];
}

+ (id _Nullable)charpArgDeref:(char*)arg on:(OC_MetaDataTest*)value
{
    return [value charpArgDeref:arg];
}

+ (id _Nullable)charpArgCounted:(char*)arg count:(int)c on:(OC_MetaDataTest*)value
{
    return [value charpArgCounted:arg count:c];
}

+ (id _Nullable)charpArgCounted:(char*)arg floatcount:(int)c on:(OC_MetaDataTest*)value
{
    return [value charpArgCounted:arg floatcount:(float)c];
}

/* Already retained values */
- (id _Nullable) NS_RETURNS_RETAINED retainedObjCObject
{
    return [[NSArray alloc] init];
}

- (id _Nullable) NS_RETURNS_RETAINED retainedCFObject
{
    return (id)CFArrayCreate(kCFAllocatorDefault, NULL, 0, &kCFTypeArrayCallBacks);
}

+(id _Nullable) NS_RETURNS_RETAINED retainedObjCObjectOn:(OC_MetaDataTest*)value
{
    return [value retainedObjCObject];
}

+(id _Nullable) NS_RETURNS_RETAINED retainedCFObjectOn:(OC_MetaDataTest*)value
{
    return [value retainedCFObject];
}

/* Handling by-ref output arguments */
/* all of them in two variants: void return and value return */

-(void)voidOutChar:(char*)value
{
    if (value) {
        *value = 44;
    }
}
-(int)intOutChar:(char*)value
{
    if (value) {
        *value = 45;
    }
    return value?1:0;
}

-(void)voidOutCharPtr:(char**)value
{
    if (value) {
        *value = "hello\0world";
    }
}
-(int)intOutCharPtr:(char**)value
{
    if (value) {
        *value = "hello\0world";
    }
    return value?1:0;
}

-(void)voidOutId:(id*)value
{
    if (value) {
        *value = @"hello world";
    }
}
-(int)intOutId:(id*)value
{
    if (value) {
        *value = @"hello world";
    }
    return value?1:0;
}

-(void)voidOutIdRetained:(id*)value
{
    if (value) {
        *value = [[NSArray alloc] init];
    }
}
-(int)intOutIdRetained:(id*)value
{
    if (value) {
        *value = [[NSArray alloc] init];
    }
    return value?1:0;
}

-(void)voidOutIdCFRetained:(id*)value
{
    if (value) {
        *value = (id)CFArrayCreate(kCFAllocatorDefault, NULL, 0, &kCFTypeArrayCallBacks);
    }
}
-(int)intOutIdCFRetained:(id*)value
{
    if (value) {
        *value = (id)CFArrayCreate(kCFAllocatorDefault, NULL, 0, &kCFTypeArrayCallBacks);
    }
    return value?1:0;
}

-(void)voidOutInt:(int*)outval add:(int)inval
{
    if (outval) {
        *outval = inval * 2;
    }
}
-(int)intOutInt:(int*)outval add:(int)inval
{
    if (outval) {
        *outval = inval * 2;
    }
    return outval?1:0;
}

+(void)voidOutChar:(char*)value on:(OC_MetaDataTest*)obj
{
    [obj voidOutChar:value];
}
+(int)intOutChar:(char*)value on:(OC_MetaDataTest*)obj
{
    return [obj intOutChar:value];
}

+(void)voidOutCharPtr:(char**)value on:(OC_MetaDataTest*)obj
{
    [obj voidOutCharPtr:value];
}
+(int)intOutCharPtr:(char**)value on:(OC_MetaDataTest*)obj
{
    return [obj intOutCharPtr:value];
}

+(void)voidOutId:(id*)value on:(OC_MetaDataTest*)obj
{
    [obj voidOutId:value];
}
+(int)intOutId:(id*)value on:(OC_MetaDataTest*)obj
{
    return [obj intOutId:value];
}

+(void)voidOutIdRetained:(id*)value on:(OC_MetaDataTest*)obj
{
    [obj voidOutIdRetained:value];
}
+(int)intOutIdRetained:(id*)value on:(OC_MetaDataTest*)obj
{
    return [obj intOutIdRetained:value];
}

+(void)voidOutIdCFRetained:(id*)value on:(OC_MetaDataTest*)obj
{
    [obj voidOutIdCFRetained:value];
}
+(int)intOutIdCFRetained:(id*)value on:(OC_MetaDataTest*)obj
{
    return [obj intOutIdCFRetained:value];
}

+(void)voidOutInt:(int*)outval add:(int)inval on:(OC_MetaDataTest*)obj
{
    [obj voidOutInt:outval add:inval];
}
+(int)intOutInt:(int*)outval add:(int)inval on:(OC_MetaDataTest*)obj
{
    return [obj intOutInt:outval add:inval];
}


@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_MetaDataTest",
                           PyObjC_IdToPython([OC_MetaDataTest class]))
        < 0) {

        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "metadata",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_metadata(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_metadata(void)
{
    return PyModuleDef_Init(&mod_module);
}
