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

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_inlines", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__inlines(void);

PyObject*
PyInit__inlines(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (m == NULL) {
        return NULL;
    }

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return NULL;
    }

    return m;
}
