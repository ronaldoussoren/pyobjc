#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#if defined(MAC_OS_X_VERSION_10_5) && MAC_OS_X_VERSION_MIN_REQUIRED <= MAC_OS_X_VERSION_10_6
 /* For some reason the CoreLocation headers don't work properly when
  *   * the deployment target is 10.5 (using the 10.11 SDK).
  *     */
#undef NS_ENUM_AVAILABLE
#define NS_ENUM_AVAILABLE(a, b)
#endif

#if PyObjC_BUILD_RELEASE >= 1011 && !defined(__LP64__)
/* Class not available on 32-bit builds causes issues
 * when building this extension.
 */
@interface NSUserActivity
{
}
@end
#endif

#import <MapKit/MapKit.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_MapKit_protocols.m"


static PyMethodDef mod_methods[] = {
  { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_MapKit)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_MapKit)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
