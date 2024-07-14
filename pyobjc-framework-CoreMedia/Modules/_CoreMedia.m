#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreMedia/CoreMedia.h>

int
parse_parameterset(Py_ssize_t parameterSetCount, PyObject* py_parameterSetPointers,
                   uint8_t*** parameterSetPointers, PyObject* py_parameterSetSizes,
                   size_t** parameterSetSizes, Py_buffer** parameterSetViews)
{
    Py_ssize_t i;
    *parameterSetPointers = NULL;
    *parameterSetSizes    = NULL;
    *parameterSetViews    = NULL;

    if (!PyTuple_Check(py_parameterSetPointers)) {
        PyErr_SetString(PyExc_TypeError, "parameterSetPointers must be tuple of buffers");
        return -1;
    }
    if (!PyTuple_Check(py_parameterSetSizes)) {
        PyErr_SetString(PyExc_TypeError, "parameterSetSizes must be tuple of buffers");
        return -1;
    }
    if (PyTuple_Size(py_parameterSetPointers) < parameterSetCount) {
        PyErr_SetString(PyExc_ValueError, "parameterSetPointers is too small");
        return -1;
    }
    if (PyTuple_Size(py_parameterSetSizes) < parameterSetCount) {
        PyErr_SetString(PyExc_ValueError, "parameterSetSizes is too small");
        return -1;
    }

    *parameterSetPointers = PyMem_Malloc(sizeof(uint8_t**) * parameterSetCount);
    if (*parameterSetPointers == NULL) {
        return -1;
    }

    *parameterSetSizes = PyMem_Malloc(sizeof(size_t*) * parameterSetCount);
    if (*parameterSetPointers == NULL) {
        PyMem_Free(parameterSetPointers);
        return -1;
    }

    *parameterSetViews = PyMem_Malloc(sizeof(Py_buffer) * parameterSetCount);
    if (*parameterSetViews == NULL) {
        PyMem_Free(parameterSetPointers);
        PyMem_Free(parameterSetSizes);
        return -1;
    }

    for (i = 0; i < parameterSetCount; i++) {
        long expected_size;

        if (PyLong_Check(PyTuple_GetItem(py_parameterSetSizes, i))) {
            expected_size = PyLong_AsLong(PyTuple_GetItem(py_parameterSetSizes, i));
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

        if (PyUnicode_Check(PyTuple_GetItem(py_parameterSetPointers, i))) {
            /* Explicitly reject unicode objects, those implement the buffer protocol but
             * are not usable here.
             */
            PyErr_Format(PyExc_TypeError,
                         "Element %d of parameterSetPointers is not a buffer", i);
            goto error;
        }

        if (PyObject_GetBuffer(PyTuple_GetItem(py_parameterSetPointers, i),
                               (*parameterSetViews) + i, PyBUF_CONTIG_RO)
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

static PyObject*
m_CMVideoFormatDescriptionCreateFromH264ParameterSets(PyObject* mod
                                                      __attribute__((__unused__)),
                                                      PyObject* args, PyObject* kwds)
{
    static char*           keywords[] = {"allocator",
                                         "parameterSetCount",
                                         "parameterSetPointers",
                                         "parameterSetSizes",
                                         "NALUnitHeaderLength",
                                         "formatDescriptionOut",
                                         NULL};
    CFAllocatorRef         allocator;
    PyObject*              py_allocator;
    Py_ssize_t             parameterSetCount;
    uint8_t**              parameterSetPointers;
    Py_buffer*             parameterSetViews;
    PyObject*              py_parameterSetPointers;
    size_t*                parameterSetSizes;
    PyObject*              py_parameterSetSizes;
    int                    NALUnitHeaderLength;
    CMFormatDescriptionRef formatDescriptionOut;
    PyObject*              py_formatDescriptionOut;
    OSStatus               rv;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OnOOiO", keywords, &py_allocator,
                                     &parameterSetCount, &py_parameterSetPointers,
                                     &py_parameterSetSizes, &NALUnitHeaderLength,
                                     &py_formatDescriptionOut)) {
        return NULL;
    }

    if (parameterSetCount < 0) {
        PyErr_SetString(PyExc_ValueError, "parameterSetCount out of range");
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) == -1) {
        return NULL;
    }
    if (py_formatDescriptionOut != Py_None) {
        PyErr_SetString(PyExc_ValueError, "formatDescriptionOut must be None");
        return NULL;
    }
    if (parse_parameterset(parameterSetCount, py_parameterSetPointers,
                           &parameterSetPointers, py_parameterSetSizes,
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
        py_formatDescriptionOut =
            PyObjC_ObjCToPython(@encode(CMFormatDescriptionRef), &formatDescriptionOut);
        CFRelease(formatDescriptionOut);
        return Py_BuildValue("iN", rv, py_formatDescriptionOut);
    } else {
        return Py_BuildValue("iO", rv, Py_None);
    }
}

#if PyObjC_BUILD_RELEASE >= 1013

static PyObject*
m_CMVideoFormatDescriptionCreateFromHEVCParameterSets(PyObject* mod
                                                      __attribute__((__unused__)),
                                                      PyObject* args, PyObject* kwds)
{
    static char*           keywords[] = {"allocator",
                                         "parameterSetCount",
                                         "parameterSetPointers",
                                         "parameterSetSizes",
                                         "NALUnitHeaderLength",
                                         "extensions",
                                         "formatDescriptionOut",
                                         NULL};
    CFAllocatorRef         allocator;
    PyObject*              py_allocator;
    Py_ssize_t             parameterSetCount;
    uint8_t**              parameterSetPointers;
    Py_buffer*             parameterSetViews;
    PyObject*              py_parameterSetPointers;
    size_t*                parameterSetSizes;
    PyObject*              py_parameterSetSizes;
    int                    NALUnitHeaderLength;
    CMFormatDescriptionRef formatDescriptionOut;
    PyObject*              py_formatDescriptionOut;
    CFDictionaryRef        extensions;
    PyObject*              py_extensions;
    OSStatus               rv;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "OkOOiOO", keywords, &py_allocator,
                                     &parameterSetCount, &py_parameterSetPointers,
                                     &py_parameterSetSizes, &NALUnitHeaderLength,
                                     &py_extensions, &py_formatDescriptionOut)) {
        return NULL;
    }

    if (parameterSetCount < 0) {
        PyErr_SetString(PyExc_ValueError, "parameterSetCount out of range");
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), py_extensions, &extensions) == -1) {
        return NULL;
    }
    if (py_formatDescriptionOut != Py_None) {
        PyErr_SetString(PyExc_ValueError, "formatDescriptionOut must be None");
        return NULL;
    }
    if (parse_parameterset(parameterSetCount, py_parameterSetPointers,
                           &parameterSetPointers, py_parameterSetSizes,
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
        py_formatDescriptionOut =
            PyObjC_ObjCToPython(@encode(CMFormatDescriptionRef), &formatDescriptionOut);
        CFRelease(formatDescriptionOut);
        return Py_BuildValue("iN", rv, py_formatDescriptionOut);
    } else {
        return Py_BuildValue("iO", rv, Py_None);
    }
}

#endif

static PyMethodDef mod_methods[] = {
    {"CMVideoFormatDescriptionCreateFromH264ParameterSets",
     (PyCFunction)m_CMVideoFormatDescriptionCreateFromH264ParameterSets,
     METH_VARARGS | METH_KEYWORDS, NULL},
#if PyObjC_BUILD_RELEASE >= 1013

    {"CMVideoFormatDescriptionCreateFromHEVCParameterSets",
     (PyCFunction)m_CMVideoFormatDescriptionCreateFromHEVCParameterSets,
     METH_VARARGS | METH_KEYWORDS, NULL},

#endif

    {NULL} /* Sentinel */
};

static int mod_exec_module(PyObject* m)
{
#if PyObjC_BUILD_RELEASE >= 1013 && MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_13

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

    if (&CMVideoFormatDescriptionCreateFromHEVCParameterSets == NULL) {
        if (PyObject_DelAttrString(m, "CMVideoFormatDescriptionCreateFromHEVCParameterSets") == -1) {
            return -1;
        }
    }

#pragma clang diagnostic pop

#endif

    if (PyObjC_ImportAPI(m) == -1)
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
        .value = Py_MOD_GIL_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_CoreMedia",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__CoreMedia(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__CoreMedia(void)
{
    return PyModuleDef_Init(&mod_module);
}
