#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface PyObjCTest_Protected : NSObject {
}
- (id)publicMethod;
- (id)_protectedMethod;
@end

@implementation PyObjCTest_Protected
- (id)publicMethod
{
    return nil;
}

- (id)_protectedMethod
{
    return nil;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "protected", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_protected(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_protected(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "PyObjCTest_Protected",
                           PyObjC_IdToPython([PyObjCTest_Protected class]))
        < 0) {
        return NULL;
    }
    return m;
}
