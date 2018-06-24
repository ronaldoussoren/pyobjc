#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "pyobjc-api.h"

#import <CoreAudio/CoreAudio.h>

static PyObject*
m_TestAudioFormatNativeEndian(PyObject* mod __attribute__((__unused__)), PyObject* args)
{
    AudioStreamBasicDescription description;
    PyObject* o;

    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AudioStreamBasicDescription), o, &description) == -1) {
        return NULL;
    }

    if (TestAudioFormatNativeEndian(description)) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyMethodDef mod_methods[] = {
  {
      "TestAudioFormatNativeEndian",
      (PyCFunction)m_TestAudioFormatNativeEndian,
      METH_VARARGS,
      NULL
  },

  { 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
PyObjC_MODULE_INIT(_CoreAudio)
{
    PyObject* m;
    m = PyObjC_MODULE_CREATE(_CoreAudio)
    if (!m) {
        PyObjC_INITERROR();
    }

    if (PyObjC_ImportAPI(m) == -1) PyObjC_INITERROR();

    PyObjC_INITDONE();
}
