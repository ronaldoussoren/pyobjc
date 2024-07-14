#define PY_SSIZE_T_CLEAN
#define NS_INLINE
#include "Python.h"
#include "pyobjc-api.h"
#import <Metal/Metal.h>

/*
 * The definitions below can cause warnings when using
 * -Wunguarded-availability, but those warnings are harmless
 * because the functions are inline functions and hence will
 * be available on all macOS versions once compiled.
 */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunknown-pragmas"
#pragma clang diagnostic ignored "-Wunguarded-availability"

static PyObjC_function_map function_map[] = {
    {"MTLOriginMake", (PyObjC_Function_Pointer)&MTLOriginMake},
    {"MTLSizeMake", (PyObjC_Function_Pointer)&MTLSizeMake},
    {"MTLRegionMake1D", (PyObjC_Function_Pointer)&MTLRegionMake1D},
    {"MTLRegionMake2D", (PyObjC_Function_Pointer)&MTLRegionMake2D},
    {"MTLRegionMake3D", (PyObjC_Function_Pointer)&MTLRegionMake3D},
    {"MTLClearColorMake", (PyObjC_Function_Pointer)&MTLClearColorMake},

#if PyObjC_BUILD_RELEASE >= 1013
    {"MTLSamplePositionMake", (PyObjC_Function_Pointer)&MTLSamplePositionMake},
#endif
#if PyObjC_BUILD_RELEASE >= 1014
    {"MTLIndirectCommandBufferExecutionRangeMake",
     (PyObjC_Function_Pointer)&MTLIndirectCommandBufferExecutionRangeMake},
#endif
#if PyObjC_BUILD_RELEASE >= 1015 && __apple_build_version__ >= 11030000
    {"MTLCoordinate2DMake", (PyObjC_Function_Pointer)&MTLCoordinate2DMake},
    {"MTLTextureSwizzleChannelsMake",
     (PyObjC_Function_Pointer)&MTLTextureSwizzleChannelsMake},
#endif
#if PyObjC_BUILD_RELEASE >= 1200
    {"MTLPackedFloat3Make", (PyObjC_Function_Pointer)&MTLPackedFloat3Make},
#endif
#if PyObjC_BUILD_RELEASE >= 1500
    {"MTLPackedFloatQuaternionMake", (PyObjC_Function_Pointer)&MTLPackedFloatQuaternionMake},
#endif
    {0, 0}};

#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) < 0)
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
