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

NS_ASSUME_NONNULL_BEGIN

static int*
makeIntArrayOf5(void)
{
    static int result[5];
    int        i;
    for (i = 0; i < 5; i++) {
        result[i] = i * i;
    }
    return result;
}

static char**
makeStringArray(void)
{
    static char* result[] = {"hello", "world", "out", "there", NULL};
    return result;
}

static int* _Nullable makeIntArrayOf_(int count)
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

static int* _Nullable nullIntArrayOf5(void) { return NULL; }

static char** _Nullable nullStringArray(void) { return NULL; }

static int* _Nullable nullIntArrayOf_(int count __attribute__((__unused__)))
{
    return NULL;
}

static NSArray* _Nullable makeIntArray_count_(int* data, unsigned count)
{
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray arrayWithCapacity:count];

    for (i = 0; i < count; i++) {
        [array addObject:[NSNumber numberWithInt:data[i]]];
    }
    return array;
}

static NSArray* _Nullable nullIntArray_count_(int* data, unsigned count)
{
    if (data) {
        return makeIntArray_count_(data, count);
    } else {
        return nil;
    }
}

static NSArray* _Nullable makeIntArray_countPtr_(int* data, unsigned* countPtr)
{
    return makeIntArray_count_(data, *countPtr);
}

static NSArray* _Nullable make4Tuple_(double* data)
{
    NSMutableArray* array;
    unsigned        i;

    array = [NSMutableArray array];

    for (i = 0; i < 4; i++) {
        [array addObject:[NSNumber numberWithDouble:data[i]]];
    }
    return array;
}

static NSArray* _Nullable null4Tuple_(double* data)
{
    if (data) {
        return make4Tuple_(data);
    } else {
        return nil;
    }
}

static NSArray* _Nullable makeStringArray_(char** data)
{
    NSMutableArray* array;

    array = [NSMutableArray array];

    while (*data != NULL) {
        NSObject* val = [NSString stringWithUTF8String:*data];
        if (val == NULL)
            continue;

        [array addObject:val];
        data++;
    }
    return array;
}

static NSArray* _Nullable nullStringArray_(char** data)
{
    if (data) {
        return makeStringArray_(data);
    } else {
        return nil;
    }
}

static NSArray* _Nullable makeObjectArray_(id* data)
{
    NSMutableArray* array;

    array = [NSMutableArray array];

    while (*data != NULL) {
        [array addObject:*data];
        data++;
    }
    return array;
}

static void
fillArray_count_(int* data, int count)
{
    int i;
    for (i = 0; i < count; i++) {
        data[i] = i * i;
    }
}

static int
nullfillArray_count_(int* data, int count)
{
    if (data == NULL) {
        return 0;
    } else {
        fillArray_count_(data, count);
        return 1;
    }
}

static void
fill4Tuple_(int* data)
{
    int i;
    for (i = 0; i < 4; i++) {
        data[i] = -i * i * i;
    }
}

static int
nullfill4Tuple_(int* data)
{
    if (data == NULL) {
        return 0;
    } else {
        fill4Tuple_(data);
        return 1;
    }
}

static int
fillStringArray_(char** data __attribute__((__unused__)))
{
    return -1;
}

static int
nullfillStringArray_(char** data)
{
    if (data == NULL)
        return 0;
    fillStringArray_(data);
    return 1;
}

static void
reverseArray_count_(float* data, int count)
{
    float t;
    int   i;
    for (i = 0; i < count / 2; i++) {
        t                   = data[i];
        data[i]             = data[count - 1 - i];
        data[count - 1 - i] = t;
    }
}

static int
nullreverseArray_count_(float* data, int count)
{
    if (data == NULL)
        return 0;
    reverseArray_count_(data, count);
    return 1;
}

static void
reverseStrings_(char** data)
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

static int
nullreverseStrings_(char** data)
{
    if (data == NULL)
        return 0;
    reverseStrings_(data);
    return 1;
}

static void
reverse4Tuple_(short* data)
{
    short t;

    t       = data[0];
    data[0] = data[3];
    data[3] = t;

    t       = data[1];
    data[1] = data[2];
    data[2] = t;
}

static int
nullreverse4Tuple_(short* data)
{
    if (data == NULL)
        return 0;
    reverse4Tuple_(data);
    return 1;
}

static int
sumX_andY_(int* x, int* y)
{
    return *x + *y;
}

static int
divBy5_remainder_(int x, int* r)
{
    *r = x % 5;
    return x / 5;
}

static void
swapX_andY_(double* x, double* y)
{
    double t = *x;
    *x       = *y;
    *y       = t;
}

static NSArray* _Nullable input_output_inputAndOutput_(int* x, int* y, int* z)
{
    char            buf[64];
    NSString*       value;
    NSMutableArray* result = [NSMutableArray array];

    snprintf(buf, sizeof(buf), "%p", (void*)x);
    value = [NSString stringWithUTF8String:buf];
    if (!value)
        return NULL;
    [result addObject:value];

    snprintf(buf, sizeof(buf), "%p", (void*)y);
    value = [NSString stringWithUTF8String:buf];
    if (!value)
        return NULL;
    [result addObject:value];

    snprintf(buf, sizeof(buf), "%p", (void*)z);
    value = [NSString stringWithUTF8String:buf];
    if (!value)
        return NULL;
    [result addObject:value];

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

static int
fillArray_uptoCount_(int* data, int count)
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

static int
maybyFillArray_(int* data)
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

static int
reverseArray_uptoCount_(float* data, int count)
{
    reverseArray_count_(data, count);
    return count / 2;
}

static int
maybeReverseArray_(short* data)
{
    reverse4Tuple_(data);
    return 2;
}

static NSArray* __attribute__((__format__(__NSString__, 1, 2)))
makeArrayWithFormat_(NSString* fmt, ...)
{
    va_list ap;
    char    buffer[2048];

    va_start(ap, fmt);
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wformat-nonliteral"

    vsnprintf(buffer, sizeof(buffer), [fmt UTF8String], ap);
#pragma clang diagnostic pop
    va_end(ap);

    return [NSArray arrayWithObjects:fmt, [NSString stringWithUTF8String:buffer], NULL];
}

#pragma GCC diagnostic   push
#pragma clang diagnostic push
#pragma GCC diagnostic   ignored "-Wformat-nonliteral"
#pragma clang diagnostic ignored "-Wformat-nonliteral"

static NSArray* _Nullable __attribute__((__format__(__printf__, 1, 2)))
makeArrayWithCFormat_(char* fmt, ...)
{
    va_list   ap;
    char      buffer[2048];
    NSString* a1;
    NSString* a2;

    va_start(ap, fmt);
    vsnprintf(buffer, sizeof(buffer), fmt, ap);
    va_end(ap);

    a1 = [NSString stringWithUTF8String:fmt];
    if (!a1)
        return NULL;
    a2 = [NSString stringWithUTF8String:buffer];
    if (!a2)
        return NULL;
    return [NSArray arrayWithObjects:a1, a2, NULL];
}

#pragma GCC diagnostic   pop
#pragma clang diagnostic pop

static int
maybeFillArray_(int* data)
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

static int
do_double(int val)
{
    return val * 2;
}

typedef int (*returnfunc)(int);
static returnfunc
getDoubleFunc(void)
{
    return do_double;
}

static returnfunc
getOldDoubleFunc(void)
{
    return do_double;
}

static void
raiseFunc(void)
{
    @throw [NSException exceptionWithName:@"ExceptionName"
                                   reason:@"No Reason"
                                 userInfo:nil];
}

static void
raiseFunc2(int* inval __attribute__((__unused__)))
{
    @throw [NSException exceptionWithName:@"ExceptionName"
                                   reason:@"No Reason"
                                 userInfo:nil];
}

static void
getxy(int* x, int* y)
{
    *x = 1;
    *y = 2;
}
typedef void (*getfunc)(int*, int*);

static getfunc
getGetter(void)
{
    return getxy;
}

union SomeUnion {
    unsigned long intvalue;
    double        doublevalue;
};

static union SomeUnion*
returnUnionArray(void)
{
    static union SomeUnion buffer[] = {
        {.intvalue = 42}, {.doublevalue = 2.5}, {.doublevalue = 4.0}};
    return buffer;
}

static struct UnknownLabel {
    int first;
    int second;
} LabelArray[] = {
    {.first = 0, .second = 1},
    {.first = 2, .second = 3},
    {.first = 4, .second = 5},
};

static struct UnknownLabel**
returnPointerArray(void)
{
    static struct UnknownLabel* buffer[] = {LabelArray, LabelArray + 1, LabelArray + 2};
    return buffer;
}

typedef void (*F)(void);
static struct function {
    char* name;
    F     function;
} gFunctionMap[] = {{"makeIntArrayOf5", (F)makeIntArrayOf5},
                    {"makeStringArray", (F)makeStringArray},
                    {"makeIntArrayOf_", (F)makeIntArrayOf_},
                    {"makeVoidPArrayOf_", (F)makeIntArrayOf_},
                    {"nullIntArrayOf5", (F)nullIntArrayOf5},
                    {"nullStringArray", (F)nullStringArray},
                    {"nullIntArrayOf_", (F)nullIntArrayOf_},
                    {"nullIntArray_count_", (F)nullIntArray_count_},
                    {"makeIntArray_countPtr_", (F)makeIntArray_countPtr_},
                    {"makeIntArray_count_", (F)makeIntArray_count_},
                    {"make4Tuple_", (F)make4Tuple_},
                    {"null4Tuple_", (F)null4Tuple_},
                    {"nullStringArray_", (F)nullStringArray_},
                    {"makeStringArray_", (F)makeStringArray_},
                    {"makeObjectArray_", (F)makeObjectArray_},
                    {"fillArray_count_", (F)fillArray_count_},
                    {"nullfillArray_count_", (F)nullfillArray_count_},
                    {"fill4Tuple_", (F)fill4Tuple_},
                    {"nullfill4Tuple_", (F)nullfill4Tuple_},
                    {"fillStringArray_", (F)fillStringArray_},
                    {"nullfillStringArray_", (F)nullfillStringArray_},
                    {"reverseArray_count_", (F)reverseArray_count_},
                    {"nullreverseArray_count_", (F)nullreverseArray_count_},
                    {"reverseStrings_", (F)reverseStrings_},
                    {"nullreverseStrings_", (F)nullreverseStrings_},
                    {"reverse4Tuple_", (F)reverse4Tuple_},
                    {"nullreverse4Tuple_", (F)nullreverse4Tuple_},
                    {"sumX_andY_", (F)sumX_andY_},
                    {"divBy5_remainder_", (F)divBy5_remainder_},
                    {"swapX_andY_", (F)swapX_andY_},
                    {"input_output_inputAndOutput_", (F)input_output_inputAndOutput_},
                    {"fillArray_uptoCount_", (F)fillArray_uptoCount_},
                    {"maybyFillArray_", (F)maybyFillArray_},
                    {"reverseArray_uptoCount_", (F)reverseArray_uptoCount_},
                    {"maybeReverseArray_", (F)maybeReverseArray_},
                    {"makeArrayWithFormat_", (F)makeArrayWithFormat_},
                    {"makeArrayWithCFormat_", (F)makeArrayWithCFormat_},
                    {"maybeFillArray_", (F)maybeFillArray_},
                    {"getDoubleFunc", (F)getDoubleFunc},
                    {"get2ndDoubleFunc", (F)getDoubleFunc},
                    {"getOldDoubleFunc", (F)getOldDoubleFunc},
                    {"raiseFunc", (F)raiseFunc},
                    {"raiseFunc2", (F)raiseFunc2},
                    {"oldDoubleFunc", (F)do_double},
                    {"getGetter", (F)getGetter},
                    {"get2ndGetter", (F)getGetter},
                    {"returnUnionArray", (F)returnUnionArray},
                    {"returnPointerArray", (F)returnPointerArray},
                    {"return2ndPointerArray", (F)returnPointerArray},

                    {NULL, NULL}};

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "metadatafunction",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* _Nullable PyInit_metadatafunction(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_metadatafunction(void)
{
    PyObject* m;
    PyObject* v;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    v = PyCapsule_New(gFunctionMap, "objc.__inline__", NULL);
    if (v == NULL) {
        return NULL;
    }

    if (PyModule_AddObject(m, "function_list", v) == -1) {
        return NULL;
    }
    if (PyModule_AddStringConstant(m, "union_SomeUnion", @encode(union SomeUnion))
        == -1) {
        return NULL;
    }

    return m;
}

NS_ASSUME_NONNULL_END
