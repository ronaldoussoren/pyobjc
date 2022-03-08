#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_UnusedClass : NSObject {
}
@end

@implementation OC_UnusedClass
+ (id)someClassMethod
{
    return @"someClassMethod";
}

- (id)someInstanceMethod
{
    return @"someInstanceMethod";
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "methodaccess", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_methodaccess(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_methodaccess(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_UnusedClass", PyObjC_IdToPython([OC_UnusedClass class]))
        < 0) {
        return NULL;
    }

    return m;
}
