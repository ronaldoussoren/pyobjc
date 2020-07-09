/*
 * Customer wrappers for a number of CoreVideo APIs.
 */
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreVideo/CoreVideo.h>

static void
mod_CVPixelBufferReleaseBytesCallback(void* releaseRefCon, const void* baseAddress)
{
    PyObject*        info  = (PyObject*)releaseRefCon;
    PyGILState_STATE state = PyGILState_Ensure();

    if (PyTuple_GetItem(info, 0) != Py_None) {
        PyObject* r = PyObject_CallFunction(PyTuple_GetItem(info, 0), "O",
                                            PyTuple_GetItem(info, 1));
        if (r == NULL) {
            Py_XDECREF(info);
            PyObjCErr_ToObjCWithGILState(&state);
        }

        Py_DECREF(r);
    }

    Py_DECREF(info);
    PyGILState_Release(state);
}


static PyObject*
mod_CVPixelBufferCreateWithBytes(PyObject* self __attribute__((__unused__)),
                                 PyObject* args)
{
    CFAllocatorRef   allocator;
    size_t           width;
    size_t           height;
    OSType           pixelFormatType;
    void*            baseAddress;
    size_t           bytesPerRow;
    CFDictionaryRef  pixelBufferAttributes;
    CVPixelBufferRef pixelBuffer;
    PyObject*        py_allocator;
    PyObject*        py_width;
    PyObject*        py_height;
    PyObject*        py_pixelFormatType;
    PyObject*        py_buffer;
    Py_ssize_t       buflen;
    PyObject*        py_bytesPerRow;
    PyObject*        releaseCallback;
    PyObject*        info;
    PyObject*        py_pixelBufferAttributes;
    PyObject*        py_pixelBuffer = Py_None;

    if (!PyArg_ParseTuple(args, "OOOOOOOOO|O", &py_allocator, &py_width, &py_height,
                          &py_pixelFormatType, &py_buffer, &py_bytesPerRow,
                          &releaseCallback, &info, &py_pixelBufferAttributes,
                          &py_pixelBuffer)) {

        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_width, &width) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_height, &height) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(OSType), py_pixelFormatType, &pixelFormatType) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), py_bytesPerRow, &bytesPerRow) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), py_pixelBufferAttributes,
                            &pixelBufferAttributes)
        < 0) {
        return NULL;
    }

    if (py_pixelBuffer != Py_None) {
        PyErr_SetString(PyExc_ValueError, "pixelBufferOut must be None");
        return NULL;
    }

    if (PyObject_AsWriteBuffer(py_buffer, &baseAddress, &buflen) < 0) {
        return NULL;
    }

    PyObject* real_info = Py_BuildValue("OOO", releaseCallback, info, py_buffer);
    if (real_info == NULL) {
        return NULL;
    }

    CVReturn rv;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CVPixelBufferCreateWithBytes(
                allocator, width, height, pixelFormatType, baseAddress, bytesPerRow,
                mod_CVPixelBufferReleaseBytesCallback, real_info, pixelBufferAttributes,
                &pixelBuffer);

        } @catch (NSException* localException) {
            rv = 0;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_DECREF(real_info);
        return NULL;
    }

    if (pixelBuffer == NULL) {
        Py_DECREF(real_info);
        Py_INCREF(Py_None);
        return Py_None;
    }

    py_pixelBuffer = PyObjC_ObjCToPython(@encode(CVPixelBufferRef), &pixelBuffer);
    CFRelease(pixelBuffer); /* Compensate for create rule */
    return py_pixelBuffer;
}

static PyMethodDef mod_methods[] = {{"CVPixelBufferCreateWithBytes",
                                     (PyCFunction)mod_CVPixelBufferCreateWithBytes,
                                     METH_VARARGS, NULL},

                                    {0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
     PyModuleDef_HEAD_INIT,
     "_CVPixelBuffer",
     NULL,                                        
     0,
     mod_methods,                                 
     NULL,                                        
     NULL,                                        
     NULL,                                        
     NULL};                                       

PyObject* PyInit__CVPixelBuffer(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__CVPixelBuffer(void)
{
    PyObject* m = PyModule_Create(&mod_module);
    if (!m)
        return NULL;

    if (PyObjC_ImportAPI(m) < 0)
        return NULL;

    return m;
}
