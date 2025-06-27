#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "structmember.h" /* Why is this needed */

#include "pyobjc-api.h"

#import <CoreAudio/CoreAudio.h>

/* Source files are included here due to use of PyObjC's API */
#include "_CoreAudio_AudioBuffer.m"
#include "_CoreAudio_AudioBufferList.m"
#include "_CoreAudio_AudioChannelDescription.m"
#include "_CoreAudio_AudioChannelLayout.m"
#include "_CoreAudio_AudioValueTranslation.m"

static PyObject*
m_TestAudioFormatNativeEndian(PyObject* mod __attribute__((__unused__)), PyObject* args)
{
    AudioStreamBasicDescription description;
    PyObject*                   o;

    if (!PyArg_ParseTuple(args, "O", &o)) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(AudioStreamBasicDescription), o, &description)
        == -1) {
        return NULL;
    }

    if (TestAudioFormatNativeEndian(description)) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyMethodDef mod_methods[] = {
    {"TestAudioFormatNativeEndian", (PyCFunction)m_TestAudioFormatNativeEndian,
     METH_VARARGS, NULL},

    {0, 0, 0, 0} /* sentinel */
};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;
    if (init_audio_buffer(m) == -1)
        return -1;
    if (init_audio_buffer_list(m) == -1)
        return -1;
    if (init_audio_value_translation(m) == -1)
        return -1;
    if (init_audio_channel_description(m) == -1)
        return -1;
    if (init_audio_channel_layout(m) == -1)
        return -1;

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
    .m_name     = "_CoreAudio",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit__CoreAudio(void);

PyObject* __attribute__((__visibility__("default")))
PyInit__CoreAudio(void)
{
    return PyModuleDef_Init(&mod_module);
}
