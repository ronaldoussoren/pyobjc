/*
 * Manual wrappers for QuartzCore
 */
#define PY_SSIZE_T_CLEAN
#include "pyobjc-api.h"
#include <Python.h>

#import <CoreImage/CIFilterBuiltins.h>
#import <CoreImage/CoreImage.h>
#import <Quartz/Quartz.h>

#include "_CoreImage_protocols.m"
#include "_QuartzCore_protocols.m"

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

PyObjC_MODULE_INIT(_quartzcore)
{
    PyObject* m = PyObjC_MODULE_CREATE(_quartzcore);
    if (!m)
        PyObjC_INITERROR();

    PyObjC_INITDONE();
}
