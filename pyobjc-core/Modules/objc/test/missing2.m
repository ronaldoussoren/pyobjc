#include "Python.h"

#define PYOBJC_API_VERSION 1

#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "missing2", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_missing2(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_missing2(void)
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
