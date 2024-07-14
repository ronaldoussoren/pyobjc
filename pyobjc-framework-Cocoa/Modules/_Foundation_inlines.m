#define PY_SSIZE_T_CLEAN
#define NS_INLINE
#include "Python.h"
#include "pyobjc-api.h"
#import <Foundation/Foundation.h>

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
    {"NSConvertHostDoubleToSwapped",
     (PyObjC_Function_Pointer)&NSConvertHostDoubleToSwapped},
    {"NSConvertHostFloatToSwapped",
     (PyObjC_Function_Pointer)&NSConvertHostFloatToSwapped},
    {"NSConvertSwappedDoubleToHost",
     (PyObjC_Function_Pointer)&NSConvertSwappedDoubleToHost},
    {"NSConvertSwappedFloatToHost",
     (PyObjC_Function_Pointer)&NSConvertSwappedFloatToHost},
    {"NSDecimalIsNotANumber", (PyObjC_Function_Pointer)&NSDecimalIsNotANumber},
    {"NSEqualRanges", (PyObjC_Function_Pointer)&NSEqualRanges},
    {"NSHeight", (PyObjC_Function_Pointer)&NSHeight},
    {"NSHostByteOrder", (PyObjC_Function_Pointer)&NSHostByteOrder},
    {"NSLocationInRange", (PyObjC_Function_Pointer)&NSLocationInRange},
    {"NSMakePoint", (PyObjC_Function_Pointer)&NSMakePoint},
    {"NSMakeRange", (PyObjC_Function_Pointer)&NSMakeRange},
    {"NSMakeRect", (PyObjC_Function_Pointer)&NSMakeRect},
    {"NSMakeSize", (PyObjC_Function_Pointer)&NSMakeSize},
    {"NSMaxRange", (PyObjC_Function_Pointer)&NSMaxRange},
    {"NSMaxX", (PyObjC_Function_Pointer)&NSMaxX},
    {"NSMaxY", (PyObjC_Function_Pointer)&NSMaxY},
    {"NSMidX", (PyObjC_Function_Pointer)&NSMidX},
    {"NSMidY", (PyObjC_Function_Pointer)&NSMidY},
    {"NSMinX", (PyObjC_Function_Pointer)&NSMinX},
    {"NSMinY", (PyObjC_Function_Pointer)&NSMinY},
    {"NSSwapBigDoubleToHost", (PyObjC_Function_Pointer)&NSSwapBigDoubleToHost},
    {"NSSwapBigDoubleToHost", (PyObjC_Function_Pointer)&NSSwapBigDoubleToHost},
    {"NSSwapBigFloatToHost", (PyObjC_Function_Pointer)&NSSwapBigFloatToHost},
    {"NSSwapBigFloatToHost", (PyObjC_Function_Pointer)&NSSwapBigFloatToHost},
    {"NSSwapBigIntToHost", (PyObjC_Function_Pointer)&NSSwapBigIntToHost},
    {"NSSwapBigLongLongToHost", (PyObjC_Function_Pointer)&NSSwapBigLongLongToHost},
    {"NSSwapBigLongToHost", (PyObjC_Function_Pointer)&NSSwapBigLongToHost},
    {"NSSwapBigShortToHost", (PyObjC_Function_Pointer)&NSSwapBigShortToHost},
    {"NSSwapDouble", (PyObjC_Function_Pointer)&NSSwapDouble},
    {"NSSwapFloat", (PyObjC_Function_Pointer)&NSSwapFloat},
    {"NSSwapHostDoubleToBig", (PyObjC_Function_Pointer)&NSSwapHostDoubleToBig},
    {"NSSwapHostDoubleToBig", (PyObjC_Function_Pointer)&NSSwapHostDoubleToBig},
    {"NSSwapHostDoubleToLittle", (PyObjC_Function_Pointer)&NSSwapHostDoubleToLittle},
    {"NSSwapHostDoubleToLittle", (PyObjC_Function_Pointer)&NSSwapHostDoubleToLittle},
    {"NSSwapHostFloatToBig", (PyObjC_Function_Pointer)&NSSwapHostFloatToBig},
    {"NSSwapHostFloatToBig", (PyObjC_Function_Pointer)&NSSwapHostFloatToBig},
    {"NSSwapHostFloatToLittle", (PyObjC_Function_Pointer)&NSSwapHostFloatToLittle},
    {"NSSwapHostFloatToLittle", (PyObjC_Function_Pointer)&NSSwapHostFloatToLittle},
    {"NSSwapHostIntToBig", (PyObjC_Function_Pointer)&NSSwapHostIntToBig},
    {"NSSwapHostIntToLittle", (PyObjC_Function_Pointer)&NSSwapHostIntToLittle},
    {"NSSwapHostLongLongToBig", (PyObjC_Function_Pointer)&NSSwapHostLongLongToBig},
    {"NSSwapHostLongLongToLittle", (PyObjC_Function_Pointer)&NSSwapHostLongLongToLittle},
    {"NSSwapHostLongToBig", (PyObjC_Function_Pointer)&NSSwapHostLongToBig},
    {"NSSwapHostLongToLittle", (PyObjC_Function_Pointer)&NSSwapHostLongToLittle},
    {"NSSwapHostShortToBig", (PyObjC_Function_Pointer)&NSSwapHostShortToBig},
    {"NSSwapHostShortToLittle", (PyObjC_Function_Pointer)&NSSwapHostShortToLittle},
    {"NSSwapInt", (PyObjC_Function_Pointer)&NSSwapInt},
    {"NSSwapLittleDoubleToHost", (PyObjC_Function_Pointer)&NSSwapLittleDoubleToHost},
    {"NSSwapLittleDoubleToHost", (PyObjC_Function_Pointer)&NSSwapLittleDoubleToHost},
    {"NSSwapLittleFloatToHost", (PyObjC_Function_Pointer)&NSSwapLittleFloatToHost},
    {"NSSwapLittleFloatToHost", (PyObjC_Function_Pointer)&NSSwapLittleFloatToHost},
    {"NSSwapLittleIntToHost", (PyObjC_Function_Pointer)&NSSwapLittleIntToHost},
    {"NSSwapLittleLongLongToHost", (PyObjC_Function_Pointer)&NSSwapLittleLongLongToHost},
    {"NSSwapLittleLongToHost", (PyObjC_Function_Pointer)&NSSwapLittleLongToHost},
    {"NSSwapLittleShortToHost", (PyObjC_Function_Pointer)&NSSwapLittleShortToHost},
    {"NSSwapLong", (PyObjC_Function_Pointer)&NSSwapLong},
    {"NSSwapLongLong", (PyObjC_Function_Pointer)&NSSwapLongLong},
    {"NSSwapShort", (PyObjC_Function_Pointer)&NSSwapShort},
    {"NSWidth", (PyObjC_Function_Pointer)&NSWidth},
    {"CFBridgingRetain", (PyObjC_Function_Pointer)&CFBridgingRetain},
    {"CFBridgingRelease", (PyObjC_Function_Pointer)&CFBridgingRelease},
    {"NSMakeCollectable", (PyObjC_Function_Pointer)&NSMakeCollectable},
    {"NSPointFromCGPoint", (PyObjC_Function_Pointer)&NSPointFromCGPoint},
    {"NSPointToCGPoint", (PyObjC_Function_Pointer)&NSPointToCGPoint},
    {"NSRectFromCGRect", (PyObjC_Function_Pointer)&NSRectFromCGRect},
    {"NSRectToCGRect", (PyObjC_Function_Pointer)&NSRectToCGRect},
    {"NSSizeFromCGSize", (PyObjC_Function_Pointer)&NSSizeFromCGSize},
    {"NSSizeToCGSize", (PyObjC_Function_Pointer)&NSSizeToCGSize},

    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int mod_exec_module(PyObject* m)
{
    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) < 0) {
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
