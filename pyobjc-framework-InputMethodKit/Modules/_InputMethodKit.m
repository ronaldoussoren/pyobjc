#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#if PyObjC_BUILD_RELEASE >= 1014
/* The SDK included with Xcode 10 no longer includes a number
 * of header files, but does #include them in <oCarbon/Carbon.h>.
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
static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "_InputMethodKit",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit__InputMethodKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__InputMethodKit(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    return m;
}
