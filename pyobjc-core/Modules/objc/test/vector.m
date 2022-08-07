#include "Python.h"
#include "pyobjc-api.h"
#import <simd/simd.h>
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_Vector : NSObject {
    PyObject* values;
}
@end

@implementation OC_Vector
- (instancetype)init
{
    self = [super init];
    if (self == nil) {
        return nil;
    }
    values = NULL;
    return self;
}

- (id)getAndResetValues
{
    if (values == NULL) {
        return nil;
    }

    id result;
    if (PyObjC_PythonToObjC(@encode(id), values, &result) == -1) {
        PyErr_Clear();
        result = nil;
    }
    Py_CLEAR(values);
    return result;
}
- (void)dealloc
{
    if (values) {
        Py_CLEAR(values);
    }
    [super dealloc];
}

- (vector_float3)getVectorFloat3
{
    return (vector_float3){1.5, 2.5, 3.5};
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "vector", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_vector(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_vector(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_Vector", PyObjC_IdToPython([OC_Vector class])) < 0) {
        return NULL;
    }

    return m;
}
