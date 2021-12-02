#include "Python.h"

#define PyObjC_EXPECTED_STRUCT_SIZE 500

#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "missing3", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_missing3(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_missing3(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    return m;
}
