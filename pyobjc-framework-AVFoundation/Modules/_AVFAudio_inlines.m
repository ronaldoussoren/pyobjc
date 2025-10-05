#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <AVFAudio/AVFAudio.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability"
#endif

static PyObjC_function_map function_map[] = {
#if PyObjC_BUILD_RELEASE >= 1010
    {"AVAudioMake3DPoint", (PyObjC_Function_Pointer)&AVAudioMake3DPoint},
    {"AVAudioMake3DVector", (PyObjC_Function_Pointer)&AVAudioMake3DVector},
    {"AVAudioMake3DVectorOrientation",
     (PyObjC_Function_Pointer)&AVAudioMake3DVectorOrientation},
    {"AVAudioMake3DAngularOrientation",
     (PyObjC_Function_Pointer)&AVAudioMake3DAngularOrientation},
#endif
#if PyObjC_BUILD_RELEASE >= 1011
    {"AVMakeBeatRange", (PyObjC_Function_Pointer)&AVMakeBeatRange},
#endif
    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return -1;
    }

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* No usage of the CPython API at all, hence safe with subinterpreters
         * and per interpreter GIL.
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
    .m_name     = "_inlines",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__inlines(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__inlines(void)
{
    return PyModuleDef_Init(&mod_module);
}
