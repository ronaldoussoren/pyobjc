#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreAudio/CoreAudio.h>

extern "C" {

static PyObjC_function_map function_map[] = {
    {"IsAudioFormatNativeEndian", (PyObjC_Function_Pointer)&IsAudioFormatNativeEndian},
    {"CalculateLPCMFlags", (PyObjC_Function_Pointer)&CalculateLPCMFlags},
    {"FillOutASBDForLPCM", (PyObjC_Function_Pointer)&FillOutASBDForLPCM},
    {"FillOutAudioTimeStampWithSampleTime",
     (PyObjC_Function_Pointer)&FillOutAudioTimeStampWithSampleTime},
    {"FillOutAudioTimeStampWithHostTime",
     (PyObjC_Function_Pointer)&FillOutAudioTimeStampWithHostTime},
    {"FillOutAudioTimeStampWithSampleAndHostTime",
     (PyObjC_Function_Pointer)&FillOutAudioTimeStampWithSampleAndHostTime},
#if PyObjC_BUILD_RELEASE >= 1011
    {"AudioChannelLayoutTag_GetNumberOfChannels",
     (PyObjC_Function_Pointer)&AudioChannelLayoutTag_GetNumberOfChannels},
#endif
    {0, 0}};

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return -1;
    }

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
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_inlines",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__inlines(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__inlines(void)
{
    return PyModuleDef_Init(&mod_module);
}


} /* extern C */
