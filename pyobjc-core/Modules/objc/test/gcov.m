#include "Python.h"
#include "pyobjc-api.h"

#include <CoreFoundation/CoreFoundation.h>

extern void __gcov_flush(void);

static PyObject*
do_flush(PyObject* m __attribute__((__unused__)))
{
#ifdef COVERAGE
    __gcov_flush();
#endif
    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {{
                                        "flush",
                                        (PyCFunction)do_flush,
                                        METH_NOARGS,
                                        NULL,
                                    },
                                    {0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m __attribute__((__unused__)))
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
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "gcov",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_gcov(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_gcov(void)
{
    return PyModuleDef_Init(&mod_module);
}
