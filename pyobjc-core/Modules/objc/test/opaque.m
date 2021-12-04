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

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "opaque", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_opaque(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_opaque(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "OC_OpaqueTest", PyObjC_IdToPython([OC_OpaqueTest class]))
        < 0) {
        return NULL;
    }

    if (PyModule_AddObject(m, "BarEncoded", PyBytes_FromString(@encode(BarHandle))) < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "FooEncoded", PyBytes_FromString(@encode(FooHandle))) < 0) {
        return NULL;
    }

    return m;
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
