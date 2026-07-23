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
m_AXValueCreate(PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    UInt32     valueType;
    AXValueRef value;
    CGPoint    point;
    CGSize     size;
    CGRect     rect;
    CFRange    range;
    AXError    error;
    void*      valuePtr;
    PyObject*  result;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(UInt32), args[0], &valueType) == -1) {
        return NULL;
    }

    switch (valueType) {
    case kAXValueTypeCGPoint:
        valuePtr = (void*)&point;
        if (PyObjC_PythonToObjC(@encode(CGPoint), args[1], valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeCGSize:
        valuePtr = (void*)&size;
        if (PyObjC_PythonToObjC(@encode(CGSize), args[1], valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeCGRect:
        valuePtr = (void*)&rect;
        if (PyObjC_PythonToObjC(@encode(CGRect), args[1], valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeCFRange:
        valuePtr = (void*)&range;
        if (PyObjC_PythonToObjC(@encode(CFRange), args[1], valuePtr) == -1) {
            return NULL;
        }
        break;

    case kAXValueTypeAXError:
        valuePtr = (void*)&error;
        if (PyObjC_PythonToObjC(@encode(AXError), args[1], valuePtr) == -1) {
            return NULL;
        }
        break;

    default:
        PyErr_SetString(PyExc_ValueError, "'type' is invalid");
        return NULL;
    }

    value = AXValueCreate(valueType, valuePtr);
    if (value == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_INCREF(Py_None);
        return Py_None;
        // LCOV_EXCL_STOP
    } else {
        result = PyObjC_ObjCToPython(@encode(AXValueRef), &value);
        CFRelease(value);
        return result;
    }
}

static PyObject*
m_AXValueGetValue(PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    UInt32     valueType;
    AXValueRef value;
    CGPoint    point;
    CGSize     size;
    CGRect     rect;
    CFRange    range;
    AXError    error;
    void*      valuePtr;
    Boolean    ok;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AXValueRef), args[0], &value) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(UInt32), args[1], &valueType) == -1) {
        return NULL;
    }

    if (args[2] != Py_None) {
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
            // LCOV_EXCL_START
            PyErr_SetString(PyExc_RuntimeError, "Unexpected Value Type");
            return NULL;
            // LCOV_EXCL_STOP
        }
    }
}

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1) // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(AXValueCreate, m_AXValueCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(AXValueGetValue, m_AXValueGetValue)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
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
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "_HIServices",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__HIServices(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__HIServices(void)
{
    return PyModuleDef_Init(&mod_module);
}
