#define Py_LIMITED_API 0x03060000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#if PyObjC_BUILD_RELEASE >= 1014
/* The SDK included with Xcode 10 no longer includes a number
 * of header files, but does #incldue them in <oCarbon/Carbon.h>.
 *
 * The defines below avoid trying to import these, which is
 * safe because we don't use any of the definitions from these files.
 */
#define __CARBONSOUND__
#define __NAVIGATIONSERVICES__
#endif

#import <InputMethodKit/InputMethodKit.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_InputMethodKit_protocols.m"

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
PyObjC_MODULE_INIT(_InputMethodKit)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_InputMethodKit) if (!m) { PyObjC_INITERROR(); }

    if (PyObjC_ImportAPI(m) == -1)
        PyObjC_INITERROR();

    PyObjC_INITDONE();
}
