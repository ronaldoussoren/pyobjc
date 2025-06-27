#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <VideoToolbox/VideoToolbox.h>

#include "_VideoToolbox_protocols.m"

static PyObject*
m_VTCompressionSessionGetTimeRangesForNextPass(PyObject* self __attribute__((__unused__)),
                                               PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"session", "timeRangeCountOut", "timeRangeArrayOut", NULL};
    PyObject*    py_session;
    PyObject*    py_timeRangeCount;
    PyObject*    py_timeRangeArray;
    OSStatus     rv;
    VTCompressionSessionRef session;
    CMItemCount             timeRangeCount;
    const CMTimeRange*      timeRangeArray;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OOO", keywords, &py_session,
                                     &py_timeRangeCount, &py_timeRangeArray)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(VTCompressionSessionRef), py_session, &session)
        == -1) {
        return NULL;
    }
    if (py_timeRangeCount != Py_None) {
        PyErr_SetString(PyExc_ValueError, "timeRangeCountOut must be None");
        return NULL;
    }
    if (py_timeRangeArray != Py_None) {
        PyErr_SetString(PyExc_ValueError, "timeRangeArrayOut must be None");
        return NULL;
    }

    rv = VTCompressionSessionGetTimeRangesForNextPass(session, &timeRangeCount,
                                                      &timeRangeArray);
    if (rv == 0) {
        py_timeRangeArray = PyObjC_CArrayToPython(@encode(CMTimeRange),
                                                  (void*)timeRangeArray, timeRangeCount);
        if (py_timeRangeArray == NULL) {
            return NULL;
        }
        return Py_BuildValue("ilN", rv, (long)timeRangeCount, py_timeRangeArray);

    } else {
        return Py_BuildValue("iOO", rv, Py_None, Py_None);
    }
}

static PyObject*
m_VTDecompressionSessionCreate(PyObject* self __attribute__((__unused__)), PyObject* args,
                               PyObject* kwds)
{
    static char* keywords[] = {"allocator",
                               "videoFormatDescription",
                               "videoDecoderSpecification",
                               "destinationImageBufferAttributes",
                               "outputCallback",
                               "decompressionSessionOut",
                               NULL};

    PyObject*                           py_allocator;
    CFAllocatorRef                      allocator;
    PyObject*                           py_videoFormatDescription;
    CMVideoFormatDescriptionRef         videoFormatDescription;
    PyObject*                           py_videoDecoderSpecification;
    CFDictionaryRef                     videoDecoderSpecification;
    PyObject*                           py_destinationImageBufferAttributes;
    CFDictionaryRef                     destinationImageBufferAttributes;
    PyObject*                           py_outputCallback;
    VTDecompressionOutputCallbackRecord outputCallback;
    PyObject*                           py_decompressionSessionOut;
    VTDecompressionSessionRef           decompressionSessionOut;
    OSStatus                            rv;
    int                                 have_outputCallback;

    if (!PyArg_ParseTupleAndKeywords(
            args, kwds, "OOOOOO", keywords, &py_allocator, &py_videoFormatDescription,
            &py_videoDecoderSpecification, &py_destinationImageBufferAttributes,
            &py_outputCallback, &py_decompressionSessionOut)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CMVideoFormatDescriptionRef),
                            py_videoFormatDescription, &videoFormatDescription)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), py_videoDecoderSpecification,
                            &videoDecoderSpecification)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), py_destinationImageBufferAttributes,
                            &destinationImageBufferAttributes)
        == -1) {
        return NULL;
    }
    if (py_decompressionSessionOut != Py_None) {
        PyErr_SetString(PyExc_ValueError, "decompressionSessionOut must be None");
        return NULL;
    }
    if (py_outputCallback == Py_None) {
        have_outputCallback = 0;
    } else if (!PyTuple_Check(py_outputCallback)
               || PyTuple_Size(py_outputCallback) != 2) {
        PyErr_SetString(PyExc_TypeError, "outputCallback should be a tuple of 2 items");
        return NULL;
    } else {
        have_outputCallback = 1;
        /* FIXME: This is annoying: there is no clear way to store associated data here...
         */
        PyErr_SetString(PyExc_ValueError,
                        "Passing an outputCallback is not supported at the moment");
    }

    rv = VTDecompressionSessionCreate(
        allocator, videoFormatDescription, videoDecoderSpecification,
        destinationImageBufferAttributes, have_outputCallback ? &outputCallback : NULL,
        &decompressionSessionOut);
    if (rv == 0) {
        py_decompressionSessionOut = PyObjC_ObjCToPython(
            @encode(VTDecompressionSessionRef), &decompressionSessionOut);
        return Py_BuildValue("iN", rv, py_decompressionSessionOut);
    } else {
        return Py_BuildValue("iO", rv, Py_None);
    }
}

static PyMethodDef mod_methods[] = {
    {"VTCompressionSessionGetTimeRangesForNextPass",
     (PyCFunction)m_VTCompressionSessionGetTimeRangesForNextPass,
     METH_VARARGS | METH_KEYWORDS, NULL},
    {"VTDecompressionSessionCreate", (PyCFunction)m_VTDecompressionSessionCreate,
     METH_VARARGS | METH_KEYWORDS, NULL},

    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;
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
    .m_name     = "_VideoToolbox",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__VideoToolbox(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__VideoToolbox(void)
{
    return PyModuleDef_Init(&mod_module);
}
