/*
 * Manual wrappers for PDFKit
 */
#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Quartz/Quartz.h>

#include "_PDFKit_protocols.m"

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_PDFKit", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__PDFKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__PDFKit(void)
{
    PyObject* m = PyModule_Create(&mod_module);
    if (!m)
        return NULL;

    return m;
}
