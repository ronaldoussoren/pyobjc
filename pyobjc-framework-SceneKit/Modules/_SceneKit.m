#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <SceneKit/SceneKit.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_SceneKit_protocols.m"

static PyObject*
m_SCNVector3ToFloat3(PyObject* module __attribute__((__unused__)), PyObject* vector)
{
    SCNVector3    arg;
    vector_float3 result;

    if (PyObjC_PythonToObjC(@encode(SCNVector3), vector, &arg) == -1) {
        return NULL;
    }

    result = SCNVector3ToFloat3(arg);

    return PyObjC_ObjCToPython("<3f>", &result);
}

static PyObject*
m_SCNVector3FromFloat3(PyObject* module __attribute__((__unused__)), PyObject* vector)
{
    SCNVector3    result;
    vector_float3 arg;

    if (PyObjC_PythonToObjC("<3f>", vector, &arg) == -1) {
        return NULL;
    }

    result = SCNVector3FromFloat3(arg);

    return PyObjC_ObjCToPython(@encode(SCNVector3), &result);
}

static PyObject*
m_SCNVector4ToFloat4(PyObject* module __attribute__((__unused__)), PyObject* vector)
{
    SCNVector4    arg;
    vector_float4 result;

    if (PyObjC_PythonToObjC(@encode(SCNVector4), vector, &arg) == -1) {
        return NULL;
    }

    result = SCNVector4ToFloat4(arg);

    return PyObjC_ObjCToPython("<4f>", &result);
}

static PyObject*
m_SCNVector4FromFloat4(PyObject* module __attribute__((__unused__)), PyObject* vector)
{
    SCNVector4    result;
    vector_float4 arg;

    if (PyObjC_PythonToObjC("<4f>", vector, &arg) == -1) {
        return NULL;
    }

    result = SCNVector4FromFloat4(arg);

    return PyObjC_ObjCToPython(@encode(SCNVector4), &result);
}

static PyObject*
m_SCNMatrix4ToMat4(PyObject* module __attribute__((__unused__)), PyObject* vector)
{
    SCNMatrix4      arg;
    matrix_float4x4 result;

    if (PyObjC_PythonToObjC(@encode(SCNMatrix4), vector, &arg) == -1) {
        return NULL;
    }

    result = SCNMatrix4ToMat4(arg);

    return PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &result);
}

static PyObject*
m_SCNMatrix4FromMat4(PyObject* module __attribute__((__unused__)), PyObject* vector)
{
    SCNMatrix4      result;
    matrix_float4x4 arg;

    if (PyObjC_PythonToObjC("{simd_float4x4=[4<4f>]}", vector, &arg) == -1) {
        return NULL;
    }

    result = SCNMatrix4FromMat4(arg);

    return PyObjC_ObjCToPython(@encode(SCNMatrix4), &result);
}

static PyMethodDef mod_methods[] = {
    {"SCNVector3ToFloat3", m_SCNVector3ToFloat3, METH_O,
     "SCNVector3ToFloat3(v,/)\n" CLINIC_SEP "\n"},
    {"SCNVector3FromFloat3", m_SCNVector3FromFloat3, METH_O,
     "SCNVector3FromFloat3(v,/)\n" CLINIC_SEP "\n"},
    {"SCNVector4ToFloat4", m_SCNVector4ToFloat4, METH_O,
     "SCNVector4ToFloat4(v,/)\n" CLINIC_SEP "\n"},
    {"SCNVector4FromFloat4", m_SCNVector4FromFloat4, METH_O,
     "SCNVector4FromFloat4(v,/)\n" CLINIC_SEP "\n"},
    {"SCNMatrix4ToMat4", m_SCNMatrix4ToMat4, METH_O,
     "SCNMatrix4ToMat4(v,/)\n" CLINIC_SEP "\n"},
    {"SCNMatrix4FromMat4", m_SCNMatrix4FromMat4, METH_O,
     "SCNMatrix4FromMat4(v,/)\n" CLINIC_SEP "\n"},
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_SceneKit", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__SceneKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__SceneKit(void)
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
