#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface
NSObject (MethodResolution1)
- (id)oc_method1;
- (id)ocmethod2;
@end

@implementation
NSObject (MethodResolution1)

- (id)oc_method1
{
    return @"NSObject.oc_method1";
}

- (id)ocmethod2
{
    return @"NSObject.ocmethod2";
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "methres1", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_methres1(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_methres1(void)
{
    return PyModule_Create(&mod_module);
}
