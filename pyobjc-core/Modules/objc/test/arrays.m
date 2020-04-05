#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

struct ArrayStruct {
    int first;
    int second;
};

typedef int                int_array_t[4];
typedef struct ArrayStruct struct_array_t[4];

@interface OC_ArrayTest : NSObject {
}
- (NSObject*)arrayOf4Ints:(int_array_t)array;
- (NSObject*)arrayOf4IntsIn:(in int_array_t)array;
- (NSObject*)arrayOf4IntsInOut:(inout int_array_t)array;
- (void)arrayOf4IntsOut:(out int_array_t)array;

- (NSObject*)arrayOf4Structs:(struct_array_t)array;
- (NSObject*)arrayOf4StructsIn:(in struct_array_t)array;
- (NSObject*)arrayOf4StructsInOut:(inout struct_array_t)array;
- (void)arrayOf4StructsOut:(out struct_array_t)array;

+ (NSObject*)callArrayOf4Ints:(OC_ArrayTest*)object;
+ (NSObject*)callArrayOf4IntsOut:(OC_ArrayTest*)object;
+ (NSObject*)callArrayOf4Structs:(OC_ArrayTest*)object;
+ (NSObject*)callArrayOf4StructsOut:(OC_ArrayTest*)object;
@end

@implementation OC_ArrayTest

- (NSObject*)arrayOf4Ints:(int_array_t)array
{
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                     [NSNumber numberWithInt:array[1]],
                                     [NSNumber numberWithInt:array[2]],
                                     [NSNumber numberWithInt:array[3]], nil];
}
- (NSObject*)arrayOf4IntsIn:(in int_array_t)array
{
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                     [NSNumber numberWithInt:array[1]],
                                     [NSNumber numberWithInt:array[2]],
                                     [NSNumber numberWithInt:array[3]], nil];
}
- (NSObject*)arrayOf4IntsInOut:(inout int_array_t)array
{
    NSObject* result = [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                                 [NSNumber numberWithInt:array[1]],
                                                 [NSNumber numberWithInt:array[2]],
                                                 [NSNumber numberWithInt:array[3]], nil];

    array[0] += 42;
    array[1] += 42;
    array[2] += 42;
    array[3] += 42;

    return result;
}
- (void)arrayOf4IntsOut:(out int_array_t)array
{
    array[0] = 99;
    array[1] = 100;
    array[2] = 102;
    array[3] = 110;
}

- (NSObject*)arrayOf4Structs:(struct_array_t)array
{
    return [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];
}
- (NSObject*)arrayOf4StructsIn:(in struct_array_t)array
{
    return [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];
}
- (NSObject*)arrayOf4StructsInOut:(inout struct_array_t)array
{
    NSObject* result = [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];

    int i;
    for (i = 0; i < 4; i++) {
        array[i].first += 42;
        array[i].second -= 42;
    }

    return result;
}
- (void)arrayOf4StructsOut:(out struct_array_t)array
{
    int i;
    for (i = 0; i < 4; i++) {
        array[i].first  = 1 + i * i;
        array[i].second = -4 - i * i * i;
    }
}

+ (NSObject*)callArrayOf4Ints:(OC_ArrayTest*)object
{
    int_array_t array = {1, 2, 3, 4};
    return [object arrayOf4Ints:array];
}

+ (NSObject*)callArrayOf4IntsOut:(OC_ArrayTest*)object
{
    int_array_t array;
    [object arrayOf4IntsOut:array];
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                     [NSNumber numberWithInt:array[1]],
                                     [NSNumber numberWithInt:array[2]],
                                     [NSNumber numberWithInt:array[3]], nil];
}

+ (NSObject*)callArrayOf4Structs:(OC_ArrayTest*)object
{
    struct_array_t array = {{1, 2}, {3, 4}, {5, 6}, {7, 8}};
    return [object arrayOf4Structs:array];
}

+ (NSObject*)callArrayOf4StructsOut:(OC_ArrayTest*)object
{
    struct_array_t array;
    [object arrayOf4StructsOut:array];

    return [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "arrays", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_arrays(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_arrays(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_ArrayTest", PyObjC_IdToPython([OC_ArrayTest class]))
        < 0) {
        return NULL;
    }

    return m;
}
