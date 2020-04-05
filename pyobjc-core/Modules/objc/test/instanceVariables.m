/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface ClassWithVariables : NSObject {
    int       intValue;
    double    floatValue;
    char      charValue;
    char*     strValue;
    NSRect    rectValue;
    NSObject* nilValue;
    PyObject* pyValue;
    NSObject* objValue;
}
- (instancetype)init;
- (void)dealloc;
@end

@implementation ClassWithVariables
- (instancetype)init
{
    self = [super init];
    if (self == nil)
        return nil;

    intValue   = 42;
    floatValue = -10.055;
    charValue  = 'a';
    strValue   = "hello world";
    rectValue  = NSMakeRect(1, 2, 3, 4);
    nilValue   = nil;
    PyObjC_BEGIN_WITH_GIL
        pyValue =
            PySlice_New(PyLong_FromLong(1), PyLong_FromLong(10), PyLong_FromLong(4));
    PyObjC_END_WITH_GIL
    objValue = [[NSObject alloc] init];
    return self;
}

- (void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        Py_XDECREF(pyValue);
    PyObjC_END_WITH_GIL
    [objValue release];
    [nilValue release];
    [super dealloc];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "instanceVariables",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_instanceVariables(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_instanceVariables(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "ClassWithVariables",
                           PyObjC_IdToPython([ClassWithVariables class]))
        < 0) {
        return NULL;
    }

    return m;
}
