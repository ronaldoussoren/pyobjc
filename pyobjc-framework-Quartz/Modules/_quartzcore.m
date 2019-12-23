/*
 * Manual wrappers for QuartzCore
 */
#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#if PyObjC_BUILD_RELEASE >= 1015
#import <CoreImage/CIFilterBuiltins.h>
#endif

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
