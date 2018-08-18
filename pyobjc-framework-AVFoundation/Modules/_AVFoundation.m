#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_AVFoundation_protocols.m"

#include "_AVFoundation_AVAudioBuffer.m"


static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_AVFoundation)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_AVFoundation)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();
    if (init_avaudiobuffer() == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
