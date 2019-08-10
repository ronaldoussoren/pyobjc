/*
 * Manual wrappers for CoreImage
 */
#define PY_SSIZE_T_CLEAN
#include "pyobjc-api.h"
#include <Python.h>

#import <CoreImage/CoreImage.h>

#include "_CoreImage_protocols.m"

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

PyObjC_MODULE_INIT(_CoreImage)
{
    PyObject* m = PyObjC_MODULE_CREATE(_CoreImage);
    if (!m)
        PyObjC_INITERROR();

    PyObjC_INITDONE();
}
