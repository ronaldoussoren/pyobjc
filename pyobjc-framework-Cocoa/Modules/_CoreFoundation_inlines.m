#define PY_SSIZE_T_CLEAN
#define CF_INLINE
#include "Python.h"
#include "pyobjc-api.h"
#import <CoreFoundation/CoreFoundation.h>

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
    {"CFByteOrderGetCurrent", (PyObjC_Function_Pointer)&CFByteOrderGetCurrent},
    {"CFConvertDoubleHostToSwapped",
     (PyObjC_Function_Pointer)&CFConvertDoubleHostToSwapped},
    {"CFConvertDoubleSwappedToHost",
     (PyObjC_Function_Pointer)&CFConvertDoubleSwappedToHost},
    {"CFConvertFloat32HostToSwapped",
     (PyObjC_Function_Pointer)&CFConvertFloat32HostToSwapped},
    {"CFConvertFloat32SwappedToHost",
     (PyObjC_Function_Pointer)&CFConvertFloat32SwappedToHost},
    {"CFConvertFloat64HostToSwapped",
     (PyObjC_Function_Pointer)&CFConvertFloat64HostToSwapped},
    {"CFConvertFloat64SwappedToHost",
     (PyObjC_Function_Pointer)&CFConvertFloat64SwappedToHost},
    {"CFConvertFloatHostToSwapped",
     (PyObjC_Function_Pointer)&CFConvertFloatHostToSwapped},
    {"CFConvertFloatSwappedToHost",
     (PyObjC_Function_Pointer)&CFConvertFloatSwappedToHost},
    {"CFRangeMake", (PyObjC_Function_Pointer)&CFRangeMake},
    {"CFStringGetCharacterFromInlineBuffer",
     (PyObjC_Function_Pointer)&CFStringGetCharacterFromInlineBuffer},
    {"CFStringInitInlineBuffer", (PyObjC_Function_Pointer)&CFStringInitInlineBuffer},
    {"CFSwapInt16", (PyObjC_Function_Pointer)&CFSwapInt16},
    {"CFSwapInt16BigToHost", (PyObjC_Function_Pointer)&CFSwapInt16BigToHost},
    {"CFSwapInt16HostToBig", (PyObjC_Function_Pointer)&CFSwapInt16HostToBig},
    {"CFSwapInt16HostToLittle", (PyObjC_Function_Pointer)&CFSwapInt16HostToLittle},
    {"CFSwapInt16LittleToHost", (PyObjC_Function_Pointer)&CFSwapInt16LittleToHost},
    {"CFSwapInt32", (PyObjC_Function_Pointer)&CFSwapInt32},
    {"CFSwapInt32BigToHost", (PyObjC_Function_Pointer)&CFSwapInt32BigToHost},
    {"CFSwapInt32HostToBig", (PyObjC_Function_Pointer)&CFSwapInt32HostToBig},
    {"CFSwapInt32HostToLittle", (PyObjC_Function_Pointer)&CFSwapInt32HostToLittle},
    {"CFSwapInt32LittleToHost", (PyObjC_Function_Pointer)&CFSwapInt32LittleToHost},
    {"CFSwapInt64", (PyObjC_Function_Pointer)&CFSwapInt64},
    {"CFSwapInt64BigToHost", (PyObjC_Function_Pointer)&CFSwapInt64BigToHost},
    {"CFSwapInt64HostToBig", (PyObjC_Function_Pointer)&CFSwapInt64HostToBig},
    {"CFSwapInt64HostToLittle", (PyObjC_Function_Pointer)&CFSwapInt64HostToLittle},
    {"CFSwapInt64LittleToHost", (PyObjC_Function_Pointer)&CFSwapInt64LittleToHost},
    {"CFUserNotificationCheckBoxChecked",
     (PyObjC_Function_Pointer)&CFUserNotificationCheckBoxChecked},
    {"CFUserNotificationPopUpSelection",
     (PyObjC_Function_Pointer)&CFUserNotificationPopUpSelection},
    {"CFUserNotificationSecureTextField",
     (PyObjC_Function_Pointer)&CFUserNotificationSecureTextField},
    {"CFStringIsSurrogateHighCharacter",
     (PyObjC_Function_Pointer)&CFStringIsSurrogateHighCharacter},
    {"CFStringIsSurrogateLowCharacter",
     (PyObjC_Function_Pointer)&CFStringIsSurrogateLowCharacter},
    {"CFStringGetLongCharacterForSurrogatePair",
     (PyObjC_Function_Pointer)&CFStringGetLongCharacterForSurrogatePair},
    {"CFStringGetSurrogatePairForLongCharacter",
     (PyObjC_Function_Pointer)&CFStringGetSurrogatePairForLongCharacter},
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
