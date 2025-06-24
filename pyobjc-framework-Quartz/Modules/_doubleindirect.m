/*
 * Functions that return arrays by indirection, something that cannot be
 * described by the metadata.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static PyObject*
m_CGWaitForScreenRefreshRects(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    CGRect*     rectArray = NULL;
    CGRectCount count     = 0;
    CGError     err;

    if (PyTuple_Size(args) == 2) {
        if (PyTuple_GetItem(args, 0) != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pRectArray");
            return NULL;
        }
        if (PyTuple_GetItem(args, 1) != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pCount");
            return NULL;
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

            err = CGWaitForScreenRefreshRects(&rectArray, &count);

#pragma clang diagnostic pop

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (err == kCGErrorSuccess) {
        /* Build the array */
        PyObject* arr = PyObjC_CArrayToPython(@encode(CGRect), rectArray, count);
        if (arr == NULL) {
            return NULL;
        }

        /* Free the C-level array */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        CGReleaseScreenRefreshRects(rectArray);

#pragma clang diagnostic pop

        return Py_BuildValue("lNl", err, arr, count);
    }

    return Py_BuildValue("lOO", err, Py_None, Py_None);
}

static PyObject*
m_CGWaitForScreenUpdateRects(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    CGRect*                 rectArray = NULL;
    size_t                  count     = 0;
    CGScreenUpdateOperation requestedOperations;
    CGScreenUpdateOperation currentOperation;
    CGScreenUpdateMoveDelta delta;
    CGError                 err;
    PyObject*               py_ops;

    if (!PyArg_ParseTuple(args, "O", &py_ops)) {
        PyObject* py_curop;
        PyObject* py_rectarr;
        PyObject* py_count;
        PyObject* py_delta;

        if (!PyArg_ParseTuple(args, "OOOOO", &py_ops, &py_curop, &py_rectarr, &py_count,
                              &py_delta)) {
            return NULL;
        }

        if (py_curop != Py_None) {
            PyErr_SetString(PyExc_ValueError, "currentOperation != None");
            return NULL;
        }
        if (py_rectarr != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pRectArray != None");
            return NULL;
        }
        if (py_count != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pCount != None");
            return NULL;
        }
        if (py_delta != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pDelta != None");
            return NULL;
        }
    }

    if (PyObjC_PythonToObjC(@encode(CGScreenUpdateOperation), py_ops,
                            &requestedOperations)
        < 0) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

            err = CGWaitForScreenUpdateRects(requestedOperations, &currentOperation,
                                             &rectArray, &count, &delta);

#pragma clang diagnostic pop

        } @catch (NSException* localException) {
            err = -1; /* Avoid compiler warning */
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (err == kCGErrorSuccess) {
        /* Build the array */
        PyObject* arr = PyObjC_CArrayToPython(@encode(CGRect), rectArray, count);
        if (arr == NULL) {
            return NULL;
        }
        PyObject* dlt = PyObjC_ObjCToPython(@encode(CGScreenUpdateMoveDelta), &delta);
        if (dlt == NULL) {
            return NULL;
        }

        /* Free the C-level array */
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

        CGReleaseScreenRefreshRects(rectArray);

#pragma clang diagnostic pop

        return Py_BuildValue("llNl", err, currentOperation, arr, count, dlt);
    }

    return Py_BuildValue("lOOOO", err, Py_None, Py_None, Py_None, Py_None);
}

static PyObject*
m_CGReleaseScreenRefreshRects(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* array;

    if (!PyArg_Parse(args, "O", &array)) {
        return NULL;
    }

    /* Do nothing, our wrappers for CGWaitForScreenRefreshRects and
     * CGWaitForScreenUpdateRects have already released the real array.
     */

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {
    {"CGWaitForScreenRefreshRects", (PyCFunction)m_CGWaitForScreenRefreshRects,
     METH_VARARGS, NULL},
    {"CGWaitForScreenUpdateRects", (PyCFunction)m_CGWaitForScreenUpdateRects,
     METH_VARARGS, NULL},
    {"CGReleaseScreenRefreshRects", (PyCFunction)m_CGReleaseScreenRefreshRects,
     METH_VARARGS, NULL},

    {0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0)
        return -1;

    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_doubleindirect",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__doubleindirect(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__doubleindirect(void)
{
    return PyModuleDef_Init(&mod_module);
}
