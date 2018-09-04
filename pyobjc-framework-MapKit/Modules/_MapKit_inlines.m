#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#if defined(MAC_OS_X_VERSION_10_5) && MAC_OS_X_VERSION_MIN_REQUIRED <= MAC_OS_X_VERSION_10_6
 /* For some reason the CoreLocation headers don't work properly when
  *   * the deployment target is 10.5 (using the 10.11 SDK).
  *     */
#undef NS_ENUM_AVAILABLE
#define NS_ENUM_AVAILABLE(a, b)
#endif

#if PyObjC_BUILD_RELEASE >= 1011 && !defined(__LP64__)
/* Class not available on 32-bit builds causes issues
 * when building this extension.
 */
@interface NSUserActivity
{
}
@end
#endif


#import <MapKit/MapKit.h>


static PyObjC_function_map function_map[] = {
#if PyObjC_BUILD_RELEASE >= 1009
    { "MKCoordinateSpanMake", (PyObjC_Function_Pointer)&MKCoordinateSpanMake },
    { "MKCoordinateRegionMake", (PyObjC_Function_Pointer)&MKCoordinateRegionMake },
    { "MKMapPointMake", (PyObjC_Function_Pointer)&MKMapPointMake },
    { "MKMapSizeMake", (PyObjC_Function_Pointer)&MKMapSizeMake },
    { "MKMapRectMake", (PyObjC_Function_Pointer)&MKMapRectMake },
    { "MKMapRectGetMinX", (PyObjC_Function_Pointer)&MKMapRectGetMinX },
    { "MKMapRectGetMinY", (PyObjC_Function_Pointer)&MKMapRectGetMinY },
    { "MKMapRectGetMidX", (PyObjC_Function_Pointer)&MKMapRectGetMidX },
    { "MKMapRectGetMidY", (PyObjC_Function_Pointer)&MKMapRectGetMidY },
    { "MKMapRectGetMaxX", (PyObjC_Function_Pointer)&MKMapRectGetMaxX },
    { "MKMapRectGetMaxY", (PyObjC_Function_Pointer)&MKMapRectGetMaxY },
    { "MKMapRectGetWidth", (PyObjC_Function_Pointer)&MKMapRectGetWidth },
    { "MKMapRectGetHeight", (PyObjC_Function_Pointer)&MKMapRectGetHeight },
    { "MKMapPointEqualToPoint", (PyObjC_Function_Pointer)&MKMapPointEqualToPoint },
    { "MKMapSizeEqualToSize", (PyObjC_Function_Pointer)&MKMapSizeEqualToSize },
    { "MKMapRectEqualToRect", (PyObjC_Function_Pointer)&MKMapRectEqualToRect },
    { "MKMapRectIsNull", (PyObjC_Function_Pointer)&MKMapRectIsNull },
    { "MKMapRectIsEmpty", (PyObjC_Function_Pointer)&MKMapRectIsEmpty },
    { "MKStringFromMapPoint", (PyObjC_Function_Pointer)&MKStringFromMapPoint },
    { "MKStringFromMapSize", (PyObjC_Function_Pointer)&MKStringFromMapSize },
    { "MKStringFromMapRect", (PyObjC_Function_Pointer)&MKStringFromMapRect },
#endif
    { 0, 0 }
};

static PyMethodDef mod_methods[] = {
    { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_MAJOR_VERSION == 3

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
    "_inlines",
    NULL,
    0,
    mod_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

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
#if PY_MAJOR_VERSION == 3
    m = PyModule_Create(&mod_module);
#else
    m = Py_InitModule4("_inlines", mod_methods,
        NULL, NULL, PYTHON_API_VERSION);
#endif
    if (!m) {
        INITERROR();
    }

    if (PyModule_AddObject(m, "_inline_list_",
        PyObjC_CreateInlineTab(function_map)) < 0) {
        INITERROR();
    }

    INITDONE();
}
