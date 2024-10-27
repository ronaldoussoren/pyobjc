/*
 * Manual wrappers for QuartzCore
 */
#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#if PyObjC_BUILD_RELEASE >= 1015
#import <CoreImage/CIFilterBuiltins.h>
#endif

#if PyObjC_BUILD_RELEASE >= 1013
#import <CoreImage/CoreImage.h>
#endif

#import <Quartz/Quartz.h>

#include "_CoreImage_protocols.m"
#include "_QuartzCore_protocols.m"

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_quartzcore", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__quartzcore(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__quartzcore(void)
{
    PyObject* m = PyModule_Create(&mod_module);
    if (!m)
        return NULL;

    return m;
}
