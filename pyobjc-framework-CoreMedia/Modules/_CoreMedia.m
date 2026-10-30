#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#ifdef USE_STATIC_ANALYZER
#include "../../pyobjc-core/Modules/objc/python-api-used.h"
#endif

#import <CoreMedia/CoreMedia.h>

NS_ASSUME_NONNULL_BEGIN

int
parse_parameterset(Py_ssize_t parameterSetCount, PyObject* py_parameterSetPointers,
                   uint8_t*** parameterSetPointers, PyObject* py_parameterSetSizes,
                   size_t** parameterSetSizes, Py_buffer** parameterSetViews)
{
    Py_ssize_t i;
    *parameterSetPointers = NULL;
    *parameterSetSizes    = NULL;
    *parameterSetViews    = NULL;

    if (parameterSetCount < 0) {
        PyErr_SetString(PyExc_ValueError, "parameterSetCount out of range");
        return -1;
    }

    PyObject* seq_psp = PySequence_Tuple(py_parameterSetPointers);
    if (seq_psp == NULL) {
        PyErr_SetString(PyExc_TypeError,
                        "parameterSetPointers must be sequence of buffers");
        return -1;
    }
    PyObject* seq_pss = PySequence_Tuple(py_parameterSetSizes);
    if (seq_pss == NULL) {
        PyErr_SetString(PyExc_TypeError,
                        "parameterSetSizes must be sequence of integers");
        return -1;
    }

    if (PyTuple_Size(seq_psp) != parameterSetCount) {
        PyErr_Format(PyExc_ValueError, "expecting %ld parameterSetPointers, got %ld",
                     parameterSetCount, PyTuple_Size(seq_psp));
        return -1;
    }
    if (PyTuple_Size(seq_pss) < parameterSetCount) {
        PyErr_Format(PyExc_ValueError, "expecting %ld parameterSetSizes, got %ld",
                     parameterSetCount, PyTuple_Size(seq_pss));
        return -1;
    }

    *parameterSetPointers = PyMem_Malloc(sizeof(uint8_t**) * parameterSetCount);
    if (*parameterSetPointers == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                       // LCOV_EXCL_LINE
    }

    *parameterSetSizes = PyMem_Malloc(sizeof(size_t*) * parameterSetCount);
    if (*parameterSetPointers == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(parameterSetPointers);
        return -1;
        // LCOV_EXCL_STOP
    }

    *parameterSetViews = PyMem_Malloc(sizeof(Py_buffer) * parameterSetCount);
    if (*parameterSetViews == NULL) { // // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyMem_Free(parameterSetPointers);
        PyMem_Free(parameterSetSizes);
        return -1;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < parameterSetCount; i++) {
        long expected_size;

        PyObject* cur_size = PyTuple_GET_ITEM(seq_pss, i);
        PyObject* cur_buf  = PyTuple_GET_ITEM(seq_psp, i);

        if (PyLong_Check(cur_size)) {
            expected_size = PyLong_AsLong(cur_size);
            if (expected_size == -1 && PyErr_Occurred()) {
                goto error;
            }

        } else {
            PyErr_Format(PyExc_TypeError,
                         "Element %d of parameterSetSizes is not an integer", i);
            goto error;
        }

        if (expected_size < 0) {
            PyErr_Format(PyExc_TypeError, "Element %d of parameterSetSizes is negative",
                         i);
            goto error;
        }

        if (PyUnicode_Check(cur_buf)) {
            /* Explicitly reject unicode objects, those implement the buffer protocol but
             * are not usable here.
             */
            PyErr_Format(PyExc_TypeError,
                         "Element %d of parameterSetPointers is not a buffer", i);
            goto error;
        }

        if (PyObject_GetBuffer(cur_buf, (*parameterSetViews) + i, PyBUF_CONTIG_RO)
            == -1) {
            goto error;
        }
        if ((*parameterSetViews)[i].len < expected_size) {
            PyErr_Format(PyExc_TypeError,
                         "Element %d of parameterSetPointers is too small", i);
            goto error;
        }

        (*parameterSetSizes)[i]    = (size_t)expected_size;
        (*parameterSetPointers)[i] = (uint8_t*)((*parameterSetViews)[i].buf);
    }

    return 0;

error:
    if (*parameterSetPointers != NULL) {
        PyMem_Free(*parameterSetPointers);
    }
    if (*parameterSetSizes != NULL) {
        PyMem_Free(*parameterSetSizes);
    }
    if (*parameterSetViews != NULL) {
        for (Py_ssize_t j = 0; j < i; j++) {
            PyBuffer_Release((*parameterSetViews) + j);
        }
        PyMem_Free(*parameterSetViews);
    }

    return -1;
}

static void
clear_parameterset(size_t parameterSetCount, uint8_t** parameterSetPointers,
                   size_t* parameterSetSizes, Py_buffer* parameterSetViews)
{
    size_t i;

    PyMem_Free(parameterSetPointers);
    PyMem_Free(parameterSetSizes);
    for (i = 0; i < parameterSetCount; i++) {
        PyBuffer_Release(parameterSetViews + i);
    }
    PyMem_Free(parameterSetViews);
}

static PyObject* _Nullable m_CMVideoFormatDescriptionCreateFromH264ParameterSets(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef         allocator;
    Py_ssize_t             parameterSetCount;
    uint8_t**              parameterSetPointers;
    Py_buffer*             parameterSetViews;
    size_t*                parameterSetSizes;
    int                    NALUnitHeaderLength;
    CMFormatDescriptionRef formatDescriptionOut;
    OSStatus               rv;

    if (PyObjC_CheckArgCount(meth, 6, 6, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &parameterSetCount) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(int), args[4], &NALUnitHeaderLength) == -1) {
        return NULL;
    }

    if (args[5] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "formatDescriptionOut must be None");
        return NULL;
    }
    if (parse_parameterset(parameterSetCount, args[2], &parameterSetPointers, args[3],
                           &parameterSetSizes, &parameterSetViews)
        == -1) {
        return NULL;
    }

    rv = CMVideoFormatDescriptionCreateFromH264ParameterSets(
        allocator, parameterSetCount, (const uint8_t* const*)parameterSetPointers,
        parameterSetSizes, NALUnitHeaderLength, &formatDescriptionOut);

    clear_parameterset(parameterSetCount, parameterSetPointers, parameterSetSizes,
                       parameterSetViews);

    if (rv == 0) {
        PyObject* py_formatDescriptionOut =
            PyObjC_ObjCToPython(@encode(CMFormatDescriptionRef), &formatDescriptionOut);
        CFRelease(formatDescriptionOut);
        return Py_BuildValue("iN", rv, py_formatDescriptionOut);
    } else {
        return Py_BuildValue("iO", rv, Py_None);
    }
}

#if PyObjC_BUILD_RELEASE >= 1013

static PyObject* _Nullable m_CMVideoFormatDescriptionCreateFromHEVCParameterSets(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef         allocator;
    Py_ssize_t             parameterSetCount;
    uint8_t**              parameterSetPointers;
    Py_buffer*             parameterSetViews;
    size_t*                parameterSetSizes;
    int                    NALUnitHeaderLength;
    CMFormatDescriptionRef formatDescriptionOut;
    CFDictionaryRef        extensions;
    OSStatus               rv;

    if (PyObjC_CheckArgCount(meth, 7, 7, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &parameterSetCount) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(int), args[4], &NALUnitHeaderLength) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), args[5], &extensions) == -1) {
        return NULL;
    }
    if (args[6] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "formatDescriptionOut must be None");
        return NULL;
    }
    if (parse_parameterset(parameterSetCount, args[2], &parameterSetPointers, args[3],
                           &parameterSetSizes, &parameterSetViews)
        == -1) {
        return NULL;
    }

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

    rv = CMVideoFormatDescriptionCreateFromHEVCParameterSets(
        allocator, parameterSetCount, (const uint8_t* const*)parameterSetPointers,
        parameterSetSizes, NALUnitHeaderLength, extensions, &formatDescriptionOut);

#pragma clang diagnostic pop

    clear_parameterset(parameterSetCount, parameterSetPointers, parameterSetSizes,
                       parameterSetViews);

    if (rv == 0) {
        PyObject* py_formatDescriptionOut =
            PyObjC_ObjCToPython(@encode(CMFormatDescriptionRef), &formatDescriptionOut);
        CFRelease(formatDescriptionOut);
        return Py_BuildValue("iN", rv, py_formatDescriptionOut);
    } else {
        return Py_BuildValue("iO", rv, Py_None);
    }
}

#endif

static PyMethodDef mod_methods[] = {
    {NULL} /* Sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1) // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(
            CMVideoFormatDescriptionCreateFromH264ParameterSets,
            m_CMVideoFormatDescriptionCreateFromH264ParameterSets)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
#if PyObjC_BUILD_RELEASE >= 1013

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
    if (PyObjCRegister_FunctionCaller(
            CMVideoFormatDescriptionCreateFromHEVCParameterSets,
            m_CMVideoFormatDescriptionCreateFromHEVCParameterSets)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
#pragma clang diagnostic pop

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
    .m_name     = "_CoreMedia",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* _Nullable PyInit__CoreMedia(void);

PyObject* _Nullable __attribute__((__visibility__("default")))
PyInit__CoreMedia(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
