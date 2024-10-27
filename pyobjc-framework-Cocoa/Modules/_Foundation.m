#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */

#include "_Foundation_netservice.m"
#include "_Foundation_protocols.m"
#include "_Foundation_string.m"
#include "_Foundation_typecode.m"

static PyMethodDef mod_methods[] = {
    FOUNDATION_TYPECODE_METHODS{0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_Foundation", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__Foundation(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__Foundation(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    if (setup_nsnetservice(m) == -1)
        return NULL;
    if (setup_nssstring(m) == -1)
        return NULL;

    return m;
}
