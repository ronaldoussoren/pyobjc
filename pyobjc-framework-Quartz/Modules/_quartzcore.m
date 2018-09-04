/*
 * Manual wrappers for QuartzCore
 */
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <Quartz/Quartz.h>

#include "_QuartzCore_protocols.m"

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, }
};

PyObjC_MODULE_INIT(_quartzcore)
{
    PyObject* m = PyObjC_MODULE_CREATE(_quartzcore);
    if (!m) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
