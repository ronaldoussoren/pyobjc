#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"
#import <SceneKit/SceneKit.h>

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
    {"SCNMatrix4FromMat4", (PyObjC_Function_Pointer)&SCNMatrix4FromMat4},
    {"SCNMatrix4MakeScale", (PyObjC_Function_Pointer)&SCNMatrix4MakeScale},
    {"SCNMatrix4MakeTranslation", (PyObjC_Function_Pointer)&SCNMatrix4MakeTranslation},
    {"SCNMatrix4ToMat4", (PyObjC_Function_Pointer)&SCNMatrix4ToMat4},
    {"SCNMatrix4Translate", (PyObjC_Function_Pointer)&SCNMatrix4Translate},
    {"SCNVector3FromFloat3", (PyObjC_Function_Pointer)&SCNVector3FromFloat3},
    {"SCNVector3FromGLKVector3", (PyObjC_Function_Pointer)&SCNVector3FromGLKVector3},
    {"SCNVector3Make", (PyObjC_Function_Pointer)&SCNVector3Make},
    {"SCNVector3ToFloat3", (PyObjC_Function_Pointer)&SCNVector3ToFloat3},
    {"SCNVector3ToGLKVector3", (PyObjC_Function_Pointer)&SCNVector3ToGLKVector3},
    {"SCNVector4FromFloat4", (PyObjC_Function_Pointer)&SCNVector4FromFloat4},
    {"SCNVector4FromGLKVector4", (PyObjC_Function_Pointer)&SCNVector4FromGLKVector4},
    {"SCNVector4Make", (PyObjC_Function_Pointer)&SCNVector4Make},
    {"SCNVector4ToFloat4", (PyObjC_Function_Pointer)&SCNVector4ToFloat4},
    {"SCNVector4ToGLKVector4", (PyObjC_Function_Pointer)&SCNVector4ToGLKVector4},
    {0, 0}};

#if PyObjC_BUILD_RELEASE >= 1013
#pragma clang diagnostic pop
#endif

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
