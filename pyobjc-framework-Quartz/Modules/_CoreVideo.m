/*
 * Customer wrappers for a number of CoreVideo APIs.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <CoreVideo/CoreVideo.h>

NS_ASSUME_NONNULL_BEGIN

static void
mod_CVPixelBufferReleaseBytesCallback(void* releaseRefCon, const void* baseAddress)
{
    PyObject*        info = (PyObject*)releaseRefCon;
    PyObject*        view;
    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(info, 0) != Py_None) {
        PyObject* r = PyObject_CallFunction(PyTuple_GetItem(info, 0), "O",
                                            PyTuple_GetItem(info, 1));
        if (r == NULL) {
            view = PyTuple_GetItem(info, 3);
            PyBuffer_Release(PyObjCMemView_GetBuffer(view));
            Py_XDECREF(info);
            PyObjCErr_ToObjCWithGILState(&state);
        }

        Py_DECREF(r);
    }

    view = PyTuple_GetItem(info, 3);
    PyBuffer_Release(PyObjCMemView_GetBuffer(view));
    Py_DECREF(info);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CVPixelBufferCreateWithBytes(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CVReturn         rv;
    CFAllocatorRef   allocator;
    size_t           width;
    size_t           height;
    OSType           pixelFormatType;
    size_t           bytesPerRow;
    CFDictionaryRef  pixelBufferAttributes;
    CVPixelBufferRef pixelBuffer;
    PyObject*        view;

    if (PyObjC_CheckArgCount(meth, 9, 10, nargs) == -1) {
        return NULL;
    }
    if (nargs == 9) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                         "leaving out 'pixelBuffer' is deprecated", 0)
            == -1) {
            return NULL;
        }
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[1], &width) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[2], &height) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(OSType), args[3], &pixelFormatType) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), args[5], &bytesPerRow) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), args[8], &pixelBufferAttributes)
        < 0) {
        return NULL;
    }

    if (nargs == 10 && args[9] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "pixelBufferOut must be None");
        return NULL;
    }

    view = PyObjCMemView_New();
    if (view == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE
    }

    if (PyObject_GetBuffer(args[4], PyObjCMemView_GetBuffer(view), PyBUF_CONTIG) < 0) {
        return NULL;
    }

    PyObject* real_info = PyTuple_Pack(4, args[6], args[7], args[4], view);
    if (real_info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CVPixelBufferCreateWithBytes(
                allocator, width, height, pixelFormatType,
                PyObjCMemView_GetBuffer(view)->buf, bytesPerRow,
                mod_CVPixelBufferReleaseBytesCallback, real_info, pixelBufferAttributes,
                &pixelBuffer);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(real_info);
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (pixelBuffer == NULL) {
        Py_DECREF(real_info);
        Py_INCREF(Py_None);
        return Py_None;
    }

    PyObject* py_pixelBuffer =
        PyObjC_ObjCToPython(@encode(CVPixelBufferRef), &pixelBuffer);
    CFRelease(pixelBuffer);       /* Compensate for create rule */
    if (py_pixelBuffer == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;              // LCOV_EXCL_LINE
    }

    return Py_BuildValue("(NN)", PyObjC_ObjCToPython(@encode(CVReturn), &rv),
                         py_pixelBuffer);
}

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) // LCOV_BR_EXCL_LINE
        return -1;               // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(CVPixelBufferCreateWithBytes,
                                      mod_CVPixelBufferCreateWithBytes)
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
    .m_name     = "_CoreVideo",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__CoreVideo(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__CoreVideo(void)
{
    return PyModuleDef_Init(&mod_module);
}
NS_ASSUME_NONNULL_END
