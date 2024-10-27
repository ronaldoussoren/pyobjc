#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
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

    if (args == NULL || !PyTuple_Check(args) || PyTuple_Size(args) != 4) {
        PyErr_SetString(PyExc_TypeError,
                        "Vision.VNNormalizedFaceBoundingBoxPointForLandmarkPoint "
                        "requires 4 arguments");
        return NULL;
    }
    if (PyObjC_PythonToObjC("<2f>", PyTuple_GetItem(args, 0), &faceLandmarkPoint) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGRect), PyTuple_GetItem(args, 1), &faceBoundingBox)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GetItem(args, 2), &imageWidth)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GetItem(args, 3), &imageHeight)
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

    if (args == NULL || !PyTuple_Check(args) || PyTuple_Size(args) != 4) {
        PyErr_SetString(PyExc_TypeError,
                        "Vision.VNImagePointForFaceLandmarkPoint requires 4 arguments");
        return NULL;
    }
    if (PyObjC_PythonToObjC("<2f>", PyTuple_GetItem(args, 0), &faceLandmarkPoint) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CGRect), PyTuple_GetItem(args, 1), &faceBoundingBox)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GetItem(args, 2), &imageWidth)
        == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(size_t), PyTuple_GetItem(args, 3), &imageHeight)
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

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_Vision", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__Vision(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__Vision(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

#if PyObjC_BUILD_RELEASE >= 1013

    if (@available(macOS 10.13, *)) {
        /* pass */
    } else {
        if (PyDict_DelItemString(PyModule_GetDict(m),
                                 "VNNormalizedFaceBoundingBoxPointForLandmarkPoint")
            == -1) {
            return NULL;
        }
        if (PyDict_DelItemString(PyModule_GetDict(m), "VNImagePointForFaceLandmarkPoint")
            == -1) {
            return NULL;
        }
    }

#endif

    return m;
}
