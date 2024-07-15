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

static int mod_exec_module(PyObject* m)
{
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
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_SceneKit",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit__SceneKit(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__SceneKit(void)
{
    return PyModuleDef_Init(&mod_module);
}
