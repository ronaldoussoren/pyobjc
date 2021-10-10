#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface
NSURL (MethodResolution2)
- (id)oc_method1;
- (id)ocmethod2;
@end

@implementation
NSURL (MethodResolution2)

- (id)oc_method1
{
    return @"NSURL.oc_method1";
}

- (id)ocmethod2
{
    return @"NSURL.ocmethod2";
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "methres2", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_methres2(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_methres2(void)
{

    return PyModule_Create(&mod_module);
}
