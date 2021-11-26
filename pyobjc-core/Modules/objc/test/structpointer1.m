/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

struct TestStructPointerStruct {
    int i1;
};

struct UnwrappedStruct {
    int i1;
    int i2;
};

static struct TestStructPointerStruct myGlobal = {1};

@interface OC_TestStructPointer : NSObject {
}
+ (struct TestStructPointerStruct*)returnPointerToStruct;
+ (struct UnwrappedStruct*)returnUnwrapped;
@end

@implementation OC_TestStructPointer
+ (struct TestStructPointerStruct*)returnPointerToStruct
{
    return &myGlobal;
}

+ (struct UnwrappedStruct*)returnUnwrapped
{
    return (struct UnwrappedStruct*)42;
}

+ (unsigned long)unwrappedToInt:(struct UnwrappedStruct*)val
{
    return (unsigned long)val;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "structpointer1",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_structpointer1(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_structpointer1(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestStructPointer",
                           PyObjC_IdToPython([OC_TestStructPointer class]))
        < 0) {
        return NULL;
    }

    return m;
}
