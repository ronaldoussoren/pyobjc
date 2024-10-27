#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03060000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreMediaIO/CMIOHardwareDevice.h>

#if PyObjC_BUILD_RELEASE >= 1203
#import <CoreMediaIO/CMIOExtensionDevice.h>
#import <CoreMediaIO/CMIOExtensionProvider.h>
#import <CoreMediaIO/CMIOExtensionStream.h>
#endif

static void __attribute__((__used__)) use_protocols(void)
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

static PyObject*
m_CMIODeviceProcessAVCCommand(PyObject* self __attribute__((__unused__)), PyObject* args,
                              PyObject* kwds)
{
    static char* keywords[] = {"deviceID", "ioAVCCommand", NULL};

    CMIODeviceID         deviceID;
    CMIODeviceAVCCommand avcCommand;
    PyObject*            py_avcCommand;
    PyObject*            t;
    OSStatus             r;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "IO", keywords, &deviceID,
                                     &py_avcCommand)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMIODeviceAVCCommand), py_avcCommand, &avcCommand)
        == -1) {
        return NULL;
    }

    r = CMIODeviceProcessAVCCommand(deviceID, &avcCommand);

    t = PyObjC_ObjCToPython(@encode(UInt32), &avcCommand.mResponseUsed);
    if (t == NULL) {
        return NULL;
    }

    if (PySequence_SetItem(py_avcCommand, 4, t) == -1) {
        Py_DECREF(t);
        return NULL;
    }

    Py_DECREF(t);
    return Py_BuildValue("iN", r, py_avcCommand);
}

static PyObject*
m_CMIODeviceProcessRS422Command(PyObject* self __attribute__((__unused__)),
                                PyObject* args, PyObject* kwds)
{
    static char* keywords[] = {"deviceID", "ioRS422Command", NULL};

    CMIODeviceID           deviceID;
    CMIODeviceRS422Command rs422Command;
    PyObject*              py_rs422Command;
    PyObject*              t;
    OSStatus               r;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "IO", keywords, &deviceID,
                                     &py_rs422Command)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMIODeviceRS422Command), py_rs422Command,
                            &rs422Command)
        == -1) {
        return NULL;
    }

    r = CMIODeviceProcessRS422Command(deviceID, &rs422Command);

    t = PyObjC_ObjCToPython(@encode(UInt32), &rs422Command.mResponseUsed);
    if (t == NULL) {
        return NULL;
    }

    if (PySequence_SetItem(py_rs422Command, 4, t) == -1) {
        Py_DECREF(t);
        return NULL;
    }

    Py_DECREF(t);
    return Py_BuildValue("iN", r, py_rs422Command);
}

static PyMethodDef mod_methods[] = {
    {"CMIODeviceProcessAVCCommand", (PyCFunction)m_CMIODeviceProcessAVCCommand,
     METH_VARARGS | METH_KEYWORDS, NULL},
    {"CMIODeviceProcessRS422Command", (PyCFunction)m_CMIODeviceProcessRS422Command,
     METH_VARARGS | METH_KEYWORDS, NULL},

    {NULL} /* Sentinel */
};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "_CoreMediaIO", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit__CoreMediaIO(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__CoreMediaIO(void)
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
