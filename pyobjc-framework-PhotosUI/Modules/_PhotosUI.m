#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#if !defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1013

/* The headers PhotosUI headers use a class that's
 * only available in 64bit mode without and guard...
 */
@interface NSExtensionContext : NSObject { }
@end
#endif

#import <PhotosUI/PhotosUI.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */

#include "_PhotosUI_protocols.m"

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_PhotosUI)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_PhotosUI)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
