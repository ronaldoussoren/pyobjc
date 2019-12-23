/*
 * Manual wrappers for CoreImage
 */
#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

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
