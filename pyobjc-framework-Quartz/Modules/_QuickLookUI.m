/*
 * Manual wrappers for QuickLookUI
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <Quartz/Quartz.h>

#include "_QuickLookUI_protocols.m"

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, }
};

PyObjC_MODULE_INIT(_QuickLookUI)
{
    PyObject* m = PyObjC_MODULE_CREATE(_QuickLookUI);
    if (!m) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
