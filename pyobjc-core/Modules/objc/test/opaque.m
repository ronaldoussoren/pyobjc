/*
 * Helper methods opaque-pointer tests (objc.test.test_opaque)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

typedef struct _Foo* FooHandle;
typedef struct _Bar* BarHandle;

@interface OC_OpaqueTest : NSObject {
}
+ (FooHandle)createFoo:(int)value;
+ (FooHandle)nullFoo;
+ (void)deleteFoo:(FooHandle)handle;
+ (int)getValueOf:(FooHandle)foo;
+ (void)setValue:(int)value forFoo:(FooHandle)handle;

+ (BarHandle)createBarWithFirst:(double)first andSecond:(double)second;
+ (BarHandle)nullBar;
+ (void)getFirst:(double*)first andSecond:(double*)second of:(BarHandle)bar;
+ (void)setFirst:(double)first andSecond:(double)second of:(BarHandle)bar;
+ (void)deleteBar:(BarHandle)handle;
+ (double)getFirst:(BarHandle)handle;
+ (double)getSecond:(BarHandle)handle;
@end

static int
do_visit(PyObject* o, void* arg)
{
    return PyList_Append((PyObject*)arg, o);
}

static PyObject*
do_traverse(PyObject* m __attribute__((__unused__)), PyObject* o)
{
    if (Py_TYPE(o)->tp_traverse == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* result = PyList_New(0);
    if (result == NULL)
        return NULL;

    int r = Py_TYPE(o)->tp_traverse(o, do_visit, result);
    if (r != 0) {
        Py_DECREF(result);
        return NULL;
    }

    return result;
}

static PyMethodDef mod_methods[] = {{
                                        .ml_name  = "traverse",
                                        .ml_meth  = (PyCFunction)do_traverse,
                                        .ml_flags = METH_O,
                                    },

                                    {0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_OpaqueTest", PyObjC_IdToPython([OC_OpaqueTest class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "BarEncoded", PyBytes_FromString(@encode(BarHandle))) < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "FooEncoded", PyBytes_FromString(@encode(FooHandle))) < 0) {
        return -1; // LCOV_EXCL_LINE
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
    .m_name = "opaque",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_opaque(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_opaque(void)
{
    return PyModuleDef_Init(&mod_module);
}

/*
 * Only define the full structs here to ensure that @encode won't include
 * the field definition into the encoded value.
 */

struct _Foo {
    int index;
};

struct _Bar {
    double first;
    double second;
};

@implementation OC_OpaqueTest
+ (FooHandle)createFoo:(int)value
{
    FooHandle result = malloc(sizeof(struct _Foo));
    if (result == NULL) {
        return NULL;
    }
    result->index = value;
    return result;
}

+ (FooHandle)nullFoo
{
    return NULL;
}

+ (void)deleteFoo:(FooHandle)handle
{
    if (handle) {
        free(handle);
    }
}

+ (int)getValueOf:(FooHandle)foo
{
    return foo->index;
}

+ (void)setValue:(int)value forFoo:(FooHandle)handle
{
    handle->index = value;
}

+ (BarHandle)createBarWithFirst:(double)first andSecond:(double)second
{
    BarHandle result = malloc(sizeof(struct _Bar));
    if (result == NULL)
        return NULL;

    result->first  = first;
    result->second = second;
    return result;
}

+ (BarHandle)nullBar
{
    return NULL;
}

+ (void)getFirst:(double*)first andSecond:(double*)second of:(BarHandle)bar
{
    *first  = bar->first;
    *second = bar->second;
}

+ (void)setFirst:(double)first andSecond:(double)second of:(BarHandle)bar
{
    bar->first  = first;
    bar->second = second;
}

+ (void)deleteBar:(BarHandle)handle
{
    if (handle) {
        free(handle);
    }
}

+ (double)getFirst:(BarHandle)handle
{
    return handle->first;
}

+ (double)getSecond:(BarHandle)handle
{
    return handle->second;
}

@end
