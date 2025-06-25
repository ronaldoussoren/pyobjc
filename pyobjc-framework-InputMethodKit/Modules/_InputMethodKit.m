#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#if PyObjC_BUILD_RELEASE >= 1014
/* The SDK included with Xcode 10 no longer includes a number
 * of header files, but does #include them in <Carbon/Carbon.h>.
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

static int
mod_exec_module(PyObject* m)
{
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_InputMethodKit",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__InputMethodKit(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__InputMethodKit(void)
{
    return PyModuleDef_Init(&mod_module);
}
