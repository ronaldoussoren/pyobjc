#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreMedia/CoreMedia.h>


static PyMethodDef mod_methods[] = {
    { NULL } /* Sentinel */
};


PyObjC_MODULE_INIT(_CoreMedia)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_CoreMedia)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
