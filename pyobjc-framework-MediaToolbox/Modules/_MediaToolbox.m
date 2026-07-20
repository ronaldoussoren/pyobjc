#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <MediaToolbox/MediaToolbox.h>

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

    cb = PyTuple_GetItem(cb_info, INIT_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* py_tap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        if (tap == NULL) {
            fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
            PyErr_Print();
        } else {

            PyObject* rv = PyObject_CallFunction(
                cb, "OOO", py_tap, PyTuple_GetItem(cb_info, INFO_OFFSET), Py_None);
            Py_DECREF(py_tap);
            if (rv == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
            }
            Py_XDECREF(rv);
        }
    }

    PyGILState_Release(state);
}

static void
finalize_callback(MTAudioProcessingTapRef tap)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GetItem(cb_info, FINALIZE_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* py_tap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        if (tap == NULL) {
            fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
            PyErr_Print();
        } else {

            PyObject* rv = PyObject_CallFunction(cb, "O", py_tap);
            Py_DECREF(py_tap);
            if (rv == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
            }
            Py_XDECREF(rv);
        }
    }

    /* The finalize callback is the last time any callback will be called,
     * therefore clean up the python state information.
     */
    Py_XDECREF(cb_info);
    PyGILState_Release(state);
}

static void
prepare_callback(MTAudioProcessingTapRef tap, CMItemCount maxFrames,
                 const AudioStreamBasicDescription* processingFormat)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GetItem(cb_info, PREPARE_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        int       have_error = 0;
        PyObject* py_tap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        PyObject* py_maxFrames        = NULL;
        PyObject* py_processingFormat = NULL;
        if (tap == NULL) {
            fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
            PyErr_Print();
            have_error = 1;
        }
        if (!have_error) {
            py_maxFrames = PyObjC_ObjCToPython(@encode(CMItemCount), &maxFrames);
            if (py_maxFrames == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
                have_error = 1;
            }
        }
        if (!have_error) {
            py_processingFormat = PyObjC_ObjCToPython(
                @encode(AudioStreamBasicDescription), (void*)processingFormat);
            if (py_processingFormat == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
                have_error = 1;
            }
        }

        if (!have_error) {
            PyObject* rv = PyObject_CallFunction(cb, "OOO", py_tap, py_maxFrames,
                                                 py_processingFormat);
            Py_DECREF(py_tap);
            if (rv == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
            }
            Py_XDECREF(rv);
        }

        Py_XDECREF(py_tap);
        Py_XDECREF(py_maxFrames);
        Py_XDECREF(py_processingFormat);
    }

    PyGILState_Release(state);
}

static void
unprepare_callback(MTAudioProcessingTapRef tap)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GetItem(cb_info, UNPREPARE_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        PyObject* py_tap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        if (tap == NULL) {
            fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
            PyErr_Print();
        } else {

            PyObject* rv = PyObject_CallFunction(cb, "O", py_tap);
            Py_DECREF(py_tap);
            if (rv == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
            }
            Py_XDECREF(rv);
        }
    }

    PyGILState_Release(state);
}

static void
process_callback(MTAudioProcessingTapRef tap, CMItemCount numberFrames,
                 MTAudioProcessingTapFlags flags, AudioBufferList* bufferListInOut,
                 CMItemCount* numberFramesOut, MTAudioProcessingTapFlags* flagsOut)
{
    PyObject* cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);

    PyObject* cb = PyTuple_GetItem(cb_info, PROCESS_OFFSET);

    PyGILState_STATE state = PyGILState_Ensure();

    if (cb != Py_None) {
        int       have_error = 0;
        PyObject* py_tap = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        PyObject* py_numberFrames    = NULL;
        PyObject* py_flags           = NULL;
        PyObject* py_bufferListInOut = NULL;
        if (tap == NULL) {
            fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
            PyErr_Print();
            have_error = 1;
        }
        if (!have_error) {
            py_numberFrames = PyObjC_ObjCToPython(@encode(CMItemCount), &numberFrames);
            if (py_numberFrames == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
                have_error = 1;
            }
        }
        if (!have_error) {
            py_flags = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapFlags), &flags);
            if (py_flags == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
                have_error = 1;
            }
        }
        if (!have_error) {
            py_bufferListInOut =
                PyObjC_ObjCToPython(@encode(AudioBufferList*), &bufferListInOut);
            if (py_bufferListInOut == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
                have_error = 1;
            }
        }

        if (!have_error) {
            PyObject* rv =
                PyObject_CallFunction(cb, "OOOOOO", py_tap, py_numberFrames, py_flags,
                                      py_bufferListInOut, Py_None, Py_None);
            Py_DECREF(py_tap);
            if (rv == NULL) {
                fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                PyErr_Print();
            }
            if (!PyTuple_Check(rv) || PyTuple_Size(rv) != 3) {
                fprintf(stderr, "MTAudioProcessing processing callback should return "
                                "(bufferListInOut, numFrames, flags)\n");
            } else {
                if (PyTuple_GetItem(rv, 0) != py_bufferListInOut) {
                    fprintf(stderr, "MTAudioProcessing processing callback should return "
                                    "(bufferListInOut, numFrames, flags)\n");
                }
                (void)PyObjC_PythonToObjC(@encode(CMItemCount), PyTuple_GetItem(rv, 1),
                                          (void*)numberFramesOut);
                (void)PyObjC_PythonToObjC(@encode(MTAudioProcessingTapFlags),
                                          PyTuple_GetItem(rv, 2), (void*)flagsOut);
                if (PyErr_Occurred()) {
                    fprintf(stderr, "Ignoring exception in MTAudioProcessing callback\n");
                    PyErr_Print();
                }
            }
            Py_XDECREF(rv);
        }

        Py_XDECREF(py_tap);
        Py_XDECREF(py_numberFrames);
        Py_XDECREF(py_bufferListInOut);
    }

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

static PyObject*
m_MTAudioProcessingTapCreate(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                             size_t    nargs)
{
    unsigned int flags;

    CFAllocatorRef                allocator;
    MTAudioProcessingTapCallbacks callbacks = callback_template;
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

    if (args[3] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "tapOut should be None");
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
    if (info == NULL) {
        return NULL;
    }

    callbacks.clientInfo = info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = MTAudioProcessingTapCreate(allocator, &callbacks, flags, &tap);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            rv = -1;
        }
    Py_END_ALLOW_THREADS

    if (allocator != NULL) {
        CFRelease(allocator);
    }

    if (rv == -1 && PyErr_Occurred()) {
        Py_DECREF(info);
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

    return Py_BuildValue("iN", rv, py_tapOut);
}

#if PyObjC_BUILD_RELEASE >= 2700
#pragma clang diagnostic ignored "-Wunknown-pragmas"
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

static PyObject*
m_MTAudioProcessingTapCreateWithPreferredFormat(PyObject* meth,
                                                PyObject* _Nonnull const* _Nonnull args,
                                                size_t nargs)
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
        PyErr_SetString(PyExc_ValueError, "tapOut should be None");
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

    info = PyTuple_Pack(OFFSET_COUNT, PyTuple_GetItem(args[1], 1),
                        PyTuple_GetItem(args[1], 2), PyTuple_GetItem(args[1], 3),
                        PyTuple_GetItem(args[1], 4), PyTuple_GetItem(args[1], 5),
                        PyTuple_GetItem(args[1], 6));

    if (info == NULL) {
        return NULL;
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

    if (allocator != NULL) {
        CFRelease(allocator);
    }
    if (preferredFormat != NULL) {
        CFRelease(preferredFormat);
    }

    if (rv == -1 && PyErr_Occurred()) {
        Py_DECREF(info);
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

    return Py_BuildValue("iN", rv, py_tapOut);
}

#pragma clang diagnostic pop
#endif

static PyObject*
m_MTAudioProcessingTapGetStorage(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                                 size_t    nargs)
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
    return PyTuple_GetItem(cb_info, INFO_OFFSET);
}

static PyMethodDef mod_methods[] = {

    {NULL} /* Sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyObjCRegister_FunctionCaller(MTAudioProcessingTapCreate,
                                      m_MTAudioProcessingTapCreate)
        == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(MTAudioProcessingTapGetStorage,
                                      m_MTAudioProcessingTapGetStorage)
        == -1) {
        return -1;
    }
#if PyObjC_BUILD_RELEASE >= 2700
    if (__builtin_available(macOS 27.0, *)) {
        if (PyObjCRegister_FunctionCaller(MTAudioProcessingTapCreateWithPreferredFormat,
                                          m_MTAudioProcessingTapCreateWithPreferredFormat)
            == -1) {
            return -1;
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

PyObject* PyInit__MediaToolbox(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__MediaToolbox(void)
{
    return PyModuleDef_Init(&mod_module);
}
