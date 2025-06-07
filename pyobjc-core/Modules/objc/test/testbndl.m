/*
 * This file implements a (number of) class(es) that are used to test
 * method calling with PyObjC (both python -> ObjC and back)
 *
 * NOTES
 * - The implementation must be synchronized with test_methods.py, see that
 *   file for more details.
 * - When adding new methods to OC_TestClass1 *always* add invoke- and call-
 *   variants to OC_TestClass2.
 */

#include "Python.h"
#include "pyobjc-api.h"
#include "pyobjc-compat.h"

#import <Foundation/Foundation.h>

#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif

#include <float.h>
#include <limits.h>

#ifdef __clang__
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#endif /* __clang__ */

#if !defined(LLONG_MAX) && defined(LONG_LONG_MAX)

#define LLONG_MAX LONG_LONG_MAX
#define LLONG_MIN LONG_LONG_MIN
#define ULLONG_MAX ULONG_LONG_MAX

#endif

struct dummy {
    int   f1;
    short f2;
};

struct dummy2 {
    int array[4];
};

struct s1 {
    int    i;
    double d;
};

struct complexStruct {
    /*  0 */ char           ch;
    /*  1 */ unsigned char  uch;
    /*  4 */ int            i1;
    /*  8 */ unsigned int   u;
    /* 12 */ short          s;
    /* 20 */ double         d;
    /* 28 */ struct s1      sub1[2];
    /* 60 */ int            i2;
    /* 62 */ unsigned short us;
    /* 64 */ char*          str;
};

typedef NSObject<NSObject> ObjectClass;

@interface OC_TestClass1 : NSObject {
}

/* Reset the test counter */
+ (void)clsReset;
- (void)reset;

/* Test return values, return various values */
+ (long long)longlongClsFunc;
+ (unsigned long long)ulonglongClsFunc;
+ (long)longClsFunc;
+ (unsigned long)ulongClsFunc;
+ (int)intClsFunc;
+ (unsigned int)uintClsFunc;
+ (short)shortClsFunc;
+ (unsigned short)ushortClsFunc;
+ (char)charClsFunc;
+ (unsigned char)ucharClsFunc;
+ (float)floatClsFunc;
+ (double)doubleClsFunc;
+ (long double)longdoubleClsFunc;
+ (char*)charpClsFunc;
+ (id)idClsFunc;

- (long long)longlongFunc;
- (unsigned long long)ulonglongFunc;
- (long)longFunc;
- (unsigned long)ulongFunc;
- (int)intFunc;
- (unsigned int)uintFunc;
- (short)shortFunc;
- (unsigned short)ushortFunc;
- (char)charFunc;
- (unsigned char)ucharFunc;
- (float)floatFunc;
- (double)doubleFunc;
- (long double)longdoubleFunc;
- (char*)charpFunc;
- (id)idFunc;
- (NSPoint)nspointFunc;

/* returns of complex values */
- (struct dummy)dummyFunc;
- (struct dummy2)dummy2Func;

/* argument passing for simple types */
- (long long)longlongArg:(long long)arg;
- (unsigned long long)ulonglongArg:(unsigned long long)arg;
- (long)longArg:(long)arg;
- (unsigned long)ulongArg:(unsigned long)arg;
- (int)intArg:(int)arg;
- (unsigned int)uintArg:(unsigned int)arg;
- (short)shortArg:(short)arg;
- (unsigned short)ushortArg:(unsigned short)arg;
- (char)charArg:(char)arg;
- (unsigned char)ucharArg:(unsigned char)arg;
- (float)floatArg:(float)arg;
- (double)doubleArg:(double)arg;
- (long double)longdoubleArg:(long double)arg;
- (char*)charpArg:(char*)arg;
- (id)idArg:(id)arg;

/* argument passing for complex values */
- (struct dummy)dummyArg:(struct dummy)arg;
- (struct dummy2)dummy2Arg:(struct dummy2)arg;

/* in, out and in-out arguments */
- (char)passInChar:(char*)arg;
- (void)passOutChar:(char*)arg;
- (void)passInOutChar:(char*)arg;
- (short)passInShort:(short*)arg;
- (void)passOutShort:(short*)arg;
- (void)passInOutShort:(short*)arg;
- (int)passInInt:(int*)arg;
- (void)passOutInt:(int*)arg;
- (void)passInOutInt:(int*)arg;
- (long)passInLong:(long*)arg;
- (void)passOutLong:(long*)arg;
- (void)passInOutLong:(long*)arg;
- (long long)passInLongLong:(long long*)arg;
- (void)passOutLongLong:(long long*)arg;
- (void)passInOutLongLong:(long long*)arg;
- (unsigned char)passInUChar:(unsigned char*)arg;
- (void)passOutUChar:(unsigned char*)arg;
- (void)passInOutUChar:(unsigned char*)arg;
- (unsigned short)passInUShort:(unsigned short*)arg;
- (void)passOutUShort:(unsigned short*)arg;
- (void)passInOutUShort:(unsigned short*)arg;
- (unsigned int)passInUInt:(unsigned int*)arg;
- (void)passOutUInt:(unsigned int*)arg;
- (void)passInOutUInt:(unsigned int*)arg;
- (unsigned long)passInULong:(unsigned long*)arg;
- (void)passOutULong:(unsigned long*)arg;
- (void)passInOutULong:(unsigned long*)arg;
- (unsigned long long)passInULongLong:(unsigned long long*)arg;
- (void)passOutULongLong:(unsigned long long*)arg;
- (void)passInOutULongLong:(unsigned long long*)arg;
- (float)passInFloat:(float*)arg;
- (void)passOutFloat:(float*)arg;
- (void)passInOutFloat:(float*)arg;
- (double)passInDouble:(double*)arg;
- (long double)passInLongDouble:(long double*)arg;
- (void)passOutDouble:(double*)arg;
- (void)passOutLongDouble:(long double*)arg;
- (void)passInOutDouble:(double*)arg;
- (void)passInOutLongDouble:(long double*)arg;
- (char*)passInCharp:(char**)arg;
- (void)passOutCharp:(char**)arg;
- (void)passInOutCharp:(char**)arg;
- (id)passInID:(id*)arg;
- (void)passOutID:(id*)arg;
- (void)passInOutID:(id*)arg;

- (ObjectClass*)returnObjectValue:(int)t;

@end

@implementation OC_TestClass1
#if __has_feature(c_atomic)
static _Atomic size_t             g_idx          = 0;
#else
static size_t             g_idx          = 0;
#endif

#define ARRAYSIZE(a) (sizeof(a) / sizeof(a[0]))
static unsigned long long g_ulonglongs[] = {0, 42, (1LL << 63)};
static unsigned long      g_ulongs[]     = {0, 42, (1 << 30)};
static long long          g_longlongs[]  = {-(1LL << 60), -42, 0, 42, (1LL << 60)};
static long               g_longs[]      = {-(1 << 30), -42, 0, 42, (1 << 30)};
static int                g_ints[]       = {-(1 << 30), -42, 0, 42, (1 << 30)};
static unsigned int       g_uints[]      = {0, 42, 1 << 30};
static short              g_shorts[]     = {-(1 << 14), -42, 0, 42, (1 << 14)};
static unsigned short     g_ushorts[]    = {0, 42, 1 << 14};
static char               g_chars[]      = {-128, 0, 127};
static unsigned char      g_uchars[]     = {0, 128, 255};
static float              g_floats[]     = {0.128, 1.0, 42.0, 1e10};
static double             g_doubles[]    = {0.128, 1.0, 42.0, 1e10};
static long double        g_longdoubles[]= {0.128, 1.0, 42.0, 1e10};

static char* g_charps[] = {"hello", "world", "foobar"};

+ (void)clsReset
{
    g_idx = 0;
}

+ (long long)longlongClsFunc
{
    if (g_idx > ARRAYSIZE(g_longlongs))
        g_idx = 0;
    return g_longlongs[g_idx++];
}

+ (unsigned long long)ulonglongClsFunc
{
    if (g_idx > ARRAYSIZE(g_ulonglongs))
        g_idx = 0;
    return g_ulonglongs[g_idx++];
}

+ (long)longClsFunc
{
    if (g_idx > ARRAYSIZE(g_longs))
        g_idx = 0;
    return g_longs[g_idx++];
}

+ (unsigned long)ulongClsFunc
{
    if (g_idx > ARRAYSIZE(g_ulongs))
        g_idx = 0;
    return g_ulongs[g_idx++];
}

+ (int)intClsFunc
{
    if (g_idx > ARRAYSIZE(g_ints))
        g_idx = 0;
    return g_ints[g_idx++];
}

+ (unsigned int)uintClsFunc
{
    if (g_idx > ARRAYSIZE(g_uints))
        g_idx = 0;
    return g_uints[g_idx++];
}

+ (short)shortClsFunc
{
    if (g_idx > ARRAYSIZE(g_shorts))
        g_idx = 0;
    return g_shorts[g_idx++];
}

+ (unsigned short)ushortClsFunc
{
    if (g_idx > ARRAYSIZE(g_ushorts))
        g_idx = 0;
    return g_ushorts[g_idx++];
}

+ (char)charClsFunc
{
    if (g_idx > ARRAYSIZE(g_chars))
        g_idx = 0;
    return g_chars[g_idx++];
}

+ (unsigned char)ucharClsFunc
{
    if (g_idx > ARRAYSIZE(g_uchars))
        g_idx = 0;
    return g_uchars[g_idx++];
}

+ (float)floatClsFunc
{
    if (g_idx > ARRAYSIZE(g_floats))
        g_idx = 0;
    return g_floats[g_idx++];
}

+ (double)doubleClsFunc
{
    if (g_idx > ARRAYSIZE(g_doubles))
        g_idx = 0;
    return g_doubles[g_idx++];
}

+ (long double)longdoubleClsFunc
{
    if (g_idx > ARRAYSIZE(g_longdoubles))
        g_idx = 0;
    return g_longdoubles[g_idx++];
}

+ (char*)charpClsFunc
{
    if (g_idx > ARRAYSIZE(g_charps))
        g_idx = 0;
    return g_charps[g_idx++];
}

+ (id)idClsFunc
{
    if (g_idx > 3)
        g_idx = 0;

    switch (g_idx++) {
    case 0:
        return [NSArray array];
    case 1:
        return [NSHost hostWithAddress:@"127.0.0.1"];
    case 2:
        return [NSMutableDictionary dictionary];
    case 3:
        return NULL;
    }
    return NULL;
}

- (void)reset
{
    g_idx = 0;
}

- (long long)longlongFunc
{
    if (g_idx > ARRAYSIZE(g_longlongs))
        g_idx = 0;
    return g_longlongs[g_idx++];
}

- (unsigned long long)ulonglongFunc
{
    if (g_idx > ARRAYSIZE(g_ulonglongs))
        g_idx = 0;
    return g_ulonglongs[g_idx++];
}

- (long)longFunc
{
    if (g_idx > ARRAYSIZE(g_longs))
        g_idx = 0;
    return g_longs[g_idx++];
}

- (unsigned long)ulongFunc
{
    if (g_idx > ARRAYSIZE(g_ulongs))
        g_idx = 0;
    return g_ulongs[g_idx++];
}

- (int)intFunc
{
    if (g_idx > ARRAYSIZE(g_ints))
        g_idx = 0;
    return g_ints[g_idx++];
}

- (unsigned int)uintFunc
{
    if (g_idx > ARRAYSIZE(g_uints))
        g_idx = 0;
    return g_uints[g_idx++];
}

- (short)shortFunc
{
    if (g_idx > ARRAYSIZE(g_shorts))
        g_idx = 0;
    return g_shorts[g_idx++];
}

- (unsigned short)ushortFunc
{
    if (g_idx > ARRAYSIZE(g_ushorts))
        g_idx = 0;
    return g_ushorts[g_idx++];
}

- (char)charFunc
{
    if (g_idx > ARRAYSIZE(g_chars))
        g_idx = 0;
    return g_chars[g_idx++];
}

- (unsigned char)ucharFunc
{
    if (g_idx > ARRAYSIZE(g_uchars))
        g_idx = 0;
    return g_uchars[g_idx++];
}

- (float)floatFunc
{
    if (g_idx > ARRAYSIZE(g_floats))
        g_idx = 0;
    return g_floats[g_idx++];
}

- (double)doubleFunc
{
    if (g_idx > ARRAYSIZE(g_doubles))
        g_idx = 0;
    return g_doubles[g_idx++];
}

- (long double)longdoubleFunc
{
    if (g_idx > ARRAYSIZE(g_longdoubles))
        g_idx = 0;
    return g_longdoubles[g_idx++];
}

- (char*)charpFunc
{
    if (g_idx > ARRAYSIZE(g_charps))
        g_idx = 0;
    return g_charps[g_idx++];
}

- (id)idFunc
{
    if (g_idx > 3)
        g_idx = 0;

    switch (g_idx++) {
    case 0:
        return [NSArray array];
    case 1:
        return [NSHost hostWithAddress:@"127.0.0.1"];
    case 2:
        return [NSMutableDictionary dictionary];
    case 3:
        return NULL;
    }
    return NULL;
}

- (NSPoint)nspointFunc
{
    NSPoint p = {1.0, 2.0};
    return p;
}

- (struct dummy)dummyFunc
{
    struct dummy res;

    res.f1 = -1;
    res.f2 = +1;

    return res;
}

- (struct dummy2)dummy2Func
{
    struct dummy2 res;

    res.array[0] = 1;
    res.array[1] = 2;
    res.array[2] = 3;
    res.array[3] = 4;

    return res;
}

/*
 *
 * Simple, single, pass by value arguments. We return the argument after
 * modifying it. This should help to uncover cases where the bridge returns
 * the first argument instead of the real return value.
 */

- (long long)longlongArg:(long long)arg
{
    return arg / 2;
}

- (unsigned long long)ulonglongArg:(unsigned long long)arg
{
    return arg / 2;
}

- (long)longArg:(long)arg
{
    return arg / 2;
}

- (unsigned long)ulongArg:(unsigned long)arg
{
    return arg / 2;
}

- (int)intArg:(int)arg
{
    return arg / 2;
}

- (unsigned int)uintArg:(unsigned int)arg
{
    return arg / 2;
}

- (short)shortArg:(short)arg
{
    return arg / 2;
}

- (unsigned short)ushortArg:(unsigned short)arg
{
    return arg / 2;
}

- (char)charArg:(char)arg
{
    return arg / 2;
}

- (unsigned char)ucharArg:(unsigned char)arg
{
    return arg / 2;
}

- (float)floatArg:(float)arg
{
    return arg / 2;
}

- (double)doubleArg:(double)arg
{
    return arg / 2;
}

- (long double)longdoubleArg:(long double)arg
{
    return arg / 2;
}

- (char*)charpArg:(char*)arg
{
    static char buf[1024];
    size_t      len = strlen(arg);
    size_t      i;

    for (i = 0; i < len; i++) {
        buf[len - i - 1] = arg[i];
    }
    buf[len] = 0;

    return buf;
}

- (id)idArg:(id)arg
{
    id temp;

    if (arg == NULL) {
        temp = [NSNull null];
    } else {
        temp = arg;
    }
    return [NSArray arrayWithObject:temp];
}

- (struct dummy)dummyArg:(struct dummy)arg
{
    struct dummy result;

    result.f1 = arg.f1 * 2;
    result.f2 = arg.f2 * 2;

    return result;
}

- (struct dummy2)dummy2Arg:(struct dummy2)arg
{
    struct dummy2 result = {{-1, -1, -1, -1}};

    result.array[0] = arg.array[3] * 2;
    result.array[1] = arg.array[2] * 2;
    result.array[2] = arg.array[1] * 2;
    result.array[3] = arg.array[0] * 2;

    return result;
}

- (char)passInChar:(char*)arg
{
    return *arg + 9;
}

- (void)passOutChar:(char*)arg
{
    if (g_idx > ARRAYSIZE(g_ints))
        g_idx = 0;
    *arg = g_chars[g_idx++];
}

- (void)passInOutChar:(char*)arg
{
    *arg += 42;
}

- (unsigned char)passInUChar:(unsigned char*)arg
{
    return *arg + 9;
}

- (void)passOutUChar:(unsigned char*)arg
{
    if (g_idx > ARRAYSIZE(g_uchars))
        g_idx = 0;
    *arg = g_uchars[g_idx++];
}

- (void)passInOutUChar:(unsigned char*)arg
{
    *arg += 42;
}

- (short)passInShort:(short*)arg
{
    return *arg + 9;
}

- (void)passOutShort:(short*)arg
{
    if (g_idx > ARRAYSIZE(g_shorts))
        g_idx = 0;
    *arg = g_shorts[g_idx++];
}

- (void)passInOutShort:(short*)arg
{
    *arg += 42;
}

- (unsigned short)passInUShort:(unsigned short*)arg
{
    return *arg + 9;
}

- (void)passOutUShort:(unsigned short*)arg
{
    if (g_idx > ARRAYSIZE(g_ushorts))
        g_idx = 0;
    *arg = g_ushorts[g_idx++];
}

- (void)passInOutUShort:(unsigned short*)arg
{
    *arg += 42;
}

- (int)passInInt:(int*)arg
{
    return *arg + 9;
}

- (void)passOutInt:(int*)arg
{
    if (g_idx > ARRAYSIZE(g_ints))
        g_idx = 0;
    *arg = g_ints[g_idx++];
}

- (void)passInOutInt:(int*)arg
{
    *arg += 42;
}

- (unsigned int)passInUInt:(unsigned int*)arg
{
    return *arg + 9;
}

- (void)passOutUInt:(unsigned int*)arg
{
    if (g_idx > ARRAYSIZE(g_uints))
        g_idx = 0;
    *arg = g_uints[g_idx++];
}

- (void)passInOutUInt:(unsigned int*)arg
{
    *arg += 42;
}

- (long)passInLong:(long*)arg
{
    return *arg + 9;
}

- (void)passOutLong:(long*)arg
{
    if (g_idx > ARRAYSIZE(g_longs))
        g_idx = 0;
    *arg = g_longs[g_idx++];
}

- (void)passInOutLong:(long*)arg
{
    *arg += 42;
}

- (unsigned long)passInULong:(unsigned long*)arg
{
    return *arg + 9;
}

- (void)passOutULong:(unsigned long*)arg
{
    if (g_idx > ARRAYSIZE(g_ulongs))
        g_idx = 0;
    *arg = g_ulongs[g_idx++];
}

- (void)passInOutULong:(unsigned long*)arg
{
    *arg += 42;
}

- (long long)passInLongLong:(long long*)arg
{
    return *arg + 9;
}

- (void)passOutLongLong:(long long*)arg
{
    if (g_idx > ARRAYSIZE(g_longlongs))
        g_idx = 0;
    *arg = g_longlongs[g_idx++];
}

- (void)passInOutLongLong:(long long*)arg
{
    *arg += 42;
}

- (unsigned long long)passInULongLong:(unsigned long long*)arg
{
    return *arg + 9;
}

- (void)passOutULongLong:(unsigned long long*)arg
{
    if (g_idx > ARRAYSIZE(g_ulonglongs))
        g_idx = 0;
    *arg = g_ulonglongs[g_idx++];
}

- (void)passInOutULongLong:(unsigned long long*)arg
{
    *arg += 42;
}

- (float)passInFloat:(float*)arg
{
    return *arg * 9;
}

- (void)passOutFloat:(float*)arg
{
    if (g_idx > ARRAYSIZE(g_floats))
        g_idx = 0;
    *arg = g_floats[g_idx++];
}

- (void)passInOutFloat:(float*)arg
{
    *arg *= 42;
}

- (double)passInDouble:(double*)arg
{
    return *arg * 9;
}

- (long double)passInLongDouble:(long double*)arg
{
    return *arg * 9;
}

- (void)passOutDouble:(double*)arg
{
    if (g_idx > ARRAYSIZE(g_doubles))
        g_idx = 0;
    *arg = g_doubles[g_idx++];
}

- (void)passOutLongDouble:(long double*)arg
{
    if (g_idx > ARRAYSIZE(g_longdoubles))
        g_idx = 0;
    *arg = g_longdoubles[g_idx++];
}

- (void)passInOutDouble:(double*)arg
{
    *arg *= 42;
}

- (void)passInOutLongDouble:(long double*)arg
{
    *arg *= 42;
}

- (char*)passInCharp:(char**)arg
{
    /* Yes this is leaking, but we're only testing method calling */
    size_t len = strlen(*arg);
    char*  res = malloc(len * 2 + 1);
    char*  p;
    char*  q;

    for (p = *arg, q = res; *p; p++) {
        *q++ = *p;
        *q++ = *p;
    }
    *q = 0;
    return res;
}

- (void)passOutCharp:(char**)arg
{
    if (g_idx > ARRAYSIZE(g_charps))
        g_idx = 0;
    *arg = g_charps[g_idx++];
}

- (void)passInOutCharp:(char**)arg
{
    /* Yes this is leaking, but we're only testing method calling */
    size_t len = strlen(*arg);
    char*  res = malloc(len * 2 + 1);
    char*  p;
    char*  q;

    for (p = *arg, q = res; *p; p++) {
        *q++ = *p;
        *q++ = *p;
    }
    *q   = 0;
    *arg = res;
}

- (id)passInID:(id*)arg
{
    id temp;

    if (*arg == NULL) {
        temp = [NSNull null];
    } else {
        temp = *arg;
    }
    return [NSArray arrayWithObject:temp];
}

- (void)passOutID:(id*)arg
{
    if (g_idx > 3)
        g_idx = 0;

    switch (g_idx++) {
    case 0:
        *arg = [NSArray array];
        break;
    case 1:
        *arg = [NSHost hostWithAddress:@"127.0.0.1"];
        break;
    case 2:
        *arg = [NSMutableDictionary dictionary];
        break;
    case 3:
        *arg = NULL;
        break;
    }
}

- (void)passInOutID:(id*)arg
{
    id temp;

    if (*arg == NULL) {
        temp = [NSNull null];
    } else {
        temp = *arg;
    }
    *arg = [NSArray arrayWithObject:temp];
}

- (ObjectClass*)returnObjectValue:(int)t
{
    switch (t) {
    case 1:
        return [[NSObject new] autorelease];
    case 2:
        return [NSArray array];
    case 3:
        return [NSDictionary dictionary];
    default:
        return nil;
    }
}

@end

/*
 * Testing of calling into python
 *
 * This is *very* incomplete at the moment, we need 'call' and 'invoke'
 * versions for all methods in OC_TestClass1 (both class and instance methods)
 */

@interface OC_TestClass2 : NSObject {
}

+ (Class)classOfObject:(NSObject*)arg;

/* "plain" calls */
- (char)callInstanceCharFuncOf:(OC_TestClass1*)arg;
- (unsigned char)callInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg;

- (short)callInstanceShortFuncOf:(OC_TestClass1*)arg;
- (unsigned short)callInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg;

- (int)callInstanceIntFuncOf:(OC_TestClass1*)arg;
- (unsigned int)callInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg;

- (long)callInstanceLongFuncOf:(OC_TestClass1*)arg;
- (unsigned long)callInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg;

- (long long)callInstanceLongLongFuncOf:(OC_TestClass1*)arg;
- (unsigned long long)callInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg;

- (float)callInstanceFloatFuncOf:(OC_TestClass1*)arg;
- (double)callInstanceDoubleFuncOf:(OC_TestClass1*)arg;
- (long double)callInstanceLongDoubleFuncOf:(OC_TestClass1*)arg;

- (id)callInstanceIdFuncOf:(OC_TestClass1*)arg;
- (struct dummy)callInstanceDummyFuncOf:(OC_TestClass1*)arg;
- (struct dummy2)callInstanceDummy2FuncOf:(OC_TestClass1*)arg;
- (NSPoint)callInstanceNSPointFuncOf:(OC_TestClass1*)arg;

- (long long)callInstanceLongLongArg:(long long)arg on:(OC_TestClass1*)obj;
- (unsigned long long)callInstanceUnsignedLongLongArg:(unsigned long long)arg
                                                   on:(OC_TestClass1*)obj;
- (long)callInstanceLongArg:(long)arg on:(OC_TestClass1*)obj;
- (unsigned long)callInstanceUnsignedLongArg:(unsigned long)arg on:(OC_TestClass1*)obj;
- (int)callInstanceIntArg:(int)arg on:(OC_TestClass1*)obj;
- (unsigned int)callInstanceUnsignedIntArg:(unsigned int)arg on:(OC_TestClass1*)obj;
- (short)callInstanceShortArg:(short)arg on:(OC_TestClass1*)obj;
- (unsigned short)callInstanceUnsignedShortArg:(unsigned short)arg on:(OC_TestClass1*)obj;
- (char)callInstanceCharArg:(char)arg on:(OC_TestClass1*)obj;
- (unsigned char)callInstanceUnsignedCharArg:(unsigned char)arg on:(OC_TestClass1*)obj;
- (float)callInstanceFloatArg:(float)arg on:(OC_TestClass1*)obj;
- (double)callInstanceDoubleArg:(double)arg on:(OC_TestClass1*)obj;
- (long double)callInstanceLongDoubleArg:(long double)arg on:(OC_TestClass1*)obj;
- (char*)callInstanceCharpArg:(char*)arg on:(OC_TestClass1*)obj;
- (id)callInstanceIdArg:(id)arg on:(OC_TestClass1*)obj;

/* "NSInvocation" calls */
- (char)invokeInstanceCharFuncOf:(OC_TestClass1*)arg;
- (unsigned char)invokeInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg;

- (short)invokeInstanceShortFuncOf:(OC_TestClass1*)arg;
- (unsigned short)invokeInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg;

- (int)invokeInstanceIntFuncOf:(OC_TestClass1*)arg;
- (unsigned int)invokeInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg;

- (long)invokeInstanceLongFuncOf:(OC_TestClass1*)arg;
- (unsigned long)invokeInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg;

- (long long)invokeInstanceLongLongFuncOf:(OC_TestClass1*)arg;
- (unsigned long long)invokeInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg;

- (float)invokeInstanceFloatFuncOf:(OC_TestClass1*)arg;
- (double)invokeInstanceDoubleFuncOf:(OC_TestClass1*)arg;
- (long double)invokeInstanceLongDoubleFuncOf:(OC_TestClass1*)arg;

- (id)invokeInstanceIdFuncOf:(OC_TestClass1*)arg;
- (struct dummy)invokeInstanceDummyFuncOf:(OC_TestClass1*)arg;
- (struct dummy2)invokeInstanceDummy2FuncOf:(OC_TestClass1*)arg;
- (NSPoint)invokeInstanceNSPointFuncOf:(OC_TestClass1*)arg;

- (long long)invokeInstanceLongLongArg:(long long)arg on:(OC_TestClass1*)obj;
- (unsigned long long)invokeInstanceUnsignedLongLongArg:(unsigned long long)arg
                                                     on:(OC_TestClass1*)obj;
- (long)invokeInstanceLongArg:(long)arg on:(OC_TestClass1*)obj;
- (unsigned long)invokeInstanceUnsignedLongArg:(unsigned long)arg on:(OC_TestClass1*)obj;
- (int)invokeInstanceIntArg:(int)arg on:(OC_TestClass1*)obj;
- (unsigned int)invokeInstanceUnsignedIntArg:(unsigned int)arg on:(OC_TestClass1*)obj;
- (short)invokeInstanceShortArg:(short)arg on:(OC_TestClass1*)obj;
- (unsigned short)invokeInstanceUnsignedShortArg:(unsigned short)arg
                                              on:(OC_TestClass1*)obj;
- (char)invokeInstanceCharArg:(char)arg on:(OC_TestClass1*)obj;
- (unsigned char)invokeInstanceUnsignedCharArg:(unsigned char)arg on:(OC_TestClass1*)obj;
- (float)invokeInstanceFloatArg:(float)arg on:(OC_TestClass1*)obj;
- (double)invokeInstanceDoubleArg:(double)arg on:(OC_TestClass1*)obj;
- (long double)invokeInstanceLongDoubleArg:(long double)arg on:(OC_TestClass1*)obj;
- (char*)invokeInstanceCharpArg:(char*)arg on:(OC_TestClass1*)obj;
- (id)invokeInstanceIdArg:(id)arg on:(OC_TestClass1*)obj;

@end

#define SETUP_INVOCATION(inv, target, selector)                                          \
    do {                                                                                 \
        inv = [NSInvocation                                                              \
            invocationWithMethodSignature:[target methodSignatureForSelector:selector]]; \
        [inv setTarget:target];                                                          \
        [inv setSelector:selector];                                                      \
    } while (0)

@implementation OC_TestClass2

+ (Class)classOfObject:(NSObject*)arg
{
    return [arg class];
}

- (char)callInstanceCharFuncOf:(OC_TestClass1*)arg
{
    return [arg charFunc];
}

- (unsigned char)callInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg
{
    return [arg ucharFunc];
}

- (short)callInstanceShortFuncOf:(OC_TestClass1*)arg
{
    return [arg shortFunc];
}

- (unsigned short)callInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg
{
    return [arg ushortFunc];
}

- (int)callInstanceIntFuncOf:(OC_TestClass1*)arg
{
    return [arg intFunc];
}

- (unsigned int)callInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg
{
    return [arg uintFunc];
}

- (long)callInstanceLongFuncOf:(OC_TestClass1*)arg
{
    return [arg longFunc];
}

- (unsigned long)callInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg
{
    return [arg ulongFunc];
}

- (char)invokeInstanceCharFuncOf:(OC_TestClass1*)arg
{
    char          res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(charFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned char)invokeInstanceUnsignedCharFuncOf:(OC_TestClass1*)arg
{
    unsigned char res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(ucharFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (short)invokeInstanceShortFuncOf:(OC_TestClass1*)arg
{
    short         res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(shortFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned short)invokeInstanceUnsignedShortFuncOf:(OC_TestClass1*)arg
{
    unsigned short res;
    NSInvocation*  inv;

    SETUP_INVOCATION(inv, arg, @selector(ushortFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (int)invokeInstanceIntFuncOf:(OC_TestClass1*)arg
{
    int           res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(intFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned int)invokeInstanceUnsignedIntFuncOf:(OC_TestClass1*)arg
{
    unsigned int  res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(uintFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (long)invokeInstanceLongFuncOf:(OC_TestClass1*)arg
{
    long          res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(longFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned long)invokeInstanceUnsignedLongFuncOf:(OC_TestClass1*)arg
{
    unsigned long res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(ulongFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (long long)callInstanceLongLongFuncOf:(OC_TestClass1*)arg
{
    return [arg longlongFunc];
}

- (unsigned long long)callInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg
{
    return [arg ulonglongFunc];
}

- (float)callInstanceFloatFuncOf:(OC_TestClass1*)arg
{
    return [arg floatFunc];
}

- (double)callInstanceDoubleFuncOf:(OC_TestClass1*)arg
{
    return [arg doubleFunc];
}

- (long double)callInstanceLongDoubleFuncOf:(OC_TestClass1*)arg
{
    return [arg longdoubleFunc];
}

- (id)callInstanceIdFuncOf:(OC_TestClass1*)arg
{
    return [arg idFunc];
}

- (struct dummy)callInstanceDummyFuncOf:(OC_TestClass1*)arg
{
    return [arg dummyFunc];
}

- (struct dummy2)callInstanceDummy2FuncOf:(OC_TestClass1*)arg
{
    struct dummy2 tmpval;

    tmpval = [arg dummy2Func];
    return tmpval;
}

- (NSPoint)callInstanceNSPointFuncOf:(OC_TestClass1*)arg
{
    return [arg nspointFunc];
}

- (long long)callInstanceLongLongArg:(long long)arg on:(OC_TestClass1*)obj
{
    return [obj longlongArg:arg];
}

- (unsigned long long)callInstanceUnsignedLongLongArg:(unsigned long long)arg
                                                   on:(OC_TestClass1*)obj
{
    return [obj ulonglongArg:arg];
}

- (long)callInstanceLongArg:(long)arg on:(OC_TestClass1*)obj
{
    return [obj longArg:arg];
}

- (unsigned long)callInstanceUnsignedLongArg:(unsigned long)arg on:(OC_TestClass1*)obj
{
    return [obj ulongArg:arg];
}

- (int)callInstanceIntArg:(int)arg on:(OC_TestClass1*)obj
{
    return [obj intArg:arg];
}

- (unsigned int)callInstanceUnsignedIntArg:(unsigned int)arg on:(OC_TestClass1*)obj
{
    return [obj uintArg:arg];
}

- (short)callInstanceShortArg:(short)arg on:(OC_TestClass1*)obj
{
    return [obj shortArg:arg];
}

- (unsigned short)callInstanceUnsignedShortArg:(unsigned short)arg on:(OC_TestClass1*)obj
{
    return [obj ushortArg:arg];
}

- (char)callInstanceCharArg:(char)arg on:(OC_TestClass1*)obj
{
    return [obj charArg:arg];
}

- (unsigned char)callInstanceUnsignedCharArg:(unsigned char)arg on:(OC_TestClass1*)obj
{
    return [obj ucharArg:arg];
}

- (float)callInstanceFloatArg:(float)arg on:(OC_TestClass1*)obj
{
    return [obj floatArg:arg];
}

- (double)callInstanceDoubleArg:(double)arg on:(OC_TestClass1*)obj
{
    return [obj doubleArg:arg];
}

- (long double)callInstanceLongDoubleArg:(long double)arg on:(OC_TestClass1*)obj
{
    return [obj longdoubleArg:arg];
}

- (char*)callInstanceCharpArg:(char*)arg on:(OC_TestClass1*)obj
{
    return [obj charpArg:arg];
}

- (id)callInstanceIdArg:(id)arg on:(OC_TestClass1*)obj
{
    return [obj idArg:arg];
}

- (long long)invokeInstanceLongLongFuncOf:(OC_TestClass1*)arg
{
    long long     res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(longlongFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned long long)invokeInstanceUnsignedLongLongFuncOf:(OC_TestClass1*)arg
{
    unsigned long long res;
    NSInvocation*      inv;

    SETUP_INVOCATION(inv, arg, @selector(ulonglongFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (float)invokeInstanceFloatFuncOf:(OC_TestClass1*)arg
{
    float         res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(floatFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (double)invokeInstanceDoubleFuncOf:(OC_TestClass1*)arg
{
    double        res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(doubleFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (long double)invokeInstanceLongDoubleFuncOf:(OC_TestClass1*)arg
{
    long double        res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(longdoubleFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (id)invokeInstanceIdFuncOf:(OC_TestClass1*)arg
{
    id            res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(idFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (struct dummy)invokeInstanceDummyFuncOf:(OC_TestClass1*)arg
{
    struct dummy  res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(dummyFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (struct dummy2)invokeInstanceDummy2FuncOf:(OC_TestClass1*)arg
{
    struct dummy2 res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(dummy2Func));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (NSPoint)invokeInstanceNSPointFuncOf:(OC_TestClass1*)arg
{
    NSPoint       res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, arg, @selector(nspointFunc));

    [arg forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (long long)invokeInstanceLongLongArg:(long long)arg on:(OC_TestClass1*)obj
{
    long long     res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(longlongArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned long long)invokeInstanceUnsignedLongLongArg:(unsigned long long)arg
                                                     on:(OC_TestClass1*)obj
{
    unsigned long long res;
    NSInvocation*      inv;

    SETUP_INVOCATION(inv, obj, @selector(ulonglongArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (long)invokeInstanceLongArg:(long)arg on:(OC_TestClass1*)obj
{
    long          res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(longArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned long)invokeInstanceUnsignedLongArg:(unsigned long)arg on:(OC_TestClass1*)obj
{
    unsigned long res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(ulonglongArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (int)invokeInstanceIntArg:(int)arg on:(OC_TestClass1*)obj
{
    int           res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(intArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned int)invokeInstanceUnsignedIntArg:(unsigned int)arg on:(OC_TestClass1*)obj
{
    unsigned int  res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(uintArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (short)invokeInstanceShortArg:(short)arg on:(OC_TestClass1*)obj
{
    short         res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(shortArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned short)invokeInstanceUnsignedShortArg:(unsigned short)arg
                                              on:(OC_TestClass1*)obj
{
    unsigned short res;
    NSInvocation*  inv;

    SETUP_INVOCATION(inv, obj, @selector(ushortArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (char)invokeInstanceCharArg:(char)arg on:(OC_TestClass1*)obj
{
    char          res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(charArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (unsigned char)invokeInstanceUnsignedCharArg:(unsigned char)arg on:(OC_TestClass1*)obj
{
    unsigned char res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(ucharArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (float)invokeInstanceFloatArg:(float)arg on:(OC_TestClass1*)obj
{
    float         res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(floatArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (double)invokeInstanceDoubleArg:(double)arg on:(OC_TestClass1*)obj
{
    double        res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(doubleArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (long double)invokeInstanceLongDoubleArg:(long double)arg on:(OC_TestClass1*)obj
{
    long double        res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(longdoubleArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (char*)invokeInstanceCharpArg:(char*)arg on:(OC_TestClass1*)obj
{
    char*         res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(charpArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

- (id)invokeInstanceIdArg:(id)arg on:(OC_TestClass1*)obj
{
    id            res;
    NSInvocation* inv;

    SETUP_INVOCATION(inv, obj, @selector(idArg:));
    [inv setArgument:&arg atIndex:2]; // First real argument

    [obj forwardInvocation:inv];
    [inv getReturnValue:&res];
    return res;
}

@end

/*============================================================================*/

@interface PyObjC_TestClass3 : NSObject {
}
+ (NSHost*)createAHostWithAddress:(NSString*)address;
+ (id)copyValue:(id<NSCopying>)source;
+ (NSData*)getBytes:(NSData*)data;
+ (id)keyValue:(int)idx forObject:value key:id;
+ (void)setKeyValue:(int)idx forObject:object key:key value:value;
@end

@implementation PyObjC_TestClass3

+ (NSHost*)createAHostWithAddress:(NSString*)address
{
    return [NSHost hostWithAddress:address];
}

+ (NSData*)getBytes:(NSData*)data
{
    const void* bytes = [data bytes];

    if (bytes == NULL) {
        return nil;
    } else {
        return [NSData dataWithBytes:bytes length:[data length]];
    }
}

+ (id)copyValue:(NSObject<NSCopying>*)source
{
    id theCopy;
    id pool;

    /* Copy the source, bracketed by the creation and
     * destruction of an autorelease pool. This should
     * cause a core-dump if the copy is not a 'new'
     * object.
     */
    pool    = [[NSAutoreleasePool alloc] init];
    theCopy = [source copy];
    [pool release];
    pool = nil;

    return theCopy;
}

+ (id)keyValue:(int)idx forObject:object key:key
{
    switch (idx) {
    case 0:
        return [object valueForKey:key];
    case 1:
        return [object valueForKeyPath:key];
    case 2:
        return [object storedValueForKey:key];
    case 3:
        return [object valuesForKeys:key];
    }
    return nil;
}

+ (void)setKeyValue:(int)idx forObject:object key:key value:value
{
    switch (idx) {
    case 0:
        [object takeValue:value forKey:key];
        break;
    case 1:
        [object takeValue:value forKeyPath:key];
        break;
    case 2:
        [object takeStoredValue:value forKey:key];
        break;
    case 3:
        [object takeValuesFromDictionary:value];
        break;

    case 4:
        [object setValue:value forKey:key];
        break;
    case 5:
        [object setValue:value forKeyPath:key];
        break;
    case 6:
        [object setValuesForKeysWithDictionary:value];
        break;
    }
}

+ (NSObject*)makeObservedOfClass:(Class)theClass
                        observer:(NSObject*)obj
                         keyPath:(NSString*)path
{
    NSObject* o = [[[theClass alloc] init] autorelease];
    [o addObserver:obj
        forKeyPath:path
           options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld
           context:0];
    return o;
}
@end

@interface PyObjC_TestClass4 : NSObject {
    id returnObject;
}
- (void)encodeWithCoder:(NSCoder*)coder;
- (void)runThread:(id)object;
- (id)returnObject;

+ (int)fetchInt:(NSCoder*)coder;
+ (double)fetchDouble:(NSCoder*)coder;
+ (NSData*)fetchData:(NSCoder*)coder;
+ (NSArray*)fetchArray:(NSCoder*)coder;
@end

@interface
NSObject (IKnowWhatImDoing)
- (id)call;
@end

@implementation PyObjC_TestClass4
- (int)_privateMethodWithArg:(float)arg
{
    return (int)arg;
}

- (void)runThread:(id)object
{
    NSObject* pool = [[NSAutoreleasePool alloc] init];
    returnObject   = [object call];
    [returnObject retain];
    [pool release];
}

- (id)returnObject
{
    return returnObject;
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    double d        = 1.5;
    int    iArray[] = {3, 4, 5, 6};
    [coder encodeValueOfObjCType:@encode(double) at:&d];
    [coder encodeArrayOfObjCType:@encode(int) count:4 at:iArray];
    [coder encodeBytes:"hello world" length:11];
}

+ (int)fetchInt:(NSCoder*)coder
{
    int i;
    [[clang::suppress]]
    [coder decodeValueOfObjCType:@encode(int) at:&i];

    return i;
}

+ (double)fetchDouble:(NSCoder*)coder
{
    double i;
    [[clang::suppress]]
    [coder decodeValueOfObjCType:@encode(double) at:&i];
    return i;
}

+ (NSData*)fetchData:(NSCoder*)coder
{
    void*      data;
    NSUInteger length;

    data = [coder decodeBytesWithReturnedLength:&length];
    return [NSData dataWithBytes:data length:length];
}

+ (NSArray*)fetchArray:(NSCoder*)coder
{
    int data[10];

    [coder decodeArrayOfObjCType:@encode(int) count:10 at:data];
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:data[0]],
                                     [NSNumber numberWithInt:data[1]],
                                     [NSNumber numberWithInt:data[2]],
                                     [NSNumber numberWithInt:data[3]],
                                     [NSNumber numberWithInt:data[4]],
                                     [NSNumber numberWithInt:data[5]],
                                     [NSNumber numberWithInt:data[6]],
                                     [NSNumber numberWithInt:data[7]],
                                     [NSNumber numberWithInt:data[8]],
                                     [NSNumber numberWithInt:data[9]], nil];
}

+ (NSString*)fetchObjectDescription:(NSObject*)value
{
    return [value description];
}

@end

@interface PyObjCTest_KVBaseClass : NSObject {
    NSString* directString;
    NSNumber* directNumber;
    NSString* indirectString;
    NSNumber* indirectNumber;
}
@end

@implementation PyObjCTest_KVBaseClass
- (instancetype)init
{
    self = [super init];
    if (!self)
        return nil;

    directString   = [@"Direct String" retain];
    directNumber   = [[NSNumber numberWithInt:42] retain];
    indirectString = [@"Indirect String" retain];
    indirectNumber = [[NSNumber numberWithInt:84] retain];

    return self;
}

- (NSString*)indirectString
{
    return indirectString;
}
- (void)setIndirectString:(NSString*)aString
{
    [aString retain];
    [indirectString release];
    indirectString = aString;
}

- (NSNumber*)indirectNumber
{
    return indirectNumber;
}
- (void)setIndirectNumber:(NSNumber*)number
{
    [number retain];
    [indirectNumber release];
    indirectNumber = number;
}
@end

@interface PyObjCTest_KVPathClass : NSObject {
    PyObjCTest_KVBaseClass* directHead;
    PyObjCTest_KVBaseClass* indirectHead;
}
@end

@implementation PyObjCTest_KVPathClass
- (instancetype)init
{
    self = [super init];
    if (!self)
        return nil;

    directHead   = [[PyObjCTest_KVBaseClass alloc] init];
    indirectHead = [[PyObjCTest_KVBaseClass alloc] init];

    return self;
}

- (PyObjCTest_KVBaseClass*)indirectHead
{
    return indirectHead;
}
- (void)setInidrectHead:(PyObjCTest_KVBaseClass*)aHead
{
    [aHead retain];
    [indirectHead release];
    indirectHead = aHead;
}
@end

@interface PyObjCTest_KeyValueObserver : NSObject {
    id        observed;
    NSString* key;
    id        value;
}
- (instancetype)initWithInstanceOfClass:(Class)cls withKey:(NSString*)key;
- (id)getValue;
- (void)dealloc;
- (void)observeValueForKeyPath:(NSString*)keyPath
                      ofObject:(id)object
                        change:(NSDictionary*)change
                       context:(void*)context;
@end

@implementation PyObjCTest_KeyValueObserver

- (instancetype)initWithInstanceOfClass:(Class)cls withKey:(NSString*)aKey
{
    self = [super init];
    if (self == nil) // LCOV_BR_EXCL_LINE
        return nil; // LCOV_EXCL_LINE
    value    = nil;
    observed = nil;

    observed = [[cls alloc] init];
    if (observed == nil) {
        [self release];
        return nil;
    }

    key = aKey;
    [aKey retain];

    [observed addObserver:self
               forKeyPath:key
                  options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld
                  context:0];
    value = [[observed valueForKey:key] retain];

    // Not actually used...
    //[observed setValue:@"Hello there" forKey:key];
    return self;
}

- (void)dealloc
{
    [observed removeObserver:self forKeyPath:key];
    [key release];
    [observed release];
    [value release];
    [super dealloc];
}

- (id)getValue
{
    return value;
}

- (void)observeValueForKeyPath:(NSString*)keyPath
                      ofObject:(id)object
                        change:(NSDictionary*)change
                       context:(void*)context
{
    id newValue = [change objectForKey:NSKeyValueChangeNewKey];
    [newValue retain];
    [value release];
    value = newValue;

    // use all arguments to avoid warnings...
    (void)&keyPath;
    (void)&context;
    (void)&object;
}

@end

static PyObject*
pyobjcpy(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    char*     signature;
    PyObject* o;
    char*     buf;
    int       r;

    if (!PyArg_ParseTuple(args, "yO", &signature, &o)) {

        return NULL;
    }

    buf = PyMem_Malloc(PyObjCRT_SizeOfType(signature));
    if (buf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    r = PyObjC_PythonToObjC(signature, o, buf);
    if (r < 0) {
        PyMem_Free(buf);
        return NULL;
    }

    o = PyObjC_ObjCToPython(signature, buf);
    PyMem_Free(buf);
    return o;
}

static PyObject*
carrayMaker(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    char*      signature;
    PyObject*  o1;
    PyObject*  o2;
    char*      buf;
    int        r;
    Py_ssize_t buflen;
    PyObject*  res;
    PyObject*  v = NULL;
    Py_buffer  view;
    int        writable = 0;

    if (!PyArg_ParseTuple(args, "yOO|p", &signature, &o1, &o2, &writable)) {
        return NULL;
    }

    if (o2 == Py_None) {
        buflen = -1;
    } else {
        r = PyObjC_PythonToObjC(@encode(Py_ssize_t), o2, &buflen);
        if (r == -1) {
            return NULL;
        }
    }

    r = PyObjC_PythonToCArray(writable?YES:NO, NO, signature, o1, (void**)&buf, &buflen, &v, &view);
    Py_XDECREF(v);
    if (r == -1) {
        return NULL;
    }

    res = PyObjC_CArrayToPython(signature, buf, buflen);
    PyObjC_FreeCArray(r, &view);

    return res;
}

static PyMethodDef mod_methods[] = {
    {"pyObjCPy", (PyCFunction)pyobjcpy, METH_VARARGS,

     "pyObjCPy(signature, object) -> object\n"
     "\n"
     "convert object to ObjC and back."},

    {"carrayMaker", (PyCFunction)carrayMaker, METH_VARARGS,

     "carrayMaker(signature, seq, count) -> str\n"
     "\n"
     "Convert a sequence of 'count' 'signature' objects to\n"
     "a C buffer, and rebuild a python tuple from it.\n"
     "count can be None."},

    {0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestClass1", PyObjC_IdToPython([OC_TestClass1 class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_TestClass2", PyObjC_IdToPython([OC_TestClass2 class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "PyObjC_TestClass3",
                           PyObjC_IdToPython([PyObjC_TestClass3 class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "PyObjC_TestClass4",
                           PyObjC_IdToPython([PyObjC_TestClass4 class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "PyObjCTest_KVBaseClass",
                           PyObjC_IdToPython([PyObjCTest_KVBaseClass class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "PyObjCTest_KVPathClass",
                           PyObjC_IdToPython([PyObjCTest_KVPathClass class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "PyObjCTest_KeyValueObserver",
                           PyObjC_IdToPython([PyObjCTest_KeyValueObserver class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_VALUEFORKEY", PyLong_FromLong(0)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_VALUEFORKEYPATH", PyLong_FromLong(1)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_STOREDVALUEFORKEY", PyLong_FromLong(2)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_VALUESFORKEYS", PyLong_FromLong(3)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_TAKEVALUE_FORKEY", PyLong_FromLong(0)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_TAKEVALUE_FORKEYPATH", PyLong_FromLong(1)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_TAKESTOREDVALUE_FORKEY", PyLong_FromLong(2)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_TAKEVALUESFROMDICT", PyLong_FromLong(3)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_SETVALUE_FORKEY", PyLong_FromLong(4)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_SETVALUE_FORKEYPATH", PyLong_FromLong(5)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DO_SETVALUESFORKEYSFROMDICT", PyLong_FromLong(6)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "UCHAR_MAX", PyLong_FromLong(UCHAR_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "SCHAR_MAX", PyLong_FromLong(SCHAR_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "SCHAR_MIN", PyLong_FromLong(SCHAR_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "CHAR_MAX", PyLong_FromLong(CHAR_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "CHAR_MIN", PyLong_FromLong(CHAR_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "USHRT_MAX", PyLong_FromLong(USHRT_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "SHRT_MAX", PyLong_FromLong(SHRT_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "SHRT_MIN", PyLong_FromLong(SHRT_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "UINT_MAX", PyLong_FromUnsignedLongLong(UINT_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "INT_MAX", PyLong_FromLong(INT_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "INT_MIN", PyLong_FromLong(INT_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "ULONG_MAX", PyLong_FromUnsignedLongLong(ULONG_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "LONG_MAX", PyLong_FromLong(LONG_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "LONG_MIN", PyLong_FromLong(LONG_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "ULLONG_MAX", PyLong_FromUnsignedLongLong(ULLONG_MAX))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "LLONG_MAX", PyLong_FromLongLong(LLONG_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "LLONG_MIN", PyLong_FromLongLong(LLONG_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DBL_MAX", PyFloat_FromDouble(DBL_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DBL_MIN", PyFloat_FromDouble(DBL_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "DBL_EPSILON", PyFloat_FromDouble(DBL_EPSILON)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "FLT_MAX", PyFloat_FromDouble(FLT_MAX)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "FLT_MIN", PyFloat_FromDouble(FLT_MIN)) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "FLT_EPSILON", PyFloat_FromDouble(FLT_EPSILON)) < 0) {
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
    .m_name = "testbndl",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_testbndl(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_testbndl(void)
{
    return PyModuleDef_Init(&mod_module);
}
