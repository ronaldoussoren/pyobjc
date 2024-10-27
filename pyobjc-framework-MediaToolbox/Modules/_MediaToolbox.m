#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
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
m_MTAudioProcessingTapCreate(PyObject* self __attribute__((__unused__)), PyObject* args,
                             PyObject* kwds)
{
    static char* keywords[] = {"allocator", "callbacks", "flags", "tapOut", NULL};

    PyObject*    py_allocator;
    PyObject*    py_callbacks;
    unsigned int flags;
    PyObject*    py_tapOut;

    CFAllocatorRef                allocator;
    MTAudioProcessingTapCallbacks callbacks = callback_template;
    MTAudioProcessingTapRef       tap;
    PyObject*                     info;
    int                           i;
    OSStatus                      rv;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOIO", keywords, &py_allocator,
                                     &py_callbacks, &flags, &py_tapOut)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) == -1) {
        return NULL;
    }

    if (!PyTuple_Check(py_callbacks) || PyTuple_Size(py_callbacks) != 7) {
        PyErr_SetString(PyExc_ValueError, "callbacks should be tuple of 7 items");
        return NULL;
    }

    if (py_tapOut != Py_None) {
        PyErr_SetString(PyExc_ValueError, "tapOut should be None");
        return NULL;
    }
    /* XXX: Validate py_callbacks[0], should be kMTAudioProcessingTapCallbacksVersion_0 */
    for (i = 2; i < 7; i++) {
        /* Most callbacks can be either None or a callable */
        if (i != 6 && PyTuple_GetItem(py_callbacks, i) == Py_None)
            continue;

        if (!PyCallable_Check(PyTuple_GetItem(py_callbacks, i))) {
            PyErr_Format(PyExc_ValueError, "callbacks[%d] should be callable", i);
            return NULL;
        }
    }

    info = PyTuple_New(OFFSET_COUNT);
    if (info == NULL) {
        return NULL;
    }

    PyTuple_SetItem(info, INFO_OFFSET, PyTuple_GetItem(py_callbacks, 1));
    Py_INCREF(PyTuple_GetItem(info, INFO_OFFSET));
    PyTuple_SetItem(info, INIT_OFFSET, PyTuple_GetItem(py_callbacks, 2));
    Py_INCREF(PyTuple_GetItem(info, INIT_OFFSET));
    PyTuple_SetItem(info, FINALIZE_OFFSET, PyTuple_GetItem(py_callbacks, 3));
    Py_INCREF(PyTuple_GetItem(info, FINALIZE_OFFSET));
    PyTuple_SetItem(info, PREPARE_OFFSET, PyTuple_GetItem(py_callbacks, 4));
    Py_INCREF(PyTuple_GetItem(info, PREPARE_OFFSET));
    PyTuple_SetItem(info, UNPREPARE_OFFSET, PyTuple_GetItem(py_callbacks, 5));
    Py_INCREF(PyTuple_GetItem(info, UNPREPARE_OFFSET));
    PyTuple_SetItem(info, PROCESS_OFFSET, PyTuple_GetItem(py_callbacks, 6));
    Py_INCREF(PyTuple_GetItem(info, PROCESS_OFFSET));

    callbacks.clientInfo = info;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = MTAudioProcessingTapCreate(allocator, &callbacks, flags, &tap);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            rv = -1;
        }
    Py_END_ALLOW_THREADS

    if (rv == -1 && PyErr_Occurred()) {
        Py_DECREF(info);
        return NULL;
    }

    if (rv != 0) {
        Py_DECREF(info);
    }

    if (rv == 0) {
        py_tapOut = PyObjC_ObjCToPython(@encode(MTAudioProcessingTapRef), &tap);
        CFRelease(tap);
    } else {
        py_tapOut = Py_None;
        Py_INCREF(Py_None);
    }

    return Py_BuildValue("iN", rv, py_tapOut);
}

static PyObject*
m_MTAudioProcessingTapGetStorage(PyObject* self __attribute__((__unused__)),
                                 PyObject* args, PyObject* kwds)
{
    static char*            keywords[] = {"tap", NULL};
    PyObject*               py_tap;
    MTAudioProcessingTapRef tap;
    PyObject*               cb_info;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &py_tap)) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(MTAudioProcessingTapRef), py_tap, &tap) == -1) {
        return NULL;
    }

    cb_info = (PyObject*)MTAudioProcessingTapGetStorage(tap);
    Py_INCREF(PyTuple_GetItem(cb_info, INFO_OFFSET));
    return PyTuple_GetItem(cb_info, INFO_OFFSET);
}

static PyMethodDef mod_methods[] = {
    {"MTAudioProcessingTapCreate", (PyCFunction)m_MTAudioProcessingTapCreate,
     METH_VARARGS | METH_KEYWORDS, NULL},
    {"MTAudioProcessingTapGetStorage", (PyCFunction)m_MTAudioProcessingTapGetStorage,
     METH_VARARGS | METH_KEYWORDS, NULL},

    {NULL} /* Sentinel */
};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_MediaToolbox", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__MediaToolbox(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__MediaToolbox(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    return m;
}
