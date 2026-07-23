#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreMediaIO/CMIOHardwareDevice.h>

#if PyObjC_BUILD_RELEASE >= 1203
#import <CoreMediaIO/CMIOExtensionDevice.h>
#import <CoreMediaIO/CMIOExtensionProvider.h>
#import <CoreMediaIO/CMIOExtensionStream.h>
#endif

// LCOV_EXCL_START
// This function is only present to ensure protocols are
// available at runtime.

static void __attribute__((__used__))
use_protocols(void)
{
#if PyObjC_BUILD_RELEASE >= 1203

    PyObject* p __attribute__((__unused__));
    p = PyObjC_IdToPython(@protocol(CMIOExtensionDeviceSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CMIOExtensionProviderSource));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(CMIOExtensionStreamSource));
    Py_XDECREF(p);
#endif
}
// LCOV_EXCL_STOP

static PyObject*
m_CMIODeviceProcessAVCCommand(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                              size_t    nargs)
{
    CMIODeviceID         deviceID;
    CMIODeviceAVCCommand avcCommand;
    PyObject*            t;
    OSStatus             r;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMIODeviceID), args[0], &deviceID) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CMIODeviceAVCCommand), args[1], &avcCommand) == -1) {
        return NULL;
    }

    r = CMIODeviceProcessAVCCommand(deviceID, &avcCommand);

    t = PyObjC_ObjCToPython(@encode(UInt32), &avcCommand.mResponseUsed);
    if (t == NULL) {
        return NULL;
    }

    if (PySequence_SetItem(args[1], 4, t) == -1) {
        Py_DECREF(t);
        return NULL;
    }

    Py_DECREF(t);
    return Py_BuildValue("iN", r, args[1]);
}

static PyObject*
m_CMIODeviceProcessRS422Command(PyObject* meth, PyObject* _Nonnull const* _Nonnull args,
                                size_t    nargs)
{
    CMIODeviceID           deviceID;
    CMIODeviceRS422Command rs422Command;
    PyObject*              t;
    OSStatus               r;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMIODeviceID), args[0], &deviceID) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CMIODeviceRS422Command), args[1], &rs422Command)
        == -1) {
        return NULL;
    }

    r = CMIODeviceProcessRS422Command(deviceID, &rs422Command);

    t = PyObjC_ObjCToPython(@encode(UInt32), &rs422Command.mResponseUsed);
    if (t == NULL) {
        return NULL;
    }

    if (PySequence_SetItem(args[1], 4, t) == -1) {
        Py_DECREF(t);
        return NULL;
    }

    Py_DECREF(t);
    return Py_BuildValue("iN", r, args[1]);
}

static PyMethodDef mod_methods[] = {
    {NULL} /* Sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1) // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE

    if (PyObjCRegister_FunctionCaller(CMIODeviceProcessAVCCommand,
                                      m_CMIODeviceProcessAVCCommand)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CMIODeviceProcessRS422Command,
                                      m_CMIODeviceProcessRS422Command)
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
    .m_name     = "_CoreMediaIO",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__CoreMediaIO(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__CoreMediaIO(void)
{
    return PyModuleDef_Init(&mod_module);
}
