#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

#undef PySequence_Fast_GET_ITEM
#define PySequence_Fast_GET_ITEM(o, i)                                                   \
    (PyList_Check(o) ? PyList_GetItem(o, i) : PyTuple_GetItem(o, i))

#undef PySequence_Fast_GET_SIZE
#define PySequence_Fast_GET_SIZE(o) (PyList_Check(o) ? PyList_Size(o) : PyTuple_Size(o))

static PyObject*
m_CTFontCopyAvailableTables(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*          py_font;
    PyObject*          py_options;
    CTFontRef          font;
    CTFontTableOptions options;
    CFArrayRef         ref;
    Py_ssize_t         len, i;
    PyObject*          result;

    if (!PyArg_ParseTuple(args, "OO", &py_font, &py_options)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CTFontRef), py_font, &font) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CTFontTableOptions), py_options, &options) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CTFontCopyAvailableTables(font, options);

        } @catch (NSException* localException) {
            ref = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (ref == NULL) {
        if (PyErr_Occurred()) {
            return NULL;
        }

        Py_INCREF(Py_None);
        return Py_None;
    }

    len    = CFArrayGetCount(ref);
    result = PyTuple_New(len);
    if (result == NULL) {
        CFRelease(ref);
        return NULL;
    }

    for (i = 0; i < len; i++) {
        CTFontTableTag tag = (CTFontTableTag)(uintptr_t)CFArrayGetValueAtIndex(ref, i);
        PyTuple_SetItem(result, i, PyLong_FromLong(tag));
        if (PyTuple_GetItem(result, i) == NULL) {
            Py_DECREF(result);
            CFRelease(ref);
            return NULL;
        }
    }
    CFRelease(ref);
    return result;
}

static PyObject*
m_CTParagraphStyleGetTabStops(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*           py_style;
    CTParagraphStyleRef style;
    CFArrayRef          output = NULL;
    PyObject*           result;
    bool                b;

    if (!PyArg_ParseTuple(args, "O", &py_style)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CTParagraphStyleRef), py_style, &style) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            b = CTParagraphStyleGetValueForSpecifier(
                style, kCTParagraphStyleSpecifierTabStops, sizeof(CFArrayRef), &output);
        } @catch (NSException* localException) {
            b = 0;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (!b) {
        return Py_BuildValue("OO", Py_False, Py_None);
    }

    result = Py_BuildValue("NN", PyBool_FromLong(b), PyObjC_IdToPython((NSArray*)output));
    return result;
}

static PyObject*
m_CTParagraphStyleCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*                py_settings;
    PyObject*                seq;
    PyObject*                result;
    Py_ssize_t               len, i;
    CFArrayRef               aref = NULL;
    CTParagraphStyleSetting* settings;
    CTParagraphStyleRef      style = NULL;
    Py_buffer*               views = NULL;

    if (!PyArg_ParseTuple(args, "On", &py_settings, &len)) {
        return NULL;
    }

    if (py_settings == Py_None) {
        /* Handle simple case */
        if (len != 0) {
            PyErr_SetString(PyExc_ValueError, "settings list is 'None', length is not 0");
            return NULL;
        }
        Py_BEGIN_ALLOW_THREADS
            @try {
                style = CTParagraphStyleCreate(NULL, 0);

            } @catch (NSException* localException) {
                style = NULL;
                PyObjCErr_FromObjC(localException);
            }
        Py_END_ALLOW_THREADS

        if (PyErr_Occurred()) {
            return NULL;
        }
        if (style == NULL) {
            Py_INCREF(Py_None);
            return Py_None;
        }

        result = PyObjC_ObjCToPython(@encode(CTParagraphStyleRef), &style);
        CFRelease(style);
        return result;
    }

    seq = PySequence_Fast(py_settings, "need sequence of settings");
    if (seq == NULL) {
        return NULL;
    }

    if (PySequence_Fast_GET_SIZE(seq) < len) {
        PyErr_Format(PyExc_ValueError, "need sequence of at least %ld arguments",
                     (long)len);
        Py_DECREF(seq);
        return NULL;
    }

    settings = malloc(sizeof(*settings) * len);
    if (settings == NULL) {
        Py_DECREF(seq);
        PyErr_NoMemory();
        return NULL;
    }

    views = malloc(sizeof(Py_buffer) * len);
    if (views == NULL) {
        free(settings);
        Py_DECREF(seq);
        PyErr_NoMemory();
        return NULL;
    }

    for (i = 0; i < len; i++) {
        CTParagraphStyleSetting* cur   = settings + i;
        PyObject*                curPy = PySequence_Fast_GET_ITEM(seq, i);
        PyObject*                s     = PySequence_Fast(curPy, "CTParagraphStyleItem");
        int                      r;

        if (s == NULL) {
            goto setup_error;
        }
        if (PySequence_Fast_GET_SIZE(s) != 3) {
            PyErr_Format(PyExc_ValueError, "settings item has length %ld, not 3",
                         (long)PySequence_Fast_GET_SIZE(s));
            goto setup_error;
        }

        r = PyObjC_PythonToObjC(@encode(CTParagraphStyleSpecifier),
                                PySequence_Fast_GET_ITEM(s, 0), &cur->spec);
        if (r == -1) {
            goto setup_error;
        }
        r = PyObjC_PythonToObjC(@encode(size_t), PySequence_Fast_GET_ITEM(s, 1),
                                &cur->valueSize);
        if (r == -1) {
            goto setup_error;
        }
        if (cur->spec == kCTParagraphStyleSpecifierTabStops) {
            /* Force the size to be correct, just in case */
            cur->valueSize = sizeof(CFArrayRef);

            if (aref != NULL) {
                PyErr_SetString(PyExc_ValueError,
                                "Multiple kCTParagraphStyleSpecifierTabStops settings");
                r = -1;
            } else {

                r          = PyObjC_PythonToObjC(@encode(CFArrayRef),
                                                 PySequence_Fast_GET_ITEM(s, 2), &aref);
                cur->value = &aref;
            }
        } else {
            r = PyObject_GetBuffer(PySequence_Fast_GET_ITEM(s, 2), views + i,
                                   PyBUF_CONTIG_RO);
            if (r != -1) {
                if ((size_t)views[i].len != cur->valueSize) {
                    PyErr_Format(PyExc_ValueError,
                                 "Got buffer of %ld bytes, need %ld bytes",
                                 (long)views[i].len, (long)cur->valueSize);
                    PyBuffer_Release(views + i);
                    r = -1;
                } else {
                    cur->value = views[i].buf;
                }
            }
        }
        if (r == -1) {
            goto setup_error;
        }
    }

    CTParagraphStyleRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CTParagraphStyleCreate(settings, len);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    for (i = 0; i < len; i++) {
        if (settings[i].spec != kCTParagraphStyleSpecifierTabStops) {
            PyBuffer_Release(views + i);
        }
    }

    free(settings);
    free(views);

    if (PyErr_Occurred()) {
        if (rv) {
            CFRelease(rv);
        }
        return NULL;
    }

    if (rv == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    result = PyObjC_ObjCToPython(@encode(CTParagraphStyleRef), &rv);
    CFRelease(rv);
    return result;

setup_error:
    Py_DECREF(seq);
    for (Py_ssize_t j = 0; j < i; j++) {
        if (settings[j].spec != kCTParagraphStyleSpecifierTabStops) {
            PyBuffer_Release(views + j);
        }
    }

    free(settings);
    free(views);
    return NULL;
}

static void
m_CTRunDelegateDeallocateCallback(void* refCon)
{
    PyGILState_STATE state = PyGILState_Ensure();

    Py_XDECREF((PyObject*)refCon);

    PyGILState_Release(state);
}

static CGFloat
m_CTRunDelegateGetAscentCallback(void* refCon)
{
    PyObject* info = (PyObject*)refCon;
    PyObject* cb   = PyTuple_GetItem(info, 0);
    PyObject* rc   = PyTuple_GetItem(info, 3);
    CGFloat   value;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* rv = PyObject_CallFunction(cb, "O", rc);
    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_PythonToObjC(@encode(CGFloat), rv, &value) < 0) {
        Py_DECREF(rv);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyGILState_Release(state);
    return value;
}

static CGFloat
m_CTRunDelegateGetDescentCallback(void* refCon)
{
    PyObject* info = (PyObject*)refCon;
    PyObject* cb   = PyTuple_GetItem(info, 1);
    PyObject* rc   = PyTuple_GetItem(info, 3);
    CGFloat   value;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* rv = PyObject_CallFunction(cb, "O", rc);
    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_PythonToObjC(@encode(CGFloat), rv, &value) < 0) {
        Py_DECREF(rv);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyGILState_Release(state);
    return value;
}

static CGFloat
m_CTRunDelegateGetWidthCallback(void* refCon)
{
    PyObject* info = (PyObject*)refCon;
    PyObject* cb   = PyTuple_GetItem(info, 2);
    PyObject* rc   = PyTuple_GetItem(info, 3);
    CGFloat   value;

    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* rv = PyObject_CallFunction(cb, "O", rc);
    if (rv == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    if (PyObjC_PythonToObjC(@encode(CGFloat), rv, &value) < 0) {
        Py_DECREF(rv);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    PyGILState_Release(state);
    return value;
}

static CTRunDelegateCallbacks m_CTRunDelegateCallbacks = {
    kCTRunDelegateCurrentVersion,     m_CTRunDelegateDeallocateCallback,
    m_CTRunDelegateGetAscentCallback, m_CTRunDelegateGetDescentCallback,
    m_CTRunDelegateGetWidthCallback,
};

static PyObject*
m_CTRunDelegateGetRefCon(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*        py_delegate;
    CTRunDelegateRef delegate;
    PyObject*        py_refcon;
    void*            refcon;

    if (!PyArg_ParseTuple(args, "O", &py_delegate)) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CTRunDelegateRef), py_delegate, &delegate) == -1) {
        return NULL;
    }

    refcon = CTRunDelegateGetRefCon(delegate);
    if (refcon == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    py_refcon = PyTuple_GetItem((PyObject*)refcon, 3);
    Py_INCREF(py_refcon);
    return py_refcon;
}

static PyObject*
m_CTRunDelegateCreate(PyObject* self __attribute__((__unused__)), PyObject* args)
{
    PyObject*        py_delegate;
    PyObject*        py_getAscender;
    PyObject*        py_getDescender;
    PyObject*        py_getWidth;
    PyObject*        py_refCon;
    PyObject*        info;
    CTRunDelegateRef delegate;

    if (!PyArg_ParseTuple(args, "(OOO)O", &py_getAscender, &py_getDescender, &py_getWidth,
                          &py_refCon)) {
        return NULL;
    }
    if (!PyCallable_Check(py_getAscender)) {
        PyErr_SetString(PyExc_TypeError, "getAscender is not callable");
        return NULL;
    }
    if (!PyCallable_Check(py_getDescender)) {
        PyErr_SetString(PyExc_TypeError, "getDescender is not callable");
        return NULL;
    }
    if (!PyCallable_Check(py_getWidth)) {
        PyErr_SetString(PyExc_TypeError, "getWidth is not callable");
        return NULL;
    }
    info =
        Py_BuildValue("(OOOO)", py_getAscender, py_getDescender, py_getWidth, py_refCon);
    if (info == NULL) {
        return NULL;
    }

    delegate = CTRunDelegateCreate(&m_CTRunDelegateCallbacks, (void*)info);
    if (delegate == NULL) {
        Py_DECREF(info);
        return NULL;
    }
    py_delegate = PyObjC_ObjCToPython(@encode(CTRunDelegateRef), &delegate);
    CFRelease(delegate);
    return py_delegate;
}

static PyMethodDef mod_methods[] = {
    {"CTFontCopyAvailableTables", (PyCFunction)m_CTFontCopyAvailableTables, METH_VARARGS,
     NULL},
    {"CTParagraphStyleGetTabStops", (PyCFunction)m_CTParagraphStyleGetTabStops,
     METH_VARARGS, "CTParagraphStyleGetTabStops(style) -> (stop, ...)"},
    {
        "CTParagraphStyleCreate",
        (PyCFunction)m_CTParagraphStyleCreate,
        METH_VARARGS,
        NULL,
    },
    {
        "CTRunDelegateGetRefCon",
        (PyCFunction)m_CTRunDelegateGetRefCon,
        METH_VARARGS,
        NULL,
    },
    {
        "CTRunDelegateCreate",
        (PyCFunction)m_CTRunDelegateCreate,
        METH_VARARGS,
        "CTRunDelegateCreate((getAscent, getDescent, getWidth), info) -> runDelegate",
    },

    {
        0,
        0,
        0,
    }};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_manual", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__manual(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__manual(void)
{
    PyObject* m = PyModule_Create(&mod_module);
    if (m == NULL)
        return NULL;

    if (PyObjC_ImportAPI(m) < 0)
        return NULL;

    if (PyModule_AddIntConstant(m, "sizeof_CGFloat", sizeof(CGFloat)) < 0)
        return NULL;
    if (PyModule_AddIntConstant(m, "sizeof_CTTextAlignment", sizeof(CTTextAlignment)) < 0)
        return NULL;
    if (PyModule_AddIntConstant(m, "sizeof_CTLineBreakMode", sizeof(CTLineBreakMode)) < 0)
        return NULL;
    if (PyModule_AddIntConstant(m, "sizeof_CTWritingDirection",
                                sizeof(CTWritingDirection))
        < 0)
        return NULL;
    if (PyModule_AddIntConstant(m, "sizeof_id", sizeof(id)) < 0)
        return NULL;

    return m;
}
