/*
 * Functions that return arrays by indirection, something that cannot be
 * described by the metadata.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static PyObject*
m_CGWaitForScreenRefreshRects(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                              size_t    nargs)
{
    CGRect*     rectArray = NULL;
    CGRectCount count     = 0;
    CGError     err;

    if (nargs == 0) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                         "leaving out 'pRectArray' and 'pCount' is deprecated", 0)
            == -1) {
            return NULL;
        }
    } else {
        if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
            return NULL;
        }

        if (args[0] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "'pRectArray' must be None");
            return NULL;
        }
        if (args[1] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "'pCount' must be None");
            return NULL;
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

            err = CGWaitForScreenRefreshRects(&rectArray, &count);

#pragma clang diagnostic pop

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
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
m_CGWaitForScreenUpdateRects(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                             size_t    nargs)
{
    CGRect*                 rectArray = NULL;
    size_t                  count     = 0;
    CGScreenUpdateOperation requestedOperations;
    CGScreenUpdateOperation currentOperation;
    CGScreenUpdateMoveDelta delta;
    CGError                 err;

    if (nargs == 1) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                         "leaving out 'currentOperation', 'pRectArray', 'pCount' and "
                         "'pDelta' is deprecated",
                         0)
            == -1) {
            return NULL;
        }
        if (PyObjC_PythonToObjC(@encode(CGScreenUpdateOperation), args[0],
                                &requestedOperations)
            < 0) {
            return NULL;
        }
    } else {
        if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
            return NULL;
        }

        if (PyObjC_PythonToObjC(@encode(CGScreenUpdateOperation), args[0],
                                &requestedOperations)
            < 0) {
            return NULL;
        }

        if (args[1] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "currentOperation must be None");
            return NULL;
        }
        if (args[2] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pRectArray must be None");
            return NULL;
        }
        if (args[3] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pCount must be None");
            return NULL;
        }
        if (args[4] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "pDelta must be None");
            return NULL;
        }
    }

    Py_BEGIN_ALLOW_THREADS
        @try {

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

            err = CGWaitForScreenUpdateRects(requestedOperations, &currentOperation,
                                             &rectArray, &count, &delta);

#pragma clang diagnostic pop

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            err = -1;                            // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
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
m_CGReleaseScreenRefreshRects(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                              size_t    nargs)
{
    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    /* Do nothing, our wrappers for CGWaitForScreenRefreshRects and
     * CGWaitForScreenUpdateRects have already released the real array.
     */

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) // LCOV_BR_EXCL_LIN#
        return -1;               // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(CGWaitForScreenRefreshRects,
                                      m_CGWaitForScreenRefreshRects)
        == -1) {   // LCOV_BR_EXCL_LIN#
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGWaitForScreenUpdateRects,
                                      m_CGWaitForScreenUpdateRects)
        == -1) {   // LCOV_BR_EXCL_LIN#
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGReleaseScreenRefreshRects,
                                      m_CGReleaseScreenRefreshRects)
        == -1) {   // LCOV_BR_EXCL_LIN#
        return -1; // LCOV_EXCL_LINE
    }

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
