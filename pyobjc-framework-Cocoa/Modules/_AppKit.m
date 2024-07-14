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

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;

    if (setup_carbon(m) == -1)
        return -1;
    if (setup_nsbezierpath(m) == -1)
        return -1;
    if (setup_nsbitmap(m) == -1)
        return -1;
    if (setup_nsview(m) == -1)
        return -1;
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_AppKit",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__AppKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__AppKit(void)
{
    return PyModuleDef_Init(&mod_module);
}
