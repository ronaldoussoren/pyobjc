/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OC_TestVoidPointer : NSObject {
    void* value;
}

- (void*)getvalue;
- (void)setvalue:(void*)v;
@end

@implementation OC_TestVoidPointer
- (instancetype)init
{
    self = [super init];
    if (self) {
        value = NULL;
    }
    return self;
}
- (void*)getvalue
{
    return value;
}
- (void)setvalue:(void*)v
{
    value = v;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "voidpointer", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_voidpointer(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_voidpointer(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }
    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_TestVoidPointer",
                           PyObjC_IdToPython([OC_TestVoidPointer class]))
        < 0) {
        return NULL;
    }

    return m;
}
