#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#import <Vision/Vision.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_Vision_protocols.m"

/*
 * These two functions have a vector_float2 argument, which requires a manual binding.
 */

#if PyObjC_BUILD_RELEASE >= 1013

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
#pragma clang diagnostic ignored "-Wunguarded-availability"

PyDoc_STRVAR(mod_VNNormalizedFaceBoundingBoxPointForLandmarkPoint_doc,
             "VNNormalizedFaceBoundingBoxPointForLandmarkPoin(faceLandmarkPoint, "
             "faceBoundingBox, imageWidth, imageHeight, /)\n" CLINIC_SEP
             "CGPoint VNNormalizedFaceBoundingBoxPointForLandmarkPoin(vector_float2 "
             "faceLandmarkPoint, CGRect faceBoundingBox, "
             "size_t imageWidth, size_t imageHeight);");
static PyObject* _Nullable mod_VNNormalizedFaceBoundingBoxPointForLandmarkPoint(
    PyObject* mod, PyObject* args)
{
    CGPoint       rv;
    vector_float2 faceLandmarkPoint;
    CGRect        faceBoundingBox;
    size_t        imageWidth;
    size_t        imageHeight;

    if (args == NULL || !PyTuple_Check(args) || PyTuple_GET_SIZE(args) != 4) {
        PyErr_SetString(PyExc_TypeError,
                        "Vision.VNNormalizedFaceBoundingBoxPointForLandmarkPoint "
                        "requires 4 arguments");
        return NULL;
    }
    if (PyObjC_PythonToObjC("<2f>", PyTuple_GET_ITEM(args, 0), &faceLandmarkPoint)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGRect), PyTuple_GET_ITEM(args, 1), &faceBoundingBox)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(args, 2), &imageWidth)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(args, 3), &imageHeight)
        == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = VNNormalizedFaceBoundingBoxPointForLandmarkPoint(
                faceLandmarkPoint, faceBoundingBox, imageWidth, imageHeight);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            rv = (CGPoint){0, 0};
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_ObjCToPython(@encode(CGPoint), &rv);
}

PyDoc_STRVAR(mod_VNImagePointForFaceLandmarkPoint_doc,
             "VNImagePointForFaceLandmarkPoint(faceLandmarkPoint, faceBoundingBox, "
             "imageWidth, imageHeight, /)\n" CLINIC_SEP
             "CGPoint VNImagePointForFaceLandmarkPoint(vector_float2 faceLandmarkPoint, "
             "CGRect faceBoundingBox, "
             "size_t imageWidth, size_t imageHeight);");
static PyObject* _Nullable mod_VNImagePointForFaceLandmarkPoint(PyObject* mod,
                                                                PyObject* args)
{
    CGPoint       rv;
    vector_float2 faceLandmarkPoint;
    CGRect        faceBoundingBox;
    size_t        imageWidth;
    size_t        imageHeight;

    if (args == NULL || !PyTuple_Check(args) || PyTuple_GET_SIZE(args) != 4) {
        PyErr_SetString(PyExc_TypeError,
                        "Vision.VNImagePointForFaceLandmarkPoint requires 4 arguments");
        return NULL;
    }
    if (PyObjC_PythonToObjC("<2f>", PyTuple_GET_ITEM(args, 0), &faceLandmarkPoint)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGRect), PyTuple_GET_ITEM(args, 1), &faceBoundingBox)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(args, 2), &imageWidth)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GET_ITEM(args, 3), &imageHeight)
        == -1) {
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = VNImagePointForFaceLandmarkPoint(faceLandmarkPoint, faceBoundingBox,
                                                  imageWidth, imageHeight);
        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            rv = (CGPoint){0, 0};
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyObjC_ObjCToPython(@encode(CGPoint), &rv);
}

#pragma clang diagnostic pop

#endif

static PyMethodDef mod_methods[] = {
#if PyObjC_BUILD_RELEASE >= 1013

    {
        "VNNormalizedFaceBoundingBoxPointForLandmarkPoint",
        (PyCFunction)mod_VNNormalizedFaceBoundingBoxPointForLandmarkPoint,
        METH_VARARGS,
        mod_VNNormalizedFaceBoundingBoxPointForLandmarkPoint_doc,
    },
    {
        "VNImagePointForFaceLandmarkPoint",
        (PyCFunction)mod_VNImagePointForFaceLandmarkPoint,
        METH_VARARGS,
        mod_VNImagePointForFaceLandmarkPoint_doc,
    },
#endif

    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
#if PyObjC_BUILD_RELEASE >= 1013

    if (@available(macOS 10.13, *)) {
        /* pass */
    } else {
        if (PyObject_DelAttrString(m, "VNNormalizedFaceBoundingBoxPointForLandmarkPoint")
            == -1) {
            return -1;
        }
        if (PyObject_DelAttrString(m, "VNImagePointForFaceLandmarkPoint") == -1) {
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
    .m_name     = "_Vision",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__Vision(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__Vision(void)
{
    return PyModuleDef_Init(&mod_module);
}
