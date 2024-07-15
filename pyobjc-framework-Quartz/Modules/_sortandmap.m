/*
 * Functions with a callback argument that isn't "retained"
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static void
m_CGPDFDictionaryApplierFunction(const char* key, CGPDFObjectRef value, void* _info)
{
    PyObject* info = (PyObject*)_info;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* args = PyTuple_New(3);
    if (args == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyTuple_SetItem(args, 0, PyBytes_FromString(key));
    if (PyTuple_GetItem(args, 0) == NULL) {
        Py_DECREF(args);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyTuple_SetItem(args, 1, PyObjC_ObjCToPython(@encode(CGPDFObjectRef), value));
    if (PyTuple_GetItem(args, 1) == NULL) {
        Py_DECREF(args);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyTuple_SetItem(args, 2, PyTuple_GetItem(info, 1));
    Py_INCREF(PyTuple_GetItem(args, 2));

    PyObject* result = PyObject_Call(PyTuple_GetItem(info, 0), args, NULL);
    Py_DECREF(args);

    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject*
m_CGPDFDictionaryApplyFunction(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*          d;
    PyObject*          f;
    PyObject*          i;
    CGPDFDictionaryRef dictionary;

    if (!PyArg_ParseTuple(args, "OOO", &d, &f, &i)) {
        return NULL;
    }
    if (!PyCallable_Check(f)) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPDFDictionaryRef), d, &dictionary) < 0) {
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", f, i);
    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGPDFDictionaryApplyFunction(dictionary, m_CGPDFDictionaryApplierFunction,
                                         (void*)real_info);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(real_info);
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

    PyObject* py_element =
        PyObject_CallFunction(gCGPathElement, "lN", element->type,
                              PyObjCVarList_New(@encode(CGPoint), element->points));
    if (element == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "ON",
                                             PyTuple_GetItem(info, 1), py_element);
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject*
setCGPathElement(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* v;

    if (!PyArg_ParseTuple(args, "O", &v)) {
        return NULL;
    }

    Py_XDECREF(gCGPathElement);
    Py_INCREF(v);
    gCGPathElement = v;

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject*
m_CGPathApply(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject* py_path;
    PyObject* callback;
    PyObject* info;
    CGPathRef path;

    if (!PyArg_ParseTuple(args, "OOO", &py_path, &info, &callback)) {
        return NULL;
    }
    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_TypeError, "callback not callable");
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGPathRef), py_path, &path) < 0) {
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OO", callback, info);
    if (real_info == NULL) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CGPathApply(path, real_info, m_CGPathApplierFunction);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF(real_info);

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef mod_methods[] = {{
                                        "CGPDFDictionaryApplyFunction",
                                        (PyCFunction)m_CGPDFDictionaryApplyFunction,
                                        METH_VARARGS,
                                        NULL,
                                    },
                                    {
                                        "CGPathApply",
                                        (PyCFunction)m_CGPathApply,
                                        METH_VARARGS,
                                        NULL,
                                    },
                                    {
                                        "setCGPathElement",
                                        (PyCFunction)setCGPathElement,
                                        METH_VARARGS,
                                        NULL,
                                    },

                                    {0, 0, 0, 0}};



static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0)
        return -1;

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
        .value = Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
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
    .m_name = "_sortandmap",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__sortandmap(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__sortandmap(void)
{
    return PyModuleDef_Init(&mod_module);
}
