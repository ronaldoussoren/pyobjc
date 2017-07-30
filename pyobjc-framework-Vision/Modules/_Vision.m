#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <Vision/Vision.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_Vision_protocols.m"


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_Vision)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_Vision)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
