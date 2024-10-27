#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreMedia/CoreMedia.h>

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunknown-pragmas"
#pragma clang diagnostic ignored "-Wunguarded-availability"

static PyObjC_function_map function_map[] = {
#if PyObjC_BUILD_RELEASE >= 1400
    {"CMTagIsValid", (PyObjC_Function_Pointer)&CMTagIsValid},
    {"CMTagGetCategory", (PyObjC_Function_Pointer)&CMTagGetCategory},
    {"CMTagCategoryEqualToTagCategory",
     (PyObjC_Function_Pointer)&CMTagCategoryEqualToTagCategory},
    {"CMTagGetValue", (PyObjC_Function_Pointer)&CMTagGetValue},
    {"CMTagHasCategory", (PyObjC_Function_Pointer)&CMTagHasCategory},
    {"CMTagCategoryValueEqualToValue",
     (PyObjC_Function_Pointer)&CMTagCategoryValueEqualToValue},
#endif

    {0, 0}};

#pragma clang diagnostic pop

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
