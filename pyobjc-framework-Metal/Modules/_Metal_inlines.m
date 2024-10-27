#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
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
    {0, 0}};

#pragma clang diagnostic pop

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_inlines", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__inlines(void);

PyObject*
PyInit__inlines(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_inlines(void);

void
init_inlines(void)
#endif
{
    PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("_inlines", mod_methods, NULL, NULL, PYTHON_API_VERSION);
#endif

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map)) < 0)

        INITERROR();

    INITDONE();
}
