#include "Python.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface
NSObject (PyObjCTestCategory)

@end

@implementation
NSObject (PyObjCTestCategory)
- (id)pyobjcTestMethod
{
    return @"hello";
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "nsobjectcategory",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_nsobjectcategory(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_nsobjectcategory(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    return m;
}
