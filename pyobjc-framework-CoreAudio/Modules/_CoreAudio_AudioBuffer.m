/*
 * AudioBuffer bindings
 *
 * These are basic bindings to the AudioBuffer type,
 * basically a buffer with extra attributes.
 *
 * XXX: This won't work if APIs return a pointer to a *writable* of *changing* AudioBuffer
 */

#include "structmember.h" /* Why is this needed */

static PyTypeObject audio_buffer_type; /* Forward definition */

#define audio_buffer_check(obj) PyObject_TypeCheck(obj, &audio_buffer_type)

struct audio_buffer {
    PyObject_HEAD

    char        ab_ownsbuffer;
    AudioBuffer ab_buf;
};

static PyMemberDef ab_members[] = {
    {
        .name = "mOwnsBuffer",
        .type = T_BOOL,
        .offset = offsetof(struct audio_buffer, ab_ownsbuffer),
        .flags = READONLY,
        .doc = "True iff this buffer owns the underlying storage"
    },
    {
        .name = "mNumberChannels",
        .type = T_UINT,
        .offset = offsetof(struct audio_buffer, ab_buf) + offsetof(AudioBuffer, mNumberChannels),
        .flags = 0,
        .doc = NULL
    },
    {
        .name = "mDataByteSize",
        .type = T_UINT,
        .offset = offsetof(struct audio_buffer, ab_buf) + offsetof(AudioBuffer, mDataByteSize),
        .flags = READONLY,
        .doc = NULL
    },

    { .name = NULL } /* Sentinel */
};

static PyObject*
ab_get_data(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    if (self->ab_buf.mData == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

#if PY_MAJOR_VERSION == 3
    return PyMemoryView_FromMemory(self->ab_buf.mData, self->ab_buf.mDataByteSize, PyBUF_WRITE);
#else
    return PyBuffer_FromMemory(self->ab_buf.mData, self->ab_buf.mDataByteSize);
#endif
}

static PyGetSetDef ab_getset[] = {
    {
        .name = "mData",
        .get = ab_get_data,
        .set = NULL,
        .doc = NULL,
        .closure = NULL
    },

    { .name = NULL } /* Sentinel */
};

static PyObject*
ab_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "nuab_channels", "bufsize", NULL };
    /* Args: channels (default to 1), size (default: no buffer) */
    struct audio_buffer* result;
    Py_ssize_t bufsize = -1;
    unsigned int nuab_channels = 1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "|"
#if PY_MAJOR_VERSION == 3
                "&" /* keyword only */
#endif
                "II", keywords, &nuab_channels, &bufsize)) {
        return NULL;
    }

    if ((bufsize != -1 && bufsize < 0) || bufsize > UINT_MAX) {
        PyErr_SetString(PyExc_ValueError, "bufsize out of range");
        return NULL;
    }

    result = PyObject_New(struct audio_buffer, &audio_buffer_type);
    if (result == NULL) {
        return NULL;
    }

    result->ab_ownsbuffer = 0;
    result->ab_buf.mNumberChannels = nuab_channels;
    result->ab_buf.mDataByteSize = 0;
    result->ab_buf.mData = NULL;

    if (bufsize != -1) {
        result->ab_buf.mData = PyMem_Malloc(bufsize);
        if (result->ab_buf.mData == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        result->ab_buf.mDataByteSize = (unsigned int)bufsize;
        result->ab_ownsbuffer = 1;
    }

    return (PyObject*)result;
}

static void
ab_dealloc(PyObject* object)
{
    struct audio_buffer* self = (struct audio_buffer*)object;

    if (self->ab_ownsbuffer && self->ab_buf.mData != NULL) {
        PyMem_Free(self->ab_buf.mData);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(ab_doc,
    "AudioBuffer(*, numchannels=1, bufsize=-1)\n"
    CLINIC_SEP
    "Return an audiobuffer. If a buffer size is specified "
    "this will allocate a buffer, otherwise no buffer is "
    "allocated\n");

static PyTypeObject audio_buffer_type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "CoreAudio.AudioBuffer",
    .tp_basicsize   = sizeof(struct audio_buffer),
    .tp_itemsize    = 0,
    .tp_dealloc     = ab_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = ab_doc,
    //.tp_methods     = ab_methods,
    .tp_getset      = ab_getset,
    .tp_members     = ab_members,
    .tp_new         = ab_new,
};

static PyObject* pythonify_audio_buffer(void* pointer)
{
    AudioBuffer* buf_pointer = *(AudioBuffer**)pointer;
    struct audio_buffer* result;

    result = PyObject_New(struct audio_buffer, &audio_buffer_type);
    if (result == NULL) {
        return NULL;
    }

    result->ab_ownsbuffer = 0;
    result->ab_buf = *(buf_pointer);

    return (PyObject*)result;
}

static int depythonify_audio_buffer(PyObject* value, void* pointer)
{
    if (!audio_buffer_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioBuffer', got '%.100s'",
            Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioBuffer**)pointer = &(((struct audio_buffer*)value)->ab_buf);
    return 0;
}

static int
init_audio_buffer(PyObject* module)
{
    int r;
    Py_INCREF(&audio_buffer_type);
    r = PyModule_AddObject(module, "AudioBuffer", (PyObject*)&audio_buffer_type);
    if (r == -1) {
        Py_DECREF(&audio_buffer_type);
        return -1;
    }

    r = PyObjCPointerWrapper_Register(
        "AudioBuffer*",
        @encode(AudioBuffer*),
        pythonify_audio_buffer,
        depythonify_audio_buffer);

    return r;
}
