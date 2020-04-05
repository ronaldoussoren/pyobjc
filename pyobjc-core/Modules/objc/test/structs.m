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

@interface OC_StructTest : NSObject {
}
+ (struct FooStruct)createWithFirst:(int)first andSecond:(int)second;
+ (int)sumFields:(struct FooStruct)foo;
- (NSObject*)arrayOf4Structs:(struct FooStruct[4])argument;

+ (NSObject*)callArrayOf4Structs:(OC_StructTest*)object;
@end

@implementation OC_StructTest
+ (struct FooStruct)createWithFirst:(int)first andSecond:(int)second
{
    struct FooStruct f;
    f.first  = first;
    f.second = second;
    return f;
}

+ (int)sumFields:(struct FooStruct)foo
{
    return foo.first + foo.second;
}

+ (NSObject*)callArrayOf4Structs:(OC_StructTest*)object
{
    static struct FooStruct structs[4] = {
        {1, 2},
        {3, 4},
        {5, 6},
        {7, 8},
    };

    return [object arrayOf4Structs:structs];
}
- (NSObject*)arrayOf4Structs:(struct FooStruct[4])argument
{
    return [NSData dataWithBytes:(void*)argument length:4 * sizeof(*argument)];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "structs", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_structs(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_structs(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_StructTest", PyObjC_IdToPython([OC_StructTest class]))
        < 0) {
        return NULL;
    }

    return m;
}
