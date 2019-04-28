/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

typedef struct TestStructPointerStruct* Foo;

static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "structpointer2",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit_structpointer2(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_structpointer2(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "FooEncoded", PyBytes_FromString(@encode(Foo))) < 0) {
        return NULL;
    }

    return m;
}
