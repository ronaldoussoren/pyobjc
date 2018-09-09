/*
 * AudioBuffer bindings
 *
 * These are basic bindings to the AudioBuffer type,
 * basically a buffer with extra attributes.
 */

static PyTypeObject audio_buffer_type; /* Forward definition */

#define audio_buffer_check(obj) PyObject_TypeCheck(obj, &audio_buffer_type)

struct audio_buffer {
    PyObject_HEAD

    char         ab_owns_storage;
    char         ab_owns_buffer;
    void*        ab_buf_pointer; /* for owned sample storage */
    AudioBuffer* ab_buf;
};

static PyMemberDef ab_members[] = {
    {
        .name = "_owns_storage",
        .type = T_BOOL,
        .offset = offsetof(struct audio_buffer, ab_owns_storage),
        .flags = READONLY,
        .doc = "True iff this buffer owns storage for the AudioBufer"
    },
    {
        .name = "_owns_buffer",
        .type = T_BOOL,
        .offset = offsetof(struct audio_buffer, ab_owns_buffer),
        .flags = READONLY,
        .doc = "True iff this buffer owns storage for the audio samples"
    },

    { .name = NULL } /* Sentinel */
};

static PyObject*
ab_get_mNumberChannels(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    return Py_BuildValue("I", self->ab_buf->mNumberChannels);
}

static int
ab_set_mNumberChannels(PyObject* _self, PyObject* value, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    if (value == NULL) {
        PyErr_SetString(PyExc_ValueError, "Cannot delete 'mNumberChannels'");
        return -1;
    }

    return PyObjC_PythonToObjC(@encode(unsigned int), value, &self->ab_buf->mNumberChannels);
}

static PyObject*
ab_get_mDataByteSize(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    return Py_BuildValue("I", self->ab_buf->mDataByteSize);
}

static PyObject*
ab_get_data(PyObject* _self, void* closure __attribute__((__unused__)))
{
    struct audio_buffer* self = (struct audio_buffer*)_self;

    if (self->ab_buf->mData == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

#if PY_MAJOR_VERSION == 3
    return PyMemoryView_FromMemory(self->ab_buf->mData, self->ab_buf->mDataByteSize, PyBUF_WRITE);
#else
    return PyBuffer_FromMemory(self->ab_buf->mData, self->ab_buf->mDataByteSize);
#endif
}

static PyGetSetDef ab_getset[] = {
    {
        .name = "mNumberChannels",
        .get = ab_get_mNumberChannels,
        .set = ab_set_mNumberChannels,
        .doc = NULL,
        .closure = NULL
    },
    {
        .name = "mDataByteSize",
        .get = ab_get_mDataByteSize,
        .set = NULL,
        .doc = NULL,
        .closure = NULL
    },
    {
        .name = "mData",
        .get = ab_get_data,
        .set = NULL,
        .doc = NULL,
        .closure = NULL
    },

    { .name = NULL } /* Sentinel */
};


PyDoc_STRVAR(ab_create_buffer_doc,
    "create_buffer(buffer_size)\n"
    CLINIC_SEP
    "Create a (new) buffer for storing audio samples. This replaces \n"
    "the previous buffer. After calling this method the memoryview \n"
    "retrieved from the mData attribute are no longer valid.");
static PyObject*
ab_create_buffer(PyObject* _self, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "buffer_size", NULL };

    struct audio_buffer* self = (struct audio_buffer*)_self;
    unsigned int buf_size;
    void* new_buf;

    if (PyArg_ParseTupleAndKeywords(args, kwds, "I", keywords, &buf_size) == -1) {
        return NULL;
    }

    new_buf = PyMem_Malloc(buf_size);
    if (new_buf == NULL) {
        return NULL;
    }

    if (self->ab_owns_buffer && self->ab_buf_pointer != NULL) {
        PyMem_Free(self->ab_buf_pointer);
    }

    self->ab_buf_pointer = self->ab_buf->mData = new_buf;
    self->ab_owns_buffer = 1;
    self->ab_buf->mDataByteSize = buf_size;

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef ab_methods[] = {
    {
      .ml_name = "create_buffer",
      .ml_meth = (PyCFunction)ab_create_buffer,
      .ml_flags = METH_VARARGS | METH_KEYWORDS,
      .ml_doc = ab_create_buffer_doc
    },

    { .ml_name = NULL } /* Sentinel */
};

static PyObject*
ab_new(PyTypeObject* cls, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "num_channels", "buffer_size", NULL };
    /* Args: channels (default to 1), size (default: no buffer) */
    struct audio_buffer* result;
    Py_ssize_t bufsize = -1;
    unsigned int num_channels = 1;

    if (!PyArg_ParseTupleAndKeywords(args, kwds,
                "|"
#if PY_MAJOR_VERSION == 3
                "$"
#endif
                "In", keywords, &num_channels, &bufsize)) {
        return NULL;
    }

#ifdef __LP64__
    if ((bufsize != -1 && bufsize < 0) || bufsize > (Py_ssize_t)UINT_MAX) {
#else
    if (bufsize != -1 && bufsize < 0) { /* 32bit means int == long == Py_ssizet */
#endif
        PyErr_Format(PyExc_ValueError, "bufsize %ld out of range", (long)bufsize);
        return NULL;
    }

    result = PyObject_New(struct audio_buffer, &audio_buffer_type);
    if (result == NULL) {
        return NULL;
    }

    result->ab_owns_storage = 1;
    result->ab_owns_buffer = 0;
    result->ab_buf_pointer = NULL;
    result->ab_buf = PyMem_Malloc(sizeof(AudioBuffer));
    if (result == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    result->ab_buf->mNumberChannels = num_channels;
    result->ab_buf->mDataByteSize = 0;
    result->ab_buf->mData = NULL;

    if (bufsize != -1) {
        result->ab_buf->mData = result->ab_buf_pointer = PyMem_Malloc(bufsize);
        if (result->ab_buf->mData == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        result->ab_buf->mDataByteSize = (unsigned int)bufsize;
        result->ab_owns_buffer = 1;
    }

    return (PyObject*)result;
}

static void
ab_dealloc(PyObject* object)
{
    struct audio_buffer* self = (struct audio_buffer*)object;

    if (self->ab_owns_buffer && self->ab_buf_pointer != NULL) {
        PyMem_Free(self->ab_buf_pointer);
    }
    if (self->ab_owns_storage) {
        PyMem_Free(self->ab_buf);
    }
    Py_TYPE(object)->tp_free(object);
}

PyDoc_STRVAR(ab_doc,
    "AudioBuffer(*, num_channels=1, buffer_size=-1)\n"
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
    .tp_methods     = ab_methods,
    .tp_getset      = ab_getset,
    .tp_members     = ab_members,
    .tp_new         = ab_new,
};

static PyObject*
ab_create(AudioBuffer* item)
{
    struct audio_buffer* result;

    result = PyObject_New(struct audio_buffer, &audio_buffer_type);
    if (result == NULL) {
        return NULL;
    }

    result->ab_owns_storage = 0;
    result->ab_owns_buffer = 0;
    result->ab_buf_pointer = NULL;
    result->ab_buf = item;

    return (PyObject*)result;
}

static PyObject* pythonify_audio_buffer(void* pointer)
{
    AudioBuffer* buf_pointer = (AudioBuffer*)pointer;

    if (buf_pointer == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    return ab_create(*(AudioBuffer**)pointer);
}

static int depythonify_audio_buffer(PyObject* value, void* pointer)
{
    if (value == Py_None) {
        *(AudioBuffer**)pointer = NULL;
        return 0;
    }

    if (!audio_buffer_check(value)) {
        PyErr_Format(PyExc_TypeError, "Expecting 'AudioBuffer', got '%.100s'",
            Py_TYPE(value)->tp_name);
        return -1;
    }

    *(AudioBuffer**)pointer = ((struct audio_buffer*)value)->ab_buf;
    return 0;
}

static int
init_audio_buffer(PyObject* module)
{
    int r;

    if (PyType_Ready(&audio_buffer_type) == -1) return -1;

    r = PyDict_SetItemString(audio_buffer_type.tp_dict, "__typestr__",
            PyBytes_FromString(@encode(AudioBuffer)));
    if (r == -1) return -1;


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
