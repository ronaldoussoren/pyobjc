#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <ApplicationServices/ApplicationServices.h>

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable m_CTFontCopyAvailableTables(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CTFontRef          font;
    CTFontTableOptions options;
    CFArrayRef         ref;
    Py_ssize_t         len, i;
    PyObject*          result;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CTFontRef), args[0], &font) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CTFontTableOptions), args[1], &options) == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            ref = CTFontCopyAvailableTables(font, options);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            ref = NULL;                          // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (ref == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;        // LCOV_EXCL_LINE
        }

        // We'll hever get here during testing,
        // the function only returns NULL for legacy fonts.
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    len    = CFArrayGetCount(ref);
    result = PyTuple_New(len);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        CFRelease(ref);
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < len; i++) {
        CTFontTableTag tag = (CTFontTableTag)(uintptr_t)CFArrayGetValueAtIndex(ref, i);
        PyTuple_SET_ITEM(result, i, PyLong_FromLong(tag));
        if (PyTuple_GET_ITEM(result, i) == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            CFRelease(ref);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }
    CFRelease(ref);
    return result;
}

static PyObject* _Nullable m_CTParagraphStyleGetValueForSpecifier(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CTParagraphStyleRef       style;
    CTParagraphStyleSpecifier spec;
    size_t                    size;
    PyObject*                 result = NULL;
    bool                      b;
    uint8_t                   uint8_value = 0;
    unsigned long             ulong_value = 0;
    CGFloat                   float_value = 0.0;
    id                        id_value    = NULL;
    void*                     value_buf   = NULL;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CTParagraphStyleRef), args[0], &style) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CTParagraphStyleSpecifier), args[1], &spec) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[2], &size) == -1) {
        return NULL;
    }
    if (args[3] != Py_None) {
        PyErr_Format(PyExc_ValueError, "'valueBuffer' must be None");
        return NULL;
    }

    if (size == 0) {
        switch (spec) {
        case kCTParagraphStyleSpecifierAlignment:
        case kCTParagraphStyleSpecifierLineBreakMode:
        case kCTParagraphStyleSpecifierBaseWritingDirection:
            value_buf = &uint8_value;
            size      = sizeof(uint8_value);
            break;

        case kCTParagraphStyleSpecifierFirstLineHeadIndent:
        case kCTParagraphStyleSpecifierHeadIndent:
        case kCTParagraphStyleSpecifierTailIndent:
        case kCTParagraphStyleSpecifierDefaultTabInterval:
        case kCTParagraphStyleSpecifierLineHeightMultiple:
        case kCTParagraphStyleSpecifierMaximumLineHeight:
        case kCTParagraphStyleSpecifierMinimumLineHeight:
        case kCTParagraphStyleSpecifierLineSpacing:
        case kCTParagraphStyleSpecifierParagraphSpacing:
        case kCTParagraphStyleSpecifierParagraphSpacingBefore:
        case kCTParagraphStyleSpecifierMaximumLineSpacing:
        case kCTParagraphStyleSpecifierMinimumLineSpacing:
        case kCTParagraphStyleSpecifierLineSpacingAdjustment:
            value_buf = &float_value;
            size      = sizeof(float_value);
            break;

        case kCTParagraphStyleSpecifierLineBoundsOptions:
            value_buf = &ulong_value;
            size      = sizeof(ulong_value);
            break;

        case kCTParagraphStyleSpecifierTabStops:
            value_buf = &id_value;
            size      = sizeof(id_value);
            break;

        default:
            PyErr_SetString(PyExc_ValueError, "Cannot automatically determine 'size'");
            return NULL;
        }

    } else if (size == sizeof(id_value) && spec == kCTParagraphStyleSpecifierTabStops) {
        value_buf = &id_value;
        size      = sizeof(id_value);

    } else {
        result = PyBytes_FromStringAndSize(NULL, size);
        if (result == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;      // LCOV_EXCL_LINE
        }
        value_buf = PyBytes_AS_STRING(result);
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            b = CTParagraphStyleGetValueForSpecifier(style, spec, size, value_buf);
        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            b = 0;                               // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_CLEAR(result);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (!b) {
        Py_CLEAR(result);
        return Py_BuildValue("OO", Py_False, Py_None);
    }

    if (result != NULL) {
        result = Py_BuildValue("ON", Py_True, result);
    } else if (value_buf == &uint8_value) {
        result = Py_BuildValue("ON", Py_True, PyLong_FromLong(uint8_value));
    } else if (value_buf == &float_value) {
        result = Py_BuildValue("ON", Py_True, PyFloat_FromDouble(float_value));
    } else if (value_buf == &ulong_value) {
        result = Py_BuildValue("ON", Py_True, PyLong_FromUnsignedLong(ulong_value));
    } else if (value_buf == &id_value) { // LCOV_BR_EXCL_LINE
        result = Py_BuildValue("ON", Py_True, PyObjC_IdToPython(id_value));
    }

    return result;
}

static PyObject* _Nullable m_CTParagraphStyleCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    PyObject*                seq;
    PyObject*                result;
    Py_ssize_t               len, i;
    CFArrayRef               aref = NULL;
    CTParagraphStyleSetting* settings;
    CTParagraphStyleRef      style = NULL;
    Py_buffer*               views = NULL;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &len) == -1) {
        return NULL;
    }

    if (args[0] == Py_None) {
        /* Handle simple case */
        if (len != 0) {
            PyErr_SetString(PyExc_ValueError, "settings list is 'None', length is not 0");
            return NULL;
        }
        Py_BEGIN_ALLOW_THREADS
            @try {
                style = CTParagraphStyleCreate(NULL, 0);

            } @catch (NSException* localException) { // LCOV_EXCL_LINE
                style = NULL;                        // LCOV_EXCL_LINE
                PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            }
        Py_END_ALLOW_THREADS

        if (style == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
            return NULL;                         // LCOV_EXCL_LINE
        }
        if (style == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_INCREF(Py_None);
            return Py_None;
            // LCOV_EXCL_STOP
        }

        result = PyObjC_ObjCToPython(@encode(CTParagraphStyleRef), &style);
        CFRelease(style);
        return result;
    }

    seq = PySequence_Tuple(args[0]);
    if (seq == NULL) {
        return NULL;
    }

    if (PyTuple_GET_SIZE(seq) < len) {
        PyErr_Format(PyExc_ValueError, "need sequence of at least %ld arguments",
                     (long)len);
        Py_DECREF(seq);
        return NULL;
    }

    settings = PyMem_Malloc(sizeof(*settings) * len);
    if (settings == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(seq);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    views = PyMem_Malloc(sizeof(Py_buffer) * len);
    if (views == NULL) { // LCOV_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(settings);
        Py_DECREF(seq);
        PyErr_NoMemory();
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < len; i++) {
        CTParagraphStyleSetting* cur   = settings + i;
        PyObject*                curPy = PyTuple_GET_ITEM(seq, i);
        PyObject*                s     = PySequence_Tuple(curPy);
        int                      r;

        if (s == NULL) {
            goto setup_error;
        }
        if (PyTuple_GET_SIZE(s) != 3) {
            PyErr_Format(PyExc_ValueError, "settings item has length %ld, not 3",
                         (long)PyTuple_GET_SIZE(s));
            goto setup_error;
        }

        r = PyObjC_PythonToObjC(@encode(CTParagraphStyleSpecifier),
                                PyTuple_GET_ITEM(s, 0), &cur->spec);
        if (r == -1) {
            goto setup_error;
        }
        r = PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(s, 1), &cur->valueSize);
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

                r = PyObjC_PythonToObjC(@encode(CFArrayRef), PyTuple_GET_ITEM(s, 2),
                                        &aref);
                cur->value = &aref;
            }
        } else {
            r = PyObject_GetBuffer(PyTuple_GET_ITEM(s, 2), views + i, PyBUF_CONTIG_RO);
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
            Py_DECREF(s);
            goto setup_error;
        }
        Py_DECREF(s);
    }
    Py_DECREF(seq);

    CTParagraphStyleRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CTParagraphStyleCreate(settings, len);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    for (i = 0; i < len; i++) {
        if (settings[i].spec != kCTParagraphStyleSpecifierTabStops) {
            PyBuffer_Release(views + i);
        }
    }

    PyMem_Free(settings);
    PyMem_Free(views);

    if (PyErr_Occurred()) { // LCOV_EXCL_LINE
        // LCOV_EXCL_START
        if (rv) {
            CFRelease(rv);
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (rv == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
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

    PyMem_Free(settings);
    PyMem_Free(views);
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
        /* This callback is invoked in a context where exceptions
         * cannot be raised
         */
        PyErr_WriteUnraisable(cb);
        // PyObjCErr_ToObjCWithGILState(&state);
        PyGILState_Release(state);
        return 42.0;
    }

    if (PyObjC_PythonToObjC(@encode(CGFloat), rv, &value) < 0) {
        Py_DECREF(rv);
        /* This callback is invoked in a context where exceptions
         * cannot be raised
         */
        PyErr_WriteUnraisable(cb);
        // PyObjCErr_ToObjCWithGILState(&state);
        PyGILState_Release(state);
        return 42.0;
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
        /* This callback is invoked in a context where exceptions
         * cannot be raised
         */
        PyErr_WriteUnraisable(cb);
        // PyObjCErr_ToObjCWithGILState(&state);
        PyGILState_Release(state);
        return 42.0;
    }

    if (PyObjC_PythonToObjC(@encode(CGFloat), rv, &value) < 0) {
        Py_DECREF(rv);
        /* This callback is invoked in a context where exceptions
         * cannot be raised
         */
        PyErr_WriteUnraisable(cb);
        // PyObjCErr_ToObjCWithGILState(&state);
        PyGILState_Release(state);
        return 42.0;
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
        /* This callback is invoked in a context where exceptions
         * cannot be raised
         */
        PyErr_WriteUnraisable(cb);
        // PyObjCErr_ToObjCWithGILState(&state);
        PyGILState_Release(state);
        return 42.0;
    }

    if (PyObjC_PythonToObjC(@encode(CGFloat), rv, &value) < 0) {
        Py_DECREF(rv);
        /* This callback is invoked in a context where exceptions
         * cannot be raised
         */
        PyErr_WriteUnraisable(cb);
        // PyObjCErr_ToObjCWithGILState(&state);
        PyGILState_Release(state);
        return 42.0;
    }

    PyGILState_Release(state);
    return value;
}

static CTRunDelegateCallbacks m_CTRunDelegateCallbacks = {
    kCTRunDelegateCurrentVersion,     m_CTRunDelegateDeallocateCallback,
    m_CTRunDelegateGetAscentCallback, m_CTRunDelegateGetDescentCallback,
    m_CTRunDelegateGetWidthCallback,
};

static PyObject* _Nullable m_CTRunDelegateGetRefCon(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CTRunDelegateRef delegate;
    PyObject*        py_refcon;
    void*            refcon;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CTRunDelegateRef), args[0], &delegate) == -1) {
        return NULL;
    }

    refcon = CTRunDelegateGetRefCon(delegate);
    if (refcon == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    }

    /* This will crash when the delegate wasn't created
     * in Python. There's nothing we can do about this
     * though.
     */
    py_refcon = PyTuple_GetItem((PyObject*)refcon, 3);
    Py_INCREF(py_refcon);
    return py_refcon;
}

static PyObject* _Nullable m_CTRunDelegateCreate(PyObject* meth,
                                                 PyObject* _Nonnull const* _Nonnull args,
                                                 size_t nargs)
{
    PyObject*        py_delegate;
    PyObject*        info;
    CTRunDelegateRef delegate;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }
    if (!PyTuple_Check(args[0]) || PyTuple_GET_SIZE(args[0]) != 3) {
        PyErr_SetString(PyExc_ValueError, "arg0 must be a tuple of 3 callables");
        return NULL;
    }
    if (!PyCallable_Check(PyTuple_GET_ITEM(args[0], 0))) {
        PyErr_SetString(PyExc_TypeError, "getAscender is not callable");
        return NULL;
    }
    if (!PyCallable_Check(PyTuple_GET_ITEM(args[0], 1))) {
        PyErr_SetString(PyExc_TypeError, "getDescender is not callable");
        return NULL;
    }
    if (!PyCallable_Check(PyTuple_GET_ITEM(args[0], 2))) {
        PyErr_SetString(PyExc_TypeError, "getWidth is not callable");
        return NULL;
    }
    info = PyTuple_Pack(4, PyTuple_GET_ITEM(args[0], 0), PyTuple_GET_ITEM(args[0], 1),
                        PyTuple_GET_ITEM(args[0], 2), args[1]);
    if (info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    delegate = CTRunDelegateCreate(&m_CTRunDelegateCallbacks, (void*)info);
    if (delegate == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(info);
        return NULL;
        // LCOV_EXCL_STOP
    }
    py_delegate = PyObjC_ObjCToPython(@encode(CTRunDelegateRef), &delegate);
    CFRelease(delegate);
    return py_delegate;
}

static PyMethodDef mod_methods[] = {{
    0,
    0,
    0,
}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(CTFontCopyAvailableTables,
                                      m_CTFontCopyAvailableTables)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CTParagraphStyleCreate, m_CTParagraphStyleCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CTRunDelegateGetRefCon, m_CTRunDelegateGetRefCon)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CTRunDelegateCreate, m_CTRunDelegateCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CTParagraphStyleGetValueForSpecifier,
                                      m_CTParagraphStyleGetValueForSpecifier)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddIntConstant(m, "sizeof_CGFloat", sizeof(CGFloat))
        < 0)       // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    if (PyModule_AddIntConstant(m, "sizeof_CTTextAlignment", sizeof(CTTextAlignment))
        < 0)       // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    if (PyModule_AddIntConstant(m, "sizeof_CTLineBreakMode", sizeof(CTLineBreakMode))
        < 0)       // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    if (PyModule_AddIntConstant(m, "sizeof_CTWritingDirection",
                                sizeof(CTWritingDirection))
        < 0)                                                     // LCOV_BR_EXCL_LINE
        return -1;                                               // LCOV_EXCL_LINE
    if (PyModule_AddIntConstant(m, "sizeof_id", sizeof(id)) < 0) // LCOV_BR_EXCL_LINE
        return -1;                                               // LCOV_EXCL_LINE

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
    .m_name     = "_CoreText",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__CoreText(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__CoreText(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
