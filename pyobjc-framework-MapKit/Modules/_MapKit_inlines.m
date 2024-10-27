#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <MapKit/MapKit.h>

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
    {"MKCoordinateSpanMake", (PyObjC_Function_Pointer)&MKCoordinateSpanMake},
    {"MKCoordinateRegionMake", (PyObjC_Function_Pointer)&MKCoordinateRegionMake},
    {"MKMapPointMake", (PyObjC_Function_Pointer)&MKMapPointMake},
    {"MKMapSizeMake", (PyObjC_Function_Pointer)&MKMapSizeMake},
    {"MKMapRectMake", (PyObjC_Function_Pointer)&MKMapRectMake},
    {"MKMapRectGetMinX", (PyObjC_Function_Pointer)&MKMapRectGetMinX},
    {"MKMapRectGetMinY", (PyObjC_Function_Pointer)&MKMapRectGetMinY},
    {"MKMapRectGetMidX", (PyObjC_Function_Pointer)&MKMapRectGetMidX},
    {"MKMapRectGetMidY", (PyObjC_Function_Pointer)&MKMapRectGetMidY},
    {"MKMapRectGetMaxX", (PyObjC_Function_Pointer)&MKMapRectGetMaxX},
    {"MKMapRectGetMaxY", (PyObjC_Function_Pointer)&MKMapRectGetMaxY},
    {"MKMapRectGetWidth", (PyObjC_Function_Pointer)&MKMapRectGetWidth},
    {"MKMapRectGetHeight", (PyObjC_Function_Pointer)&MKMapRectGetHeight},
    {"MKMapPointEqualToPoint", (PyObjC_Function_Pointer)&MKMapPointEqualToPoint},
    {"MKMapSizeEqualToSize", (PyObjC_Function_Pointer)&MKMapSizeEqualToSize},
    {"MKMapRectEqualToRect", (PyObjC_Function_Pointer)&MKMapRectEqualToRect},
    {"MKMapRectIsNull", (PyObjC_Function_Pointer)&MKMapRectIsNull},
    {"MKMapRectIsEmpty", (PyObjC_Function_Pointer)&MKMapRectIsEmpty},
    {"MKStringFromMapPoint", (PyObjC_Function_Pointer)&MKStringFromMapPoint},
    {"MKStringFromMapSize", (PyObjC_Function_Pointer)&MKStringFromMapSize},
    {"MKStringFromMapRect", (PyObjC_Function_Pointer)&MKStringFromMapRect},
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
