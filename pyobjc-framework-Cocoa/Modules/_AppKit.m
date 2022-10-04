/*#define Py_LIMITED_API 0x03060000*/
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#include <objc/runtime.h>

#import <AppKit/AppKit.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_AppKit_appmain.m"
#include "_AppKit_carbon.m"
#include "_AppKit_nsbezierpath.m"
#include "_AppKit_nsbitmap.m"
#include "_AppKit_nsfont.m"
#include "_AppKit_nsview.m"
#include "_AppKit_protocols.m"

static PyMethodDef mod_methods[] = {
    APPKIT_APPMAIN_METHODS APPKIT_NSFONT_METHODS{0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_AppKit", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__AppKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__AppKit(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    if (setup_carbon(m) == -1)
        return NULL;
    if (setup_nsbezierpath(m) == -1)
        return NULL;
    if (setup_nsbitmap(m) == -1)
        return NULL;
    if (setup_nsview(m) == -1)
        return NULL;

    return m;
}
