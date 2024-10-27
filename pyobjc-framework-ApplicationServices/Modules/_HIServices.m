#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

#if PyObjC_BUILD_RELEASE < 1011
#define kAXValueTypeCGPoint kAXValueCGPointType
#define kAXValueTypeCGSize kAXValueCGSizeType
#define kAXValueTypeCGRect kAXValueCGRectType
#define kAXValueTypeCFRange kAXValueCFRangeType
#define kAXValueTypeAXError kAXValueAXErrorType
#define kAXValueTypeIllegal kAXValueIllegalType
#endif

static PyObject*
m_AXValueCreate(PyObject* mod __attribute__((__unused__)), PyObject* args)
{
    UInt32     valueType;
    PyObject*  py_value;
    AXValueRef value;
    CGPoint    point;
    CGSize     size;
    CGRect     rect;
    CFRange    range;
    AXError    error;
    void*      valuePtr;
    PyObject*  result;

    if (!PyArg_ParseTuple(args, "IO", &valueType, &py_value)) {
        return NULL;
    }

    switch (valueType) {
    case kAXValueTypeCGPoint:
        valuePtr = (void*)&point;
        if (PyObjC_PythonToObjC(@encode(CGPoint), py_value, valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeCGSize:
        valuePtr = (void*)&size;
        if (PyObjC_PythonToObjC(@encode(CGSize), py_value, valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeCGRect:
        valuePtr = (void*)&rect;
        if (PyObjC_PythonToObjC(@encode(CGRect), py_value, valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeCFRange:
        valuePtr = (void*)&range;
        if (PyObjC_PythonToObjC(@encode(CFRange), py_value, valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeAXError:
        valuePtr = (void*)&error;
        if (PyObjC_PythonToObjC(@encode(AXError), py_value, valuePtr) == -1) {
            return NULL;
        }
        break;

    default:
        PyErr_SetString(PyExc_ValueError, "'type' is invalid");
        return NULL;
    }

    value = AXValueCreate(valueType, valuePtr);
    if (value == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    } else {
        result = PyObjC_ObjCToPython(@encode(AXValueRef), &value);
        CFRelease(value);
        return result;
    }
}

static PyObject*
m_AXValueGetValue(PyObject* mod __attribute__((__unused__)), PyObject* args)
{
    UInt32     valueType;
    PyObject*  py_value;
    PyObject*  py_valuePtr;
    AXValueRef value;
    CGPoint    point;
    CGSize     size;
    CGRect     rect;
    CFRange    range;
    AXError    error;
    void*      valuePtr;
    Boolean    ok;

    if (!PyArg_ParseTuple(args, "OIO", &py_value, &valueType, &py_valuePtr)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AXValueRef), py_value, &value) == -1) {
        return NULL;
    }

    if (py_valuePtr != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'valuePtr' should be None");
        return NULL;
    }

    switch (valueType) {
    case kAXValueTypeCGPoint:
        valuePtr = (void*)&point;
        break;

    case kAXValueTypeCGSize:
        valuePtr = (void*)&size;
        break;

    case kAXValueTypeCGRect:
        valuePtr = (void*)&rect;
        break;

    case kAXValueTypeCFRange:
        valuePtr = (void*)&range;
        break;

    case kAXValueTypeAXError:
        valuePtr = (void*)&error;
        break;
    default:
        PyErr_SetString(PyExc_ValueError, "'type' is invalid");
        return NULL;
    }

    ok = AXValueGetValue(value, valueType, valuePtr);
    if (!ok) {
        return Py_BuildValue("OO", Py_False, Py_None);
    } else {
        switch (valueType) {
        case kAXValueTypeCGPoint:
            return Py_BuildValue("ON", Py_True,
                                 PyObjC_ObjCToPython(@encode(CGPoint), (void*)&point));

        case kAXValueTypeCGSize:
            return Py_BuildValue("ON", Py_True,
                                 PyObjC_ObjCToPython(@encode(CGSize), (void*)&size));

        case kAXValueTypeCGRect:
            return Py_BuildValue("ON", Py_True,
                                 PyObjC_ObjCToPython(@encode(CGRect), (void*)&rect));

        case kAXValueTypeCFRange:
            return Py_BuildValue("ON", Py_True,
                                 PyObjC_ObjCToPython(@encode(CFRange), (void*)&range));

        case kAXValueTypeAXError:
            return Py_BuildValue("ON", Py_True,
                                 PyObjC_ObjCToPython(@encode(AXError), (void*)&error));

        default:
            /* We shouldn't get here, argument validation has already checked
             * the range of values
             */
            PyErr_SetString(PyExc_RuntimeError, "Unexpected Value Type");
            return NULL;
        }
    }
}

static PyMethodDef mod_methods[] = {
    {"AXValueCreate", (PyCFunction)m_AXValueCreate, METH_VARARGS,
     "AXValueCreate(/, type, value) -> axvalue"},
    {"AXValueGetValue", (PyCFunction)m_AXValueGetValue, METH_VARARGS,
     "AXValueGetValue(/, axvalue, type, *None*) -> value"},

    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_HIServices", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__HIServices(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__HIServices(void)
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
