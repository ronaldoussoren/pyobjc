#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#ifdef __LP64__
/* Framework is 64-bit only */

#import <Foundation/Foundation.h>
#import <CoreSpotlight/CoreSpotlight.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_CoreSpotlight_protocols.m"

#endif

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_CoreSpotlight)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_CoreSpotlight)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
