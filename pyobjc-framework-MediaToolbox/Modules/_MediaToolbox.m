#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <MediaToolbox/MediaToolbox.h>

NS_ASSUME_NONNULL_BEGIN

enum {
    INFO_OFFSET,
    INIT_OFFSET,
    FINALIZE_OFFSET,
    PREPARE_OFFSET,
    UNPREPARE_OFFSET,
    PROCESS_OFFSET,

    OFFSET_COUNT
};

static void
init_callback(MTAudioProcessingTapRef tap, void* clientInfo, void** tapStorageOut)
{
    PyObject* cb_info = (PyObject*)clientInfo;
    PyObject* cb;
    *tapStorageOut = clientInfo;
    Py_INCREF(clientInfo);

    cb = PyTuple_GET_ITEM(cb_info, INIT_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* py_tap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        if (tap == NULL) // LCOV_BR_EXCL_LINE
            goto error;  // LCOV_EXCL_LINE
        PyObject* rv = PyObject_CallFunction(
            cb,
            "NO"
            "O",
            py_tap, PyTuple_GET_ITEM(cb_info, INFO_OFFSET), Py_None);
        if (rv == NULL)
            goto error;
        Py_DECREF(PyTuple_GET_ITEM(clientInfo, INFO_OFFSET));
        PyTuple_SET_ITEM(clientInfo, INFO_OFFSET, rv);
    }

    PyGILState_Release(state);
    return;

error:
    fputs("Ignoring exception in MTAudioProcessing callback\n", stderr);
    PyErr_Print();
    Py_DECREF(PyTuple_GET_ITEM(clientInfo, INFO_OFFSET));
    PyTuple_SET_ITEM(clientInfo, INFO_OFFSET, Py_None);
    Py_INCREF(Py_None);
    PyGILState_Release(state);
}

static void
finalize_callback(MTAudioProcessingTapRef tap)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GET_ITEM(cb_info, FINALIZE_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* pytap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        if (pytap == NULL) // LCOV_BR_EXCL_LINE
            goto error;    // LCOV_EXCL_LINE
        PyObject* rv = PyObject_CallFunctionObjArgs(cb, pytap, NULL);
        Py_CLEAR(pytap);
        if (rv == NULL)
            goto error;

        Py_CLEAR(rv);
    }

    /* The finalize callback is the last time any callback will be called,
     * therefore clean up the python state information.
     */
    Py_XDECREF(cb_info);
    PyGILState_Release(state);
    return;

error:
    fputs("Ignoring exception in MTAudioProcessing callback\n", stderr);
    PyErr_Print();

    Py_XDECREF(cb_info);
    PyGILState_Release(state);
}

static void
prepare_callback(MTAudioProcessingTapRef tap, CMItemCount maxFrames,
                 const AudioStreamBasicDescription* processingFormat)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GET_ITEM(cb_info, PREPARE_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* rv = PyObject_CallFunction(
            cb, "NNN", PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap),
            PyObjC_ObjCToPython(@encode(CMItemCount), &maxFrames),
            PyObjC_ObjCToPython(@encode(AudioStreamBasicDescription),
                                (void*)processingFormat));
        if (rv == NULL)
            goto error;
        Py_XDECREF(rv);
    }

    PyGILState_Release(state);
    return;

error:
    fputs("Ignoring exception in MTAudioProcessing callback\n", stderr);
    PyErr_Print();
    PyGILState_Release(state);
}

static void
unprepare_callback(MTAudioProcessingTapRef tap)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GET_ITEM(cb_info, UNPREPARE_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* rv = PyObject_CallFunction(
            cb, "N", PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap));
        if (rv == NULL) {
            goto error;
        }
        Py_XDECREF(rv);
    }

    PyGILState_Release(state);
    return;

error:
    fputs("Ignoring exception in MTAudioProcessing callback\n", stderr);
    PyErr_Print();
    PyGILState_Release(state);
}

static void
process_callback(MTAudioProcessingTapRef tap, CMItemCount numberFrames,
                 MTAudioProcessingTapFlags flags, AudioBufferList* bufferListInOut,
                 CMItemCount* numberFramesOut, MTAudioProcessingTapFlags* flagsOut)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GET_ITEM(cb_info, PROCESS_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* py_bufferListInOut;
        PyObject* rv = PyObject_CallFunction(
            cb, "NNNNOO", PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap),
            PyObjC_ObjCToPython(@encode(CMItemCount), &numberFrames),
            PyObjC_ObjCToPython(@encode(MTAudioProcessingTapFlags), &flags),
            (py_bufferListInOut =
                 PyObjC_ObjCToPython(@encode(AudioBufferList*), &bufferListInOut)),
            Py_None, Py_None);
        if (rv == NULL)
            goto error;

        if (!PyTuple_Check(rv) || PyTuple_Size(rv) != 3) {
            PyErr_SetString(PyExc_TypeError,
                            "MTAudioProcessing processing callback should return "
                            "(bufferListInOut, numFrames, flags)\n");
            goto error;
        }
        if (PyTuple_GET_ITEM(rv, 0) != py_bufferListInOut) {
            /* XXX: Is this correct? Can one replace the bufferList entirely? */
            PyErr_SetString(PyExc_TypeError,
                            "MTAudioProcessing processing callback should return "
                            "(bufferListInOut, numFrames, flags)\n");
            goto error;
        }
        (void)PyObjC_PythonToObjC(@encode(CMItemCount), PyTuple_GET_ITEM(rv, 1),
                                  (void*)numberFramesOut);
        (void)PyObjC_PythonToObjC(@encode(MTAudioProcessingTapFlags),
                                  PyTuple_GET_ITEM(rv, 2), (void*)flagsOut);
        Py_CLEAR(rv);
        if (PyErr_Occurred()) {
            goto error;
        }
    }

    PyGILState_Release(state);
    return;
error:
    fputs("Ignoring exception in MTAudioProcessing callback\n", stderr);
    PyErr_Print();
    PyGILState_Release(state);
}

static MTAudioProcessingTapCallbacks callback_template = {
    .version    = kMTAudioProcessingTapCallbacksVersion_0,
    .clientInfo = NULL,
    .init       = init_callback,
    .finalize   = finalize_callback,
    .prepare    = prepare_callback,
    .unprepare  = unprepare_callback,
    .process    = process_callback};

static PyObject* _Nullable m_MTAudioProcessingTapCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    unsigned int flags;

    CFAllocatorRef                allocator;
    MTAudioProcessingTapCallbacks callbacks = callback_template;
    MTAudioProcessingTapRef       tap;
    PyObject*                     info;
    int                           i;
    OSStatus                      rv;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) == -1) {
        return NULL;
    }

    if (!PyTuple_Check(args[1]) || PyTuple_Size(args[1]) != 7) {
        PyErr_SetString(PyExc_ValueError, "callbacks should be tuple of 7 items");
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(unsigned int), args[2], &flags) == -1) {
        return NULL;
    }

    if (args[3] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'tapOut' should be None");
        return NULL;
    }

    if (!PyLong_Check(PyTuple_GET_ITEM(args[1], 0))
        || PyLong_AsLong(PyTuple_GET_ITEM(args[1], 0))
               != kMTAudioProcessingTapCallbacksVersion_0) {
        PyErr_SetString(PyExc_ValueError,
                        "callbacks[0] must be kMTAudioProcessingTapCallbacksVersion_0");
        return NULL;
    }
    /* Note: callbacks[1] can be an arbitrary object */
    for (i = 2; i < 7; i++) {
        /* Most callbacks can be either None or a callable */
        if (i != 6 && PyTuple_GET_ITEM(args[1], i) == Py_None)
            continue;

        if (!PyCallable_Check(PyTuple_GET_ITEM(args[1], i))) {
            PyErr_Format(PyExc_ValueError, "callbacks[%d] should be callable", i);
            return NULL;
        }
    }

    info = PyTuple_Pack(OFFSET_COUNT, PyTuple_GET_ITEM(args[1], 1),
                        PyTuple_GET_ITEM(args[1], 2), PyTuple_GET_ITEM(args[1], 3),
                        PyTuple_GET_ITEM(args[1], 4), PyTuple_GET_ITEM(args[1], 5),
                        PyTuple_GET_ITEM(args[1], 6));
    if (info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    callbacks.clientInfo = info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = MTAudioProcessingTapCreate(allocator, &callbacks, flags, &tap);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            rv = -1;                             // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (rv == -1 && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        Py_DECREF(info);                // LCOV_EXCL_LINE
        return NULL;                    // LCOV_EXCL_LINE
    }

    if (rv != 0) {
        Py_DECREF(info);
    }

    PyObject* py_tapOut;
    if (rv == 0) {
        py_tapOut = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        CFRelease(tap);
    } else {
        py_tapOut = Py_None;
        Py_INCREF(Py_None);
    }

    return Py_BuildValue("lN", (long)rv, py_tapOut);
}

#if PyObjC_BUILD_RELEASE >= 2700
#pragma clang diagnostic ignored "-Wunknown-pragmas"
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

static PyObject* _Nullable m_MTAudioProcessingTapCreateWithPreferredFormat(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    unsigned int flags;

    CFAllocatorRef                allocator;
    MTAudioProcessingTapCallbacks callbacks = callback_template;
    CMAudioFormatDescriptionRef   preferredFormat;
    MTAudioProcessingTapRef       tap;
    PyObject*                     info;
    int                           i;
    OSStatus                      rv;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) == -1) {
        return NULL;
    }

    if (!PyTuple_Check(args[1]) || PyTuple_Size(args[1]) != 7) {
        PyErr_SetString(PyExc_ValueError, "callbacks should be tuple of 7 items");
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(unsigned int), args[2], &flags) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMAudioFormatDescriptionRef), args[3],
                            &preferredFormat)
        == -1) {
        return NULL;
    }

    if (args[4] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'tapOut' should be None");
        return NULL;
    }
    if (!PyLong_Check(PyTuple_GET_ITEM(args[1], 0))
        || PyLong_AsLong(PyTuple_GET_ITEM(args[1], 0))
               != kMTAudioProcessingTapCallbacksVersion_0) {
        PyErr_SetString(PyExc_ValueError,
                        "callbacks[0] must be kMTAudioProcessingTapCallbacksVersion_0");
        return NULL;
    }
    /* callbacks[1] can be an arbitrary value */
    for (i = 2; i < 7; i++) {
        /* Most callbacks can be either None or a callable */
        if (i != 6 && PyTuple_GET_ITEM(args[1], i) == Py_None)
            continue;

        if (!PyCallable_Check(PyTuple_GET_ITEM(args[1], i))) {
            PyErr_Format(PyExc_ValueError, "callbacks[%d] should be callable", i);
            return NULL;
        }
    }

    info = PyTuple_Pack(OFFSET_COUNT, PyTuple_GET_ITEM(args[1], 1),
                        PyTuple_GET_ITEM(args[1], 2), PyTuple_GET_ITEM(args[1], 3),
                        PyTuple_GET_ITEM(args[1], 4), PyTuple_GET_ITEM(args[1], 5),
                        PyTuple_GET_ITEM(args[1], 6));

    if (info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    callbacks.clientInfo = info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = MTAudioProcessingTapCreateWithPreferredFormat(
                allocator, &callbacks, flags, preferredFormat, &tap);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            rv = -1;
        }
    Py_END_ALLOW_THREADS
    Py_DECREF(info);

    if (rv == -1 && PyErr_Occurred()) {
        return NULL;
    }

    if (rv != 0) {
        Py_DECREF(info);
    }

    PyObject* py_tapOut;
    if (rv == 0) {
        py_tapOut = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        CFRelease(tap);
    } else {
        py_tapOut = Py_None;
        Py_INCREF(Py_None);
    }

    return Py_BuildValue("lN", (long)rv, py_tapOut);
}

#pragma clang diagnostic pop
#endif

static PyObject* _Nullable m_MTAudioProcessingTapGetStorage(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    MTAudioProcessingTapRef tap;
    PyObject*               cb_info;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(MTAudioProcessingTapRef), args[0], &tap) == -1) {
        return NULL;
    }

    cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);
    Py_INCREF(PyTuple_GET_ITEM(cb_info, INFO_OFFSET));
    return PyTuple_GET_ITEM(cb_info, INFO_OFFSET);
}

static PyMethodDef mod_methods[] = {

    {NULL} /* Sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyObjCRegister_FunctionCaller(MTAudioProcessingTapCreate,
                                      m_MTAudioProcessingTapCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(MTAudioProcessingTapGetStorage,
                                      m_MTAudioProcessingTapGetStorage)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
#if PyObjC_BUILD_RELEASE >= 2700
    if (__builtin_available(macOS 27.0, *)) {
        if (PyObjCRegister_FunctionCaller(MTAudioProcessingTapCreateWithPreferredFormat,
                                          m_MTAudioProcessingTapCreateWithPreferredFormat)
            == -1) {   // LCOV_BR_EXCL_LINE
            return -1; // LCOV_EXCL_LINE
        }
    }
#endif
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
    .m_name     = "_MediaToolbox",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__MediaToolbox(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__MediaToolbox(void)
{
    return PyModuleDef_Init(&mod_module);
}
NS_ASSUME_NONNULL_END
