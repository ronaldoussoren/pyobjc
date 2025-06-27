#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

static CFStringRef aString = CFSTR("a static string");

union test_union {
    int   a;
    float b;
};

@interface OC_PointerSupport : NSObject {
}
@end

@implementation OC_PointerSupport

+ (int)intFromUnion:(union test_union*)value
{
    return value->a;
}

+ (union test_union*)getUnion
{
    static union test_union value;
    value.a = 99;
    return &value;
}

+ (Py_ssize_t)getObjectLen:(PyObject*)value
{
    PyGILState_STATE state  = PyGILState_Ensure();
    Py_ssize_t       result = PyObject_Length(value);
    PyGILState_Release(state);
    return result;
}

+ (PyObject*)getNone
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF(Py_None);
    PyGILState_Release(state);
    return Py_None;
}

+ (Class)getClass
{
    return (Class)[OC_PointerSupport class];
}

+ (id)className:(Class)class
{
    if (class == Nil) {           // LCOV_BR_EXCL_LINE
        return @"No class given"; // LCOV_EXCL_LINE
    }
    return [NSString
        stringWithUTF8String:(const char* _Nonnull)class_getName((Class) class)];
}

+ (CFStringRef)getString
{
    return aString;
}

+ (CFStringRef)getContext
{
    return (CFStringRef)kCFAllocatorUseContext;
}

@end

static PyObject* _Nullable union_new(void* obj)
{
    return PyCapsule_New(obj, "__union__", NULL);
}

static int
union_convert(PyObject* obj, void* pObj)
{
    union test_union* value = PyCapsule_GetPointer(obj, "__union__");
    if (value == NULL && PyErr_Occurred()) {
        return -1;
    }
    *(union test_union**)pObj = value;
    return 0;
}

static PyObject*
make_opaque_capsule(PyObject* mod __attribute__((__unused__)))
{
    return PyCapsule_New((void*)1234, "objc.__opaque__", NULL);
}

static PyObject*
make_object_capsule(PyObject* mod __attribute__((__unused__)))
{
    NSObject* object = [[[NSObject alloc] init] autorelease];
    return PyCapsule_New(object, "objc.__object__", NULL);
}

static PyMethodDef mod_methods[] = {{
                                        "opaque_capsule",
                                        (PyCFunction)make_opaque_capsule,
                                        METH_NOARGS,
                                        0,
                                    },
                                    {
                                        "object_capsule",
                                        (PyCFunction)make_object_capsule,
                                        METH_NOARGS,
                                        0,
                                    },
                                    {0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_PointerSupport",
                           PyObjC_IdToPython([OC_PointerSupport class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    int r = PyObjCPointerWrapper_Register("union_test", @encode(union test_union*),
                                          union_new, union_convert);
    if (r == -1) {
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
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "pointersupport",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_pointersupport(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_pointersupport(void)
{
    return PyModuleDef_Init(&mod_module);
}
