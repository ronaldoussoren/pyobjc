#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#import <AppKit/AppKit.h>

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
    {"NSEdgeInsetsMake", (PyObjC_Function_Pointer)&NSEdgeInsetsMake},
    {"NSEventMaskFromType", (PyObjC_Function_Pointer)&NSEventMaskFromType},
#if PyObjC_BUILD_RELEASE >= 1012
    {"NSTouchTypeMaskFromType", (PyObjC_Function_Pointer)&NSTouchTypeMaskFromType},
#endif
#if PyObjC_BUILD_RELEASE >= 1015
    {"NSDirectionalEdgeInsetsMake",
     (PyObjC_Function_Pointer)&NSDirectionalEdgeInsetsMake},
#endif
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
    if (!m) {
        return NULL;
    }

    if (PyModule_AddObject(m, "_inline_list_", PyObjC_CreateInlineTab(function_map))
        < 0) {
        return NULL;
    }

    return m;
}
