#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreMediaIO/CMIOHardwareDevice.h>

static PyObject*
m_CMIODeviceProcessAVCCommand(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "deviceID", "ioAVCCommand", NULL };

    CMIODeviceID deviceID;
    CMIODeviceAVCCommand avcCommand;
    PyObject* py_avcCommand;
    PyObject* t;
    OSStatus r;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "IO", keywords, &deviceID, &py_avcCommand)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMIODeviceAVCCommand), py_avcCommand, &avcCommand) == -1) {
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
m_CMIODeviceProcessRS422Command(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "deviceID", "ioRS422Command", NULL };

    CMIODeviceID deviceID;
    CMIODeviceRS422Command rs422Command;
    PyObject* py_rs422Command;
    PyObject* t;
    OSStatus r;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "IO", keywords, &deviceID, &py_rs422Command)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CMIODeviceRS422Command), py_rs422Command, &rs422Command) == -1) {
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
    {
        "CMIODeviceProcessAVCCommand",
        (PyCFunction)m_CMIODeviceProcessAVCCommand,
        METH_VARARGS|METH_KEYWORDS,
        NULL
    },
    {
        "CMIODeviceProcessRS422Command",
        (PyCFunction)m_CMIODeviceProcessRS422Command,
        METH_VARARGS|METH_KEYWORDS,
        NULL
    },

    { NULL } /* Sentinel */
};


PyObjC_MODULE_INIT(_CoreMediaIO)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_CoreMediaIO)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
