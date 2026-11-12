#include "Python.h"
#include "pyobjc-api.h"
#import <Foundation/Foundation.h>
#include <simd/simd.h>

NS_ASSUME_NONNULL_BEGIN

static int
doubleInt(int value)
{
    return value * 2;
}

static int
trippleInt(int value)
{
    return value * 3;
}

static int
quadrupleInt(int value)
{
    return value * 4;
}

static id
retainedFromVector(simd_float4x4 v) NS_RETURNS_RETAINED
{
    return [[NSString stringWithFormat:@"%.1f %.1f %.1f", v.columns[0][0],
                                       v.columns[0][1], v.columns[0][2]] retain];
}

static id __attribute__((cf_returns_retained))
cfretainedFromVector(simd_float4x4 v)
{
    id result = [NSString stringWithFormat:@"%.1f %.1f %.1f", v.columns[0][0],
                                           v.columns[0][1], v.columns[0][2]];
    CFRetain(result);
    return result;
}

typedef int (*intfunc)(int);
typedef void (*callbackfunc)(intfunc);

static void
passFunction(callbackfunc func)
{
    func(doubleInt);
}

static int
sum4ints(int values[4])
{
    return values[0] + values[1] + values[2] + values[3];
}

static double
distance(NSPoint points[2])
{
    double dx = points[0].x - points[1].x;
    double dy = points[0].y - points[1].y;
    return sqrt(dx * dx + dy * dy);
}

typedef void (*F)(void);
static struct function {
    char* name;
    F     function;
} gFunctionMap[] = {{"doubleInt", (F)doubleInt},
                    {"trippleInt", (F)trippleInt},
                    {"quadrupleInt", (F)quadrupleInt},
                    {"passFunction", (F)passFunction},
                    {"retainedFromVector", (F)retainedFromVector},
                    {"cfretainedFromVector", (F)cfretainedFromVector},
                    {"sum4ints", (F)sum4ints},
                    {"distance", (F)distance},

                    {NULL, NULL}};

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static PyObject* _Nullable invoke_custom(PyObject* meth __attribute__((__unused__)),
                                         PyObject* _Nonnull const* _Nonnull args,
                                         size_t nargs)
{
    int r;
    if (nargs != 1) {
        PyErr_SetString(PyExc_TypeError, "bad argcount");
        return NULL;
    }
    if (!PyLong_Check(args[0])) {
        PyErr_SetString(PyExc_TypeError, "bad arg type");
        return NULL;
    }

    r = doubleInt(-PyLong_AsLong(args[0]));
    return PyLong_FromLong(r);
}

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    PyObject* v = PyCapsule_New(gFunctionMap, "objc.__inline__", NULL);
    if (v == NULL) {
        return -1;
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "function_list", v)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjCRegister_FunctionCaller( // LCOV_BR_EXCL_LINE
            doubleInt, invoke_custom)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller( // LCOV_BR_EXCL_LINE
            trippleInt, invoke_custom)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller( // LCOV_BR_EXCL_LINE
            quadrupleInt, invoke_custom)
        == -1) {
        return -1; // LCOV_EXCL_LINE
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
    .m_name     = "function",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_function(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_function(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
