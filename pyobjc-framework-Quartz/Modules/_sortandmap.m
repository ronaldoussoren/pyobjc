/*
 * Functions with a callback argument that isn't "retained"
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <ApplicationServices/ApplicationServices.h>

NS_ASSUME_NONNULL_BEGIN

static void
m_CGPDFDictionaryApplierFunction(const char* key, CGPDFObjectRef value, void* _info)
{
    PyObject* info    = (PyObject*)_info;
    PyObject* args[4] = {NULL};

    PyGILState_STATE state = PyGILState_Ensure();

    args[1] = PyBytes_FromString(key);
    if (args[1] == NULL) {                    // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }

    args[2] = PyObjC_ObjCToPython(@encode(CGPDFObjectRef), &value);
    if (args[2] == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_CLEAR(args[1]);
        PyObjCErr_ToObjCWithGILState(&state);
        // LCOV_EXCL_STOP
    }

    args[3] = PyTuple_GET_ITEM(info, 1);

    PyObject* result = PyObject_Vectorcall(PyTuple_GET_ITEM(info, 0), args + 1,
                                           3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
    Py_CLEAR(args[1]);
    Py_CLEAR(args[2]);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable m_CGPDFDictionaryApplyFunction(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CGPDFDictionaryRef dictionary;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }
    if (!PyCallable_Check(args[1])) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPDFDictionaryRef), args[0], &dictionary) < 0) {
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", args[1], args[2]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGPDFDictionaryApplyFunction(dictionary, m_CGPDFDictionaryApplierFunction,
                                         (void*)real_info);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_CLEAR(real_info);
    if (PyErr_Occurred()) {
        return NULL;
    }
    Py_INCREF(Py_None);
    return Py_None;
}

/*
 * CGPathApply
 */

static PyObject* gCGPathElement = NULL;

static void
m_CGPathApplierFunction(void* _info, const CGPathElement* element)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* result = PyObject_CallFunction(
        PyTuple_GetItem(info, 0), "ON", PyTuple_GetItem(info, 1),
        PyObject_CallFunction(gCGPathElement, "lN", element->type,
                              PyObjCVarList_New(@encode(CGPoint), element->points)));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable setCGPathElement(PyObject* meth __attribute__((__unused__)),
                                            PyObject* arg)
{
    /* This function is only called during import, therefore it
     * is not necessary to use a lock to protect access to gCGPathElement.
     */
    Py_XDECREF(gCGPathElement);
    Py_INCREF(arg);
    gCGPathElement = arg;

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject* _Nullable m_CGPathApply(PyObject* meth,
                                         PyObject* _Nonnull const* _Nonnull args,
                                         size_t nargs)
{
    CGPathRef path;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (!PyCallable_Check(args[2])) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPathRef), args[0], &path) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(2, args[2], args[1]);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGPathApply(path, real_info, m_CGPathApplierFunction);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(real_info);

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {{
                                        "_setCGPathElement",
                                        (PyCFunction)setCGPathElement,
                                        METH_O,
                                        NULL,
                                    },

                                    {0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(CGPDFDictionaryApplyFunction,
                                      m_CGPDFDictionaryApplyFunction)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CGPathApply, m_CGPathApply)
        == -1) {   // LCOV_BR_EXCL_LINE
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
    .m_name     = "_sortandmap",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__sortandmap(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__sortandmap(void)
{
    return PyModuleDef_Init(&mod_module);
}
NS_ASSUME_NONNULL_END
